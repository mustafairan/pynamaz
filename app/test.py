# -*- coding: utf-8 -*-
#xyzggg
import sys
import os #just for os.system and os.chdir

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

from ui_pynamaz import Ui_MainWindow

app = QtGui.QApplication(sys.argv)

class PyNamaz(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
        QtGui.QMainWindow.setWindowTitle(self,"pyNamaz")

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        #self.printit()
        self.drawTime()


    def printit(self):
        print "printit called"
        self.trayIcon.showMessage("Namaz Vakti","12345",self.trayIcon.Information, 15550)

    def drawTime(self):
        te=QtGui.QTextEdit("11")
        te.resize(30, 30)
        pix=QtGui.QPixmap.grabWidget (te, 0,0,-1,-1)
        pix.save("test.png")


if __name__ == "__main__":
    app.setApplicationName("pynamaz") #necessary for phonon module.
    program = PyNamaz()
    program.show()
    sys.exit(app.exec_())
