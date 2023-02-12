from typing import TYPE_CHECKING

from google.cloud.firestore import FirestoreProperty

from classifly.utils.google.firebase.auth import CLIENT as AUTH_CLIENT

if TYPE_CHECKING:
    from classifly.objects.user.singular import User

class ClassiflyUserNameProperty(FirestoreProperty):
    def __init__(self, db_name: str):
        super().__init__(db_name, str)

    def fset(self):
        def set(user:'User',val:str):
            super().fset()(user,val)
            AUTH_CLIENT.update_user(
                uid=user.id,
                display_name=f"{user.first_name} {user.last_name}"
            )
        return set
