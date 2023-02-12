from typing import TYPE_CHECKING
from dataclasses import dataclass

from google.cloud.firestore_v1 import ArrayRemove

if TYPE_CHECKING:
    from classifly.objects.account.utils import ClassiflyAccountDocumentReference
    from classifly.objects.user.singular import User

@dataclass
class UserAccount:
    user: 'User' #: The Classifly User the User Account is tied to
    admin: bool #: Whether the user is an admin of the account
    account: 'ClassiflyAccountDocumentReference' #: The Account the user has access to

    def delete(self):
        """
            Remove's the users access to the Account
        """
        connected_accounts_info = self.user.get().to_dict()["Connected_Accounts_Info"]
        connected_accounts_info.pop(self.account.path,None)

        self.user.update({
            "Connected_Accounts" : ArrayRemove([self.account]),
            "Connected_Accounts_Info": connected_accounts_info
        })

    def convert_status(self) -> bool:
        """
            Either adds or revokes the user's admin privileges for the account

            :return: The User's updated status
        """
        connected_accounts_info = self.user.get().to_dict()["Connected_Accounts_Info"]
        new_admin_status = not connected_accounts_info[self.account.path]["Admin"]
        connected_accounts_info[self.account.path]["Admin"] = new_admin_status

        self.user.update({
            "Connected_Accounts_Info": connected_accounts_info
        })
        return new_admin_status
