# -*- coding: utf-8 -*-

import sys, urllib


try:
    from PyQt4 import QtCore, QtGui
except:
    print u"PyQt modülü yüklü değil.\nPyQt 4.5 veya üzeri bir sürüm yükledikten tekrar deneyin."
    sys.exit()

try:
    from PyQt4.phonon import Phonon
except:
    QtGui.QMessageBox.information(None, u"Modül Hatası", u"Phonon modülü bulunamadı. Yükledikten sonra tekrar deneyin",
                                  "Kapat")
    sys.exit()

# from moduller.UlkelerSehirler import UlkelerSehirler
from ui_pynamaz import Ui_MainWindow

# uygulama = QtGui.QApplication(sys.argv)
uygulama = QtGui.QApplication(sys.argv)


class PyNamaz(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)


        self.pushButton_first.clicked.connect(self.siteyeGir)
        #self.actionCleanlooks.triggered.connect(self.cleanlooksGorunumu)

        self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        self.pushButton_2.clicked.connect(lambda: self.siteyeGir('http://diyanet.gov.tr'))
        
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))













    # def cleanlooksGorunumu(self):
    #     self.gorunum = "Cleanlooks"
    #     QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))

    def setAppereance(self,appereance_choice):
         #self.gorunum = "Cleanlooks"
         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(appereance_choice))


    def siteyeGir(self,url=''):

        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))


if __name__ == "__main__":
    # uygulama.setApplicationName("rastgele bir isim") Phonon modülünün kusursuz çalışması için gerekli.
    uygulama.setApplicationName("pynamaz")
    program = PyNamaz()
    program.show()
    sys.exit(uygulama.exec_())
