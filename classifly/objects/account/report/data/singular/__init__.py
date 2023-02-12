from typing import Any
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.portfolio_company.singular import PortfolioCompany
from classifly.objects.account.report.data.constants import COLLECTION_PATH, ReportDataFieldNames

class ReportData(ClassiflyAccountDocumentReference):
    """
        Report Data. The Input data the Portfolio Company submitted for the Report.
    """
    portfolio_company: PortfolioCompany = FirestoreProperty(ReportDataFieldNames.PORTFOLIO_COMPANY, PortfolioCompany) #: The Portfolio Company that submitted the data
    id: str = FirestoreProperty(ReportDataFieldNames.ID,str) #: The Input's ID
    label: str = FirestoreProperty(ReportDataFieldNames.LABEL, str) #: The Input's Name
    position: int = FirestoreProperty(ReportDataFieldNames.POSITION, int) #: The Input's order in the Report
    type: str = FirestoreProperty(ReportDataFieldNames.TYPE,str) #: The Input's Type. Ex: Text, Number, etc.
    value: Any = FirestoreProperty(ReportDataFieldNames.VALUE, Any) #: The Portfolio Company's Provided value for the Input.

    def __init__(self, *args, report_data_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(*(COLLECTION_PATH + [report_data_id]))
