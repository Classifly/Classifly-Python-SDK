"""
    Research - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.utils.properties.blob import FirestoreBlobProperty, ClassiflyBlob
from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.research.constants import ResearchFieldNames

class Research(ClassiflyAccountDocumentReference):
    """
        A Classifly Research Object. Classifly Research is special type of document storage allowing Venture Firms to create a centralized repository for all proprietary research conducted by the firm. Ex: White Paper, Market Map, etc.
    """
    name: str = FirestoreProperty(ResearchFieldNames.NAME,str) #: The Research's Name
    document: ClassiflyBlob = FirestoreBlobProperty(ResearchFieldNames.DOCUMENT)

    def __init__(self, *args, research_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Research",document_id=research_id)
