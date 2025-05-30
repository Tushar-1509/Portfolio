
from email import message_from_string

def email_agent(raw_email):
    msg = message_from_string(raw_email)
    sender = msg['From']
    subject = msg['Subject']
    body = msg.get_payload()
    urgency = "High" if "urgent" in body.lower() else "Normal"
    return {
        "sender": sender,
        "subject": subject,
        "body": body,
        "urgency": urgency
    }
