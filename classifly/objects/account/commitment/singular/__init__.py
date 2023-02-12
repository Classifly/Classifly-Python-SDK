"""
    Commitment - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.limited_partner.singular import LimitedPartner
from classifly.objects.account.fund.singular import Fund
from classifly.objects.account.commitment.constants import CommitmentFieldNames

class Commitment(ClassiflyAccountDocumentReference):
    """
        A Commitment. Represents a Limited Partner's commitment to a fund
    """
    limited_partner: LimitedPartner = FirestoreProperty(CommitmentFieldNames.LIMITED_PARTNER,LimitedPartner) #: The Limited Partner Committing Capital
    amount: float = FirestoreProperty(CommitmentFieldNames.AMOUNT,float) #: The Limited Partner's total commitment amount
    fund: Fund = FirestoreProperty(CommitmentFieldNames.FUND,Fund) #: The Fund the Limited Partner is committing to

    def __init__(self, *args, commitment_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Commitments",document_id=commitment_id)