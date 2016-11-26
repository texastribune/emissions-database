class URLBuilder(object):
    def __init__(self, initial=0, final=None, ignore_list=[]):
        self.initial = initial
        self.current = initial - 1
        self.ignore_list = ignore_list
        if final:
            self.final = final
        else:
            self.final = initial + 10

    def next(self):
        if not self.is_finalized():
            self.current = self._find_next(self.current)
            return self.current
        else:
            raise StopIteration("No more URLs")

    def current_url(self, tracking_number=None):
        if tracking_number:
            return self.url(tracking_number)
        else:
            return self.url(self.current)

    def current_tracking_number(self):
        return self.current

    def is_finalized(self):
        return self.current > self.final

    def url(self, tracking_number):
        return "http://www2.tceq.texas.gov/oce/eer/index.cfm?fuseaction=main.getDetails&target=%i" % tracking_number

    def _find_next(self, tmp):
        tmp += 1
        if tmp in self.ignore_list:
            return self._find_next(tmp)
        else:
            return tmp
