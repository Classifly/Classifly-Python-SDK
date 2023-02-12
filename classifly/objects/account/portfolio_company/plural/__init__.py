"""
    Classifly Portfolio Companies Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.portfolio_company.constants import COLLECTION_PATH, PortfolioCompanyFieldNames
from classifly.objects.account.portfolio_company.utils import convert_to_portfolio_company
from classifly.objects.account.portfolio_company.singular import PortfolioCompany


class PortfolioCompanies(CoreClassiflyCollectionReference):
    """
        Classifly Portfolio Companies. Used to retrieve Portfolio Companies, either all Portfolio Companies or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_portfolio_company
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['PortfolioCompany']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class PortfolioCompaniesQuery(Query):
            @convert_to_portfolio_company
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['PortfolioCompany']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return PortfolioCompaniesQuery(
            parent=self
        )

    def get_records(self,about:FirestoreQueryData=None) -> List['PortfolioCompany']:
        """
            Gets all Portfolio Company records matching the specified filters.

            :param about: The filter on the Portfolio Company's About description. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=PortfolioCompanyFieldNames.ABOUT,
                query_data=about
            )
        ])

    def add(self,about:str) -> 'PortfolioCompany':
        """
            Creates a new Portfolio Company.

            :param about: The new Portfolio Company's About description

            :return: The newly created Portfolio Company
        """
        return super().add(
            document_data={
                PortfolioCompanyFieldNames.ABOUT: about,
            }
        )
