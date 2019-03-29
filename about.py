from PyQt5 import QtCore, QtGui, QtWidgets

class ab_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 170)
        Dialog.setWindowIcon(QtGui.QIcon("icon.png"))
        Dialog.setMinimumSize(QtCore.QSize(331, 171))
        Dialog.setMaximumSize(QtCore.QSize(331, 171))
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 331, 171))
        self.textBrowser.setMinimumSize(QtCore.QSize(331, 171))
        self.textBrowser.setMaximumSize(QtCore.QSize(331, 171))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.textBrowser.setText("Batch Message is a tool which sends SMS and E-mail to multiple contacts fetched from a sqlite database.\n"
                                                                 "\nSource:\n\n"
                                                                 "https://github.com/Destroyerrockz/BatchMessage")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def about(self):
        Dialog = QtWidgets.QDialog()
        ui = ab_dialog()
        Dialog.setModal(True)
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()