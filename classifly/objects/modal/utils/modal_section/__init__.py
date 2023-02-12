from google.cloud.firestore import FirestoreProperty

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.modal.section import Section

class ModalSection(ClassiflyDocumentReference):
    section: Section = FirestoreProperty("Section",Section) #: The Section within the Modal
    position: int = FirestoreProperty("Position",int) #: The Section's position within the Modal

    def __init__(self, modal_id:str, section_id:str) -> None:
        super().__init__(*('Modal_Data', "Data_Structures",'Entities', modal_id, "Sections", section_id))