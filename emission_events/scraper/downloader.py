import urllib2
import logging
from emissions.models import PageHTML, RequestAttempt


class Downloader(object):
    def __init__(self, url, tracking_number):
        self.url = url
        self.tracking_number = tracking_number

    def __call__(self):
        if not self.is_downloaded():
            return self.download()
        else:
            return False

    def download(self):
        try:
            response = urllib2.urlopen(self.url)
            html = response.read()
            logging.info("Getting %i" % self.tracking_number)
            self.store_page(html)
            self.store_attempt("%i downloaded." % self.tracking_number, failed=False)
            return True
        except (urllib2.URLError, urllib2.HTTPError) as e:
            logging.error("Fail %i | %s" % (self.tracking_number, str(e)))
            self.store_attempt(str(e), failed=True)
            return False

    def store_page(self, content):
        page_html = PageHTML(
            tracking_number=self.tracking_number,
            content=content.strip()
        )
        return page_html.save()

    def store_attempt(self, message, failed=False):
        request_attempt = RequestAttempt(
            tracking_number=self.tracking_number,
            message=message,
            failed=failed
        )
        return request_attempt.save()

    def is_downloaded(self):
        try:
            PageHTML.objects.get(tracking_number=self.tracking_number)
            return True
        except PageHTML.DoesNotExist:
            return False
