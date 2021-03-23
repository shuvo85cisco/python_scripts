import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Email Subject"
body = "Email Body"
sender_email = "sender_email_address"
receiver_email = "recipeint_email_addresses"
user = "AWS_SES_access_key"
password = "AWS_SES_secret_access_key"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP("AWS_SES_Host_name", 587) as server:
    server.starttls(context=context)
    server.login(user, password)
    server.sendmail(sender_email, ["recipeint_email_addresses"], text)
