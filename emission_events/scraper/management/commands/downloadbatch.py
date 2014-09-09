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
    )

    def handle(self, *args, **options):
        if options.get('initial') is None:
            raise CommandError('You need an initial tracking number')

        url_builder = URLBuilder(
            options.get('initial'),
            options.get('final')
        )
        HTMLGetter(url_builder)()
