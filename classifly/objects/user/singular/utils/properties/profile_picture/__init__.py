from typing import TYPE_CHECKING

from classifly.utils.google.firebase.auth import CLIENT as AUTH_CLIENT
from classifly.objects.user.constants import UserFieldNames
from classifly.objects.utils.properties.blob import FirestoreBlobProperty, ClassiflyBlob

if TYPE_CHECKING:
    from classifly.objects.user.singular import User

class ClassiflyUserProfilePictureProperty(FirestoreBlobProperty):
    def __init__(self):
        super().__init__(UserFieldNames.PROFILE_PICTURE)

    def fset(self):
        def set(user:'User',updated_profile_picture:ClassiflyBlob):
            super().fset()(user,updated_profile_picture)
            AUTH_CLIENT.update_user(
                uid=user.id,
                photo_url=updated_profile_picture.public_url
            )
        return set
