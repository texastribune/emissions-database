# -*- coding: utf-8 -*-

from datetime import datetime
import re
import urllib
import urllib2
from bs4 import BeautifulSoup


class IssuedOrdersScraper(object):
    url = 'http://www14.tceq.texas.gov/epic/CIO/index.cfm?fuseaction=search.searchByRN'

    def __init__(self, rn_number):
        self.rn_number = rn_number
        self.populate_html()
        self.populate_number_of_records()

    def populate_html(self):
        data = urllib.urlencode({'reg_int_num_txt' : self.rn_number})
        request = urllib2.Request(self.url, data)
        response = urllib2.urlopen(request)
        self.html = response.read()

    def populate_number_of_records(self):
        if re.search('No results were found', self.html):
            self.records_found = 0
        else:
            match = re.search('(\d+) Record(:?s)? found', self.html)
            self.records_found = int(match.group(1))
        return self.records_found

    def get_orders(self):
        output = {}
        soup = BeautifulSoup(self.html)

        orders = self.identify_orders(soup)

        # if len(orders) == self.records_found:
        for order in orders:
            order['agended_at'] = self.get_agenda_date(order['agenda_date'])
            order['penalty_value'] = self.get_amount(order['penalty_amount'])

        return orders
        # else:
        #     raise Exception('Error on number of records for %s' % self.rn_number)

    def identify_orders(self, soup):
        orders = []
        for link in soup.find_all('a'):
            if re.match('\d{4}\-\d{4}\-\w{3}(?:\-\w)?', link.get_text()):
                orders.append({
                    'docket_number': link.get_text().strip(),
                    'docket_link': link.get('href'),
                    'agenda_date': link.nextSibling.nextSibling.nextSibling.strip(),
                    'penalty_amount': link.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.strip(),
                    'summary': link.find_next('div').find_next('div').get_text().strip()[0:999],
                    'regulated_entity_rn_number': self.rn_number
                })
        return orders

    def get_amount(self, cad):
        try:
            value = re.findall('\d+', cad)[0]
            return int(value)
        except (IndexError, ValueError):
            return None

    def get_agenda_date(self, cad):
        return datetime.strptime(cad, "%m/%d/%Y")
