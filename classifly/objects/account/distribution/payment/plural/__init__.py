"""
    Classifly Distribution Payments Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.distribution.payment.constants import COLLECTION_PATH, DistributionPaymentFieldNames
from classifly.objects.account.distribution.payment.utils import convert_to_distribution_payment
from classifly.objects.account.distribution.payment.singular import DistributionPayment

from classifly.objects.account.distribution.singular import Distribution

if TYPE_CHECKING:
    from classifly.objects.account.limited_partner.singular import LimitedPartner
    from classifly.objects.account.fund.singular import Fund

class DistributionPayments(CoreClassiflyCollectionReference):
    """
        Classifly Distribution Payments. Used to retrieve Distribution Payments, either all Distribution Payments or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_distribution_payment
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['DistributionPayment']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class DistributionPaymentsQuery(Query):
            @convert_to_distribution_payment
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['DistributionPayment']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return DistributionPaymentsQuery(
            parent=self
        )

    def get_records(self,distribution:FirestoreQueryData=None,fund:FirestoreQueryData=None,amount:FirestoreQueryData=None,banking_metadata:FirestoreQueryData=None,limited_partner:FirestoreQueryData=None,paid:FirestoreQueryData=None,payment_date:FirestoreQueryData=None) -> List['DistributionPayment']:
        """
            Gets all Distribution Payment records matching the specified filters.

            :param distribution: The filter on the Distribution Payment's Distribution. Default: None (No filters)
            :param fund: The filter on the Distribution Payment's Fund. Default: None (No filters)
            :param amount: The filter on the Distribution Payment's Amount. Default: None (No filters)
            :param banking_metadata: The filter on the Distribution Payment's Banking Metadata. Default: None (No filters)
            :param limited_partner: The filter on the Distribution Payment's Limited Partner. Default: None (No filters)
            :param paid: The filter on the Distribution Payment's Payment Status. Default: None (No filters)
            :param paid: The filter on the Distribution Payment's Payment Date. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.DISTRIBUTION,
                query_data=distribution
            ),
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.FUND,
                query_data=fund
            ),
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.AMOUNT,
                query_data=amount
            ),
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.BANKING_METADATA,
                query_data=banking_metadata
            ),
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.LIMITED_PARTNER,
                query_data=limited_partner
            ),
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.PAID,
                query_data=paid
            ),
            FirestoreWhereQueryData(
                field_name=DistributionPaymentFieldNames.PAYMENT_DATE,
                query_data=payment_date
            ),
        ])

    def add(self,distribution:Distribution,fund:'Fund',amount:float,banking_metadata:dict,limited_partner:'LimitedPartner',paid:bool,payment_date:DatetimeWithNanoseconds=None) -> 'DistributionPayment':
        """
            Creates a new Distribution Payment.

            :param distribution: The new Distribution Payment's Distribution
            :param fund: The new Distribution Payment's Fund
            :param amount: The new Distribution Payment's Amount
            :param banking_metadata: The new Distribution Payment's Banking Metadata
            :param limited_partner: The new Distribution Payment's Limited Partner
            :param paid: The new Distribution Payment's Payment Status
            :param payment_date: The new Distribution Payment's Payment Date

            :return: The newly created Distribution
        """
        return super().add(
            document_data={
                DistributionPaymentFieldNames.DISTRIBUTION: distribution,
                DistributionPaymentFieldNames.FUND: fund,
                DistributionPaymentFieldNames.AMOUNT: amount,
                DistributionPaymentFieldNames.BANKING_METADATA: banking_metadata,
                DistributionPaymentFieldNames.LIMITED_PARTNER: limited_partner,
                DistributionPaymentFieldNames.PAID: paid,
                DistributionPaymentFieldNames.PAYMENT_DATE: payment_date
            }
        )
