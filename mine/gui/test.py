# -*- coding: utf-8 -*-

import sys,urllib


try:
    from PyQt4 import QtCore, QtGui
except:
    print u"PyQt modülü yüklü değil.\nPyQt 4.5 veya üzeri bir sürüm yükledikten tekrar deneyin."
    sys.exit()

try:
    from PyQt4.phonon import Phonon
except:
    QtGui.QMessageBox.information(None, u"Modül Hatası", u"Phonon modülü bulunamadı. Yükledikten sonra tekrar deneyin", "Kapat")
    sys.exit()

#from moduller.UlkelerSehirler import UlkelerSehirler
from ui_pynamaz.py import Ui_MainWindow

uygulama = QtGui.QApplication(sys.argv)

