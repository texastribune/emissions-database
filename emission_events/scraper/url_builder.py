class URLBuilder(object):
    def __init__(self, initial, final=None):
        self.initial = initial
        self.current = initial - 1
        if final:
            self.final = final
        else:
            self.final = initial + 10

    def next(self):
        if not self.is_finalized():
            self.current += 1
            return self.current
        else:
            raise StopIteration("No more URLs")

    def current_url(self):
        return self.url(self.current)

    def current_tracking_number(self):
        return self.current

    def is_finalized(self):
        return self.current > self.final

    def url(self, tracking_number):
        return "http://www11.tceq.texas.gov/oce/eer/index.cfm?fuseaction=main.getDetails&target=%i" % tracking_number
