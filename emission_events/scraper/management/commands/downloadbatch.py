from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from scraper.url_builder import URLBuilder
from scraper.downloader import Downloader


class HTMLGetter(object):
    def __init__(self, url_builder):
        self.url_builder = url_builder

    def __call__(self):
        while not self.url_builder.is_finalized():
            downloader = Downloader(
                self.url_builder.next(),
                self.url_builder.current)
            downloader()


class Command(BaseCommand):
    args = "-i INITIAL_TRACKING_NUMBER -f FINAL_TRACKING_NUMBER"
    help = "Echo all positional arguments."

    option_list = BaseCommand.option_list + (
        make_option('-i', '--initial', action='store', type='int',
                    dest='initial', help="Initial ID."),
        make_option('-f', '--final', action='store', type='int',
                    dest='final', help="Final ID."),
    )

    def handle(self, *args, **options):
        if options.get('initial') is None:
            raise CommandError('You need an initial tracking number')

        url_builder = URLBuilder(
            options.get('initial'),
            options.get('final')
        )
        HTMLGetter(url_builder)()
