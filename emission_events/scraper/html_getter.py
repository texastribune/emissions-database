from downloader import Downloader


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
            downloader()
