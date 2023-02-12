from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from classifly.email.client import SendGrid

class SendGridMailingList:
    def __init__(self,list_id:str) -> None:
        self.id = list_id

    def add_contact(self,sendgrid_client:'SendGrid',email_address:str):
        return sendgrid_client.client.marketing.contacts.put(request_body={
            "list_ids": [
                self.id
            ],
            "contacts": [{
                "email": email_address.lower()
            }]
        })
