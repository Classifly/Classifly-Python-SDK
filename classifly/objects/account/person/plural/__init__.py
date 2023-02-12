"""
    Classifly People Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.person.constants import COLLECTION_PATH, PersonFieldNames
from classifly.objects.account.person.utils import convert_to_person
from classifly.objects.account.person.singular import Person

if TYPE_CHECKING:
    from classifly.objects.account.investment.dataclass.investment_vehicles import InvestmentVehicles
    from classifly.objects.account.fund.singular import Fund
    from classifly.objects.account.portfolio_company.singular import PortfolioCompany
    from google.api_core.datetime_helpers import DatetimeWithNanoseconds

class People(CoreClassiflyCollectionReference):
    """
        Classifly People. Used to retrieve People, either all People or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_person
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Person']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class PeopleQuery(Query):
            @convert_to_person
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Person']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return PeopleQuery(
            parent=self
        )

    def get_records(self,email:FirestoreQueryData=None) -> List['Person']:
        """
            Gets all People records matching the specified filters.

            :param email: The filter on the Person's Email Address. Default: None (No filters)

        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=PersonFieldNames.EMAIL,
                query_data=email
            )
        ])

    def add(self,email:str) -> 'Person':
        """
            Creates a new Person.

            :param email: The new Limited Partner's Email Address

            :return: The newly created Person
        """
        return super().add(
            document_data={
                PersonFieldNames.EMAIL: email,
            }
        )
