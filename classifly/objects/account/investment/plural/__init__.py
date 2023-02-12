"""
    Classifly Investments Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.investment.constants import COLLECTION_PATH, InvestmentFieldNames
from classifly.objects.account.investment.utils import convert_to_investment
from classifly.objects.account.investment.singular import Investment

if TYPE_CHECKING:
    from classifly.objects.account.investment.dataclass.investment_vehicles import InvestmentVehicles
    from classifly.objects.account.fund.singular import Fund
    from classifly.objects.account.portfolio_company.singular import PortfolioCompany
    from google.api_core.datetime_helpers import DatetimeWithNanoseconds

class Investments(CoreClassiflyCollectionReference):
    """
        Classifly Investments. Used to retrieve Investments, either all Investments or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_investment
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Investment']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class InvestmentsQuery(Query):
            @convert_to_investment
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Investment']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return InvestmentsQuery(
            parent=self
        )

    def get_records(self,portfolio_company:FirestoreQueryData=None,amount:FirestoreQueryData=None,fund:FirestoreQueryData=None,date:FirestoreQueryData=None,vehicle:FirestoreQueryData=None,name:FirestoreQueryData=None) -> List['Investment']:
        """
            Gets all Investment records matching the specified filters.

            :param portfolio_company: The filter on the Investment's Portfolio Company. Default: None (No filters)
            :param amount: The filter on the Investment's Amount. Default: None (No filters)
            :param fund: The filter on the Investment's Fund. Default: None (No filters)
            :param date: The filter on the Investment's date. Default: None (No filters)
            :param vehicle: The filter on the Investment's Vehicle. Default: None (No filters)
            :param name: The filter on the Investment's name. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=InvestmentFieldNames.PORTFOLIO_COMPANY,
                query_data=portfolio_company
            ),
            FirestoreWhereQueryData(
                field_name=InvestmentFieldNames.AMOUNT,
                query_data=amount
            ),
            FirestoreWhereQueryData(
                field_name=InvestmentFieldNames.FUND,
                query_data=fund
            ),
            FirestoreWhereQueryData(
                field_name=InvestmentFieldNames.DATE,
                query_data=date
            ),
            FirestoreWhereQueryData(
                field_name=InvestmentFieldNames.VEHICLE,
                query_data=vehicle
            ),
            FirestoreWhereQueryData(
                field_name=InvestmentFieldNames.NAME,
                query_data=name
            ),
        ])

    def add(self,portfolio_company:'PortfolioCompany',amount:float,fund:'Fund',date:'DatetimeWithNanoseconds',vehicle:'InvestmentVehicles',name:str) -> 'Investment':
        """
            Creates a new Investment.

            :param portfolio_company: The new Investment's Portfolio Company
            :param amount: The new Investment's Amount
            :param fund: The new Investment's Fund
            :param date: The new Investment's Date
            :param vehicle: The new Investment's Vehicle
            :param name: The new Investment's Name

            :return: The newly created Investment
        """
        return super().add(
            document_data={
                InvestmentFieldNames.PORTFOLIO_COMPANY: portfolio_company,
                InvestmentFieldNames.AMOUNT: amount,
                InvestmentFieldNames.FUND: fund,
                InvestmentFieldNames.DATE: date,
                InvestmentFieldNames.VEHICLE: vehicle,
                InvestmentFieldNames.NAME: name
            }
        )
