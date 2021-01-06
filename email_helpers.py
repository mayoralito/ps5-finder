from send_email import gmail_send_email

def build_email_content_not_found_to(receiver_email):
    subject = "PS5: Nothing yet"
    body = "This is a test email, nothing found yet"
    build_email_content_to(receiver_email, subject, body)

def build_email_content_found_to(receiver_email, content):
    # Get store details
    store_details = content.find("Store")
    subject = "PS5- Found!"
    body = content
    build_email_content_to(receiver_email, subject, content)

def build_email_content_to(receiver_email, subject, body):
    # Sending email using the method.
    gmail_send_email(receiver_email, subject, body)