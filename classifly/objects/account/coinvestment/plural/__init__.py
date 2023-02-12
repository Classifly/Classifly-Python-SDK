"""
    Classifly Co-Investments Object Representation
"""
from typing import List
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.coinvestor.singular import CoInvestor
from classifly.objects.account.portfolio_company.singular import PortfolioCompany

from classifly.objects.account.coinvestment.constants import COLLECTION_PATH, CoInvestmentFieldNames
from classifly.objects.account.coinvestment.utils import convert_to_coinvestment
from classifly.objects.account.coinvestment.singular import CoInvestment

class CoInvestments(CoreClassiflyCollectionReference):
    """
        Classifly Co-Investments. Used to retrieve Co-Investments, either all co-investments or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_coinvestment
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CoInvestment']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class CoInvestmentsQuery(Query):
            @convert_to_coinvestment
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CoInvestment']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return CoInvestmentsQuery(
            parent=self
        )

    def get_records(self,co_investor:FirestoreQueryData=None,portfolio_company:FirestoreQueryData=None) -> List['CoInvestment']:
        """
            Gets all Co-Investment records matching the specified filters.

            :param co_investor: The filter on the Co-Investment's Co-Investor. Default: None (No filters)
            :param portfolio_company: The filter on the Co-Investment's Portfolio Company. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=CoInvestmentFieldNames.CO_INVESTOR,
                query_data=co_investor
            ),
            FirestoreWhereQueryData(
                field_name=CoInvestmentFieldNames.PORTFOLIO_COMPANY,
                query_data=portfolio_company
            )
        ])

    def add(self,co_investor:CoInvestor,portfolio_company:PortfolioCompany) -> 'CoInvestment':
        """
            Creates a new Co-Investment.

            :param co_investor: The new Co-Investment's Co-Investor
            :param portfolio_company: The new Co-Investments's Portfolio Company

            :return: The newly created Co-Investment
        """
        return super().add(
            document_data={
                CoInvestmentFieldNames.CO_INVESTOR: co_investor,
                CoInvestmentFieldNames.PORTFOLIO_COMPANY: portfolio_company
            }
        )
