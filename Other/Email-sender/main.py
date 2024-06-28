import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

subject = "Subject"
sender = "your_email@gmail.com"
recipient = "recipient_email@gmail.com"
password = "password to app" #gmail -> security -> two-step verification -> application passwords
body = "I received an e-email!"


def send_email(subject, body, sender, recipient, password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.attach(MIMEText(body))
    with open('heart.jpg', 'rb') as attachment:
        image = MIMEImage(attachment.read(), name='heart.jpg')
        msg.attach(image)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server: # 465 is gmail's port number
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
    smtplib.SMTP_SSL('smtp.gmail.com', 465).quit()
    print("Sent")

send_email(subject, body, sender, recipient, password)
