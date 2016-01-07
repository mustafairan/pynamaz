# -*- coding: utf-8 -*-
#xyz
import sys
import os #just for os.system
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
    currentTime="88:88:88"
    fajrTime="88:88"
    asrTime="88:88"
    dhuhrTime="88:88"
    sunriseTime="88:88"
    maghribTime="88:88"
    ishaTime="88:88"
    nextFajrTime="88:88"
    nextTime=""#indicates next prayer time. it can be Asr,Dhuhr,Maghrib,Isha or Fajr
    currentDate=""
    remainingTime="00:00:00"#indicates remaining time for the next prayer time
    differences=[] #no use anymore!

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
        QtGui.QMainWindow.setWindowTitle(self,"pyNamaz")


        QtGui.QMessageBox.information(None, u"Nasıl kullanılır?",
                                      u"Uygulama sistem saatinizi kullanmaktadır. Saatinizin doğru olduğundan emin olun.\n"
                                      u"Uygulamanın çalışması için gerekli vakit bilgisini PrayerTimes.txt dosyasına kaydetmelisiniz.\n"

                                      u"\nGerekli aylık vakit bilgilerine ulaşmak için linkler bölümündeki vakit bağlantısı butonunu kullanın ve gelen tablodaki bilgileri farenizle seçip kopyalayın\n"
                                      u"Dosyayı açmak için Namaz vakitleri dosyasını aç butonunu kullanınız",u"Anladım")

        #prayerTimesObj=prayerTimes()
        #TODO self.pushButtonSetTimesManuelly.clicked.connect(lambda: prayerTimes.getTimesManuelly(prayerTimesObj))


        #Continually updating time and remaining time
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.setCurrentTime)
        timer.timeout.connect(self.calculateRemainingTime3)
        timer.start(1000)

        self.setPrayerTimes2() #Parsing times file PrayerTimes.txt and setting time variables
        self.printPrayerTimes() #printing prayer times to the gui

        #Menu Section
            #Appereance Preferances
        self.actionCleanlooks.triggered.connect(lambda: self.setAppearance('Cleanlooks'))
        self.actionPlastique.triggered.connect(lambda: self.setAppearance('Plastique'))
        self.actionPlastique.triggered.connect(lambda: self.setAppearance('Gtk'))
        self.actionBespin.triggered.connect(lambda: self.setAppearance('Bespin'))
        self.actionCDE.triggered.connect(lambda: self.setAppearance('CDE'))
        self.actionMotif.triggered.connect(lambda: self.setAppearance('Motif'))
        self.actionOxygen.triggered.connect(lambda: self.setAppearance('Oxygen'))
        self.actionQtcurve.triggered.connect(lambda: self.setAppearance('Qtcurve'))
        self.actionWindows.triggered.connect(lambda: self.setAppearance('Windows'))

        self.pushButtonOpenPrayerTimesText.clicked.connect(self.openPrayerTimesText)

        #Link Buttons Section
        self.pushButton_2.clicked.connect(lambda: self.openLink('http://mustafairan.wordpress.com'))
        self.pushButton_3.clicked.connect(lambda: self.openLink('http://github.com/mustafairan/pynamaz'))
        self.pushButton.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))
        self.pushButton_4.clicked.connect(lambda: self.openLink('http://www.diyanet.gov.tr/tr/PrayerTime/WorldPrayerTimes'))



    def openPrayerTimesText(self):
        """
        opens PrayerTimes.txt file with a text editor
        """
        if sys.platform.startswith("linux"):
            os.system('xdg-open "../data/PrayerTimes.txt"')
        else:
            os.system('start "../data/PrayerTimes.txt"') #TODO this usage can cause problem. file paths should be specified in more efficient way. should be tested in windows systems
    def setCurrentTime(self): #sets and continually updates then prints current time
        #TODO Should warn the user to set his system clock properly
        self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
        self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
        self.lcdNumberCurrentHour.display(self.currentTime.split(':')[0])
        self.lcdNumberCurrentMinute.display(self.currentTime.split(':')[1])
        self.lcdNumberCurrentSecond.display(self.currentTime.split(':')[2])
    def setPrayerTimes(self): #Parses times file PrayerTimes.txt and sets time variables #!!!no use anymore!!!

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

        currentDate= QtCore.QDate.fromString(self.currentDate,"dd.MM.yy")
        nextDate=currentDate.addDays(1)
        nextDate= nextDate.toString("dd.MM.yy")
        #Finding Current date's prayer times from the file and assigning

        #TODO prayertimes.txt path should be specified with more efficient way
        timesFileObject = open(r"../data/PrayerTimes.txt", 'r')
        for line in timesFileObject:
            if line.split(' ')[0]==self.currentDate:

                self.fajrTime=line.split(' ')[1]
                self.sunriseTime=line.split(' ')[2]
                self.dhuhrTime=line.split(' ')[3]
                self.asrTime=line.split(' ')[4]
                self.maghribTime=line.split(' ')[5]
                self.ishaTime=(line.split(' ')[6]).strip('\n') #stripping enter en of it
            elif line.split(' ')[0]==nextDate:
                self.nextFajrTime=line.split(" ")[1]
                break
    def setPrayerTimes2(self): #Parses times file PrayerTimes.txt and sets time variables

        #PrayerTimes.txt format:
            #07.01.2016 \t05:33 \t07:03 \t12:03 \t14:27 \t16:50 \t18:13 \t10:32\n

        #firstly, Current date and time must be set
        try:
            self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
            self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
            #print self.currentDate + " "+ self.currentTime
            # pass
        except:
            print "current time and date can't be obtained from operating system" #should be gui warning

        currentDate= QtCore.QDate.fromString(self.currentDate,"dd.MM.yy")
        nextDate=currentDate.addDays(1)
        nextDate= nextDate.toString("dd.MM.yy")
        #Finding Current date's prayer times from the file and assigning

        #TODO prayertimes.txt path should be specified with more efficient way
        timesFileObject = open(r"../data/PrayerTimes.txt", 'r')
        for line in timesFileObject:

            print str(nextDate)[0:6]+"20"+str(nextDate)[6:]
            if line.split('\t')[0].strip(' ')== str(self.currentDate)[0:6]+"20"+str(self.currentDate)[6:]:
                timeArray=line.split('\t')
                self.fajrTime=timeArray[1].strip(' ')
                self.sunriseTime=timeArray[2].strip(' ')
                self.dhuhrTime=timeArray[3].strip(' ')
                self.asrTime=timeArray[4].strip(' ')
                self.maghribTime=timeArray[5].strip(' ')
                self.ishaTime=timeArray[6].strip(' ')
            elif line.split('\t')[0].strip(' ')==str(nextDate)[0:6]+"20"+str(nextDate)[6:]:#TODO I didnt test this
                self.nextFajrTime=line.split('\t')[1].strip(' ')
                break
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
    def setAppearance(self,appereance_choice):
         if appereance_choice == None:
            appereance_choice = "Cleanlooks"
         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(appereance_choice))
    def openLink(self,url=''):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))
    def calculateRemainingTime(self): #no use anymore
        #TODO following type castings should be done with fromstring() function from QTime
        #type casting time variables from string to qtime
        fajrQtime=QtCore.QTime.fromString(self.fajrTime,"hh:mm")
        currentQtime=QtCore.QTime.fromString(self.currentTime,"hh:mm:ss")
        asrQtime=QtCore.QTime.fromString(self.asrTime,"hh:mm")
        dhuhrQtime=QtCore.QTime.fromString(self.dhuhrTime,"hh:mm")
        sunriseQtime=QtCore.QTime.fromString(self.sunriseTime,"hh:mm")
        maghribQtime=QtCore.QTime.fromString(self.maghribTime,"hh:mm")
        ishaQtime=QtCore.QTime.fromString(self.ishaTime,"hh:mm")
        nextFajrQtime=QtCore.QTime.fromString(self.nextFajrTime,"hh:mm")

        #to find out the time interval for the next time, we should find the minimum of negative differrences among prayer times and current time
        #QtCore.QTime.secsTo(param1,param2) returns the two time object's difference in second
        differences=[QtCore.QTime.secsTo(fajrQtime,currentQtime),
                     QtCore.QTime.secsTo(sunriseQtime,currentQtime),
                     QtCore.QTime.secsTo(dhuhrQtime,currentQtime),
                     QtCore.QTime.secsTo(asrQtime,currentQtime),
                     QtCore.QTime.secsTo(maghribQtime,currentQtime),
                     QtCore.QTime.secsTo(ishaQtime,currentQtime)]
        print differences
        print self.currentTime
        for index in range(0,6):
            if differences[index] < 0: #first negative value is the next prayer time
                seconds=differences[index]
                break
            else :
                seconds=abs(QtCore.QTime.secsTo(nextFajrQtime,currentQtime))
                self.nextTime="Fajr"
        # if index==6:#then we are in isha-fajr time range. We should take next days Fajr time and calculate diffrence with current time

        if index==0:
            self.nextTime="Fajr"
            self.labelNextPrayer.setText(u"İmsağa kalan süre")
        elif index==1:
            self.nextTime="Sunrise"
            self.labelNextPrayer.setText(u"Güneşe kalan süre")
        elif index==2:
            self.nextTime="Dhuhr"
            self.labelNextPrayer.setText(u"Öğleye kalan süre")
        elif index==3:
            self.nextTime="Asr"
            self.labelNextPrayer.setText(u"İkindiye kalan süre")
        elif index==4:
            self.nextTime="Maghrib"
            self.labelNextPrayer.setText(u"Akşama kalan süre")
        elif index==5 and self.nextTime=="Fajr":

            self.labelNextPrayer.setText(u"İmsağa kalan süre")
        elif index==5 and self.nextTime!="Fajr":
            self.nextTime="Isha"
            self.labelNextPrayer.setText(u"Yatsıya kalan süre")

        self.remainingTime=str(self.turnSecondsInto((-1)*seconds)) #turn remaining seconds to hh:mm:ss
        #printing time into remaining time section
        self.lcdNumberNextPrayerHour.display(self.remainingTime.split(':')[0])
        self.lcdNumberNextPrayerMinute.display(self.remainingTime.split(':')[1])
        self.lcdNumberNextPrayerSecond.display(self.remainingTime.split(':')[2])
    def calculateRemainingTime2(self): #no use anymore
        #TODO following type castings should be done with fromstring() function from QTime
        #type casting time variables from string to qtime
        fajrQtime=QtCore.QTime.fromString(self.fajrTime,"hh:mm")
        currentQtime=QtCore.QTime.fromString(self.currentTime,"hh:mm:ss")
        asrQtime=QtCore.QTime.fromString(self.asrTime,"hh:mm")
        dhuhrQtime=QtCore.QTime.fromString(self.dhuhrTime,"hh:mm")
        sunriseQtime=QtCore.QTime.fromString(self.sunriseTime,"hh:mm")
        maghribQtime=QtCore.QTime.fromString(self.maghribTime,"hh:mm")
        ishaQtime=QtCore.QTime.fromString(self.ishaTime,"hh:mm")
        nextFajrQtime=QtCore.QTime.fromString(self.nextFajrTime,"hh:mm")

        midnightQtime=QtCore.QTime.fromString("24:00:00","hh:mm:ss")

        #to find out the time interval for the next time, we should find the minimum of negative differrences among prayer times and current time
        #QtCore.QTime.secsTo(param1,param2) returns the two time object's difference in second
        differences=[QtCore.QTime.secsTo(currentQtime ,midnightQtime ),
                     QtCore.QTime.secsTo(fajrQtime    ,midnightQtime ),
                     QtCore.QTime.secsTo(sunriseQtime ,midnightQtime ),
                     QtCore.QTime.secsTo(dhuhrQtime   ,midnightQtime ),
                     QtCore.QTime.secsTo(asrQtime     ,midnightQtime ),
                     QtCore.QTime.secsTo(maghribQtime ,midnightQtime ),
                     QtCore.QTime.secsTo(ishaQtime    ,midnightQtime )]


        if differences[1]>differences[0]>differences[6]:#time is bigger than fajr and smaller than Isha time (after fajr before İsha)
            if differences[1]>=differences[0]>differences[2]:
                self.nextTime="Sunrise"
                self.labelNextPrayer.setText(u"Güneşe kalan süre")
            elif differences[2]>=differences[0]>differences[3]:
                self.nextTime="Dhuhr"
                self.labelNextPrayer.setText(u"Öğleye kalan süre")
            elif differences[3]>=differences[0]>differences[4]:
                self.nextTime="Asr"
                self.labelNextPrayer.setText(u"İkindiye kalan süre")
            elif differences[4]>=differences[0]>differences[5]:
                self.nextTime="Maghrib"
                self.labelNextPrayer.setText(u"Akşama kalan süre")
            elif differences[5]>=differences[0]>differences[6]:
                self.nextTime="Isha"
                self.labelNextPrayer.setText(u"Yatsıya kalan süre")
        else:
            # if differences[0]>=0 and differences[0]>=differences[6]: #we are in the range ishatime-midnight (after isha before midnight )
            #     self.nextTime="Fajr"
            #     self.labelNextPrayer.setText(u"İmsağa kalan süre")
            # elif differences[0]<0 and differences[0]<=differences[1]: #we are in the range midnight-Fajrtime (after midnight before fajr)
            #     self.nextTime="Fajr"
            #     self.labelNextPrayer.setText(u"imsağa kalan süre")
            # else:#!!!trivial!!!
            self.nextTime="Fajr"
            self.labelNextPrayer.setText(u"imsağa kalan süre")
        print(self.nextTime)
        for item in differences:
            print self.turnSecondsInto(item)

        #print(currentQtime)
        #self.remainingTime=str(self.turnSecondsInto((-1)*seconds)) #turn remaining seconds to hh:mm:ss
        #printing time into remaining time section
        self.lcdNumberNextPrayerHour.display(self.remainingTime.split(':')[0])
        self.lcdNumberNextPrayerMinute.display(self.remainingTime.split(':')[1])
        self.lcdNumberNextPrayerSecond.display(self.remainingTime.split(':')[2])
    def calculateRemainingTime3(self):
        #type casting time variables from string to qtime
        fajrQtime=QtCore.QTime.fromString(self.fajrTime+":00","hh:mm:ss")
        currentQtime=QtCore.QTime.fromString(self.currentTime,"hh:mm:ss")
        asrQtime=QtCore.QTime.fromString(self.asrTime+":00","hh:mm:ss")
        dhuhrQtime=QtCore.QTime.fromString(self.dhuhrTime+":00","hh:mm:ss")
        sunriseQtime=QtCore.QTime.fromString(self.sunriseTime+":00","hh:mm:ss")
        maghribQtime=QtCore.QTime.fromString(self.maghribTime+":00","hh:mm:ss")
        ishaQtime=QtCore.QTime.fromString(self.ishaTime+":00","hh:mm:ss")
        nextFajrQtime=QtCore.QTime.fromString(self.nextFajrTime+":00","hh:mm:ss")
        midnightQtime=QtCore.QTime.fromString("00:00:00","hh:mm:ss")


        # if   currentQtime==QtCore.QTime.fromString("23:59:59","hh:mm:ss"): #TODO midnight (00:00) must trick updating time ,date and prayer timess
        #     print "gecti"
        #     self.setCurrentTime()
        #     self.setPrayerTimes()


        if fajrQtime<=currentQtime<=ishaQtime:#time is bigger than fajr and smaller than Isha time (after fajr before İsha)
            if fajrQtime<currentQtime<=sunriseQtime:
                self.nextTime="Sunrise"
                seconds=abs(QtCore.QTime.secsTo(sunriseQtime,currentQtime))
                self.labelNextPrayer.setText(u"Güneşe kalan süre")
            elif sunriseQtime<currentQtime<=dhuhrQtime:
                self.nextTime="Dhuhr"
                seconds=abs(QtCore.QTime.secsTo(dhuhrQtime,currentQtime))
                self.labelNextPrayer.setText(u"Öğleye kalan süre")
            elif dhuhrQtime<currentQtime<=asrQtime:
                self.nextTime="Asr"
                seconds=abs(QtCore.QTime.secsTo(asrQtime,currentQtime))
                self.labelNextPrayer.setText(u"İkindiye kalan süre")
            elif asrQtime<currentQtime<=maghribQtime:
                self.nextTime="Maghrib"
                seconds=abs(QtCore.QTime.secsTo(maghribQtime,currentQtime))
                self.labelNextPrayer.setText(u"Akşama kalan süre")
            elif maghribQtime<currentQtime<=ishaQtime:
                self.nextTime="Isha"
                seconds=abs(QtCore.QTime.secsTo(ishaQtime,currentQtime))
                self.labelNextPrayer.setText(u"Yatsıya kalan süre")
        else: #after isha before next fajr

            if  currentQtime>ishaQtime and currentQtime>midnightQtime and currentQtime>fajrQtime : #we are in the range ishatime-midnight (after isha before midnight )
                 self.nextTime="Fajr"
                 seconds=(-1)*(QtCore.QTime.secsTo(fajrQtime,currentQtime))
                 self.labelNextPrayer.setText(u"İmsağa kalan süre")
            elif currentQtime>=midnightQtime and currentQtime<=fajrQtime and currentQtime<=ishaQtime: #we are in the range midnight-Fajrtime (after midnight before fajr)
                 self.nextTime="Fajr"
                 seconds=abs(QtCore.QTime.secsTo(fajrQtime,currentQtime))
                 self.labelNextPrayer.setText(u"İmsağa kalan süre")

        self.remainingTime=self.turnSecondsInto(seconds)

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
    app.setApplicationName("pynamaz") #necessary for phonon module.
    program = PyNamaz()
    program.show()
    sys.exit(app.exec_())
