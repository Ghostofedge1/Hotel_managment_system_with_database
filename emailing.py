
from email.message import EmailMessage
import ssl
import smtplib


email_sender='ahmed.elwakad2021@gmail.com'
password='uxys jgzd yrzc srnm'
email_recevier='yanoyix587@24rumen.com'

id=3

subject='welocming message'
body="""\t\t\t\t Welcome to our hotel \t\t\t\t \n we hope that you are gonna have a nice time here your ID is """+ str(id)

em=EmailMessage()

em['From']=email_sender
em['To']=email_recevier
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_recevier,em.as_string())













#    try:

#    smtplib.SMTPAuthenticationError:


# num=13212
# h=""" Hello your number is """ + str(num)
# print (h)