"""
    Limited Partner - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyUserEnabledPipelineAccountDocumentReference
from classifly.objects.account.limited_partner.constants import LimitedPartnerFieldNames

class LimitedPartner(ClassiflyUserEnabledPipelineAccountDocumentReference):
    """
        A Limited Partner / Investor in Classifly.
    """
    # address: FirestoreAddress = FirestoreProperty("Address_Google", FirestoreAddress)
    affiliation: str = FirestoreProperty(LimitedPartnerFieldNames.AFFILIATION, str) #: How the Limited Partner is Affiliated to a Venture Firm.
    investor_type: str = FirestoreProperty(LimitedPartnerFieldNames.INVESTOR_TYPE, str) #: The Type of Limited Partner. Ex: "Individual" or "Institution"
    name: str = FirestoreProperty(LimitedPartnerFieldNames.NAME, str) #: The Limited Partner's Name

    def __init__(self, *args, limited_partner_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Limited_Partners",document_id=limited_partner_id)

    def get_reports(self):
        """
            To-Do: This function is not yet implemented
        """
