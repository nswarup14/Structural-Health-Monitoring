# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Arima.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import arima
import basic_exponential
import trend_exponential
import seasoning_exponential
import ARMA, ARIMA
from arima import ma,ar


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
	
    def moving_average(self):
        ma.main()

    def basic_exponential(self):
    	self.selfForm= QtGui.QWidget()
    	self.otherForm= basic_exponential.Ui_Form()
    	self.otherForm.setupUi(self.selfForm)
    	self.selfForm.show()

    def trend_exponential(self):
    	self.selfForm= QtGui.QWidget()
    	self.otherForm= trend_exponential.Ui_Form()
    	self.otherForm.setupUi(self.selfForm)
    	self.selfForm.show()

    def seasoning_exponential(self):
    	self.selfForm= QtGui.QWidget()
    	self.otherForm= seasoning_exponential.Ui_Form()
    	self.otherForm.setupUi(self.selfForm)
    	self.selfForm.show()

    def ARMA(self):
    	self.selfForm= QtGui.QWidget()
    	self.otherForm= ARMA.Ui_Form()
    	self.otherForm.setupUi(self.selfForm)
    	self.selfForm.show()

    def ARIMA(self):
    	self.selfForm= QtGui.QWidget()
    	self.otherForm= ARIMA.Ui_Form()
    	self.otherForm.setupUi(self.selfForm)
    	self.selfForm.show()

    def autoRegression(self):
    	ar.main()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(700, 300)
        self.pushButton_7= QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(51,20,200,27))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(51, 60, 200, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 100, 200, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(51, 140,200,27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4= QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(51, 180,280,27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5= QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(51, 220,200,27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6= QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(51, 260,200,27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "MainWindow", None))
        self.pushButton.setText(_translate("Form", "Moving Average Model", None))
        self.pushButton_2.setText(_translate("Form", "Basic Exponential Smoothing", None))
        self.pushButton_3.setText(_translate("Form", "Trend Exponential Smoothing", None))
        self.pushButton_4.setText(_translate("Form", "Trend and seasonal Exponential Smoothing", None))
        self.pushButton_5.setText(_translate("Form", "ARMA", None))
        self.pushButton_6.setText(_translate("Form", "ARIMA", None))
        self.pushButton_7.setText(_translate("Form","Auto Regression Model",None))
        

        self.pushButton.clicked.connect(self.moving_average)
        self.pushButton_2.clicked.connect(self.basic_exponential)
        self.pushButton_3.clicked.connect(self.trend_exponential)
        self.pushButton_4.clicked.connect(self.seasoning_exponential)
        self.pushButton_5.clicked.connect(self.ARMA)
        self.pushButton_6.clicked.connect(self.ARIMA)
        self.pushButton_7.clicked.connect(self.autoRegression)
        #self.pushButton_2.setText(_translate("Form", "\"Enter Text here\"", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
