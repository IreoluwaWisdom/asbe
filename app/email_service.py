from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from app.config import MAIL_USERNAME, MAIL_PASSWORD, MAIL_FROM, MAIL_SERVER, MAIL_PORT, MAIL_STARTTLS, MAIL_SSL_TLS

# FastMail configuration using config.py
conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_FROM,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_STARTTLS=MAIL_STARTTLS,
    MAIL_SSL_TLS=MAIL_SSL_TLS,
)

# Email Schema
class EmailSchema(BaseModel):
    email: EmailStr
    subject: str
    body: str

# Function to send an email
async def send_email(email: EmailSchema):
    message = MessageSchema(
        subject=email.subject,
        recipients=[email.email],  # Must be a list
        body=email.body,
        subtype="html",  # Change to "plain" for plain text emails
    )
    mail = FastMail(conf)

    try:
        await mail.send_message(message)
        print(f"Email sent to {email.email}")
    except Exception as e:
        print(f"Error sending email: {e}")
