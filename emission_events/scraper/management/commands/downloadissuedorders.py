from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from emissions.models import RegulatedEntity, IssuedOrder
from scraper.issued_orders_scraper import IssuedOrdersScraper


class Command(BaseCommand):
    args = "--rn RN_NUMBER"
    help = "Download Issured orders for each RN."

    option_list = BaseCommand.option_list + (
        make_option('--rn', action='store', type='string', default=None,
                    dest='rn', help="Download for a particular RN_NUMBER"),
    )

    def handle(self, *args, **options):
        if options.get('rn') is None:
            for regulated_entity in RegulatedEntity.objects.all():
                scraper = IssuedOrdersScraper(regulated_entity.regulated_entity_rn_number)
                if scraper.records_found > 0:
                    orders_stored = self.store(scraper)
                    print "%s: %i records found, %i records stored" %\
                        (scraper.rn_number, scraper.records_found, orders_stored)
                else:
                    print "No records for %s" % scraper.rn_number

        else:
            scraper = IssuedOrdersScraper(options.get('rn'))
            if scraper.records_found > 0:
                orders_stored = self.store(scraper)
                print "%s: %i records found, %i records stored" &\
                    (scraper.rn_number, scraper.records_found, orders_stored)
            else:
                print "No records for %s" % scraper.rn_number

    # Returns the number of orders created
    def store(self, scraper):
        output = 0
        for order in scraper.get_orders():
            if IssuedOrder.objects.filter(docket_number=order['docket_number']).exists():
                continue

            try:
                regulated_entity = RegulatedEntity.objects.get(regulated_entity_rn_number=order['regulated_entity_rn_number'])
                order['regulated_entity'] = regulated_entity

                IssuedOrder.objects.create(**order)
                output +=1
            except RegulatedEntity.DoesNotExist:
                continue
        return output
