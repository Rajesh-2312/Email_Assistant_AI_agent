from gmail_auth import get_gmail_service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_latest_email():
    try:
        service = get_gmail_service()
        results = service.users().messages().list(
            userId='me', 
            labelIds=['INBOX'], 
            q="is:unread"
        ).execute()
        messages = results.get('messages', [])
        logger.info(f"Found {len(messages)} unread messages")

        emails = []
        if not messages:
            return emails

        for msg in messages[:5]:
            try:
                msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
                headers = msg_data['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
                sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")
                body = extract_email_body(msg_data)
                sender_email = extract_email_from_sender(sender)
                emails.append({
                    'sender': sender_email,
                    'sender_name': sender,
                    'subject': subject,
                    'body': body,
                    'id': msg['id']
                })
                service.users().messages().modify(
                    userId='me', 
                    id=msg['id'], 
                    body={'removeLabelIds': ['UNREAD']}
                ).execute()
                logger.info(f"Processed email from: {sender_email}")
            except Exception as e:
                logger.error(f"Error processing message {msg['id']}: {str(e)}")
                continue
        return emails
    except Exception as e:
        logger.error(f"Error fetching emails: {str(e)}")
        raise e

def extract_email_body(msg_data):
    try:
        payload = msg_data['payload']
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    if 'data' in part['body']:
                        import base64
                        return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8', errors='ignore')
        if 'data' in payload['body']:
            import base64
            return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='ignore')
        return "Email content could not be extracted"
    except Exception as e:
        logger.error(f"Error extracting email body: {str(e)}")
        return "Error reading email content"

def extract_email_from_sender(sender):
    import re
    email_pattern = r'<([^>]+)>'
    match = re.search(email_pattern, sender)
    if match:
        return match.group(1)
    else:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(email_pattern, sender)
        return match.group(0) if match else sender