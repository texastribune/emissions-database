from datetime import datetime
from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self, html, tracking_number):
        self.html = html
        self.soup = BeautifulSoup(html)
        self.tracking_number = tracking_number

    def __call__(self):
        tds = self.soup.table.find_all('td')
        metas = self.soup.find_all('meta')
        began_date = self.parse_date(tds[5].string.strip())
        ended_date = self.parse_date(tds[7].string.strip())

        return {
            'tracking_number':             self.tracking_number,
            'dc_date_meta':                self.get_dc_date_meta(metas),
            'regulated_entity_name':       self.clean(tds[0].string, 30),
            'physical_location':           self.clean(tds[1].string),
            'regulated_entity_rn_number':  self.clean(tds[2].string, 50),
            'city_county':                 self.clean(tds[3].string, 50),
            'type_of_air_emissions_event': self.clean(tds[4].string, 50).upper(),
            'based_on_the':                self.clean(tds[6].string, 50).upper(),
            'event_began':                 self.clean(tds[5].string, 30),
            'event_ended':                 self.clean(tds[7].string, 30),
            'cause':                       self.clean(tds[8].string),
            'action_taken':                self.clean(tds[9].string),
            'emissions_estimation_method': self.clean(tds[10].string),

            'city':       self.get_city(tds[3].string),
            'county':     self.get_county(tds[3].string),
            'began_date': began_date,
            'ended_date': ended_date,
            'duration':   self.get_duration(began_date, ended_date)
        }

    def clean(self, cad, limit=200):
        if cad == None:
            return ''
        else:
            return cad.strip()[0:limit]

    def get_dc_date_meta(self, metas):
        for meta in metas:
            try:
                if meta['name'] == 'DC.Date':
                    return meta['content']
            except KeyError:
                pass
        return None

    def get_city(self, cad):
        city = cad.split(',')[0].strip()
        if city == '':
            return None
        else:
            return city

    def get_county(self, cad):
        county = cad.split(',')[1].strip()
        if county == '':
            return None
        else:
            return county

    def parse_date(self, cad):
        try:
            if len(cad.split()) == 2:
                print "parsing " + cad
                print datetime.strptime(cad, "%m/%d/%Y %I:%M%p")
                return datetime.strptime(cad, "%m/%d/%Y %I:%M%p")
            else:
                print "parsing (short) " + cad
                print datetime.strptime(cad, "%m/%d/%Y")
                return datetime.strptime(cad, "%m/%d/%Y")
        except ValueError:
            print "fallo: " + cad
            return None

    def get_duration(self, begin, end):
        if begin == None or end == None:
            return None
        else:
            return (end - begin).total_seconds()/3600