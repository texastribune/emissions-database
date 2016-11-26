from django.core.management.base import NoArgsCommand
from emissions.models import PageHTML, UnsettledReport
from scraper.handle_unsettled_reports import HandleUnsettledReports
from scraper.url_builder import URLBuilder
from scraper.html_getter import HTMLGetter


class Command(NoArgsCommand):
    help = "Download the following 100 emission events."

    def handle_noargs(self, **options):
        self.handleUnsettledReports()
        self.getNewReports()

    def handleUnsettledReports(self):
        reports = UnsettledReport.objects.order_by('tracking_number')
        if reports.count():
            handleUnsettledReports = HandleUnsettledReports(URLBuilder(), HTMLGetter(), reports)

            print "Checking %i unsettled reports" % (reports.count())

            info = handleUnsettledReports.updateReports()

            print "Success: %i | Failed: %i" % (info['success'], info['failed'])

    def getNewReports(self):
        page = PageHTML.objects.order_by('-tracking_number')[0]
        initial = page.tracking_number
        final = initial + 300

        print "Updating from %i to %i" % (initial, final)

        url_builder = URLBuilder(initial, final)
        info = HTMLGetter(url_builder)()

        print "Success: %i | Failed: %i" % (info['success'], info['failed'])
