class URLBuilder(object):
    def __init__(self, initial, final=None):
        self.initial = initial
        self.current = initial
        if final:
            self.final = final
        else:
            self.final = initial + 10

    def next(self):
        if not self.is_finalized():
            url = self.url(self.current)
            self.current += 1
            return url
        else:
            raise StopIteration("No more URLs")

    def is_finalized(self):
        return self.current > self.final

    def url(self, tracking_number):
        return "http://www11.tceq.texas.gov/oce/eer/index.cfm?fuseaction=main.getDetails&target=%i" % tracking_number
