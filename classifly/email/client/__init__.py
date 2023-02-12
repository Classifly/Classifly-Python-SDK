from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SendGrid(SendGridAPIClient):
    def send_email(self,to_email,subject,html_content):
        message = Mail(
            from_email='support@classifly.io',
            to_emails=to_email,
            subject=subject,
            html_content=str(html_content)
        )
        try:
            print(f"Email sent to {to_email}")
            return self.send(message)
        except Exception as e:
            print(e)
