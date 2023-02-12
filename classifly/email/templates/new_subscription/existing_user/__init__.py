from typing import TYPE_CHECKING
from classifly.email.templates import EmailTemplate

if TYPE_CHECKING:
    from classifly.email.client import SendGrid

class NewSubscriptionExistingUserEmailTemplate(EmailTemplate):
    def __init__(self):
        super().__init__(template_name="account_added_email.html",variables=[])

    def send(self,sendgrid_client:'SendGrid',to_email:str):
        return super().send(
            sendgrid_client=sendgrid_client,
            subject="Welcome to Classifly!",
            to_email=to_email
        )
