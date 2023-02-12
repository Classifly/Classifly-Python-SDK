"""
    Classifly Distributions Object Representation
"""
from typing import List, TYPE_CHECKING

from google.cloud.firestore import Transaction, Query
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classifly.objects.utils.collection_reference import CoreClassiflyCollectionReference
from classifly.objects.utils.query.dataclass.query_data import FirestoreQueryData, FirestoreWhereQueryData

from classifly.objects.account.distribution.constants import COLLECTION_PATH, DistributionFieldNames
from classifly.objects.account.distribution.utils import convert_to_distribution
from classifly.objects.account.distribution.singular import Distribution

if TYPE_CHECKING:
    from classifly.objects.account.limited_partner.singular import LimitedPartner
    from classifly.objects.account.fund.singular import Fund

class Distributions(CoreClassiflyCollectionReference):
    """
        Classifly Distributions. Used to retrieve Distributions, either all Distributions or based on a series of filters.
    """

    def __init__(self) -> None:
        super().__init__(*COLLECTION_PATH)

    @convert_to_distribution
    def get(self, transaction: Transaction = None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Distribution']:
        return super().get(transaction=transaction,retry=retry,timeout=timeout)

    def _query(self):
        class DistributionsQuery(Query):
            @convert_to_distribution
            def get(self, transaction=None, retry: retries.Retry = gapic_v1.method.DEFAULT, timeout: float = None) -> List['Distribution']:
                return super().get(transaction=transaction,retry=retry,timeout=timeout)

        return DistributionsQuery(
            parent=self
        )

    def get_records(self,fund:FirestoreQueryData=None,purpose:FirestoreQueryData=None,due_date:FirestoreQueryData=None,name:FirestoreQueryData=None) -> List['Distribution']:
        """
            Gets all Distribution records matching the specified filters.

            :param fund: The filter on the Distribution's Fund. Default: None (No filters)
            :param purpose: The filter on the Distribution's Purpose. Default: None (No filters)
            :param due_date: The filter on the Distribution's Due Date. Default: None (No filters)
            :param name: The filter on the Distribution's Name. Default: None (No filters)
        """
        return super().get_records(compound_queries=[
            FirestoreWhereQueryData(
                field_name=DistributionFieldNames.FUND,
                query_data=fund
            ),
            FirestoreWhereQueryData(
                field_name=DistributionFieldNames.PURPOSE,
                query_data=purpose
            ),
            FirestoreWhereQueryData(
                field_name=DistributionFieldNames.DUE_DATE,
                query_data=due_date
            ),
            FirestoreWhereQueryData(
                field_name=DistributionFieldNames.NAME,
                query_data=name
            )
        ])

    def add(self,fund:'Fund',purpose:str,due_date:DatetimeWithNanoseconds,name:str) -> 'Distribution':
        """
            Creates a new Distribution.

            :param fund: The new Distribution's Fund
            :param purpose: The new Distribution's Purpose
            :param due_date: The new Distribution's Due Date
            :param name: The new Distribution's Name

            :return: The newly created Distribution
        """
        return super().add(
            document_data={
                DistributionFieldNames.FUND: fund,
                DistributionFieldNames.PURPOSE: purpose,
                DistributionFieldNames.DUE_DATE: due_date,
                DistributionFieldNames.NAME: name
            }
        )
