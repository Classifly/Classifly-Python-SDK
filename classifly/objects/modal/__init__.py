"""
    Classifly Modal Object Representation
"""

from typing import List

from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.modal.utils.modal_section import ModalSection

class Modal(ClassiflyDocumentReference):
    def __init__(self, modal_id:str) -> None:
        super().__init__(*('Modal_Data', "Data_Structures",'Entities', modal_id))

    def sections(self) -> List[ModalSection]:
        """
            All of the Sections within the Modal
        """
        return [
            ModalSection(
                self.id,modal_section.id
            )
            for modal_section in self.collection("Sections").get()
        ]