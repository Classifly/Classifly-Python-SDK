"""
    Classifly Capital Calls Object Representation
"""
from typing import List, TYPE_CHECKING

from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries


from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.capital_call.constants import COLLECTION_PATH, CapitalCallFieldNames
from classifly.objects.account.capital_call.utils import convert_to_capital_call
from classifly.objects.account.capital_call.singular import CapitalCall

if TYPE_CHECKING:
    from classifly.objects.account.fund.singular import Fund

class CapitalCalls(CoreClassiflyCollectionReference):
    """
        Classifly Capital Calls. Used to retrieve Capital Calls, either all Capital Calls or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_capital_call
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CapitalCall']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class CapitalCallsQuery(Query):
            @convert_to_capital_call
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['CapitalCall']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return CapitalCallsQuery(
            parent=self
        )

    def get_records(self,fund:FirestoreQueryData=None,purpose:FirestoreQueryData=None,due_date:FirestoreQueryData=None,name:FirestoreQueryData=None) -> List['CapitalCall']:
        """
            Gets all Capital Call records matching the specified filters.

            :param fund: The filter on the Capital Call's Fund. Default: None (No filters)
            :param purpose: The filter on the Capital Call's Purpose. Default: None (No filters)
            :param due_date: The filter on the Capital Call's Due Date. Default: None (No filters)
            :param name: The filter on the Capital Call's Name. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=CapitalCallFieldNames.FUND,
                query_data=fund
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallFieldNames.PURPOSE,
                query_data=purpose
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallFieldNames.DUE_DATE,
                query_data=due_date
            ),
            FirestoreWhereQueryData(
                field_name=CapitalCallFieldNames.NAME,
                query_data=name
            ),
        ])

    def add(self,fund:'Fund',purpose:str,due_date:DatetimeWithNanoseconds,name:str) -> 'CapitalCall':
        """
            Creates a new Capital Call.

            :param fund: The new Capital Call's Fund
            :param purpose: The new Capital Call's Purpose
            :param due_date: The new Capital Call's Due Date
            :param name: The new Capital Call's Name

            :return: The newly created Capital Call
        """
        return super().add(
            document_data={
                CapitalCallFieldNames.FUND: fund,
                CapitalCallFieldNames.PURPOSE: purpose,
                CapitalCallFieldNames.DUE_DATE: due_date,
                CapitalCallFieldNames.NAME: name
            }
        )

if __name__ == "__main__":
    for capital_call in CapitalCalls().get():
        print(capital_call.fund.name)