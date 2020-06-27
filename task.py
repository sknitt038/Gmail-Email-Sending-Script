
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendMail(message):
    mail_content=message
    #The mail addresses and password

    sender_address = str(input("Please Enter Sender Email Address: "))
    sender_pass = str(input("Please Enter Sender Password: "))
    receiver_address = str(input("Please Enter Receiver Email Address: "))
    subject = str(input("Please Enter your subject: "))
    #Setup the MIME
    # sender_address = 'sknitt38@gmail.com'
    # sender_pass = '****'
    # receiver_address = 'sknitt38@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To']   = receiver_address
    
    message["Subject"] = subject  #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

message=str(input("Please Enter your message: "))
sendMail(message)


#Kindly visit the below link and enable your security options
#https://myaccount.google.com/lesssecureapps
#https://myaccount.google.com/lesssecureapps ---please give the permission to smtp