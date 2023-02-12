"""
    Report Data - Object Representation
"""
from typing import List, Any, TYPE_CHECKING
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreWhereQueryData, FirestoreQueryData

from classifly.objects.account.report.data.constants import ReportDataFieldNames, COLLECTION_PATH
from classifly.objects.account.report.data.singular import ReportData
from classifly.objects.account.report.data.utils import convert_to_report_data

if TYPE_CHECKING:
    from classifly.objects.account.portfolio_company.singular import PortfolioCompany
    from classifly.objects.account.report.singular import Report

class ReportDataCollection(CoreClassiflyCollectionReference):
    """
        Classifly Report Data Collection. Used to retrieve report data, either all report data or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_report_data
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['ReportData']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class ReportsQuery(Query):
            @convert_to_report_data
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['ReportData']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return ReportsQuery(
            parent=self
        )


    def get_records(self,portfolio_company:FirestoreQueryData=None,id:FirestoreQueryData=None,label:FirestoreQueryData=None,position:FirestoreQueryData=None,report:FirestoreQueryData=None,type:FirestoreQueryData=None,value:FirestoreQueryData=None) -> List['ReportData']:
        """
            Gets all Report Data records matching the specified filters.

            :param portfolio_company: The filter on the Report Data's Portfolio Company. Default: None (No filters)
            :param id: The filter on the Report Data's ID. Default: None (No filters)
            :param label: The filter on the Report Data's Label. Default: None (No filters)
            :param position: The filter on the Report Data's Position. Default: None (No filters)
            :param report: The filter on the Report Data's Report. Default: None (No filters)
            :param type: The filter on the Report Data's Type. Default: None (No filters)
            :param value: The filter on the Report Data's Value. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.PORTFOLIO_COMPANY,
                query_data=portfolio_company
            ),
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.ID,
                query_data=id
            ),
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.LABEL,
                query_data=label
            ),
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.POSITION,
                query_data=position
            ),
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.REPORT,
                query_data=report
            ),
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.TYPE,
                query_data=type
            ),
            FirestoreWhereQueryData(
                field_name=ReportDataFieldNames.VALUE,
                query_data=value
            )
        ])

    def add(self,portfolio_company:'PortfolioCompany',id:str,label:str,position:int,report:'Report',type:str,value:Any) -> 'ReportData':
        """
            Creates a new Report Data Record.

            :param portfolio_company: The new Report Data's Portfolio Company
            :param id: The new Report Data's ID
            :param label: The new Report Data's Label
            :param position: The new Report Data's Position
            :param report: The new Report Data's Report
            :param type: The new Report Data's Type
            :param value: The new Report Data's Value

            :return: The newly created Report Data
        """
        return super().add(
            document_data={
                ReportDataFieldNames.PORTFOLIO_COMPANY: portfolio_company,
                ReportDataFieldNames.ID: id,
                ReportDataFieldNames.LABEL: label,
                ReportDataFieldNames.POSITION: position,
                ReportDataFieldNames.REPORT: report,
                ReportDataFieldNames.TYPE: type,
                ReportDataFieldNames.VALUE: value
            }
        )