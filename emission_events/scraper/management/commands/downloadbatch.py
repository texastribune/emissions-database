from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from scraper.url_builder import URLBuilder
from scraper.html_getter import HTMLGetter


class Command(BaseCommand):
    args = "-i INITIAL_TRACKING_NUMBER -f FINAL_TRACKING_NUMBER"
    help = "Echo all positional arguments."

    option_list = BaseCommand.option_list + (
        make_option('-i', '--initial', action='store', type='int',
                    dest='initial', help="Initial ID."),
        make_option('-f', '--final', action='store', type='int',
                    dest='final', help="Final ID."),
        make_option('--ignore', action='store', type='string', default=None,
                    dest='ignore', help="File with tracking numbers to ignore"),
    )

    def handle(self, *args, **options):
        if options.get('initial') is None:
            raise CommandError('You need an initial tracking number')

        ignore_list = []
        if options.get('ignore'):
            with open(options.get('ignore')) as ignorefile:
                ignore_list = [int(tracking_number) for tracking_number in ignorefile.read().split()]

        url_builder = URLBuilder(
            options.get('initial'),
            options.get('final'),
            ignore_list
        )

        info = HTMLGetter(url_builder)()
        print "Success: %i | Failed: %i" % (info['success'], info['failed'])
