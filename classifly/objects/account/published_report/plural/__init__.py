"""
    Classifly Published Reports Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.published_report.constants import COLLECTION_PATH, PublishedReportFieldNames
from classifly.objects.account.published_report.utils import convert_to_published_report
from classifly.objects.account.published_report.singular import PublishedReport

if TYPE_CHECKING:
    from classifly.objects.utils.properties.blob import ClassiflyBlob

class PublishedReports(CoreClassiflyCollectionReference):
    """
        Classifly Published Reports. Used to retrieve Published Reports, either all Published Reports or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_published_report
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['PublishedReport']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class PublishedReportsQuery(Query):
            @convert_to_published_report
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['PublishedReport']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return PublishedReportsQuery(
            parent=self
        )

    def get_records(self,name:FirestoreQueryData=None,document:FirestoreQueryData=None) -> List['PublishedReport']:
        """
            Gets all Published Report records matching the specified filters.

            :param name: The filter on the Published Report's Name. Default: None (No filters)
            :param document: The filter on the Published Report's Document file. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=PublishedReportFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=PublishedReportFieldNames.DOCUMENT,
                query_data=document
            )
        ])

    def add(self,name:str,document:'ClassiflyBlob') -> 'PublishedReport':
        """
            Creates a new Published Report.

            :param name: The new Published Report's Name
            :param document: The new Published Report's Document File

            :return: The newly created Published Report
        """
        return super().add(
            document_data={
                PublishedReportFieldNames.NAME: name,
                PublishedReportFieldNames.DOCUMENT: document
            }
        )
