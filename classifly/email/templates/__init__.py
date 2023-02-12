from typing import List, TYPE_CHECKING

import requests
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from classifly.email.templates.utils.dataclasses.variable import EmailTemplateVariable
    from classifly.email.client import SendGrid

class EmailTemplate(BeautifulSoup):
    """
        A Classifly Email Template.
    """
    def __init__(self,template_name:str,variables:List['EmailTemplateVariable']):
        email_templates_base_url = "https://brand-assets.classifly.io/email_templates/"
        r = requests.get(email_templates_base_url + template_name)
        super().__init__(r.text,"lxml")
        self.template_name = template_name
        self.variables = variables

        for variable in variables:
            for span in self.findAll("span",{"class":variable.class_name}):
                span.string.replace_with(variable.updated_value)

    def send(self,sendgrid_client:'SendGrid',subject:str,to_email:str):
        return sendgrid_client.send_email(to_email,subject,self.html)
