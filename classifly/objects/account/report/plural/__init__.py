"""
    Reports - Object Representation
"""
from typing import List
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreWhereQueryData, FirestoreQueryData

from classifly.objects.account.report.constants import ReportFieldNames, COLLECTION_PATH
from classifly.objects.account.report.singular import Report
from classifly.objects.account.report.utils import convert_to_report

class Reports(CoreClassiflyCollectionReference):
    """
        Classifly Reports. Used to retrieve reports, either all reports or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_report
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Report']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class ReportsQuery(Query):
            @convert_to_report
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Report']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return ReportsQuery(
            parent=self
        )

    def get_records(self,as_of_date:FirestoreQueryData=None,due_date:FirestoreQueryData=None) -> List['Report']:
        """
            Gets all Report records matching the specified filters.

            :param as_of_date: The filter on the Report's as of date. Default: None (No filters)
            :param due_date: THe filter on the Report's due date. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=ReportFieldNames.AS_OF_DATE,
                query_data=as_of_date
            ),
            FirestoreWhereQueryData(
                field_name=ReportFieldNames.DUE_DATE,
                query_data=due_date
            )
        ])

    def add(self,as_of_date:DatetimeWithNanoseconds,due_date:DatetimeWithNanoseconds) -> 'Report':
        """
            Creates a new Report.

            :param as_of_date: The new Reports's As of Date
            :param due_date: The new Reports's Due Date

            :return: The newly created Report
        """
        return super().add(
            document_data={
                ReportFieldNames.AS_OF_DATE: as_of_date,
                ReportFieldNames.DUE_DATE: due_date
            }
        )