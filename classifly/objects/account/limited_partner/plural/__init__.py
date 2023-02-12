"""
    Classifly Limited Partners Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.limited_partner.constants import COLLECTION_PATH, LimitedPartnerFieldNames
from classifly.objects.account.limited_partner.utils import convert_to_limited_partner
from classifly.objects.account.limited_partner.singular import LimitedPartner

if TYPE_CHECKING:
    from classifly.objects.account.investment.dataclass.investment_vehicles import InvestmentVehicles
    from classifly.objects.account.fund.singular import Fund
    from classifly.objects.account.portfolio_company.singular import PortfolioCompany
    from google.api_core.datetime_helpers import DatetimeWithNanoseconds

class LimitedPartners(CoreClassiflyCollectionReference):
    """
        Classifly Limited Partners. Used to retrieve Limited Partners, either all Limited Partners or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_limited_partner
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['LimitedPartner']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class LimitedPartnersQuery(Query):
            @convert_to_limited_partner
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['LimitedPartner']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return LimitedPartnersQuery(
            parent=self
        )

    def get_records(self,affiliation:FirestoreQueryData=None,investor_type:FirestoreQueryData=None,name:FirestoreQueryData=None) -> List['LimitedPartner']:
        """
            Gets all Limited Partner records matching the specified filters.

            :param affiliation: The filter on the Limited Partner's Affiliation. Default: None (No filters)
            :param investor_type: The filter on the Limited Partner's Investor Type. Default: None (No filters)
            :param name: The filter on the Limited Partner's name. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=LimitedPartnerFieldNames.AFFILIATION,
                query_data=affiliation
            ),
            FirestoreWhereQueryData(
                field_name=LimitedPartnerFieldNames.INVESTOR_TYPE,
                query_data=investor_type
            ),
            FirestoreWhereQueryData(
                field_name=LimitedPartnerFieldNames.NAME,
                query_data=name
            )
        ])

    def add(self,affiliation:str,investor_type:str,name:str) -> 'LimitedPartner':
        """
            Creates a new Limited Partner.

            :param affiliation: The new Limited Partner's Affiliation
            :param investor_type: The new Limited Partner's Investor Type
            :param name: The new Limited Partner's name

            :return: The newly created Investment
        """
        return super().add(
            document_data={
                LimitedPartnerFieldNames.AFFILIATION: affiliation,
                LimitedPartnerFieldNames.INVESTOR_TYPE: investor_type,
                LimitedPartnerFieldNames.NAME: name
            }
        )
