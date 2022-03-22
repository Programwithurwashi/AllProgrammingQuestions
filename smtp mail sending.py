#WAP to send mail
import smtplib
try:
    smtp=smtplib.SMTP('smtp.gmail.com,587')
    #smtpobj.ehlo()
    smtp.starttls()
    smtp.login('urwashi238srivastava@gmail.com','srivastava@123')

    smtp.sendermail('urwashi238srivastava@gmail.com','urwashisrivastava238@gmail.com','subject:smtp check \n it is test email by python')
    smtpobj.quit()
    print("email send successfully")
except Exception as ex:
    print("something went wrong",ex)