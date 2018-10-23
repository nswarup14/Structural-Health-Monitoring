# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'variable.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import FFT_Variable
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

class Ui_variableTime(object):

    def messagePoint1(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("One of the Input values havent been entered. Please enter them all")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return

    def messagePoint2(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("Value of l2 < l1. Please enter the correct values")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return
    def checkPoint(self):
        if(self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == ""):
            self.messagePoint1()
            return
        if( int(self.lineEdit_3.text()) < int(self.lineEdit_2.text())):
            self.messagePoint2()
            return

        else:  
            #print(self.lineEdit.text(), " ", self.lineEdit_2.text(), " ", self.lineEdit_3.text(), " ", self.lineEdit_4.text())
            FFT_Variable.main(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())

    def setupUi(self, variableTime):
        variableTime.setObjectName(_fromUtf8("variableTime"))
        variableTime.resize(688, 300)
        self.layoutWidget = QtGui.QWidget(variableTime)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 586, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 3, 1)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(variableTime)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 88, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(variableTime)
        QtCore.QMetaObject.connectSlotsByName(variableTime)

    def retranslateUi(self, variableTime):
        variableTime.setWindowTitle(_translate("variableTime", "Form", None))
        self.label_2.setText(_translate("variableTime", "2) Enter the sampling rate (integer) at which the reading was taken", None))
        self.label.setText(_translate("variableTime", "1) Enter the Name of the file", None))
        self.label_3.setText(_translate("variableTime", "3) Enter the sampling rate (integer) at which you want the FFT to be done, in case", None))
        self.label_4.setText(_translate("variableTime", " of doubt enter the sampling rate you entered previously for observing results", None))
        self.pushButton.setText(_translate("variableTime", "OK", None))

        self.pushButton.clicked.connect(self.checkPoint)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    variableTime = QtGui.QWidget()
    ui = Ui_variableTime()
    ui.setupUi(variableTime)
    variableTime.show()
    sys.exit(app.exec_())

