from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.portfolio_company.singular import PortfolioCompany
from classifly.objects.account.utils import ClassiflyAccountDocumentReference

from classifly.objects.account.report.singular import Report
from classifly.objects.account.report.recipient.constants import ReportRecipientFieldNames, COLLECTION_PATH


class ReportRecipient(ClassiflyAccountDocumentReference):
    """
        A Report Recipient. Used to track whether a Portfolio Company has completed a report
    """
    portfolio_company: PortfolioCompany = FirestoreProperty(ReportRecipientFieldNames.PORTFOLIO_COMPANY, PortfolioCompany) #: The Portfolio Company responsible to complete the Report
    report: Report = FirestoreProperty(ReportRecipientFieldNames.REPORT,Report) #: The Report the Portfolio Company is responsible for completing
    completed: bool = FirestoreProperty(ReportRecipientFieldNames.COMPLETED,bool) #: Whether the Portfolio Company has completed the Report.

    def __init__(self, *args, report_recipient_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(*(COLLECTION_PATH + [report_recipient_id]))


    def send_reminder(self):
        """
            Notifies a report recipient to complete the report.
        """
        if self.completed:
            raise Exception("The report recipient has already completed the report; therefore, they don't need to be sent a reminder.")
        raise NotImplementedError()