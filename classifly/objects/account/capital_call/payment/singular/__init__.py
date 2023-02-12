from typing import Dict

from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.account.capital_call.singular import CapitalCall
from classifly.objects.account.fund.singular import Fund
from classifly.objects.account.limited_partner.singular import LimitedPartner

from classifly.objects.account.capital_call.payment.constants import COLLECTION_PATH

class CapitalCallPayment(ClassiflyDocumentReference):
    """
        A Capital Call Payment. Represents the Limited Partner's Individual Capital Obligation to the fund
    """
    capital_call: CapitalCall = FirestoreProperty("Account", CapitalCall) #: The Capital Call the Limited Partner is responsible for
    fund: Fund = FirestoreProperty("Funds_Dropdown",Fund) #: The Fund the Capital Call originates from
    amount: float = FirestoreProperty("Amount", float) #: The Amount the Individal Investor is responsible to pay the Fund.
    banking_metadata: Dict = FirestoreProperty("Banking Metadata",dict) #: Once the Capital Call has been paid, this field will display metadata related to how the Capital Call was paid.
    limited_partner: LimitedPartner = FirestoreProperty("Limited_Partner", LimitedPartner) #: The Limited Partner Responsible for paying the Capital Call.
    paid: bool = FirestoreProperty("Paid",bool) #: Whether the Capital Call has been paid by the Limited Partner
    payment_date: DatetimeWithNanoseconds = FirestoreProperty("Payment Date", DatetimeWithNanoseconds) #: When the Limited Partner paid the Capital Call

    def __init__(self, *args, capital_call_payment_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(*(COLLECTION_PATH + [capital_call_payment_id]))
