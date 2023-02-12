from typing import List

from classifly.objects.user.dataclass.account import UserAccount
from classifly.objects.utils.document_reference.core import CoreClassiflyDocumentReference
from classifly.objects.utils.properties.blob import ClassiflyBlob
from classifly.objects.user.constants import UserFieldNames, COLLECTION_PATH

from classifly.objects.user.singular.utils.properties.email import ClassiflyUserEmailProperty
from classifly.objects.user.singular.utils.properties.name import ClassiflyUserNameProperty
from classifly.objects.user.singular.utils.properties.profile_picture import ClassiflyUserProfilePictureProperty

class User(CoreClassiflyDocumentReference):
    """
        A Classifly User. Users are able to access data via the Classifly Web Portal.
    """
    email: str = ClassiflyUserEmailProperty() #: The User's Email Address (used to login)
    first_name: str = ClassiflyUserNameProperty(UserFieldNames.FIRST_NAME) #: The User's First Name
    last_name: str = ClassiflyUserNameProperty(UserFieldNames.LAST_NAME) #: The User's Last Name
    profile_picture: ClassiflyBlob = ClassiflyUserProfilePictureProperty()

    @property
    def accounts(self) -> List[UserAccount]:
        """
            The accounts the user has access to. In this context, an account is a Classifly Object that has access to the web portal (Venture Firm, Limited Partner, Portfolio Company).
        """
        data = self.get().to_dict()
        account_info = data["Connected_Accounts_Info"]
        return [
            UserAccount(
                user=self,
                admin=account_info[account.path]["Admin"],
                account=account
            )
            for account in data[UserFieldNames.CONNECTED_ACCOUNTS]
        ]

    def __init__(self, *args, user_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],CoreClassiflyDocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(*COLLECTION_PATH + [user_id])

if __name__ == "__main__":
    User(user_id="OXZuq7rvimh8jr3qFUO6GvxBLfi2").email = "ryan@compertore.com"