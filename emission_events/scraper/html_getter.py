from emissions.models import EmissionEvent
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
                output = Scraper(page_html.content, page_html.tracking_number)()
                output['page_html'] = page_html
                EmissionEvent.objects.create(**output)
