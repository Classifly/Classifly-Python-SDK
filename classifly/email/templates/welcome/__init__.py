from typing import TYPE_CHECKING
from classifly.email.templates import EmailTemplate
from classifly.email.templates.utils.dataclasses.variable import EmailTemplateVariable

if TYPE_CHECKING:
    from classifly.email.client import SendGrid

class WelcomeEmail(EmailTemplate):

    def __init__(self,user_name:str,first_name:str,last_name:str,account_name:str,temporary_password:str):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.account_name = account_name
        self.temporary_password = temporary_password

        super().__init__(template_name="welcome_email.html",variables=[
            EmailTemplateVariable(
                class_name="username",
                updated_value=self.user_name
            ),
            EmailTemplateVariable(
                class_name="first_name",
                updated_value=self.first_name
            ),
            EmailTemplateVariable(
                class_name="last_name",
                updated_value=self.last_name
            ),
            EmailTemplateVariable(
                class_name="account_name",
                updated_value=self.account_name
            ),
            EmailTemplateVariable(
                class_name="password",
                updated_value=self.temporary_password
            )
        ])

    def send(self,sendgrid_client:'SendGrid'):
        return super().send(
            sendgrid_client=sendgrid_client,
            subject="Welcome to Classifly!",
            to_email=self.user_name
        )
