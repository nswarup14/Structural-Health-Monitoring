# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FFT.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import inputTime
import test
import variable
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

class Ui_FFT_technique(object):


    def fft_inputTime(self):
        self.form= QtGui.QWidget()
        self.other= inputTime.Ui_InputTime_FFT()
        self.other.setupUi(self.form)
        self.form.show()
    def fft_test(self):
        #FFT_Test.main()
        self.form= QtGui.QWidget()
        self.other= test.Ui_test_FFT()
        self.other.setupUi(self.form)
        self.form.show()
    def fft_variable(self):
        #FFT_Variable.main()
        self.form= QtGui.QWidget()
        self.other= variable.Ui_variableTime()
        self.other.setupUi(self.form)
        self.form.show()

    def setupUi(self, FFT_technique):
        FFT_technique.setObjectName(_fromUtf8("FFT_technique"))
        FFT_technique.setWindowModality(QtCore.Qt.ApplicationModal)
        FFT_technique.resize(400, 300)
        self.widget = QtGui.QWidget(FFT_technique)
        self.widget.setGeometry(QtCore.QRect(40, 50, 341, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.retranslateUi(FFT_technique)
        QtCore.QMetaObject.connectSlotsByName(FFT_technique)

    def retranslateUi(self, FFT_technique):
        FFT_technique.setWindowTitle(_translate("FFT_technique", "Form", None))
        self.pushButton.setText(_translate("FFT_technique", "Testing", None))
        self.label.setText(_translate("FFT_technique", "Select time and the transformation function", None))

        self.pushButton.clicked.connect(self.fft_inputTime)

        self.pushButton_2.setText(_translate("FFT_technique", "Custom", None))
        self.label_2.setText(_translate("FFT_technique", "Choose Sampling rate", None))

        self.pushButton_2.clicked.connect(self.fft_variable)

        self.pushButton_3.setText(_translate("FFT_technique", "Best Fit", None))
        self.label_3.setText(_translate("FFT_technique", "Mean Sampling rate", None))

        self.pushButton_3.clicked.connect(self.fft_test)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FFT_technique = QtGui.QWidget()
    ui = Ui_FFT_technique()
    ui.setupUi(FFT_technique)
    FFT_technique.show()
    sys.exit(app.exec_())

