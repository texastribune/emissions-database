from emissions.models import UnsettledReport
from downloader import Downloader

class HandleUnsettledReports(object):

    def __init__(self, url_builder, html_getter, reports):
        self.url_builder = url_builder
        self.html_getter = html_getter
        self.reports = reports

    def updateReports(self):
        for report in self.reports:
            downloader = Downloader(
                self.url_builder.current_url(report.tracking_number),
                report.tracking_number,
                isUnsettledReport=True
            )
            if downloader():
                emission_event_data = self.html_getter.scrapeReport(downloader)
                print(emission_event_data)
                if not self.isUnsettledReport(emission_event_data):
                    report.delete()
            else:
                self.html_getter.metadata['failed'] += 1
        
        return self.html_getter.metadata

    @staticmethod
    def isUnsettledReport(emission_event_data):
        return emission_event_data['based_on_the'] != 'FINAL REPORT'

    @staticmethod
    def addNewReport(trackingNumber):
        try:
            UnsettledReport.objects.get(tracking_number=trackingNumber)
        except UnsettledReport.DoesNotExist:
            print('ADDING: ' + str(trackingNumber))
            unsettledReport = UnsettledReport(
                tracking_number=trackingNumber
            )
            return unsettledReport.save()

    

