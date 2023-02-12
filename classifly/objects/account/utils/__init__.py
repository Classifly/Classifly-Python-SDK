"""
    Classifly Account Object Utilities
"""
from typing import List, Type, TYPE_CHECKING

from google.cloud.firestore import FirestoreProperty

from classifly.objects.account.utils.dataclass.account_statuses import AccountStatuses
from classifly.objects.utils.document_reference.standard import ClassiflyDocumentReference
from classifly.objects.modal import Modal
from classifly.objects.modal.section.input import Input
from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference

if TYPE_CHECKING:
    from classifly.objects.user.singular import User

class ClassiflyAccountDocumentReference(ClassiflyDocumentReference):
    """
        A Classifly Account Document Reference object. In this context an Account is any Object within the "/Accounts" Path of Classifly's Firestore Database (Venture Firm, Activity, etc.).

        A Classifly Account Document Reference can be initialized 2 different ways.

        Option 1 -> Convert a Classifly Document Reference to a Classifly Account Document Reference:
            :param ClassiflyDocumentReference _: The Classifly Document Reference to be converted

        Option 2 -> Key-word Argument Based:
            :param str account_name: The Account's name. Ex: Activity, Capital Call, etc.
            :param str document_id: The Account's Id.
    """

    #To-Do: Fix Recurision Issue
    # accessible_firms: List['ClassiflyAccountDocumentReference'] = FirestoreProperty("accessible_firms",ClassiflyAccountDocumentReference) #: The Classifly Accounts that can access view the document's data

    def __init__(self, *args,**kwargs):
        if len(args) == 1:
            classifly_document_reference: ClassiflyDocumentReference = args[0]
            account_name = classifly_document_reference.parent.parent.id
            document_id = classifly_document_reference.id
        else:
            account_name = kwargs["account_name"]
            document_id = kwargs["document_id"]

        super().__init__(*('Accounts', account_name,'Entities', document_id))

class ClassiflyPipelineAccountDocumentReference(ClassiflyAccountDocumentReference):
    pipeline_account: bool = FirestoreProperty("Pipeline Account", bool)
    account_status: AccountStatuses = FirestoreProperty("Account_Status", AccountStatuses)

class ClassiflyUserEnabledPipelineAccountDocumentReference(ClassiflyPipelineAccountDocumentReference):
    users_invited: bool = FirestoreProperty("users_invited",bool)

    def get_people(self):
        """
            Lists all of the People tied to the Account
        """
        from classifly.objects.account.person.singular import Person
        return [
            Person(person_id=person.id) for person in CoreClassiflyCollectionReference("Accounts","People","Entities").where("Account","array_contains",self).stream()
        ]

    def get_users(self):
        """
            Lists all of the Classifly Users tied to the Account
        """
        from classifly.objects.user.singular import User
        return [
            User(user) for user in CoreClassiflyCollectionReference("Users").where("Connected_Accounts","array_contains",self).stream()
        ]

    def invite_users(self):
        """
            TO-DO: This function is still not implemented.

            Invites all of the People connected to the Account and creates/retrieves them as users and adds each User to the Account
        """
        if self.users_invited:
            raise Exception("Users were already invited to this account.")

        for person in self.get_people():
            #Create/Get the Person's User profile based on email address then add the User to the Account
            pass

        self.users_invited = True
        raise NotImplementedError()

    def add_user(self,user:'User'):
        raise NotImplementedError()


class ClassiflyAccountObjects(ClassiflyDocumentReference):
    """
        Classifly Account Objects:
            This is an Account Collection within Classifly's Firestore Database. Ex: "Accounts/Venture Firms"
    """
    modal: Modal = FirestoreProperty("Data Structure", Modal) #: The Modal assigned to the Account Object to create/edit an Account Entity's Data
    fields_to_display: List[Input] = FirestoreProperty("Fields to Display",List[Input])#: The Inputs to display when showing a list of Account Entities. Ex: The fields contained in the table of Limited Partners
    plural: str = FirestoreProperty("Plural",str) #: The Plural name of the Account. Ex: Venture Firms
    singular: str = FirestoreProperty("Singluar",str) #: The singular name of the Account: Ex: Venture Firm
    activity_enabled: bool = FirestoreProperty("activity_enabled",bool) #: Whether Activies can be attributed to the Account's Entities
    include_in_search: bool = FirestoreProperty("Include in Search",bool) #: Whether to include the Account's Entities in the search bar of the Classifly Web Portal
    include_on_map: bool = FirestoreProperty("Include on Map", bool) #: Whether to include the Account's Entities on the Map for Venture Firms in the Classifly Web Portal.

    def __init__(self, singular_object:Type[ClassiflyAccountDocumentReference]) -> None:
        super().__init__(*("Accounts",singular_object.account_name))
        self.singular_object = singular_object

    def get_entities(self) -> List['ClassiflyAccountObjects']:
        """
            All of the Entities within the Account
        """
        return [
            self.singular_object(entity.id) for entity in self.collection("Entities").get()
        ]

if __name__ == "__main__":
    CoreClassiflyCollectionReference("Users")
