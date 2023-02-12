from typing import Callable, Any

from google.cloud.firestore import FirestoreProperty


class ClassiflyUserProperty(FirestoreProperty):
    def __init__(self, db_name: str):
        from classifly.objects.user.singular import User
        super().__init__(db_name, User)