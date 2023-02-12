from typing import List
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.account.portfolio_company.singular import PortfolioCompany
from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreWhereQueryData, FirestoreQueryData

from classifly.objects.account.report.singular import Report
from classifly.objects.account.report.recipient.singular import ReportRecipient
from classifly.objects.account.report.recipient.constants import ReportRecipientFieldNames, COLLECTION_PATH
from classifly.objects.account.report.recipient.utils import convert_to_report_recipient

class ReportRecipients(CoreClassiflyCollectionReference):
    """
        Classifly Report Recipients. Used to retrieve report recipients, either all report recipients or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_report_recipient
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['ReportRecipient']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class ReportRecipientsQuery(Query):
            @convert_to_report_recipient
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['ReportRecipient']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return ReportRecipientsQuery(
            parent=self
        )

    def get_records(self,portfolio_company:FirestoreQueryData=None,report:FirestoreQueryData=None,completed:FirestoreQueryData=None) -> List['ReportRecipient']:
        """
            Gets all Report Recipient records matching the specified filters.

            :param portfolio_company: The filter on the Report Recipient's Portfolio Company. Default: None (No filters)
            :param report: The filter on the Report Recipient's corresponding report. Default: None (No filters)
            :param completed: The filter on the Report Recipient's completed status. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=ReportRecipientFieldNames.PORTFOLIO_COMPANY,
                query_data=portfolio_company
            ),
            FirestoreWhereQueryData(
                field_name=ReportRecipientFieldNames.REPORT,
                query_data=report
            ),
            FirestoreWhereQueryData(
                field_name=ReportRecipientFieldNames.COMPLETED,
                query_data=completed
            ),
        ])

    def add(self,portfolio_company:PortfolioCompany=None,report:Report=None,completed:bool=None) -> 'ReportRecipient':
        """
            Creates a new Report Recipient.

            :param portfolio_company: The new Report Recipient's Portfolio Company
            :param report: The new Report Recipient's Report
            :param completed: The new Report Recipient's completion status

            :return: The newly created Portfolio Company
        """
        return super().add(
            document_data={
                ReportRecipientFieldNames.PORTFOLIO_COMPANY: portfolio_company,
                ReportRecipientFieldNames.REPORT: report,
                ReportRecipientFieldNames.COMPLETED: completed,
            }
        )
