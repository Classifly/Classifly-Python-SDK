"""
    Classifly Users Object Representation
"""
from typing import List
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.properties.blob import ClassiflyBlob
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData
from classifly.utils.google.auth import CLIENT as AUTH_CLIENT

from classifly.objects.user.constants import UserFieldNames, COLLECTION_PATH
from classifly.objects.user.singular import User
from classifly.objects.user.plural.utils import convert_to_user

class Users(CoreClassiflyCollectionReference):
    """
        Classifly Users. Used to retrieve users, either all users or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_user
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['User']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class UsersQuery(Query):
            @convert_to_user
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['User']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return UsersQuery(
            parent=self
        )

    def get_records(self,first_name:FirestoreQueryData=None,last_name:FirestoreQueryData=None,email:FirestoreQueryData=None,connected_accounts:FirestoreQueryData=None) -> List['User']:
        """
            Gets all User records matching the specified filters.

            :param first_name: The filter on the User's first name. Default: None (No filters)
            :param last_name: The filter on the User's last name. Default: None (No filters)
            :param email: The filter on the User's email address. Default: None (No filters)
            :param connected_accounts: The filter on the User's connected accounts. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=UserFieldNames.FIRST_NAME,
                query_data=first_name
            ),
            FirestoreWhereQueryData(
                field_name=UserFieldNames.LAST_NAME,
                query_data=last_name
            ),
            FirestoreWhereQueryData(
                field_name=UserFieldNames.EMAIL,
                query_data=email
            ),
            FirestoreWhereQueryData(
                field_name=UserFieldNames.CONNECTED_ACCOUNTS,
                query_data=connected_accounts
            )
        ])

    def add(self,first_name:str,last_name:str,email:str,profile_picture:ClassiflyBlob=None) -> 'User':
        """
            Creates a new User.

            :param first_name: The new User's first name
            :param last_name: The new User's last name
            :param email: The new User's email address
            :param profile_picture: The new User's profile picture. Defaults to, None (No Profile Picture)

            :return: The newly created User
        """
        profile_picture_url = profile_picture.public_url if profile_picture is not None else None
        created_user = AUTH_CLIENT.create_user(display_name = f"{first_name} {last_name}",email=email,photo_url=profile_picture_url)
        super().add(
            document_id=created_user.uid,
            document_data={
                UserFieldNames.FIRST_NAME: first_name,
                UserFieldNames.LAST_NAME: last_name,
                UserFieldNames.EMAIL: email,
                UserFieldNames.PROFILE_PICTURE: profile_picture
            }
        )
        return User(user_id=created_user.uid,)

if __name__ == "__main__":
    Users().create("Ryan", "Wilson","ryan@wilson.com")