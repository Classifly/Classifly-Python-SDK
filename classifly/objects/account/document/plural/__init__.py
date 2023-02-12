"""
    Classifly Distributions Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.document.constants import COLLECTION_PATH, DocumentFieldNames
from classifly.objects.account.document.utils import convert_to_document
from classifly.objects.account.document.singular import Document

if TYPE_CHECKING:
    from classifly.objects.utils.properties.blob import ClassiflyBlob
    from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference

class Documents(CoreClassiflyCollectionReference):
    """
        Classifly Documents. Used to retrieve Documents, either all Documents or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_document
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Document']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class DocumentsQuery(Query):
            @convert_to_document
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Document']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return DocumentsQuery(
            parent=self
        )

    def get_records(self,name:FirestoreQueryData=None,account:FirestoreQueryData=None,document:FirestoreQueryData=None) -> List['Document']:
        """
            Gets all Document records matching the specified filters.

            :param name: The filter on the Document's Name. Default: None (No filters)
            :param account: The filter on the Document's Account. Default: None (No filters)
            :param document: The filter on the Document's File. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=DocumentFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=DocumentFieldNames.ACCOUNT,
                query_data=account
            ),
            FirestoreWhereQueryData(
                field_name=DocumentFieldNames.DOCUMENT,
                query_data=document
            ),
        ])

    def add(self,name:str,account:'ClassiflyDocumentReference',document:'ClassiflyBlob') -> 'Document':
        """
            Creates a new Document.

            :param name: The new Document's Name
            :param account: The new Document's Account
            :param document: The new Document's Document File

            :return: The newly created Document
        """
        return super().add(
            document_data={
                DocumentFieldNames.NAME: name,
                DocumentFieldNames.ACCOUNT: account,
                DocumentFieldNames.DOCUMENT: document
            }
        )
