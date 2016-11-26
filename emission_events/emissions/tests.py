from django.test import TestCase
from scraper.scraper import Scraper
from scraper.handle_unsettled_reports import HandleUnsettledReports
from emissions.models import UnsettledReport
from scraper.testStubs.expected.reportFinal import reportFinal


class ScraperTestCase(TestCase):
    def setUp(self):
        self.finalHtml = open('emission_events/scraper/testStubs/fixtures/report_final_state.html').read()
        self.initialHtml = open('emission_events/scraper/testStubs/fixtures/report_initial_state.html').read()
        
        self.finalScraper = Scraper(self.finalHtml, 1)
        self.initalScraper = Scraper(self.initialHtml, 1)

        self.finalReport = self.finalScraper.emission_event_data()
        self.initialReport = self.initalScraper.emission_event_data()

        UnsettledReport.objects.create(tracking_number=self.finalReport['tracking_number'])
        UnsettledReport.objects.create(tracking_number=self.initialReport['tracking_number'])

    def test_scrapeFinalReport(self):
        for key in reportFinal:
            self.assertEqual(self.finalReport[key], reportFinal[key])

    def test_scrapeInitialReport(self):
        for key in initialFinal:
            self.assertEqual(self.initialReport[key], initialFinal[key])

    def test_updateUnsettledReports(self):
        reports = UnsettledReport.objects.order_by('tracking_number')
        self.assertEqual(reports.count(), 2)
        for report in reports:
            if not HandleUnsettledReports.isUnsettledReport(report):
                report.delete()
        self.assertEqual(reports.count(), 1)
