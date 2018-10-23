# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
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

class Ui_test_FFT(object):

    def messagePoint(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("One of the Input values havent been entered. Please enter them all")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return

    def checkPoint(self):
        
        
        if(self.lineEdit.text() == "" or self.lineEdit_2.text() == "" ):
            self.messagePoint()
            return
        else:
            
            #print(self.lineEdit.text(), " ", self.lineEdit_2.text(), " ", self.lineEdit_3.text(), " ", self.lineEdit_4.text())
            FFT_Test.main(self.lineEdit.text(), self.lineEdit_2.text())

    def setupUi(self, test_FFT):
        test_FFT.setObjectName(_fromUtf8("test_FFT"))
        test_FFT.resize(614, 300)
        self.widget = QtGui.QWidget(test_FFT)
        self.widget.setGeometry(QtCore.QRect(23, 60, 562, 103))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.gridLayout)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton)

        self.retranslateUi(test_FFT)
        QtCore.QMetaObject.connectSlotsByName(test_FFT)

    def retranslateUi(self, test_FFT):
        test_FFT.setWindowTitle(_translate("test_FFT", "Form", None))
        self.label.setText(_translate("test_FFT", "Enter Sampling rate", None))
        self.label_2.setText(_translate("test_FFT", "Enter time lenght in seconds, the time for which you want to perform the fft", None))
        self.pushButton.setText(_translate("test_FFT", "OK", None))

        self.pushButton.clicked.connect(self.checkPoint)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    test_FFT = QtGui.QWidget()
    ui = Ui_test_FFT()
    ui.setupUi(test_FFT)
    test_FFT.show()
    sys.exit(app.exec_())

