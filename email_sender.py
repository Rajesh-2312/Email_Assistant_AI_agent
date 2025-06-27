from gmail_auth import get_gmail_service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FROM_EMAIL = "onytrajesh@gmail.com"

def send_email(to_email, subject, body):
    try:
        if not to_email or not subject or not body:
            raise ValueError("Missing required email parameters")
        to_email = to_email.strip()
        if not '@' in to_email:
            raise ValueError("Invalid email address")
        logger.info(f"Attempting to send email to: {to_email}")
        logger.info(f"Subject: {subject}")
        service = get_gmail_service()
        message = {
            'raw': create_message(FROM_EMAIL, to_email, subject, body)
        }
        result = service.users().messages().send(userId='me', body=message).execute()
        logger.info(f"Email sent successfully. Message ID: {result.get('id', 'Unknown')}")
        return True
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise e
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        raise e

def create_message(sender, to, subject, message_text):
    import base64
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    try:
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        text_part = MIMEText(message_text, 'plain', 'utf-8')
        message.attach(text_part)
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return raw
    except Exception as e:
        logger.error(f"Error creating message: {str(e)}")
        raise e