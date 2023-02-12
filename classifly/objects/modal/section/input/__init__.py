from google.cloud.firestore import FirestoreProperty

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference

class Input(ClassiflyDocumentReference):
    name: str = FirestoreProperty("Name",str) #: The Input's Name
    type: str = FirestoreProperty("Type",str) #: The Type of Input. Ex: Text, Select, etc.

    def __init__(self, input_id:str) -> None:
        super().__init__(*('Modal_Data', "Inputs",'Entities', input_id))