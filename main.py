from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
from twilio.rest import Client
from sqlite import slite
import smtplib
import configparser
import base64

s = slite()

config = configparser.ConfigParser()
config.read("config.ini")

class batchmessage:
    db = config.get('Sqlite', 'database/uri')
    if db !="":
        p = []
        e = []


        s.connecttodb()
        p = s.getphone()
        e = s.getemail()

    def sendsms(self, msg):
        try:
            name = "SMS"
            account_sid = config.get('Twilio','Account_sid')
            auth_token = config.get('Twilio','Auth_token')
            client = Client(account_sid, auth_token)

            for a in self.p:
                message = client.messages \
                    .create(
                         body=msg,
                         from_=config.get('Twilio','Twilio_number'),
                         to='+'+str(a)
                     )
        except Exception as e:
            self.errormsg(e)
        else:
            self.success(name)

    def sendemail(self, body, sub):
        try:
            name = "E-mail"
            myaddress = config.get('Email','Your_email')
            password = base64.b64decode(config.get('Email','Password')).decode('utf-8')

            s = smtplib.SMTP_SSL(host=config.get('Email','Host'), port='465')
            s.login(myaddress, password)
            msg = MIMEMultipart()
            body = MIMEText(body)
            msg.attach(body)
            msg['Subject'] = sub
            msg['From'] = myaddress
            for a in self.e:
                msg['To'] = a
                s.send_message(msg)

            s.quit()
        except Exception as e:
           self.errormsg(e)
        else:
            self.success(name)

    def success(self,name):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("success.png"))
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText(name+" Sent\t")
        msg.setWindowTitle("Success")
        msg.exec_()

    def errormsg(self,error):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("error.png"))
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText(str(error))
        msg.setWindowTitle("Error")
        msg.exec_()
