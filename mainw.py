from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from settings import set_dialog
from about import ab_dialog
from main import batchmessage

set = set_dialog()
ab  = ab_dialog()
bm = batchmessage()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 447)
        MainWindow.setMinimumSize(QtCore.QSize(421, 447))
        MainWindow.setMaximumSize(QtCore.QSize(421, 447))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.msgtxt = QtWidgets.QTextEdit(self.centralwidget)
        self.msgtxt.setGeometry(QtCore.QRect(10, 170, 401, 171))
        self.msgtxt.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.msgtxt.setObjectName("textEdit")

        self.subjectline = QtWidgets.QLineEdit(self.centralwidget)
        self.subjectline.setGeometry(QtCore.QRect(10, 80, 401, 31))
        self.subjectline.setStyleSheet("border:1px solid rgb(0, 120, 215);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.subjectline.setObjectName("lineEdit")


        self.warninglbl = QtWidgets.QLabel(self.centralwidget)
        self.warninglbl.setGeometry(QtCore.QRect(60, 10, 291, 20))
        self.warninglbl.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.warninglbl.setObjectName("label")

        self.smsbtn = QtWidgets.QPushButton(self.centralwidget)
        self.smsbtn.setGeometry(QtCore.QRect(10, 370, 81, 23))
        self.smsbtn.setStyleSheet("border:2px solid rgb(0, 120, 215);")
        self.smsbtn.setObjectName("pushButton")


        self.emailbtn = QtWidgets.QPushButton(self.centralwidget)
        self.emailbtn.setGeometry(QtCore.QRect(170, 370, 81, 23))
        self.emailbtn.setStyleSheet("border:2px solid rgb(0, 120, 215)")
        self.emailbtn.setObjectName("pushButton_2")



        self.bothbtn = QtWidgets.QPushButton(self.centralwidget)
        self.bothbtn.setGeometry(QtCore.QRect(330, 370, 81, 23))
        self.bothbtn.setStyleSheet("border:2px solid rgb(0, 120, 215)")
        self.bothbtn.setObjectName("pushButton_3")

        self.smsbtn.clicked.connect(self.sendtext)
        self.emailbtn.clicked.connect(self.sendmail)
        self.bothbtn.clicked.connect(self.sendtext)
        self.bothbtn.clicked.connect(self.sendmail)

        self.subjectlbl = QtWidgets.QLabel(self.centralwidget)
        self.subjectlbl.setGeometry(QtCore.QRect(10, 50, 181, 21))
        self.subjectlbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.subjectlbl.setObjectName("label_2")

        self.msglbl = QtWidgets.QLabel(self.centralwidget)
        self.msglbl.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.msglbl.setStyleSheet("font: 75 10.5pt \"MS Shell Dlg 2\";")
        self.msglbl.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setStyleSheet("border-top:1px solid rgb(0, 120, 215);\n"
"border-bottom:1px solid rgb(0, 120, 215);")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")

        self.helpmenu = QtWidgets.QMenu(self.menubar)
        self.helpmenu.setObjectName("menuHelp")

        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setStyleSheet("")
        self.filemenu.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.settingsaction = QtWidgets.QAction(MainWindow)
        self.settingsaction.setObjectName("actionSetting")

        self.exitaction = QtWidgets.QAction(MainWindow)
        self.exitaction.setObjectName("actionExit")

        self.aboutaction = QtWidgets.QAction(MainWindow)
        self.aboutaction.setObjectName("actionAbout")

        self.filemenu.addAction(self.settingsaction)
        self.filemenu.addAction(self.exitaction)

        self.helpmenu.addAction(self.aboutaction)

        self.menubar.addAction(self.filemenu.menuAction())
        self.settingsaction.triggered.connect(set.setting)
        self.exitaction.triggered.connect(sys.exit)
        self.aboutaction.triggered.connect(ab.about)

        self.menubar.addAction(self.helpmenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Batch Message"))
        self.warninglbl.setText(_translate("MainWindow", "***SMS Have A Limit Of 160 Characters***"))
        self.smsbtn.setText(_translate("MainWindow", "Send SMS"))
        self.emailbtn.setText(_translate("MainWindow", "Send Email"))
        self.bothbtn.setText(_translate("MainWindow", "Send Both"))
        self.subjectlbl.setText(_translate("MainWindow", "Subject:- (Only For Emails)"))
        self.msglbl.setText(_translate("MainWindow", "Message:-"))
        self.helpmenu.setTitle(_translate("MainWindow", "Help"))
        self.filemenu.setTitle(_translate("MainWindow", "File"))
        self.settingsaction.setText(_translate("MainWindow", "Settings"))
        self.exitaction.setText(_translate("MainWindow", "Exit"))
        self.aboutaction.setText(_translate("MainWindow", "About"))


    def sendtext(self):
        msg = self.msgtxt.toPlainText()
        sms = partial(bm.sendsms, msg)
        return sms()

    def sendmail(self):
        sub = self.subjectline.text()
        body = self.msgtxt.toPlainText()
        mail = partial(bm.sendemail, body, sub)
        return mail()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
