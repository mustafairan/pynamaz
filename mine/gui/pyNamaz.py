# -*- coding: utf-8 -*-

import sys
from preferences import *
from prayerTimes import *

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

# uygulama = QtGui.QApplication(sys.argv)
app = QtGui.QApplication(sys.argv)

class PyNamaz(QtGui.QMainWindow, Ui_MainWindow):
    currentTime="88:88:88"
    fajrTime="88:88"
    asrTime="88:88"
    dhuhrTime="88:88"
    sunriseTime="88:88"
    maghribTime="88:88"
    ishaTime="88:88"
    nextTime=""#indicates next prayer time. it can be Asr,Dhuhr,Maghrib,Isha or Fajr
    currentDate=""
    remainingTime="00:00:00"#indicates remaining time for the next prayer time
    differences=[]

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        #creating and instance of preferences class.
        #this class sets and keeps preferences variables. also it can return sttings to default etc.
        preferences.__init__
        #Continually updating time
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.setCurrentTime)
        timer.timeout.connect(self.calculateRemainingTime)
        timer.start(1000)

        self.setPrayerTimes() #Parsing times file PrayerTimes.txt and setting time variables
        self.printPrayerTimes() #printing prayer times to the gui

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

    
        #Link Buttons Section
        self.pushButton_2.clicked.connect(lambda: self.openLink('http://mustafairan.wordpress.com'))
        self.pushButton_3.clicked.connect(lambda: self.openLink('http://github.com/mustafairan/pynamaz'))
        self.pushButton.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))
    def setCurrentTime(self): #sets and continually updates then prints current time
        #TODO Should warn the user to set his system clock properly
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
            self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
            self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
            #print self.currentDate + " "+ self.currentTime
            # pass
        except:
            print "current time and date can't be obtained from operating system" #should be gui warning

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
        self.labelCurrentDate.setText(self.currentDate)
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
        def setAppereance(self,appereance_choice):
         if appereance_choice == None:
            appereance_choice = "Cleanlooks"
         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(appereance_choice))
    def openLink(self,url=''):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))
    def TESTFUNC(self):
        #print QtCore.QTime.currentTime()
        #currentDate = QtCore.QDate().currentDate().toString("dd MMMM yyyy")
        #print(currentDate)

        # self.timerSaat = QtCore.QTimer()
        # self.connect(self.timerSaat, QtCore.SIGNAL("timeout()"), self.TESTFUNC2())
        # self.timerSaat.start(300)
        #getObject=getPrayerTimes()
        #getPrayerTimes.__init__(getObject)
        pass
    def TESTFUNC2(self):

        # if self.simdikiTarih != self.tarih:
        #     self.label_4.setText(self.label)
        #     self.simdikiTarih = self.tarih
        pass
    def TESTFUNC3(self):
        #warn template
        if self.nextTime=='Sunrise':
            pass
        if self.nextTime=='Fajr':
            pass
        if self.nextTime=='Dhuhr':
            pass
        if self.nextTime=='Asr':
            pass
        if self.nextTime=='Maghrib':
            pass
        if self.nextTime=='Asr':

            pass


    def calculateRemainingTime(self):
        #type casting time variables from string to qtime
        currentQtime=QtCore.QTime(int(self.currentTime.split(":")[0]),int(self.currentTime.split(":")[1]),int(self.currentTime.split(":")[2]))
        fajrQtime=QtCore.QTime(int(self.fajrTime.split(":")[0]),int(self.fajrTime.split(":")[1]),0)
        asrQtime=QtCore.QTime(int(self.asrTime.split(":")[0]),int(self.asrTime.split(":")[1]),0)
        dhuhrQtime=QtCore.QTime(int(self.dhuhrTime.split(":")[0]),int(self.dhuhrTime.split(":")[1]),0)
        sunriseQtime=QtCore.QTime(int(self.sunriseTime.split(":")[0]),int(self.sunriseTime.split(":")[1]),0)
        maghribQtime=QtCore.QTime(int(self.maghribTime.split(":")[0]),int(self.maghribTime.split(":")[1]),0)
        ishaQtime=QtCore.QTime(int(self.ishaTime.split(":")[0]),int(self.ishaTime.split(":")[1]),0)

        #to find out the time interval for the next time, we should find the minimum of negative differrences among times and current time
        #QtCore.QTime.secsTo(param1,param2) returns the two time object's difference in second
        differences=[QtCore.QTime.secsTo(fajrQtime,currentQtime),
                     QtCore.QTime.secsTo(sunriseQtime,currentQtime),
                     QtCore.QTime.secsTo(dhuhrQtime,currentQtime),
                     QtCore.QTime.secsTo(asrQtime,currentQtime),
                     QtCore.QTime.secsTo(maghribQtime,currentQtime),
                     QtCore.QTime.secsTo(ishaQtime,currentQtime)]
        #print differences

        #print self.turnSecondsInto(differences[4])

        for index in range(0,6):
            if differences[index] < 0:
                seconds=differences[index]
                break

        if index==0:
            self.nextTime=="Fajr"
            self.labelNextPrayer.setText(u"İmsağa kalan süre")
        if index==1:
            self.nextTime=="Sunrise"
            self.labelNextPrayer.setText(u"Güneşe kalan süre")
        if index==2:
            self.nextTime=="Dhuhr"
            self.labelNextPrayer.setText(u"Öğleye kalan süre")
        if index==3:
            self.nextTime=="Asr"
            self.labelNextPrayer.setText(u"İkindiye kalan süre")
        if index==4:
            self.nextTime=="Maghrib"
            self.labelNextPrayer.setText(u"Akşama kalan süre")
        if index==5:
            self.nextTime=="Isha"
            self.labelNextPrayer.setText(u"Yatsıya kalan süre")

        self.remainingTime=str(self.turnSecondsInto((-1)*seconds)) #turn remaining seconds to hh:mm:ss
        #printing time into remaining time section
        self.lcdNumberNextPrayerHour.display(self.remainingTime.split(':')[0])
        self.lcdNumberNextPrayerMinute.display(self.remainingTime.split(':')[1])
        self.lcdNumberNextPrayerSecond.display(self.remainingTime.split(':')[2])


    def turnSecondsInto(self,seconds):#turns seconds into hour minute and second . returns as string hh:mm:ss
        days, seconds = divmod(seconds, 24*60*60)
        hours, seconds = divmod(seconds, 60*60)
        minutes, seconds = divmod(seconds, 60)
        return str(hours)+":"+str(minutes)+":"+str(seconds)


if __name__ == "__main__":
    # uygulama.setApplicationName("rastgele bir isim") Phonon modülünün kusursuz çalışması için gerekli.
    app.setApplicationName("pynamaz")
    program = PyNamaz()
    program.show()
    sys.exit(app.exec_())
