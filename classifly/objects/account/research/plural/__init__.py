"""
    Classifly Research Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.research.constants import COLLECTION_PATH, ResearchFieldNames
from classifly.objects.account.research.utils import convert_to_research
from classifly.objects.account.research.singular import Research

if TYPE_CHECKING:
    from classifly.objects.utils.properties.blob import ClassiflyBlob

class ResearchCollection(CoreClassiflyCollectionReference):
    """
        Classifly Research. Used to retrieve Research, either all Research or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_research
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Research']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class ResearchQuery(Query):
            @convert_to_research
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Research']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return ResearchQuery(
            parent=self
        )

    def get_records(self,name:FirestoreQueryData=None,document:FirestoreQueryData=None) -> List['Research']:
        """
            Gets all Research records matching the specified filters.

            :param name: The filter on the Research's Name. Default: None (No filters)
            :param document: The filter on the Research's Document file. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=ResearchFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=ResearchFieldNames.DOCUMENT,
                query_data=document
            )
        ])

    def add(self,name:str,document:'ClassiflyBlob') -> 'Research':
        """
            Creates a new Research Record.

            :param name: The new Research's Name
            :param document: The new Research's Document File

            :return: The newly created Research Record
        """
        return super().add(
            document_data={
                ResearchFieldNames.NAME: name,
                ResearchFieldNames.DOCUMENT: document
            }
        )
