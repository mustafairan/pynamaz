# -*- coding: utf-8 -*-

import os #just for os.system and os.chdir
import sys
import preferences
import prayerTimes

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

from app.ui_pynamaz import Ui_MainWindow

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
    appRootDirectory=""#indicates where the main (pyNamaz.py) class in (app directory)
    warningTime="00:30:00" #indicates the warning time before next time becomes
    isShown=False #keep if warning showed or not. changes to true when prayertime changes
    lastWarningWasFor=""# indicates what was the last warning for

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
        QtGui.QMainWindow.setWindowTitle(self,"pyNamaz")



        #prayerTimesObj=prayerTimes()
        #TODO self.pushButtonSetTimesManuelly.clicked.connect(lambda: prayerTimes.getTimesManuelly(prayerTimesObj))

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.printUseWarning() #prints initial warning
        self.setRootDirectory() #sets approotdirectory variable to able to know where we in
        self.centerMainWindow() #to be sure the main window cented on screen

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

        #to be able to open prayertimes.txt and edit it
        self.pushButtonOpenPrayerTimesText.clicked.connect(self.openPrayerTimesText)

        #Link Buttons Section
        self.pushButton_2.clicked.connect(lambda: self.openLink('http://mustafairan.wordpress.com'))
        self.pushButton_3.clicked.connect(lambda: self.openLink('http://github.com/mustafairan/pynamaz'))
        self.pushButton.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))
        self.pushButton_4.clicked.connect(lambda: self.openLink('http://www.diyanet.gov.tr/tr/PrayerTime/WorldPrayerTimes'))#Times data can be copy from here




    def showTrayIcon(self):
        """
        shows a tray icon
        """
        #self.trayIcon.setIcon(QtGui.QIcon(self.appRootDirectory+"/data/mosque.png"))#TODO path should be specified correctly
        ####################
        # te=QtGui.QTextEdit(str(int(self.remainingTime.split(":")[0])*60+int(self.remainingTime.split(":")[1])))
        # te.resize(40, 40)
        # te.autoFillBackground()
        # pix=QtGui.QPixmap.grabWidget (te, 0,0,-1,-1)
        #pix.save("test.png")


        te=QtGui.QLCDNumber(3)
        te.display((int(self.remainingTime.split(":")[0])*60+int(self.remainingTime.split(":")[1])))
        te.setSegmentStyle(QtGui.QLCDNumber.Flat)

        te.resize(40,40)

        pix=QtGui.QPixmap.grabWidget (te, 0,0,-3,-10)
        #pix.save("test.png")

        self.trayIcon.setIcon(QtGui.QIcon(pix))#TODO path should be specified correctly




        ######################

        #############################

        # image=QtGui.QImage( 50, 50, QtGui.QImage.Format_RGB16)
        # painter=QtGui.QPainter(image)
        # painter.fillRect(image.rect(),QtCore.Qt.yellow)
        # text=QtCore.QString
        #
        # painter.drawText(image.rect(),QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter, "234")
        #
        # print id(image)
        # image.save("sqqsqsq.png")
        # self.trayIcon.setIcon(QtGui.QIcon("sqqsqsq.png"))#TODO path should be specified correctly
        # painter.end()
        ######################

        if self.trayIcon.isVisible():
            pass
        else:
            self.trayIcon.show()
    def setRootDirectory(self):
        """
        Sets root directory of application.
        """
        os.chdir("../")#for this usage pynamaz.py should be one level deep from root directory.
        self.appRootDirectory=os.getcwd()
    def printUseWarning(self):
        """
        prints how the application works
        """
        QtGui.QMessageBox.information(None, u"Nasıl kullanılır?",
                                      u"Uygulama sistem saatinizi kullanmaktadır. Saatinizin doğru olduğundan emin olun.\n"
                                      u"Uygulamanın çalışması için gerekli vakit bilgisini PrayerTimes.txt dosyasına kaydetmelisiniz.\n"

                                      u"\nGerekli aylık vakit bilgilerine ulaşmak için linkler bölümündeki vakit bağlantısı butonunu kullanın ve gelen tablodaki bilgileri farenizle seçip kopyalayın\n"
                                      u"Dosyayı açmak için Namaz vakitleri dosyasını aç butonunu kullanınız",u"Anladım")
    def openPrayerTimesText(self):
        """
        opens PrayerTimes.txt file with a text editor
        """
        if sys.platform.startswith("linux"):
            os.system('xdg-open "'+self.appRootDirectory+'/data/PrayerTimes.txt"')
        else:
            os.system('start "'+self.appRootDirectory+'/data/PrayerTimes.txt"') #TODO this usage can cause problem. file paths should be specified in more efficient way. should be tested in windows systems
    def setCurrentTime(self):
        """sets and continually updates then prints current time"""
        #TODO Should warn the user to set his system clock properly
        self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
        self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
        self.lcdNumberCurrentHour.display(self.currentTime.split(':')[0])
        self.lcdNumberCurrentMinute.display(self.currentTime.split(':')[1])
        self.lcdNumberCurrentSecond.display(self.currentTime.split(':')[2])
    def setPrayerTimes2(self):
        """Parses times file PrayerTimes.txt and sets time variables

        PrayerTimes.txt format:
            #07.01.2016 \t05:33 \t07:03 \t12:03 \t14:27 \t16:50 \t18:13 \t10:32\n
        """
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
        timesFileObject = open(self.appRootDirectory+r"/data/PrayerTimes.txt", 'r')
        for line in timesFileObject:

            #print str(nextDate)[0:6]+"20"+str(nextDate)[6:]
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
    def printPrayerTimes(self):
        """prints current date and prayer times to the gui"""
        self.labelCurrentDate.setText("<h1>"+self.currentDate+"</h>")
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
        """
        sets appereance (eg: qtcurve , bespin)
        """
        if appereance_choice == None:
            appereance_choice = "Cleanlooks"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(appereance_choice))
    def openLink(self,url=''):
        """
        opens a given url
        """
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))
    def calculateRemainingTime3(self):
        """
        Calculates remaining time and prints to gui , decides next time (eg: asr, fajr )
        """
        #type casting time variables from string to qtime
        fajrQtime=self.convertToQtime(self.fajrTime+":00")
        currentQtime=self.convertToQtime(self.currentTime)
        asrQtime=self.convertToQtime(self.asrTime+":00")
        dhuhrQtime=self.convertToQtime(self.dhuhrTime+":00")
        sunriseQtime=self.convertToQtime(self.sunriseTime+":00")
        maghribQtime=self.convertToQtime(self.maghribTime+":00")
        ishaQtime=self.convertToQtime(self.ishaTime+":00")
        nextFajrQtime=self.convertToQtime(self.nextFajrTime+":00")
        midnightQtime=self.convertToQtime("00:00:00")


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
        self.remainingTimeWarning(self.nextTime)
        self.showTrayIcon() #shows a tray icon


    def remainingTimeWarning(self,forTime):
        """
        Decides if warning is necessary or not
        :param forTime: for which time we trying to warn (Asr, Fajr etc)


        """
        warningQTime = self.convertToQtime(self.warningTime)
        remainingQtime=self.convertToQtime(self.remainingTime)

        if remainingQtime<=warningQTime and self.lastWarningWasFor!=forTime:
            self.printWarn()
            self.isShown=True
            self.lastWarningWasFor=forTime
    def printWarn(self):
        """
        prints remaining time warning as notification
        """
        # QtGui.QMessageBox.information(None, u"Vakit uyarısı",
        #                               u"sıradaki vakit: "+self.nextTime+u" Son "+self.remainingTime,u"Tamam")

        dict = {'Fajr': u'İmsak','Sunrise': u'Güneş','Dhuhr': u'Öğle', 'Asr': u'İkindi', 'Isha': u'Yatsı','Maghrib': u'Akşam'}#Turkish meanings of prayer times
        self.trayIcon.showMessage(u"Bilgi",u"Sonraki vakit : "+dict[self.nextTime]+u"\n"+u"Kalan süre: "+self.remainingTime,
                                  self.trayIcon.Information,6000)



    def turnSecondsInto(self,seconds):
        """turns seconds into hour minute and second . returns as string hh:mm:ss"""
        days, seconds = divmod(seconds, 24*60*60)
        hours, seconds = divmod(seconds, 60*60)
        minutes, seconds = divmod(seconds, 60)

        #return format must be hh:mm:ss
        #for example 0:11:59 cause problem. so it must be 00:11:59
        if hours<10:
            hours=str(hours)
            hours="0"+hours
        else:
            hours=str(hours)
        if seconds<10:
            seconds=str(seconds)
            seconds="0"+seconds
        else:
            seconds=str(seconds)
        if minutes<10:
            minutes=str(minutes)
            minutes="0"+minutes
        else:
            minutes=str(minutes)
        return hours+":"+minutes+":"+seconds
    def convertToQtime(self,timeString):
        """
        converts a given string to Qtime
        :param timeString: hh:mm:ss
        :return: timeQ  Qtime
        """
        timeQ=QtCore.QTime.fromString(timeString,"hh:mm:ss")
        return timeQ
    def centerMainWindow(self):
        self.move((QtGui.QDesktopWidget().screenGeometry().width() - self.geometry().width()) / 2, \
                  (QtGui.QDesktopWidget().screenGeometry().height() - self.geometry().height()) / 2)


if __name__ == "__main__":
    app.setApplicationName("pynamaz") #necessary for phonon module.
    program = PyNamaz()
    program.show()
    sys.exit(app.exec_())
