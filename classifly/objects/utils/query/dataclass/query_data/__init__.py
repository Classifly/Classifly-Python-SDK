from typing import Any
from dataclasses import dataclass

@dataclass
class FirestoreQueryData:
    operator_string: str
    value: Any

@dataclass
class FirestoreWhereQueryData:
    field_name: str
    query_data: FirestoreQueryData
