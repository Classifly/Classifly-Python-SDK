"""
    Capital Call - Object Representation
"""
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.fund.singular import Fund

from classifly.objects.account.capital_call.constants import CapitalCallFieldNames

class CapitalCall(ClassiflyAccountDocumentReference):
    """
        A Capital Call. Capital Calls are used to recieve a Fund's capital from Limited Partners
    """
    fund: Fund = FirestoreProperty(CapitalCallFieldNames.FUND,Fund) #: The Fund the Capital Call originates from
    purpose: str = FirestoreProperty(CapitalCallFieldNames.PURPOSE,str) #: The Reason the Capital Call has occured.
    due_date: DatetimeWithNanoseconds = FirestoreProperty(CapitalCallFieldNames.DUE_DATE,DatetimeWithNanoseconds) # When the Capital Call is Due
    name: str = FirestoreProperty(CapitalCallFieldNames.NAME,str) #: The Capital Call's Name

    def __init__(self, *args, capital_call_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Capital_Calls",document_id=capital_call_id)