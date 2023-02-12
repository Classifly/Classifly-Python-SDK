"""
    Person - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.person.constants import PersonFieldNames

class Person(ClassiflyAccountDocumentReference):
    """
        A Person. People are typically connected to an Account Object (Co-Investor, Portfolio Company, etc.). Note: A Person is not a user. A Person is similar to the Contact Object within Salesforce
    """
    email: str = FirestoreProperty(PersonFieldNames.EMAIL, str) #: The Person's Email Address

    def __init__(self, *args, person_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="People",document_id=person_id)