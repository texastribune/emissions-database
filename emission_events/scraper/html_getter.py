class HTMLGetter(object):
    def __init__(self, url_builder):
        self.url_builder = url_builder

    def __call__(self):
        while not self.url_builder.is_finalized():
            downloader = Downloader(
                self.url_builder.next(),
                self.url_builder.current)
            downloader()
