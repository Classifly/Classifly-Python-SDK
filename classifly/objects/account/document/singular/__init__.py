"""
    Document - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.utils.properties.blob import FirestoreBlobProperty, ClassiflyBlob
from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.account.utils import ClassiflyAccountDocumentReference

from classifly.objects.account.document.constants import DocumentFieldNames

class Document(ClassiflyAccountDocumentReference):
    """
        A Document. Documents allow User's to store Files within Classifly.
    """
    name: str = FirestoreProperty(DocumentFieldNames.NAME,str) #: The Document's Name
    account: ClassiflyDocumentReference = FirestoreProperty(DocumentFieldNames.ACCOUNT, ClassiflyDocumentReference) #: The Account connected to the Document
    document: ClassiflyBlob = FirestoreBlobProperty(DocumentFieldNames.DOCUMENT) #: The Raw file

    def __init__(self, *args, document_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Documents",document_id=document_id)

if __name__ == "__main__":
    Document("4py5yFUFa4iYYUpN04FF").document.download()