"""
    Co-Investor - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyPipelineAccountDocumentReference
from classifly.objects.account.coinvestor.constants import CoInvestorFieldNames
from classifly.objects.utils.properties.blob import FirestoreBlobProperty, ClassiflyBlob

class CoInvestor(ClassiflyPipelineAccountDocumentReference):
    """
        A Co-Investor. Co-Investors are used to better understand a Venture Firm's network of who is investing in similar Portfolio Companies as them.
    """
    # address: FirestoreAddress = FirestoreProperty("Address_Google",FirestoreAddress)
    logo: ClassiflyBlob = FirestoreBlobProperty("Logo")
    name: str = FirestoreProperty(CoInvestorFieldNames.NAME,str) #: The Co-Investor's Name
    pipeline_account: bool = FirestoreProperty(CoInvestorFieldNames.PIPELINE_ACCOUNT,bool) #: The Co-Investor's Pipeline Status. Default `True`

    def __init__(self, *args, coinvestor_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Co-Investors",document_id=coinvestor_id)