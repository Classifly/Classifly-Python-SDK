"""
    Report - Object Representation
"""
from typing import List
from google.cloud.firestore import FirestoreProperty, DocumentReference
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.report.constants import ReportFieldNames

class Report(ClassiflyAccountDocumentReference):
    """
        A Classifly Report. A Report is issued by a Venture Firm and distributed to Companies to enter information about their Company. Once completed, the Venture Firm is then able to view this information.
    """
    as_of_date: DatetimeWithNanoseconds = FirestoreProperty(ReportFieldNames.AS_OF_DATE,DatetimeWithNanoseconds) #: The date the Report's data is as of
    due_date: DatetimeWithNanoseconds = FirestoreProperty(ReportFieldNames.DUE_DATE, DatetimeWithNanoseconds) #: When the Portfolio Company is required to provide complete the report by

    def __init__(self, *args, report_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Reports",document_id=report_id)

    def alert(self):
        """
            TO-DO: This function is not yet fully implemented

            Notifies all User's if their Account has not completed the Report. This function is typically only invoked by VC users.
        """
        from classifly.objects.account.report.recipient.plural import ReportRecipients
        from classifly.objects.account.report.recipient.singular import ReportRecipient
        incomplete_report_recipients: List['ReportRecipient'] = ReportRecipients().get_records(report=self,completed=False)

        for incomplete_report_recipient in incomplete_report_recipients:
            incomplete_report_recipient.send_reminder()
