"""
    Classifly Venture Firms Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.venture_firm.constants import COLLECTION_PATH, VentureFirmFieldNames
from classifly.objects.account.venture_firm.utils import convert_to_venture_firm
from classifly.objects.account.venture_firm.singular import VentureFirm

if TYPE_CHECKING:
    from classifly.objects.utils.properties.blob import ClassiflyBlob

class VentureFirms(CoreClassiflyCollectionReference):
    """
        Classifly Venture Firms. Used to retrieve Venture Firms, either all Venture Firms or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_venture_firm
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['VentureFirm']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class VentureFirmsQuery(Query):
            @convert_to_venture_firm
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['VentureFirm']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return VentureFirmsQuery(
            parent=self
        )

    def get_records(self,name:FirestoreQueryData=None,primary_color:FirestoreQueryData=None) -> List['VentureFirm']:
        """
            Gets all Venture Firm records matching the specified filters.

            :param name: The filter on the Venture Firm's Name. Default: None (No filters)
            :param document: The filter on the Venture Firm's Primary Color. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=VentureFirmFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=VentureFirmFieldNames.PRIMARY_COLOR,
                query_data=primary_color
            )
        ])

    def add(self,name:str,primary_color:str) -> 'VentureFirm':
        """
            Creates a new Venture Firm.

            :param name: The new Venture Firm's Name
            :param primary_color: The new Venture Firm's Primary Color

            :return: The newly created Published Report
        """
        return super().add(
            document_data={
                VentureFirmFieldNames.NAME: name,
                VentureFirmFieldNames.PRIMARY_COLOR: primary_color
            }
        )
