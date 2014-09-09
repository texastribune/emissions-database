  from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Print a cliche to the console."

    def handle_noargs(self, **options):
        print "Hello, World!"
