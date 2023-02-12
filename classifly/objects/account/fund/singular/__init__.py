"""
    Fund - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyPipelineAccountDocumentReference
from classifly.objects.account.fund.dataclass.waterfall_types import WaterfallTypes
from classifly.objects.account.fund.constants import FundFieldNames

class Fund(ClassiflyPipelineAccountDocumentReference):
    """
        A Fund.
    """
    status: str = FirestoreProperty(FundFieldNames.STATUS,str) #: The Fund's Status
    carried_interest: float = FirestoreProperty(FundFieldNames.CARRIED_INTEREST,float) #: The Carried Interest Percentage of the Fund. Ex: 20%
    general_partner_commitment_amount: float = FirestoreProperty(FundFieldNames.GENERAL_PARTNER_COMMITMENT_AMOUNT, float) #: The GP's Commitment to the fund
    general_partner_name: str = FirestoreProperty(FundFieldNames.GENERAL_PARTNER_NAME,str) #: The GP's Name
    management_fee: float = FirestoreProperty(FundFieldNames.MANAGEMENT_FEE,float) #: The Fund's Annual Management Fee. Ex: 2%
    name: str = FirestoreProperty(FundFieldNames.NAME,str) #: The Fund's Name
    preferred_return: float = FirestoreProperty(FundFieldNames.PREFERRED_RETURN, float) #: The Fund's preferred return
    waterfall_type: WaterfallTypes = FirestoreProperty(FundFieldNames.WATERFALL_TYPE,WaterfallTypes) #: The waterfall type to clear the Fund's Preferred Return. Ex: American or European

    def __init__(self, *args, fund_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Funds",document_id=fund_id)

    def get_metrics(self):
        """
            To-Do: This function is not yet implemented
        """
