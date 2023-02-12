from dataclasses import dataclass, asdict

from google.cloud.firestore import FirestoreProperty, DocumentReference
from google.cloud.storage import Blob

from classifly.utils.google.storage.client import CLIENT

@dataclass
class FirestoreDatabaseStorageRepresentation:
    bucket: str #: The Google Storage Bucket's name where the Blob is stored
    name: str #: The Blob's Name
    path: str #: The Blob's path within the Google Storage Bucket

    def get_blob(self):
        return ClassiflyBlob(name=self.path,bucket=CLIENT.bucket(self.bucket))

class ClassiflyBlob(Blob):

    def firestore_representation(self):
        return FirestoreDatabaseStorageRepresentation(
            bucket=self.bucket.name,
            name=self.file_name,
            path=self.name
        )

class FirestoreBlobProperty(FirestoreProperty):
    def __init__(self, db_name: str):
        super().__init__(db_name, dict)

    def fget(self):
        parent = super()
        def get(document_reference:DocumentReference):
            return FirestoreDatabaseStorageRepresentation(
                **parent.fget()(document_reference)
            ).get_blob()
        return get

    def fset(self):
        def set(document_reference:DocumentReference,val:ClassiflyBlob):
            return super().fset()(document_reference,asdict(val.firestore_representation()))
        return set
