# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana_pencere.ui'
#
# Created: Mon Dec 14 23:25:01 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 226, 481, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fahrenheit_box = QtGui.QSpinBox(self.gridLayoutWidget)
        self.fahrenheit_box.setObjectName(_fromUtf8("fahrenheit_box"))
        self.gridLayout.addWidget(self.fahrenheit_box, 1, 1, 1, 1)
        self.to_fahrenheit_btn = QtGui.QPushButton(self.gridLayoutWidget)
        self.to_fahrenheit_btn.setObjectName(_fromUtf8("to_fahrenheit_btn"))
        self.gridLayout.addWidget(self.to_fahrenheit_btn, 2, 0, 1, 1)
        self.celcius_box = QtGui.QSpinBox(self.gridLayoutWidget)
        self.celcius_box.setObjectName(_fromUtf8("celcius_box"))
        self.gridLayout.addWidget(self.celcius_box, 1, 0, 1, 1)
        self.to_celcius_btn = QtGui.QPushButton(self.gridLayoutWidget)
        self.to_celcius_btn.setObjectName(_fromUtf8("to_celcius_btn"))
        self.gridLayout.addWidget(self.to_celcius_btn, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.to_fahrenheit_btn.setText(_translate("MainWindow", ">>>>to fahrenheit", None))
        self.to_celcius_btn.setText(_translate("MainWindow", "to celcius<<<<", None))
        self.label_2.setText(_translate("MainWindow", "fahrenheit", None))
        self.label.setText(_translate("MainWindow", "celcius", None))

