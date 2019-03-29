from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtWidgets import QFileDialog
import configparser
import base64

config = configparser.ConfigParser()
config.read('config.ini')

class set_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 360)
        Dialog.setMinimumSize(QtCore.QSize(421, 360))
        Dialog.setMaximumSize(QtCore.QSize(421, 360))
        Dialog.setWindowIcon(QtGui.QIcon("settings.png"))

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 421, 360))
        self.tabWidget.setMinimumSize(QtCore.QSize(421, 360))
        self.tabWidget.setMaximumSize(QtCore.QSize(421, 360))
        self.tabWidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.tabWidget.setObjectName("tabWidget")

        self.sqlite = QtWidgets.QWidget()
        self.sqlite.setObjectName("sqlite")

        self.dblbl = QtWidgets.QLabel(self.sqlite)
        self.dblbl.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.dblbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.dblbl.setObjectName("label")

        self.dbselbtn = QtWidgets.QPushButton(self.sqlite)
        self.dbselbtn.setGeometry(QtCore.QRect(170, 30, 151, 31))
        self.dbselbtn.setStyleSheet("border:2px solid rgb(0, 120, 215);\n"
"background-color: rgb(255, 255, 255);""font: 75 11pt \"MS Shell Dlg 2\";")
        self.dbselbtn.setObjectName("pushButton")
        self.dbselbtn.clicked.connect(self.fileopen)

        self.tablelbl = QtWidgets.QLabel(self.sqlite)
        self.tablelbl.setGeometry(QtCore.QRect(10, 100, 81, 31))
        self.tablelbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.tablelbl.setObjectName("label_2")

        self.tableline = QtWidgets.QLineEdit(self.sqlite)
        self.tableline.setGeometry(QtCore.QRect(170, 100, 231, 31))
        self.tableline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.tableline.setText(config.get('General','Table'))
        self.tableline.setObjectName("lineEdit")
        self.tableline.setText(config.get('General', 'Table'))


        self.phonecollbl = QtWidgets.QLabel(self.sqlite)
        self.phonecollbl.setGeometry(QtCore.QRect(10, 170, 161, 31))
        self.phonecollbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.phonecollbl.setObjectName("label_3")

        self.phonecolline = QtWidgets.QLineEdit(self.sqlite)
        self.phonecolline.setGeometry(QtCore.QRect(170, 170, 231, 31))
        self.phonecolline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.phonecolline.setObjectName("lineEdit_2")
        self.phonecolline.setText(config.get('General', 'Phone_column'))

        self.emcollbl = QtWidgets.QLabel(self.sqlite)
        self.emcollbl.setGeometry(QtCore.QRect(10, 240, 161, 31))
        self.emcollbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.emcollbl.setObjectName("label_4")

        self.emcolline = QtWidgets.QLineEdit(self.sqlite)
        self.emcolline.setGeometry(QtCore.QRect(170, 240, 231, 31))
        self.emcolline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.emcolline.setObjectName("lineEdit_3")
        self.emcolline.setText(config.get('General','Email_column'))

        self.sqokbtn = QtWidgets.QPushButton(self.sqlite)
        self.sqokbtn.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.sqokbtn.setStyleSheet("border:2px solid rgb(0, 120, 215);\n"
"background-color: rgb(255, 255, 255);")
        self.sqokbtn.setDefault(False)
        self.sqokbtn.setFlat(True)
        self.sqokbtn.setObjectName("pushButton_3")
        self.sqokbtn.clicked.connect(self.savesettings)
        self.sqokbtn.clicked.connect(Dialog.close)

        self.tabWidget.addTab(self.sqlite, "")

        self.twilio = QtWidgets.QWidget()
        self.twilio.setObjectName("twilio")

        self.sidlbl = QtWidgets.QLabel(self.twilio)
        self.sidlbl.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.sidlbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.sidlbl.setObjectName("label_5")

        self.authlbl = QtWidgets.QLabel(self.twilio)
        self.authlbl.setGeometry(QtCore.QRect(10, 100, 111, 31))
        self.authlbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.authlbl.setObjectName("label_6")

        self.twinumlbl = QtWidgets.QLabel(self.twilio)
        self.twinumlbl.setGeometry(QtCore.QRect(10, 170, 111, 31))
        self.twinumlbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.twinumlbl.setObjectName("label_7")

        self.twinumline = QtWidgets.QLineEdit(self.twilio)
        self.twinumline.setGeometry(QtCore.QRect(120, 170, 231, 31))
        self.twinumline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.twinumline.setObjectName("lineEdit_4")
        self.twinumline.setText(config.get('Twilio', 'Twilio_number'))

        self.authline = QtWidgets.QLineEdit(self.twilio)
        self.authline.setGeometry(QtCore.QRect(120, 100, 231, 31))
        self.authline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.authline.setObjectName("lineEdit_5")
        self.authline.setText(config.get('Twilio', 'Auth_token'))

        self.sidline = QtWidgets.QLineEdit(self.twilio)
        self.sidline.setGeometry(QtCore.QRect(120, 30, 231, 31))
        self.sidline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.sidline.setObjectName("lineEdit_6")
        self.sidline.setText(config.get('Twilio', 'Account_sid'))

        self.twiokbtn = QtWidgets.QPushButton(self.twilio)
        self.twiokbtn.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.twiokbtn.setStyleSheet("border:2px solid rgb(0, 120, 215);\n"
"background-color: rgb(255, 255, 255);")
        self.twiokbtn.setDefault(False)
        self.twiokbtn.setFlat(True)
        self.twiokbtn.setObjectName("pushButton_2")
        self.twiokbtn.clicked.connect(self.savesettings)
        self.twiokbtn.clicked.connect(Dialog.close)

        self.tabWidget.addTab(self.twilio, "")

        self.email = QtWidgets.QWidget()
        self.email.setObjectName("email")

        self.serverlbl = QtWidgets.QLabel(self.email)
        self.serverlbl.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.serverlbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.serverlbl.setObjectName("label_8")

        self.emaillbl = QtWidgets.QLabel(self.email)
        self.emaillbl.setGeometry(QtCore.QRect(10, 100, 61, 31))
        self.emaillbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.emaillbl.setObjectName("label_9")

        self.passlbl = QtWidgets.QLabel(self.email)
        self.passlbl.setGeometry(QtCore.QRect(10, 170, 71, 31))
        self.passlbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.passlbl.setObjectName("label_10")

        self.passline = QtWidgets.QLineEdit(self.email)
        self.passline.setGeometry(QtCore.QRect(90, 170, 231, 31))
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.passline.setObjectName("lineEdit_7")
        self.passw = config.get('Email', 'Password')
        if self.passw:
            self.passw = str(base64.b64decode(self.passw).decode('utf-8'))
        self.passline.setText(self.passw)

        self.emailline = QtWidgets.QLineEdit(self.email)
        self.emailline.setGeometry(QtCore.QRect(90, 100, 231, 31))
        self.emailline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.emailline.setObjectName("lineEdit_8")
        self.emailline.setText(config.get('Email','Your_email'))

        self.serverline = QtWidgets.QLineEdit(self.email)
        self.serverline.setGeometry(QtCore.QRect(90, 30, 231, 31))
        self.serverline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.serverline.setObjectName("lineEdit_9")
        self.serverline.setText(config.get('Email', 'Host'))

        self.mailokbtn = QtWidgets.QPushButton(self.email)
        self.mailokbtn.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.mailokbtn.setStyleSheet("border:2px solid rgb(0, 120, 215);\n"
"background-color: rgb(255, 255, 255);")
        self.mailokbtn.setDefault(False)
        self.mailokbtn.setFlat(True)
        self.mailokbtn.setObjectName("pushButton_4")
        self.mailokbtn.clicked.connect(self.savesettings)
        self.mailokbtn.clicked.connect(Dialog.close)

        self.tabWidget.addTab(self.email, "")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.dblbl.setText(_translate("Dialog", "Database File:-"))
        self.dbname = config.get('General', 'Db_name')
        self.dbdir = config.get('Sqlite', 'database/uri')
        if not self.dbdir:
            self.dbselbtn.setText(_translate("Dialog", "Choose File"))
        else:
            self.dbselbtn.setText(_translate("Dialog", self.dbname))
        self.tablelbl.setText(_translate("Dialog", "Table Name:-"))
        self.phonecollbl.setText(_translate("Dialog", "Phone Number Column:-"))
        self.emcollbl.setText(_translate("Dialog", "Email Address Column:-"))
        self.sqokbtn.setText(_translate("Dialog", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sqlite), _translate("Dialog", "SQLite"))
        self.sidlbl.setText(_translate("Dialog", "Account Sid:-"))
        self.authlbl.setText(_translate("Dialog", "Auth Token:-"))
        self.twinumlbl.setText(_translate("Dialog", "Twilio Number:-"))
        self.twiokbtn.setText(_translate("Dialog", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.twilio), _translate("Dialog", "Twilio"))
        self.serverlbl.setText(_translate("Dialog", "Server:-"))
        self.emaillbl.setText(_translate("Dialog", "E-Mail:-"))
        self.passlbl.setText(_translate("Dialog", "Password:-"))
        self.mailokbtn.setText(_translate("Dialog", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.email), _translate("Dialog", "Email"))

    def fileopen(self):
        self.dbsel = QFileDialog()
        self.filedir, _ = self.dbsel.getOpenFileName(None, "Choose Database File", "", "All Files (*);;Database Files (*.sqlite3)")
        url = QUrl.fromLocalFile(self.filedir)
        filename = QFileInfo(self.filedir).fileName()
        self.dbselbtn.setText(str(filename))

    def savesettings(self):

        table = str(self.tableline.text())
        pcol = str(self.phonecolline.text())
        ecol = str(self.emcolline.text())
        sid = str(self.sidline.text())
        token = str(self.authline.text())
        tnumber = str(self.twinumline.text())
        server = str(self.serverline.text())
        email = str(self.emailline.text())
        password = self.passline.text()
        password = base64.b64encode(password.encode()).decode('utf-8')
        config.set('Sqlite', 'Database/URI', self.filedir)
        config.set('General', 'Table', table)
        config.set('General', 'Phone_column', pcol)
        config.set('General', 'Email_column', ecol)
        config.set('Twilio', 'Account_sid', sid)
        config.set('Twilio', 'Auth_token', token)
        config.set('Twilio', 'Twilio_number', tnumber)
        config.set('Email', 'Host', server)
        config.set('Email', 'Your_email', email)
        config.set('Email', 'Password', password)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def setting(self):
        Dialog = QtWidgets.QDialog()
        ui = set_dialog()
        ui.setupUi(Dialog)
        Dialog.setModal(True)
        Dialog.show()
        Dialog.exec_()
