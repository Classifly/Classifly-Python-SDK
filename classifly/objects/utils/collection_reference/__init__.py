"""
    Classifly Object Utilities
"""
from abc import abstractmethod
from typing import List
from google.cloud.firestore import CollectionReference

from classifly.objects.utils.query.dataclass.query_data import FirestoreWhereQueryData
from classifly.utils.google.firestore.client import CLIENT

class CoreClassiflyCollectionReference(CollectionReference):
    """
        A Collection in Classifly's Firestore Database
    """
    def __init__(self, *path) -> None:
        if len(path) == 1:
            if isinstance(path[0],CollectionReference):
                path = path[0].path.split("/")
        super().__init__(*path, client=CLIENT)

    @property
    def path(self):
        parent_path = ""
        if self.parent is not None:
            parent_path = self.parent.path
        return f"{parent_path}/{self.id}"

    @abstractmethod
    def get_records(self,compound_queries:List['FirestoreWhereQueryData']):
        base_query = self._query()
        for compound_query in compound_queries:
            if compound_query.query_data is not None:
                base_query = base_query.where(compound_query.field_name,compound_query.query_data.operator_string,compound_query.query_data.value)

        return base_query.get()
