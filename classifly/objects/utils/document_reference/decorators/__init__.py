from typing import Type, TYPE_CHECKING
from google.cloud.firestore import DocumentSnapshot

if TYPE_CHECKING:
    from classifly.objects.utils.document_reference.core import CoreClassiflyDocumentReference

def convert_to_classifly_object(classifly_object_type:Type['CoreClassiflyDocumentReference']):
    """
        Takes an Array of Document Snapshots and converts them to the specified Classifly Object (ex: 'User')
    """
    def convert_to_object(func):
        def object_conversion(*args,**kwargs):
            classifly_objects = []
            for document_snapshot in func(*args,**kwargs):
                if isinstance(document_snapshot,classifly_object_type):
                    classifly_objects.append(document_snapshot)
                elif isinstance(document_snapshot,DocumentSnapshot):
                    classifly_object = classifly_object_type(document_snapshot.reference)
                    classifly_object._document_snapshot = document_snapshot
                    classifly_objects.append(classifly_object)

            return classifly_objects
        return object_conversion
    return convert_to_object
