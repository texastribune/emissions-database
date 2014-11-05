import logging
from django.core.management.base import NoArgsCommand
from emissions.models import EmissionEvent, RegulatedEntity, REPermit
from scraper.regulated_entity_scraper import RegulatedEntityScraper


logger = logging.getLogger('emissions_downloader')


class Command(NoArgsCommand):
    help = "Download the following 100 emission events."
    valid_emissions = [
        'air-shutdown',
        'air-startup',
        'emissions-event',
        'emissions-event-emergency-resp',
        'excess-opacity',
        'maintenance',
    ]

    def handle_noargs(self, **options):
        for re_number in self._regulated_entities_numbers():

            logger.info("Starting with %s" % re_number)
            if not self._is_already_saved(re_number):
                scraper = RegulatedEntityScraper(re_number)

                if scraper.has_page():
                    regulated_entity = RegulatedEntity.objects.\
                        create(**scraper.get_values())

                    logger.info("%s stored!" % re_number)
                    self._update_emissions_with(regulated_entity)
                    self._store_permits(regulated_entity, scraper.get_permits())
            else:
                regulated_entity = RegulatedEntity.objects.\
                    get(regulated_entity_rn_number=re_number)
                REPermit.objects.filter(regulated_entity_id=regulated_entity.id).delete()

                scraper = RegulatedEntityScraper(re_number)
                self._store_permits(regulated_entity, scraper.get_permits())
                logger.info("%s Updated!" % re_number)

    def _store_permits(self, regulated_entity, permits_values):
        for values in permits_values:
            values['regulated_entity'] = regulated_entity
            REPermit.objects.create(**values)
            logger.info("%s permit created for %s" %\
                (values['id_number'], regulated_entity.regulated_entity_rn_number))

    def _regulated_entities_numbers(self):
        regulated_entities = EmissionEvent.objects.\
            filter(type_of_emission__in=self.valid_emissions).\
            distinct('regulated_entity_rn_number').\
            values('type_of_emission', 'regulated_entity_rn_number')

        return [rn['regulated_entity_rn_number'] for rn in regulated_entities]

    def _is_already_saved(self, re_number):
        return RegulatedEntity.objects.\
            filter(regulated_entity_rn_number=re_number).exists()

    def _update_emissions_with(self, regulated_entity):
        emission_events = EmissionEvent.objects.\
            filter(regulated_entity_rn_number='RN104198643',
                   regulated_entity_id=None)
        for emission_event in emission_events:
            emission_event.regulated_entity = regulated_entity
            emission_event.save()
