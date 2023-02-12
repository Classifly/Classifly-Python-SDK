"""
    Classifly Activites Object Representation
"""
from typing import List
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.activity.constants import COLLECTION_PATH, ActivityFieldNames
from classifly.objects.account.activity.utils import convert_to_activity
from classifly.objects.account.activity.singular import Activity

class Activities(CoreClassiflyCollectionReference):
    """
        Classifly Activies. Used to retrieve Activities, either all activities or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_activity
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Activity']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class ActivitiesQuery(Query):
            @convert_to_activity
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Activity']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return ActivitiesQuery(
            parent=self
        )

    def get_records(self,name:FirestoreQueryData=None,account:FirestoreQueryData=None,comments:FirestoreQueryData=None,is_html:FirestoreQueryData=None) -> List['Activity']:
        """
            Gets all Activty records matching the specified filters.

            :param name: The filter on the Activity's name. Default: None (No filters)
            :param last_name: The filter on the Activity's account. Default: None (No filters)
            :param email: The filter on the Activity's comments. Default: None (No filters)
            :param connected_accounts: The filter on the Activity's HTML Status. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=ActivityFieldNames.NAME,
                query_data=name
            ),
            FirestoreWhereQueryData(
                field_name=ActivityFieldNames.ACCOUNT,
                query_data=account
            ),
            FirestoreWhereQueryData(
                field_name=ActivityFieldNames.COMMENTS,
                query_data=comments
            ),
            FirestoreWhereQueryData(
                field_name=ActivityFieldNames.IS_HTML,
                query_data=is_html
            )
        ])

    def add(self,name:str,account:'ClassiflyAccountDocumentReference',comments:str,is_html:bool):
        """
            Creates a new Activity.

            :param name: The new Activity's Name
            :param account: The new Activity's Account it's related to
            :param comments: The new Activity's Comments
            :param is_html: Whether the new Activity's comments are HTML.

            :return: The newly created Activity
        """
        return super().add(
            document_data={
                ActivityFieldNames.NAME: name,
                ActivityFieldNames.ACCOUNT: account,
                ActivityFieldNames.COMMENTS: comments,
                ActivityFieldNames.IS_HTML: is_html
            }
        )

if __name__ == "__main__":
    for activity in Activities().get_records(is_html=FirestoreQueryData(operator_string="==",value=True)):
        print(activity.is_html)