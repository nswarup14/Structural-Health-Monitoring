# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CWT.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import CWT_noise
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):

    def checkPoint(self):
        msg= QtGui.QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setText("Please a valid file path")
        msg.setWindowTitle("MessageBox")

        msg.setStandardButtons(QtGui.QMessageBox.Yes)
        ret= msg.exec_()
    
        if(ret== QtGui.QMessageBox.Yes):
            return

    def messagePoint(self):
        
        try:
            open(self.lineEdit.text(),"r")
        except FileNotFoundError as e:
            self.checkPoint()
            return

        CWT_noise.main(self.lineEdit.text())

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 100, 151, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 113, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton= QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40,150, 80,27))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Enter the path of the file", None))
        self.pushButton.setText(_translate("Form","Ok",None))

        self.pushButton.clicked.connect(self.messagePoint)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

