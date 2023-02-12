"""
    Activity - Object Representation
"""
from google.cloud.firestore import DocumentReference, FirestoreProperty

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.activity.constants import ActivityFieldNames

class Activity(ClassiflyAccountDocumentReference):
    """
        An Activity. Activities are used to log a Venture Firm's correspondence with an Account
    """
    name: str = FirestoreProperty(ActivityFieldNames.NAME,str) #: The Activity's Name/Subject
    account: DocumentReference = FirestoreProperty(ActivityFieldNames.ACCOUNT,DocumentReference) #: The Account the Activity is related to
    comments: str = FirestoreProperty(ActivityFieldNames.COMMENTS,str) #: The Activity's Comments/Description
    is_html: bool = FirestoreProperty(ActivityFieldNames.IS_HTML,bool) #: Whether the comments are HTML or raw text. Activity Comments can be HTML if the Email Add-in is used.


    def __init__(self, *args, account_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Activity",document_id=account_id)
