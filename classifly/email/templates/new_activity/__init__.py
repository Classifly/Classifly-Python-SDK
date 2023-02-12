from typing import TYPE_CHECKING
from classifly.email.templates import EmailTemplate
from classifly.email.templates.utils.dataclasses.variable import EmailTemplateVariable

if TYPE_CHECKING:
    from classifly.email.client import SendGrid

class NewActivityEmailTemplate(EmailTemplate):
    def __init__(self,first_name:str,account_type:str):
        self.first_name = first_name
        self.account_type = account_type
        super().__init__(template_name="new_activity_email.html",variables=[
            EmailTemplateVariable(
                class_name="first_name",
                updated_value=self.first_name
            ),
            EmailTemplateVariable(
                class_name="account_type_lower",
                updated_value=self.account_type.lower()
            ),
            EmailTemplateVariable(
                class_name="account_type_title",
                updated_value=self.account_type.title()
            )
        ])

    def send(self,sendgrid_client:'SendGrid',to_email:str):
        return super().send(
            sendgrid_client=sendgrid_client,
            subject=f"New {self.account_type.title()}!",
            to_email=to_email
        )
