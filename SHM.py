#
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SHM.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import defaultPress
import Arima_1

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

class Ui_SHM(object):

    def defaultPressCall(self):
        self.form1= QtGui.QWidget()
        self.other1= defaultPress.Ui_Signal_Processing()
        self.other1.setupUi(self.form1)
        self.form1.show()
  	 
    def arimaPressCall(self):
    	self.form2= QtGui.QWidget()
    	self.other2= Arima_1.Ui_Arima_Processing()
    	self.other2.setupUi(self.form2)
    	self.form2.show()
	
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(307, 207)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.verticalLayout.addLayout(self.formLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_3)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton_3)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_4)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.SpanningRole, self.textBrowser)
   
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        
        self.label_6.setText(_translate("Form", "About:-", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is a toolbox made for performing SHM easier. It consits of Signal Processing tools and other Machine Learning Algorithms. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("Form", "Please Click one of the below to run the software", None))
        self.pushButton.setText(_translate("Form", "Signal Processing", None))

        self.pushButton.clicked.connect(self.defaultPressCall)
        
        self.label_3.setText(_translate("Form", "Techniques for signal processing", None))
        self.pushButton_3.setText(_translate("Form", "Arima", None))
        self.label_4.setText(_translate("Form", "Techniques for the Arima model", None))
        
        
        self.pushButton_3.clicked.connect(self.arimaPressCall)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_SHM()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

