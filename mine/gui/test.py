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
    currentTime="88:88:88"
    fajrTime="88:88"
    asrTime="88:88"
    dhuhrTime="88:88"
    sunriseTime="88:88"
    maghribTime="88:88"
    ishaTime="88:88"
    nextTime="88:88"
    currentDate="18.12.15"
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)

        #Continually updating time
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.setCurrentTime)
        timer.start(1000)
        #self.setCurrentTime()

        #TEST BUTTON
        #self.testbutton.clicked.connect(self.setPrayerTimes)#takes current date for now
        #self.testbutton.clicked.connect(self.printPrayerTimes)

        self.setPrayerTimes()
        self.printPrayerTimes()

        #Menu Section
            #Appereance Preferances
        self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))
        self.actionPlastique.triggered.connect(lambda: self.setAppereance('Plastique'))
        self.actionPlastique.triggered.connect(lambda: self.setAppereance('Gtk'))
        self.actionBespin.triggered.connect(lambda: self.setAppereance('Bespin'))
        self.actionCDE.triggered.connect(lambda: self.setAppereance('CDE'))
        self.actionMotif.triggered.connect(lambda: self.setAppereance('Motif'))
        self.actionOxygen.triggered.connect(lambda: self.setAppereance('Oxygen'))
        self.actionQtcurve.triggered.connect(lambda: self.setAppereance('Qtcurve'))
        self.actionWindows.triggered.connect(lambda: self.setAppereance('Windows'))

        #Current date Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

        #Current City Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

        #Current Time Section
        # self.lcdNumberCurrentHour.display(self.currentTimeHour)
        # self.lcdNumberCurrentMinute.display(self.currentTimeMinute)
        # self.lcdNumberFajrHour.display(self.fajrTimeHour)
        # self.lcdNumberFajrMinute.display(self.fajrTimeMinute)
        # self.lcdNumberSunriseHour.display(self.sunriseTimeHour)
        # self.lcdNumberSunriseMinute.display(self.sunriseTimeMinute)
        # self.lcdNumberMaghribHour.display(self.maghribTimeHour)
        # self.lcdNumberMaghribMinute.display(self.maghribTimeMinute)
        # self.lcdNumberDhuhrHour.display(self.dhuhrTimeHour)
        # self.lcdNumberDhuhrMinute.display(self.dhuhrTimeMinute)
        # self.lcdNumberAsrHour.display(self.asrTimeHour)
        # self.lcdNumberAsrMinute.display(self.asrTimeMinute)
        # self.lcdNumberIshaHour.display(self.ishaTimeHour)
        # self.lcdNumberIshaMinute.display(self.ishaTimeMinute)
        # self.lcdNumberNextPrayerHour.display(self.nextTimeHour)
        # self.lcdNumberNextPrayerMinute.display(self.nextTimeMinute)


        #Prayer Time Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

        #Next Prayer Time Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))


        #Select Region Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

         #Time Warnings Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

        #Preferences Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

        #Qadha Counts Section
        # self.actionCleanlooks.triggered.connect(lambda: self.setAppereance('Cleanlooks'))

        #Link Buttons Section
        self.pushButton_2.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))
        self.pushButton_3.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))
        self.pushButton_first.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))

    def setCurrentTime(self): #sets and continually updates then prints current time
        self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
        self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
        self.lcdNumberCurrentHour.display(self.currentTime.split(':')[0])
        self.lcdNumberCurrentMinute.display(self.currentTime.split(':')[1])
        self.lcdNumberCurrentSecond.display(self.currentTime.split(':')[2])

    def setPrayerTimes(self): #Parses times file PrayerTimes.txt and sets time variables

        #PrayerTimes.txt format:
            #dd_mm_yy fajr_time sunrise_time dhuhr_time asr_time maghrib_time isha_time
            #17.12.15 06:08 07:09 08:08 09:11 10:12: 11:13

        #firstly, Current date and time must be set
        try:
            #self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
            #self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
            #print self.currentDate + " "+ self.currentTime
            pass
        except:
            print "current time and date cant be obtained from operating system" #should be gui warning

        #Finding Current date's prayer times from the file and assigning
        timesFileObject = open("PrayerTimes.txt", 'r')
        for line in timesFileObject:
            if line.split(' ')[0]==self.currentDate:
                self.fajrTime=line.split(' ')[1]
                self.sunriseTime=line.split(' ')[2]
                self.dhuhrTime=line.split(' ')[3]
                self.asrTime=line.split(' ')[4]
                self.maghribTime=line.split(' ')[5]
                self.ishaTime=line.split(' ')[6]
    def printPrayerTimes(self): #prints prayer times to the gui
        #self.labelCurrentDate.setText(self.currentDate)

        self.lcdNumberFajrHour.display(self.fajrTime.split(':')[0])
        self.lcdNumberFajrMinute.display(self.fajrTime.split(':')[1])
        self.lcdNumberSunriseHour.display(self.sunriseTime.split(':')[0])
        self.lcdNumberSunriseMinute.display(self.sunriseTime.split(':')[1])
        self.lcdNumberDhuhrHour.display(self.dhuhrTime.split(':')[0])
        self.lcdNumberDhuhrMinute.display(self.dhuhrTime.split(':')[1])
        self.lcdNumberAsrHour.display(self.asrTime.split(':')[0])
        self.lcdNumberAsrMinute.display(self.asrTime.split(':')[1])
        self.lcdNumberMaghribHour.display(self.maghribTime.split(':')[0])
        self.lcdNumberMaghribMinute.display(self.maghribTime.split(':')[1])
        self.lcdNumberIshaHour.display(self.ishaTime.split(':')[0])
        self.lcdNumberIshaMinute.display(self.ishaTime.split(':')[1])

    def TESTFUNC(self):
        #print QtCore.QTime.currentTime()
        #currentDate = QtCore.QDate().currentDate().toString("dd MMMM yyyy")
        #print(currentDate)

        # self.timerSaat = QtCore.QTimer()
        # self.connect(self.timerSaat, QtCore.SIGNAL("timeout()"), self.TESTFUNC2())
        # self.timerSaat.start(300)
        pass
    def TESTFUNC2(self):
        pass




        print(self.currentDate)


        # if self.simdikiTarih != self.tarih:
        #     self.label_4.setText(self.label)
        #     self.simdikiTarih = self.tarih

    def setAppereance(self,appereance_choice):
         if appereance_choice == None:
             appereance_choice = "Cleanlooks"
         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(appereance_choice))
    def openLink(self,url=''):

        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))

if __name__ == "__main__":
    # uygulama.setApplicationName("rastgele bir isim") Phonon modülünün kusursuz çalışması için gerekli.
    uygulama.setApplicationName("pynamaz")
    program = PyNamaz()
    program.show()
    sys.exit(uygulama.exec_())
