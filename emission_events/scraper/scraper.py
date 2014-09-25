import re
import django
import logging
import inflection
from datetime import datetime
from bs4 import BeautifulSoup


logger = logging.getLogger('emissions_downloader')
logger_conversions = logging.getLogger('conversions')


class Scraper(object):
    def __init__(self, html, tracking_number):
        self.html = html
        self.soup = BeautifulSoup(html)
        self.tracking_number = tracking_number
        self.lbs_regex = re.compile(r"lbs$|lbs\s")
        self.float_regex = re.compile(r"(\d+\.\d+)|(\d+)")
        self.percentage_regex = re.compile(r"%")

    def emission_event_data(self):
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
            'duration':   self.get_duration(began_date, ended_date),
            'type_of_emission': self.parameterize(tds[4].string)[0:30]
        }

    def has_contaminants(self):
        return len(self.soup.find_all('table')) > 1

    def contaminants(self):
        contaminants = []
        for table in self.soup.find_all('table')[1:]:
            for tr in table.find_all('tr')[1:]:
                tds = tr.find_all('td')
                contaminants.append({
                    'tracking_number': self.tracking_number,
                    'contaminant': self.clean(tds[0].string, 100),
                    'authorization': self.clean(tds[1].string),
                    'limit': self.clean(tds[2].string),
                    'amount_released': self.clean(tds[3].string),
                    'contaminant_parameterized': self.parameterize(tds[0].string),
                    'limit_lbs': self.get_lbs(tds[2].string),
                    'amount_released_lbs': self.get_lbs(tds[3].string),
                    'limit_op': self.get_opacity(tds[2].string),
                    'amount_released_op': self.get_opacity(tds[3].string)
                   })
        return contaminants

    def clean(self, cad, limit=200):
        if cad == None:
            return ''
        else:
            return cad.strip()[0:limit]

    def parameterize(self, cad):
        return inflection.parameterize(unicode(cad))

    def get_opacity(self, cad):
        cad = cad.strip().lower()
        if self.percentage_regex.search(cad):
            try:
                value = float(self.float_regex.search(cad).group())
                logger_conversions.info("OPACITY - %s | %s : %f " % (self.tracking_number, cad, value))
                return value
            except:
                logger_conversions.error("OPACITY - %s | %s was not parsed!" % (self.tracking_number, cad))
                return None
        else:
            logger_conversions.error("OPACITY - %s | %s did not match" % (self.tracking_number, cad))
            return None

    def get_lbs(self, cad):
        cad = cad.strip().lower()
        if cad == '0.0':
            return 0.0
        elif self.lbs_regex.search(cad):
            try:
                value = float(self.float_regex.search(cad).group())
                logger_conversions.info("%s | %s : %f " % (self.tracking_number, cad, value))
                return value
            except:
                logger_conversions.error("%s | %s was not parsed!" % (self.tracking_number, cad))
                return None
        else:
            logger_conversions.error("%s | %s did not match" % (self.tracking_number, cad))
            return None

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
        cad = ' '.join(cad.split())
        time_zone = django.utils.timezone.get_current_timezone()
        try:
            if len(cad.split()) == 2:
                dt = datetime.strptime(cad, "%m/%d/%Y %I:%M%p")
                return time_zone.localize(dt)
            else:
                dt = datetime.strptime(cad, "%m/%d/%Y")
                return time_zone.localize(dt)
        except ValueError:
            logger.error("Parsing date on %i | %s" % (self.tracking_number, cad))
            return None

    def get_duration(self, begin, end):
        if begin == None or end == None:
            return None
        else:
            return (end - begin).total_seconds()/3600
