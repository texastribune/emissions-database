from emissions.models import EmissionEvent, ContaminantReleased
from downloader import Downloader
from scraper import Scraper


class HTMLGetter(object):
    def __init__(self, url_builder):
        self.url_builder = url_builder

    def __call__(self):
        while not self.url_builder.is_finalized():
            self.url_builder.next()

            downloader = Downloader(
                self.url_builder.current_url(),
                self.url_builder.current_tracking_number()
            )
            if downloader():
                page_html = downloader.page_html
                scraper = Scraper(page_html.content, page_html.tracking_number)
                emission_event_data = scraper.emission_event_data()
                emission_event_data['page_html'] = page_html

                emission_event = EmissionEvent.objects.create(**emission_event_data)

                if scraper.has_contaminants():
                    for contaminant_data in scraper.contaminants():
                        contaminant_data['emission_event'] = emission_event
                        ContaminantReleased.objects.create(**contaminant_data)
