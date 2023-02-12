from dataclasses import dataclass

@dataclass
class EmailTemplateVariable:
    class_name: str
    updated_value: str
