from typing import Dict

from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.account.distribution.singular import Distribution
from classifly.objects.account.fund.singular import Fund
from classifly.objects.account.limited_partner.singular import LimitedPartner
from classifly.objects.account.distribution.payment.constants import COLLECTION_PATH


class DistributionPayment(ClassiflyDocumentReference):
    """
        A Distribution Payment. Represents the Fund's return of capital to the Limited Partner
    """
    distribution: Distribution = FirestoreProperty("Account", Distribution) #: The Distribution the Limited Partner is recieving
    fund: Fund = FirestoreProperty("Funds_Dropdown",Fund) #: The Fund the Distribution originates from
    amount: float = FirestoreProperty("Amount", float) #: The dollar amount fund returns to the Limited Partner
    banking_metadata: Dict = FirestoreProperty("Banking Metadata",dict) #: Once the Distribution has been paid, this field will display metadata related to how the Distribution was paid.
    limited_partner: LimitedPartner = FirestoreProperty("Limited_Partner", LimitedPartner) #: The Limited Partner Responsible related to the Distribution.
    paid: bool = FirestoreProperty("Paid",bool) #: Whether the Distribution has been paid by the Fund
    payment_date: DatetimeWithNanoseconds = FirestoreProperty("Payment Date", DatetimeWithNanoseconds) #: When the Fund paid the Limited Partner

    def __init__(self, *args, distribution_payment_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(*(COLLECTION_PATH + [distribution_payment_id]))