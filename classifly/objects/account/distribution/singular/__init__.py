"""
    Distribution - Object Representation
"""
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.fund.singular import Fund
from classifly.objects.account.distribution.constants import DistributionFieldNames

class Distribution(ClassiflyAccountDocumentReference):
    """
        A Distribution. Distributions are used in Classifly to return a Fund's capital back to Limited Partners
    """
    fund: Fund = FirestoreProperty(DistributionFieldNames.FUND,Fund) #: The Fund issuing the Distribution
    purpose: str = FirestoreProperty(DistributionFieldNames.PURPOSE,str) #: The Distribution's Description
    due_date: DatetimeWithNanoseconds = FirestoreProperty(DistributionFieldNames.DUE_DATE,DatetimeWithNanoseconds) #: When the Distribution will be distributed
    name: str = FirestoreProperty(DistributionFieldNames.NAME,str) #: The Distribution's name

    def __init__(self, *args, distribution_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Distributions",document_id=distribution_id)