# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Mon Jan 11 19:40:15 2016
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
        MainWindow.resize(273, 319)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSdsd = QtGui.QMenu(self.menubar)
        self.menuSdsd.setObjectName(_fromUtf8("menuSdsd"))
        self.menuSdsdsds = QtGui.QMenu(self.menuSdsd)
        self.menuSdsdsds.setObjectName(_fromUtf8("menuSdsdsds"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSdsd = QtGui.QAction(MainWindow)
        self.actionSdsd.setObjectName(_fromUtf8("actionSdsd"))
        self.actionSdsdsds = QtGui.QAction(MainWindow)
        self.actionSdsdsds.setObjectName(_fromUtf8("actionSdsdsds"))
        self.actionSdsds = QtGui.QAction(MainWindow)
        self.actionSdsds.setObjectName(_fromUtf8("actionSdsds"))
        self.actionSdsdsdsd = QtGui.QAction(MainWindow)
        self.actionSdsdsdsd.setObjectName(_fromUtf8("actionSdsdsdsd"))
        self.menuSdsdsds.addAction(self.actionSdsds)
        self.menuSdsdsds.addAction(self.actionSdsdsdsd)
        self.menuSdsd.addAction(self.actionSdsd)
        self.menuSdsd.addAction(self.actionSdsdsds)
        self.menuSdsd.addAction(self.menuSdsdsds.menuAction())
        self.menubar.addAction(self.menuSdsd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuSdsd.setTitle(_translate("MainWindow", "sdsd", None))
        self.menuSdsdsds.setTitle(_translate("MainWindow", "sdsdsds", None))
        self.actionSdsd.setText(_translate("MainWindow", "sdsd", None))
        self.actionSdsdsds.setText(_translate("MainWindow", "sdsdsds", None))
        self.actionSdsds.setText(_translate("MainWindow", "sdsds", None))
        self.actionSdsdsdsd.setText(_translate("MainWindow", "sdsdsdsd", None))

