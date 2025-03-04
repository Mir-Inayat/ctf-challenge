import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Brevo SMTP Configuration
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587
SMTP_USERNAME = "871698001@smtp-brevo.com"  # Your Brevo login
SMTP_PASSWORD = "3PyKBOpNcvgCYL4s"  # Replace with your Brevo SMTP password

# Email Configuration
sender_email = "rimdaas30@gmail.com"  # Replace with your sender email
recipient_list = [
    "pradeepmajji853@gmail.com",
    "mirinayatahmed@gmail.com",
]  # Add participant emails here

# Create Email Message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["Subject"] = "CTF Challenge - Hidden Flag Inside!"
msg["X-Secret-Flag"] = "flag{email_headers}"  # Hidden flag in the header

# Email Body
body = "Check the raw email source to find the hidden flag!"
msg.attach(MIMEText(body, "plain"))

# Send Email to All Participants
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    for recipient in recipient_list:
        msg["To"] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())

print("Emails sent successfully to all participants!")
