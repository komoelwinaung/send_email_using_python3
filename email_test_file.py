import smtplib
fromaddr = 'sender@gmail.com'
toaddrs = 'receiver@gmail.com'
username = 'sender@gmail.com'
password = 'Send$2022'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
print ("Successful")


Data_Sent_in_Email = ""
Header = """From: Test Email <sender@gmail.com>
To: To Receiver <receiver@gmail.com>
Subject: This is the test email.
"""
Data_Sent_in_Email += Header
Data_Sent_in_Email +="============Email Test by Python3============"


server.sendmail(fromaddr, toaddrs, Data_Sent_in_Email)
server.quit()
