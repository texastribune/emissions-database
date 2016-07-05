from django.core.management.base import NoArgsCommand
from emissions.models import PageHTML
from scraper.url_builder import URLBuilder
from scraper.html_getter import HTMLGetter


class Command(NoArgsCommand):
    help = "Download the following 100 emission events."

    def handle_noargs(self, **options):
        page = PageHTML.objects.order_by('-tracking_number')[0]
        initial = page.tracking_number
        final = initial + 300

        print "Updating from %i to %i" % (initial, final)

        url_builder = URLBuilder(initial, final)
        info = HTMLGetter(url_builder)()

        print "Success: %i | Failed: %i" % (info['success'], info['failed'])
