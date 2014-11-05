import mechanize
from bs4 import BeautifulSoup


class RegulatedEntityScraper(object):
    url = "http://www15.tceq.texas.gov/crpub/index.cfm?fuseaction=regent.RNSearch"

    def __init__(self, rn_number):
        self.rn_number = rn_number
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.open(self.url)
        br.select_form(nr=0)
        br.form['re_ref_num_txt'] = self.rn_number
        response = br.submit()
        self.regulated_entity_url = response.geturl()
        self.html = response.read()

        if self.regulated_entity_url.find('notfound') >= 0:
            raise Exception("Regulated Entity not found")

    def get_values(self):
        output = {}
        soup = BeautifulSoup(self.html)
        return {
            'regulated_entity_rn_number': self.rn_number,
            'regulated_entity_url': self.regulated_entity_url,
            'name': self.get_name(soup),
            'primary_business': self.get_primary_business(soup),
            'street_address': self.get_street_address(soup),
            'county': self.get_county(soup),
            'nearest_city': self.get_nearest_city(soup),
            'nearest_zipcode': self.get_nearest_zipcode(soup),
            'physical_location': self.get_physical_location(soup),
            'permits': self.get_permits(soup)
        }

    def get_name(self, soup):
        return soup.find(id='reinfo').find_all('p')[1].contents[-1].strip()

    def get_primary_business(self, soup):
        return soup.find(id='reinfo').find_all('p')[2].contents[-1].strip()

    def get_street_address(self, soup):
        return soup.find(id='street_addr').find_all('p')[0].contents[-1].strip()

    def get_county(self, soup):
        return soup.find(id='geo_loc').find_all('p')[0].contents[-1].strip()

    def get_nearest_city(self, soup):
        return soup.find(id='geo_loc').find_all('p')[1].contents[-1].strip()

    def get_nearest_zipcode(self, soup):
        return soup.find(id='geo_loc').find_all('p')[3].contents[-1].strip()

    def get_physical_location(self, soup):
        return soup.find(id='geo_loc').find_all('p')[4].contents[-1].strip()

    def get_permits(self, soup):
        output = []
        for tr in self._get_permit_trs(soup)[1:-1]:
            output.append(
                {
                    'program': self._get_program(tr),
                    'id_type': self._get_id_type(tr),
                    'id_number': self._get_id_number(tr),
                    'id_status': self._get_id_status(tr),
                    'url': self._get_url(tr)
                }
            )
        return output

    def _get_program(self, tr):
        if tr.find_all('td')[0].find('a'):
            return tr.find_all('td')[0].find('a').text.strip()
        else:
            return tr.find_all('td')[0].contents[0].strip()

    def _get_id_type(self, tr):
        return tr.find_all('td')[1].contents[0].strip()

    def _get_id_number(self, tr):
        link = tr.find_all('td')[2].find('a')
        if link:
            return link.text.strip()
        else:
            return tr.find_all('td')[2].contents[0].strip()

    def _get_id_status(self, tr):
        return tr.find_all('td')[3].contents[0].strip()

    def _get_url(self, tr):
        if tr.find('a'):
            return tr.find('a').attrs['href']
        else:
            return None

    def _get_permit_trs(self, soup):
        return soup.find_all('table', class_='iddisplay')[0].find_all('tr')
