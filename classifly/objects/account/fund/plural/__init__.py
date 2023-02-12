"""
    Classifly Distributions Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.fund.constants import COLLECTION_PATH, FundFieldNames
from classifly.objects.account.fund.utils import convert_to_fund
from classifly.objects.account.fund.singular import Fund

if TYPE_CHECKING:
    from classifly.objects.account.fund.dataclass.waterfall_types import WaterfallTypes

class Funds(CoreClassiflyCollectionReference):
    """
        Classifly Funds. Used to retrieve Funds, either all Funds or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_fund
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Fund']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class FundsQuery(Query):
            @convert_to_fund
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Fund']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return FundsQuery(
            parent=self
        )

    def get_records(self,status:FirestoreQueryData=None,carried_interest:FirestoreQueryData=None,general_partner_commitment_amount:FirestoreQueryData=None,general_partner_name:FirestoreQueryData=None,management_fee:FirestoreQueryData=None,name:FirestoreQueryData=None,preferred_return:FirestoreQueryData=None,waterfall_type:FirestoreQueryData=None) -> List['Fund']:
        """
            Gets all Fund records matching the specified filters.

            :param status: The filter on the Fund's status. Default: None (No filters)
            :param carried_interest: The filter on the Fund's Carried Interest Percentage. Default: None (No filters)
            :param general_partner_commitment_amount: The filter on the Fund's General Partner Commitment Amount. Default: None (No filters)
            :param general_partner_name: The filter on the Fund's General Partner Name. Default: None (No filters)
            :param management_fee: The filter on the Fund's Management Fee. Default: None (No filters)
            :param name: The filter on the Fund's name. Default: None (No filters)
            :param preferred_return: The filter on the Fund's status. Default: None (No filters)
            :param waterfall_type: The filter on the Fund's waterfall type. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=FundFieldNames.STATUS,
                query_data=status
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.CARRIED_INTEREST,
                query_data=carried_interest
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.GENERAL_PARTNER_COMMITMENT_AMOUNT,
                query_data=general_partner_commitment_amount
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.GENERAL_PARTNER_NAME,
                query_data=general_partner_name
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.MANAGEMENT_FEE,
                query_data=management_fee
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.PREFERRED_RETURN,
                query_data=preferred_return
            ),
            FirestoreWhereQueryData(
                field_name=FundFieldNames.WATERFALL_TYPE,
                query_data=waterfall_type
            ),
        ])

    def add(self,status:str,carried_interest:float,general_partner_commitment_amount:float,general_partner_name:str,managment_fee:float,name:str,preferred_return:float,waterfall_type:'WaterfallTypes') -> 'Fund':
        """
            Creates a new Fund.

            :param status: The new Fund's Status
            :param carried_interest: The new Fund's Carried Interest
            :param general_partner_commitment_amount: The new Fund's General Partner Commitment Amount
            :param general_partner_name: The new Fund's General Partner Name
            :param managment_fee: The new Fund's Management Fee
            :param name: The new Fund's Name
            :param preferred_return: The new Fund's Preferred Return
            :param waterfall_type: The new Fund's Waterfall Type

            :return: The newly created Fund
        """
        return super().add(
            document_data={
                FundFieldNames.STATUS: status,
                FundFieldNames.CARRIED_INTEREST: carried_interest,
                FundFieldNames.GENERAL_PARTNER_COMMITMENT_AMOUNT: general_partner_commitment_amount,
                FundFieldNames.GENERAL_PARTNER_NAME: general_partner_name,
                FundFieldNames.MANAGEMENT_FEE: managment_fee,
                FundFieldNames.NAME: name,
                FundFieldNames.PREFERRED_RETURN: preferred_return,
                FundFieldNames.WATERFALL_TYPE: waterfall_type
            }
        )
