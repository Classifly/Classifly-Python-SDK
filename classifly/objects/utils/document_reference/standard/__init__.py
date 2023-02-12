"""
    Classifly Object Utilities
"""
from typing import TYPE_CHECKING

from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import FirestoreProperty

from classifly.objects.utils.document_reference.core import CoreClassiflyDocumentReference
from classifly.objects.utils.properties.user import ClassiflyUserProperty

if TYPE_CHECKING:
    from classifly.objects.user.singular import User

class ClassiflyDocumentReference(CoreClassiflyDocumentReference):
    """
        The base object representing a document reference in Classifly's Firestore Database
    """

    ## TO-DO: Create these properties without circular import errors
    created_by: 'User' = ClassiflyUserProperty("Created by") #: The Classifly User who created the Document
    created_date: DatetimeWithNanoseconds = FirestoreProperty("Created on", DatetimeWithNanoseconds) #: When the Document was created
    last_modified_by: 'User' = ClassiflyUserProperty("Last Modified by") #: The last User to modify the Document
    last_modified_date: DatetimeWithNanoseconds = FirestoreProperty("Last Modified on", DatetimeWithNanoseconds) #: When the Document was last modified
