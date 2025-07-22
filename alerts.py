import smtplib
from twilio.rest import Client
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = os.getenv("EMAIL_USER")
    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        server.send_message(msg)

def send_whatsapp_alert(message):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        body=message,
        to=os.getenv("ALERT_PHONE")
    )