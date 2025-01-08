import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = config.SMTP_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
        server.send_message(msg)

def send_welcome_email(email):
    subject = "Welcome to Our CRM Platform"
    body = """
    <h1>Welcome!</h1>
    <p>Thank you for choosing our CRM platform.</p>
    <p>Get started by completing your onboarding tasks.</p>
    """
    send_email(email, subject, body)
