from emissions.models import EmissionEvent, ContaminantReleased, PageHTML
from downloader import Downloader
from scraper import Scraper
from handle_unsettled_reports import HandleUnsettledReports


class HTMLGetter(object):
    def __init__(self, url_builder=None):
        self.url_builder = url_builder
        self.metadata = {
            'failed': 0,
            'success': 0
        }

    def __call__(self):
        if self.url_builder:
            while not self.url_builder.is_finalized():
                self.url_builder.next()
                downloader = Downloader(
                    self.url_builder.current_url(),
                    self.url_builder.current_tracking_number()
                )
                if downloader():
                    emission_event_data = self.scrapeReport(downloader)
                    if HandleUnsettledReports.isUnsettledReport(emission_event_data):
                        HandleUnsettledReports.addNewReport(downloader.page_html.tracking_number)
                else:
                    self.metadata['failed'] += 1
        return self.metadata

    def scrapeReport(self, downloader):
        self.metadata['success'] += 1
        page_html = downloader.page_html
        scraper = Scraper(page_html.content, page_html.tracking_number)
        emission_event_data = scraper.emission_event_data()
        emission_event_data['page_html'] = page_html
        emission_event_tuple = EmissionEvent.objects.update_or_create(**emission_event_data)
        emission_event = emission_event_tuple[0]

        if scraper.has_contaminants():
            for contaminant_data in scraper.contaminants():
                contaminant_data['emission_event'] = emission_event
                ContaminantReleased.objects.update_or_create(**contaminant_data)
        return emission_event_data
