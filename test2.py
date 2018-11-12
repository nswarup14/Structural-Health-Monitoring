# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import FFT_Test
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

    def messagePoint2(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("Please check atleast 1 checkbox")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return


    def messagePoint1(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("Please do not check both the boxes for the same coefficient")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return

    def messagePoint(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("One of the Input values havent been entered. Please enter them all")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return

    def checkPoint(self): 

        flag=0
        #print(self.checkBox_5.isChecked())

        if(self.lineEdit_5.text()=="" or self.lineEdit_6.text()==""):
            flag=1
            self.messagePoint()
            return

        if(self.checkBox.isChecked() or self.checkBox_2.isChecked() or self.checkBox_3.isChecked() or self.checkBox_4.isChecked() or self.checkBox_5.isChecked() or self.checkBox_6.isChecked() or self.checkBox_7.isChecked() or self.checkBox_8.isChecked()):
            pass
        else:
            flag=1
            self.messagePoint2()
            return            

        if((self.checkBox.isChecked() and self.checkBox_5.isChecked()) or (self.checkBox_2.isChecked() and self.checkBox_6.isChecked()) or (self.checkBox_3.isChecked() and self.checkBox_7.isChecked()) or (self.checkBox_4.isChecked() and self.checkBox_8.isChecked())):
            flag=1
            self.messagePoint1()
            return

        if(flag == 0):
            list_func=[]
            #coefficient1
            if(self.checkBox.isChecked()):
                list_func.append(self.checkBox.text())
            else:
                if(self.checkBox_5.isChecked()):
                    list_func.append(self.checkBox_5.text())
                else:
                    list_func.append("none")


            if(self.checkBox_2.isChecked()):
                list_func.append(self.checkBox_2.text())
            else:
                if(self.checkBox_6.isChecked()):
                    list_func.append(self.checkBox_6.text())
                else:
                    list_func.append("none")

            if(self.checkBox_3.isChecked()):
                list_func.append(self.checkBox_3.text())
            else:
                if(self.checkBox_7.isChecked()):
                    list_func.append(self.checkBox_7.text())
                else:
                    list_func.append("none")

            if(self.checkBox_4.isChecked()):
                list_func.append(self.checkBox_4.text())
            else:
                if(self.checkBox_8.isChecked()):
                    list_func.append(self.checkBox_8.text())
                else:
                    list_func.append("none")

            FFT_Test.main(self.lineEdit.text(), self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),list_func, self.lineEdit_5.text(),self.lineEdit_6.text())

    """   
        if(self.lineEdit.text() == "" or self.lineEdit_2.text() == "" ):
            self.messagePoint()
            return
        else:
            
            #print(self.lineEdit.text(), " ", self.lineEdit_2.text(), " ", self.lineEdit_3.text(), " ", self.lineEdit_4.text())
            FFT_Test.main(self.lineEdit.text(), self.lineEdit_2.text())
    """

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 423)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 80, 54, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 54, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 361, 61))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 110, 310, 140))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 4, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_4.addWidget(self.checkBox_5, 0, 1, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout_4.addWidget(self.checkBox_6, 1, 1, 1, 1)
        self.checkBox_7 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout_4.addWidget(self.checkBox_7, 2, 1, 1, 1)
        self.checkBox_8 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.gridLayout_4.addWidget(self.checkBox_8, 3, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 88, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 260, 231, 66))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Sine", None))
        self.label_2.setText(_translate("Form", "Cosine", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tick boxes of the functions you want to select. The function is of the format, sin(x*omega*t), where omega is 2*pi and t is time and x is the coffiencient that is taken as an input.</p></body></html>", None))
        self.label_3.setText(_translate("Form", "coefficient x", None))
        self.checkBox.setText(_translate("Form", "sine", None))
        self.checkBox_2.setText(_translate("Form", "sine", None))
        self.checkBox_3.setText(_translate("Form", "sine", None))
        self.checkBox_4.setText(_translate("Form", "sine", None))
        self.checkBox_5.setText(_translate("Form", "cos", None))
        self.checkBox_6.setText(_translate("Form", "cos", None))
        self.checkBox_7.setText(_translate("Form", "cos", None))
        self.checkBox_8.setText(_translate("Form", "cos", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.label_4.setText(_translate("Form", "Enter time for sampling", None))
        self.label_5.setText(_translate("Form", "Enter sampling rate", None))


        self.pushButton.clicked.connect(self.checkPoint)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

