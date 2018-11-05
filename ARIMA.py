# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ARIMA.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import arima
from arima import starima
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

    def message_alert(self):
        try:
            p= int(self.lineEdit.text())
            d= int(self.lineEdit_2.text())
            q= int(self.lineEdit_3.text())
        except ValueError as e:
            msg= QtGui.QMessageBox()
            #msg.setIcon(QMessageBox.Critical)
            msg.setText("Please enter Integer values")
            msg.setWindowTitle("MessageBox")

            msg.setStandardButtons(QtGui.QMessageBox.Yes)
            ret= msg.exec_()
        
            if(ret== QtGui.QMessageBox.Yes):
                return

        if(int(self.lineEdit_2.text())>2):
            msg= QtGui.QMessageBox()
            #msg.setIcon(QMessageBox.Critical)
            msg.setText("The value of D has to be less than 2")
            msg.setWindowTitle("MessageBox")

            msg.setStandardButtons(QtGui.QMessageBox.Yes)
            ret= msg.exec_()
        
            if(ret== QtGui.QMessageBox.Yes):
                return
        starima.main(self.lineEdit.text(),self.lineEdit_2.text(), self.lineEdit_3.text())

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 88, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 60, 180, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.label.setText(_translate("Form", "Enter P value", None))
        self.label_2.setText(_translate("Form", "Enter D value", None))
        self.label_3.setText(_translate("Form", "Enter Q value", None))


        self.pushButton.clicked.connect(self.message_alert)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

