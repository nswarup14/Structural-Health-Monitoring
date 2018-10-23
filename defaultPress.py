# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defaultPress.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import FFT
import CWT

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

class Ui_Signal_Processing(object):

    def FFTcall(self):
        self.form= QtGui.QWidget()
        self.other= FFT.Ui_FFT_technique()
        self.other.setupUi(self.form)
        self.form.show()
    def CWDcall(self):
        self.form= QtGui.QWidget()
        self.other= CWT.Ui_Form()
        self.other.setupUi(self.form)
        self.form.show()
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(367, 229)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.textBrowser)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton_2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_2)
       

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Try out one of the 2 buttons for results. Both these Signal Processing tools are for Time to Frequency Domain Analysis. They can also be used for noise filtering using filters, etc. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.pushButton_2.setText(_translate("Form", "FFT", None))
        self.pushButton_2.clicked.connect(self.FFTcall)
        self.label.setText(_translate("Form", "Click to demonstrate the FFT technique", None))
        self.pushButton.setText(_translate("Form", "CWT", None))
        self.pushButton.clicked.connect(self.CWDcall)
        self.label_2.setText(_translate("Form", "Click to demonstrate the CWT technique", None))
     

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Signal_Processing()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


