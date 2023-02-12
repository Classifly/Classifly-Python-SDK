"""
    Published Report - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.utils.properties.blob import FirestoreBlobProperty, ClassiflyBlob
from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.published_report.constants import PublishedReportFieldNames

class PublishedReport(ClassiflyAccountDocumentReference):
    """
        A Published Report. A Published Report is a document created by a Venture Firm and meant to be shared with the Venture Firm's Limited Partners. Typically this is a Quarterly Report or something similar.
    """
    name: str = FirestoreProperty(PublishedReportFieldNames.NAME,str) #: The Name of the Published Report
    document: ClassiflyBlob = FirestoreBlobProperty(PublishedReportFieldNames.DOCUMENT)


    def __init__(self, *args, published_report_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Published_Reports",document_id=published_report_id)

    def delete(self):
        self.document.delete()
        return super().delete()

if __name__ == "__main__":
    PublishedReport("CcpDVgWbIAywZyf0VRLU").delete()