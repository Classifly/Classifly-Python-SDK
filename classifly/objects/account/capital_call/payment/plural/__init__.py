"""
    Classifly Capital Call Payments Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.capital_call.payment.constants import COLLECTION_PATH, CapitalCallPaymentFieldNames
from classifly.objects.account.capital_call.payment.utils import convert_to_capital_call_payment
from classifly.objects.account.capital_call.payment.singular import CapitalCallPayment

if TYPE_CHECKING:
    from google.api_core.datetime_helpers import DatetimeWithNanoseconds
    from classifly.objects.account.capital_call.singular import CapitalCall
    from classifly.objects.account.fund.singular import Fund
    from classifly.objects.account.limited_partner.singular import LimitedPartner

class CapitalCallPayments(CoreClassiflyCollectionReference):
    """
        Classifly Capital Call Payments. Used to retrieve Capital Call Payments, either all Capital Call Payments or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_capital_call_payment
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CapitalCallPayment']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class CapitalCallPaymentsQuery(Query):
            @convert_to_capital_call_payment
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CapitalCallPayment']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return CapitalCallPaymentsQuery(
            parent=self
        )

    def get_records(self,capital_call:FirestoreQueryData=None,fund:FirestoreQueryData=None,amount:FirestoreQueryData=None,banking_metadata:FirestoreQueryData=None,limited_partner:FirestoreQueryData=None,paid:FirestoreQueryData=None,payment_date:FirestoreQueryData=None) -> List['CapitalCallPayment']:
        """
            Gets all Capital Call Payment records matching the specified filters.

            :param capital_call: The filter on the Capital Call Payment's Capital Call. Default: None (No filters)
            :param fund: The filter on the Capital Call Payment's Fund. Default: None (No filters)
            :param amount: The filter on the Capital Call Payment's Amount. Default: None (No filters)
            :param banking_metadata: The filter on the Capital Call Payment's Banking Metadata. Default: None (No filters)
            :param limited_partner: The filter on the Capital Call Payment's Limited Partner. Default: None (No filters)
            :param paid: The filter on the Capital Call Payment's Payment Status. Default: None (No filters)
            :param payment_date: The filter on the Capital Call Payment's Payment Date. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.CAPITAL_CALL,
                query_data=capital_call
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.FUND,
                query_data=fund
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.AMOUNT,
                query_data=amount
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.BANKING_METADATA,
                query_data=banking_metadata
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.LIMITED_PARTNER,
                query_data=limited_partner
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.PAID,
                query_data=paid
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallPaymentFieldNames.PAYMENT_DATE,
                query_data=payment_date
            ),
        ])

    def add(self,capital_call:'CapitalCall'=None,fund:'Fund'=None,amount:float=None,banking_metadata:dict=None,limited_partner:'LimitedPartner'=None,paid:bool=None,payment_date:'DatetimeWithNanoseconds'=None) -> 'CapitalCallPayment':
        """
            Creates a new Capital Call Payment.

            :param capital_call: The new Capital Call Payment's Capital Call
            :param fund: The new Capital Call Payment's Fund
            :param amount: The new Capital Call Payment's Amount
            :param banking_metadata: The new Capital Call Payment's Banking Metadata
            :param limited_partner: The new Capital Call Payment's Limited Partner
            :param paid: The new Capital Call Payment's Payment Status
            :param payment_date: The new Capital Call Payment's Payment Date

            :return: The newly created Capital Call Payment
        """
        return super().add(
            document_data={
                CapitalCallPaymentFieldNames.CAPITAL_CALL: capital_call,
                CapitalCallPaymentFieldNames.FUND: fund,
                CapitalCallPaymentFieldNames.AMOUNT: amount,
                CapitalCallPaymentFieldNames.BANKING_METADATA: banking_metadata,
                CapitalCallPaymentFieldNames.LIMITED_PARTNER: limited_partner,
                CapitalCallPaymentFieldNames.PAID: paid,
                CapitalCallPaymentFieldNames.PAYMENT_DATE: payment_date,
            }
        )
