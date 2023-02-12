from typing import List

from google.cloud.firestore import FirestoreProperty

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.modal.section.utils.section_input import SectionInput

class Section(ClassiflyDocumentReference):
    name: str = FirestoreProperty("Name",str) #: The Sections name

    def __init__(self, section_id:str) -> None:
        super().__init__(*('Modal_Data', "Sections",'Entities', section_id))

    def inputs(self) -> List[SectionInput]:
        """
            All of the Inputs within the section
        """
        return [
            SectionInput(
                self.id, section_input.id
            )
            for section_input in self.collection("Inputs").get()
        ]
