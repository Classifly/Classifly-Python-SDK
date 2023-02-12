"""
    Venture Firm - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.venture_firm.constants import VentureFirmFieldNames

class VentureFirm(ClassiflyAccountDocumentReference):
    """
        A Classifly Venture Firm
    """
    name: str = FirestoreProperty(VentureFirmFieldNames.NAME,str) #: The Venture Firm's Name
    primary_color: str = FirestoreProperty(VentureFirmFieldNames.PRIMARY_COLOR, str) #: The Venture Firm's Primary Color (Hex Representation). Used to theme the Classifly Web Portal

    def __init__(self, *args, venture_firm_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Venture_Firms",document_id=venture_firm_id)
