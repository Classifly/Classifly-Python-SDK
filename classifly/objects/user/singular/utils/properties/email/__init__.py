from typing import TYPE_CHECKING

from google.cloud.firestore import FirestoreProperty

from classifly.utils.google.firebase.auth import CLIENT as AUTH_CLIENT
from classifly.objects.user.constants import UserFieldNames

if TYPE_CHECKING:
    from classifly.objects.user.singular import User

class ClassiflyUserEmailProperty(FirestoreProperty):
    def __init__(self):
        super().__init__(UserFieldNames.EMAIL, str)

    def fset(self):
        parent = super()
        def set(user:'User',updated_email:str):
            parent.fset()(user,updated_email)
            AUTH_CLIENT.update_user(
                uid=user.id,
                email=updated_email
            )
        return set
