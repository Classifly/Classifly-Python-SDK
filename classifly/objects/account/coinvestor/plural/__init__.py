"""
    Classifly Co-Investors Object Representation
"""
from typing import List
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.coinvestor.constants import COLLECTION_PATH, CoInvestorFieldNames
from classifly.objects.account.coinvestor.utils import convert_to_coinvestor
from classifly.objects.account.coinvestor.singular import CoInvestor

class CoInvestors(CoreClassiflyCollectionReference):
    """
        Classifly Co-Investors. Used to retrieve Co-Investors, either all co-investors or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_coinvestor
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CoInvestor']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class CoInvestorsQuery(Query):
            @convert_to_coinvestor
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CoInvestor']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return CoInvestorsQuery(
            parent=self
        )

    def get_records(self,name:FirestoreQueryData=None,pipeline_account:FirestoreQueryData=None) -> List['CoInvestor']:
        """
            Gets all Co-Investor records matching the specified filters.

            :param name: The filter on the Co-Investor's Name. Default: None (No filters)
            :param pipeline_account: The filter on the Co-Investor's Pipeline Account Status. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=CoInvestorFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=CoInvestorFieldNames.PIPELINE_ACCOUNT,
                query_data=pipeline_account
            )
        ])

    def add(self,name:str,pipeline_account:bool) -> 'CoInvestor':
        """
            Creates a new Co-Investor.

            :param name: The new Co-Investor's Name
            :param pipeline_account: The new Co-Investor's Pipeline Account Status

            :return: The newly created Co-Investor
        """
        return super().add(
            document_data={
                CoInvestorFieldNames.NAME: name,
                CoInvestorFieldNames.PIPELINE_ACCOUNT: pipeline_account
            }
        )
