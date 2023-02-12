"""
    Classifly Object Utilities
"""
from google.cloud.firestore import DocumentReference, DocumentSnapshot

from classifly.objects.utils.properties.blob import FirestoreBlobProperty
from classifly.utils.google.firestore.client import CLIENT

class CoreClassiflyDocumentReference(DocumentReference):
    """
        A Document Reference in Classifly's Firestore Database
    """
    def __init__(self, *path) -> None:
        if len(path) == 1:

            match path[0]:
                #Check if only argument is a DocumentSnapshot, if so Get the Reference's Path
                case DocumentSnapshot():
                    path = path[0].reference.path.split("/")
                #Check if only argument is a DocumentReference, if so get the Reference's path
                case DocumentReference():
                    path = path[0].path.split("/")
        super().__init__(*path, client=CLIENT)

    def delete(self):
        """
            Deletes a Classifly Document Reference and and external objects (ex: Storage Blobs) linked to the document
        """
        for _, attribute_value in vars(self):
            match attribute_value:
                case FirestoreBlobProperty():
                    attribute_value.delete()
        return super().delete()
