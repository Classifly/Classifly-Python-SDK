from google.cloud.firestore import FirestoreProperty

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.modal.section.input import Input

class SectionInput(ClassiflyDocumentReference):
    input: Input = FirestoreProperty("Input", Input) #: The Input within the Section
    position: int = FirestoreProperty("Position", int) #: The Position of the Input within the section
    required: bool = FirestoreProperty("Required", bool) #: Whether the Input is required to submit the Modal

    def __init__(self, section_id:str, section_input_id:str) -> None:
        super().__init__(*('Modal_Data', "Sections",'Entities', section_id, "Inputs", section_input_id))
