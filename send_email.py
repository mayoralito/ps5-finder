import smtplib, ssl
import os


PORT = 465  # For SSL
SENDER_EMAIL = os.environ.get('EMAIL_SOURCE')
PASSWORD_EMAIL = os.environ.get('EMAIL_SOURCE_PASSWORD')

def gmail_send_email(receiver_email, subject, message):
    # Create a secure SSL context
    context = ssl.create_default_context()
    try: 
        print(SENDER_EMAIL)
        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
            server.login(SENDER_EMAIL, PASSWORD_EMAIL)
            server.sendmail(SENDER_EMAIL, receiver_email, "Subject:" + subject + "\n\n" + message)
            print("email sent!")
    finally:
        print("Process completed!")