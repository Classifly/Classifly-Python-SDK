"""
    Classifly Commitment Object Representation
"""
from typing import List, TYPE_CHECKING
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData


from classifly.objects.account.commitment.constants import COLLECTION_PATH, CommitmentFieldNames
from classifly.objects.account.commitment.utils import convert_to_commitment
from classifly.objects.account.commitment.singular import Commitment

if TYPE_CHECKING:
    from classifly.objects.account.limited_partner.singular import LimitedPartner
    from classifly.objects.account.fund.singular import Fund

class Commitments(CoreClassiflyCollectionReference):
    """
        Classifly Commitment. Used to retrieve Commitments, either all Commitments or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_commitment
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Commitment']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class CoInvestorsQuery(Query):
            @convert_to_commitment
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Commitment']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return CoInvestorsQuery(
            parent=self
        )

    def get_records(self,limited_partner:FirestoreQueryData=None,amount:FirestoreQueryData=None,fund:FirestoreQueryData=None) -> List['Commitment']:
        """
            Gets all Commitment records matching the specified filters.

            :param limited_partner: The filter on the Commitment's Limited Partner. Default: None (No filters)
            :param amount: The filter on the Commitment's Amount. Default: None (No filters)
            :param fund: The filter on the Commitment's Fund. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=CommitmentFieldNames.LIMITED_PARTNER,
                query_data=limited_partner
            ),
            FirestoreWhereQueryData(
                field_name=CommitmentFieldNames.AMOUNT,
                query_data=amount
            ),
            FirestoreWhereQueryData(
                field_name=CommitmentFieldNames.FUND,
                query_data=fund
            )
        ])

    def add(self,limited_partner:'LimitedPartner',amount:float,fund:'Fund') -> 'Commitment':
        """
            Creates a new Commitment.

            :param limited_partner: The new Commitment's Limited Partner
            :param amount: The new Commitment's Amount
            :param fund: The new Commitment's Fund

            :return: The newly created Co-Investor
        """
        return super().add(
            document_data={
                CommitmentFieldNames.LIMITED_PARTNER: limited_partner,
                CommitmentFieldNames.AMOUNT: amount,
                CommitmentFieldNames.FUND: fund
            }
        )
