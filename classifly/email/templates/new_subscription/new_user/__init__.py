from typing import TYPE_CHECKING
from classifly.email.templates import EmailTemplate
from classifly.email.templates.utils.dataclasses.variable import EmailTemplateVariable

if TYPE_CHECKING:
    from classifly.email.client import SendGrid

class NewSubscriptionNewUserEmailTemplate(EmailTemplate):
    def __init__(self,user_name:str,temporary_password:str):
        self.user_name = user_name
        self.temporary_password = temporary_password

        super().__init__(template_name="new_account_email_new_user.html.html",variables=[
            EmailTemplateVariable(
                class_name="username",
                updated_value=self.user_name
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
