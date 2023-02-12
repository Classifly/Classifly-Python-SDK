from typing import TYPE_CHECKING
from classifly.email.templates import EmailTemplate
from classifly.email.templates.utils.dataclasses.variable import EmailTemplateVariable

if TYPE_CHECKING:
    from classifly.email.client import SendGrid

class AccountAddedEmail(EmailTemplate):
    _account_name: str = None

    def __init__(self,first_name:str,account_name:str):
        self.first_name = first_name
        self.account_name = account_name

        super().__init__(template_name="account_added_email.html",variables=[
            EmailTemplateVariable(
                class_name="first_name",
                updated_value=self.first_name
            ),
            EmailTemplateVariable(
                class_name="account_name",
                updated_value=self.account_name
            )
        ])

    @property
    def account_name(self):
        account_name = f"{self._account_name}'"
        if account_name[-2].lower() != "s":
            account_name += "s"
        return account_name

    def send(self,sendgrid_client:'SendGrid',to_email:str):
        return super().send(
            sendgrid_client=sendgrid_client,
            subject="New Account Added!",
            to_email=to_email
        )
