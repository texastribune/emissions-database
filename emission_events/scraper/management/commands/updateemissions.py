from django.core.management.base import NoArgsCommand
from emissions.models import PageHTML
from scraper.url_builder import URLBuilder
from scraper.html_getter import HTMLGetter


class Command(NoArgsCommand):
    help = "Print a cliche to the console."

    def handle_noargs(self, **options):
        page = PageHTML.objects.order_by('-tracking_number')[0]
        initial = page.tracking_number
        final = initial + 100

        url_builder = URLBuilder(initial, final)
        HTMLGetter(url_builder)()
