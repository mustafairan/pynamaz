# -*- coding: utf-8 -*-
# /usr/bin/env python

import functools  # to make cxfreeze work on windows

application_title = "pyNamaz"  # for cxfreeze
main_python_file = "pyNamaz.py"  # for cxfreeze

import sys
from os import system,chdir

from preferences import *
from prayerTimes import prayerTimes

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
    currentTime = "88:88:88"
    fajrTime = "88:88"
    asrTime = "88:88"
    dhuhrTime = "88:88"
    sunriseTime = "88:88"
    maghribTime = "88:88"
    ishaTime = "88:88"
    nextFajrTime = "88:88"
    nextTime = ""  # indicates next prayer time. it can be Asr,Dhuhr,Maghrib,Isha or Fajr
    currentDate = ""
    remainingTime = "00:00:00"  # indicates remaining time for the next prayer time
    appRootDirectory = ""  # indicates where the main (pyNamaz.py) class in (app directory)
    warningTime = "00:30:00"  # indicates the warning time before next time becomes
    hasShown = False  # keeps track of if warning showed or not. changes to true when prayertime changes
    lastWarningWasFor = ""  # indicates what was the last warning for
    preferencesDict = {}  # keeps current preferences as a dictionary
    homedir = expanduser('~')  # coz  python doesnt understand tilda. this is the prefix location for main folder. default tilda is for linux.
    platform = ""  # linux windows  mac or unknown
    preferencesObj = preferences()

    def __init__(self):
        self.findOutPlatform()
        self.setHomedir()
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
        QtGui.QMainWindow.setWindowTitle(self, "pyNamaz")

        self.preferencesDict = self.preferencesObj.getPreferences()  # Getting preferences to the dictionary

        self.trayIcon = QtGui.QSystemTrayIcon(self)

        self.printUseWarning()  # prints initial warning
        # self.setRootDirectory() #sets approotdirectory variable to able to know where we in
        self.centerMainWindow()  # to be sure the main window centered on screen



        self.testt()



        # Continually updating time and remaining time
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.setCurrentTime)
        timer.timeout.connect(self.calculateRemainingTime3)
        timer.start(1000)

        self.setPrayerTimes2()   # Parsing times file PrayerTimes.txt and setting time variables
        self.printPrayerTimes()  # printing prayer times to the gui
        self.printPreferences()  # prints preferences to the gui. Also necessary for controls

        # Menu Section
        # Appereance Preferances
        self.actionCleanlooks.triggered.connect(lambda: self.setAppearance('Cleanlooks'))
        self.actionPlastique.triggered.connect(lambda: self.setAppearance('Plastique'))
        self.actionPlastique.triggered.connect(lambda: self.setAppearance('Gtk'))
        self.actionBespin.triggered.connect(lambda: self.setAppearance('Bespin'))
        self.actionCDE.triggered.connect(lambda: self.setAppearance('CDE'))
        self.actionMotif.triggered.connect(lambda: self.setAppearance('Motif'))
        self.actionOxygen.triggered.connect(lambda: self.setAppearance('Oxygen'))
        self.actionQtcurve.triggered.connect(lambda: self.setAppearance('Qtcurve'))
        self.actionWindows.triggered.connect(lambda: self.setAppearance('Windows'))
        self.actionNas_l_kullan_l_r.triggered.connect(lambda: self.printUseWarning(isAgain="yes"))
        self.action_k.triggered.connect(lambda: exit(0))

        # to be able to open prayertimes.txt and edit it
        self.pushButtonOpenPrayerTimesText.clicked.connect(self.openPrayerTimesText)
        #TODO self.pushButtonSetTimesManuelly.clicked.connect(self.openPrayerTimesText)

        # Link Buttons Section
        self.pushButton_2.clicked.connect(lambda: self.openLink('http://mustafairan.wordpress.com'))
        self.pushButton_3.clicked.connect(lambda: self.openLink('http://github.com/mustafairan/pynamaz'))
        self.pushButton.clicked.connect(lambda: self.openLink('http://diyanet.gov.tr'))
        self.pushButton_4.clicked.connect(lambda: self.openLink(
            'http://www.diyanet.gov.tr/tr/PrayerTime/WorldPrayerTimes'))  # Times data can be copy from here

        # preferences Tab
        self.pushButtonPreferencesReset.clicked.connect(lambda: self.printPreferences())
        self.pushButtonPreferencesReturnToDefaults.clicked.connect(
            lambda: self.preferencesObj.retunToDefaults(option="prefs"))
        self.pushButtonPreferencesReturnToDefaults.clicked.connect(lambda: self.printPreferences())
        self.pushButtonPreferencesReturnToDefaults.clicked.connect(self.turnToFalse)
        # self.pushButtonPreferencesReturnToDefaults.clicked.connect(self.restartWarning)
        self.pushButtonPreferencesSave.clicked.connect(self.saveNewPreferencesForPreferenceTab)

        # Warnins tab
        self.pushButtonWarningsReset.clicked.connect(lambda: self.printPreferences())
        self.pushButtonWarningsReturnToDefaults.clicked.connect(
            lambda: self.preferencesObj.retunToDefaults(option="warns"))
        self.pushButtonWarningsReturnToDefaults.clicked.connect(lambda: self.printPreferences())
        self.pushButtonWarningsReturnToDefaults.clicked.connect(self.turnToFalse)
        # self.pushButtonWarningsReturnToDefaults.clicked.connect(self.restartWarning)
        self.pushButtonWarningsSave.clicked.connect(self.saveNewPreferencesForWarnings)


        # signal slot mechanism
        # QtCore.QObject.connect(self.testbutton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.menubar.show)
        # QtCore.QObject.connect(self.testbutton, QtCore.SIGNAL( QtCore.QString.fromUtf8("clicked()")),self.menuMen.show)
        # self.connect(self.trayIcon,QtCore.SIGNAL( QtGui.QSystemTrayIcon.activated(2)),self.menuMen.show)

    def setHomedir(self):
        if self.platform == "linux":
            self.homedir = expanduser('~')
        elif self.platform == "windows":
            self.homedir = "%userprofile%\documents"
        elif self.platform == "mac":
            self.homedir = expanduser('~')
        else:
            pass

    def testt(self):

        # print "I came"
        # output = Phonon.AudioOutput(Phonon.MusicCategory)
        # m_media = Phonon.MediaObject()
        #
        # Phonon.createPath(m_media, output)
        #
        # m_media.stop()
        # m_media.setCurrentSource(Phonon.MediaSource("/home/mnc/.pyNamaz/data/sound.mp3"))
        # m_media.play()
        # video_widget = Phonon.VideoWidget()
        # video_widget.show()
        pass





    def findOutPlatform(self):

        # linux (2.x and 3.x) 	'linux2'
        # Windows 	'win32'
        # Windows/Cygwin 	'cygwin'
        # Mac OS X 	'darwin'
        # OS/2 	'os2'
        # OS/2 EMX 	'os2emx'
        # RiscOS 	'riscos'
        # AtheOS 	'atheos'


        if sys.platform.startswith("linux"):
            self.platform = "linux"
        elif sys.platform.startswith("win32"):
            self.platform = "windows"
        elif sys.platform.startswith("cygwin"):
            self.platform = "windows"
        elif sys.platform.startswith("darwin"):
            self.platform = "mac"
        elif sys.platform.startswith("os2"):
            self.platform = "mac"
        elif sys.platform.startswith("os2emx"):
            self.platform = "mac"
        else:
            self.platform = "unknown"

    def saveNewPreferencesForPreferenceTab(self):
        """
        save new preferences which from prefereces tab to config file. Reprints new pref. to gui
        """
        self.preferencesDict["playadhan"] = str(self.checkBoxPlayAdhan.isChecked())
        self.preferencesDict["playwarnsound"] = str(self.checkBoxPlayWarnSound.isChecked())
        self.preferencesDict["showintray"] = str(self.checkBoxShowInTray.isChecked())
        self.preferencesDict["showsystemnotifications"] = str(self.checkBoxSystemNotifications.isChecked())
        self.preferencesDict["muteinadhantime"] = str(self.checkBoxMuteInAdhanTime.isChecked())
        self.preferencesObj.savePreferences(self.preferencesDict)
        self.preferencesDict = self.preferencesObj.getPreferences()
        self.printPreferences()
        self.hasShown=False

    def turnToFalse(self):
        self.hasShown=False

    def saveNewPreferencesForWarnings(self):
        """
        Handles save button for preferences tab. make prefs save and reloads prefdictionary

        """
        self.preferencesDict["sunrisewarn"] = str(self.checkBoxSunriseWarn.isChecked())
        self.preferencesDict["asrwarn"] = str(self.checkBoxAsrWarn.isChecked())
        self.preferencesDict["dhuhrwarn"] = str(self.checkBoxDhuhrWarn.isChecked())
        self.preferencesDict["fajrwarn"] = str(self.checkBoxFajrWarn.isChecked())
        self.preferencesDict["ishawarn"] = str(self.checkBoxIshaWarn.isChecked())
        self.preferencesDict["maghribwarn"] = str(self.checkBoxMaghribWarn.isChecked())
        self.preferencesDict["beforefajr"] = str(self.spinBoxFacrWarn.value())
        self.preferencesDict["beforesunrise"] = str(self.spinBoxSunriseWarn.value())
        self.preferencesDict["beforedhduhr"] = str(self.spinBoxDhuhrWarn.value())
        self.preferencesDict["beforeasr"] = str(self.spinBoxAsrWarn.value())
        self.preferencesDict["beforemaghrib"] = str(self.spinBoxMaghribWarn.value())
        self.preferencesDict["beforeisha"] = str(self.spinBoxIshaWarn.value())
        self.preferencesObj.savePreferences(self.preferencesDict)
        self.preferencesDict = self.preferencesObj.getPreferences()
        self.printPreferences()
        self.hasShown=False #


    def printPreferences(self):
        """
        prints preferences to the gui. Also necessary for controls
        """

        self.preferencesDict = self.preferencesObj.getPreferences()
        self.checkBoxSunriseWarn.setChecked('True' == self.preferencesDict["sunrisewarn"])
        self.checkBoxAsrWarn.setChecked('True' == self.preferencesDict["asrwarn"])
        self.checkBoxDhuhrWarn.setChecked('True' == self.preferencesDict["dhuhrwarn"])
        self.checkBoxFajrWarn.setChecked('True' == self.preferencesDict["fajrwarn"])
        self.checkBoxIshaWarn.setChecked('True' == self.preferencesDict["ishawarn"])
        self.checkBoxMaghribWarn.setChecked('True' == self.preferencesDict["maghribwarn"])

        #TODO self.checkBoxPlayAdhan.setChecked('True' == self.preferencesDict["playadhan"])
        #TODO self.checkBoxMuteInAdhanTime.setChecked('True' == self.preferencesDict["muteinadhantime"])
        #TODO self.checkBoxPlayWarnSound.setChecked('True' == self.preferencesDict["playwarnsound"])
        #TODO self.checkBoxShowInTray.setChecked('True' == self.preferencesDict["showintray"])
        self.checkBoxSystemNotifications.setChecked('True' == self.preferencesDict["showsystemnotifications"])

        self.spinBoxFacrWarn.setValue(int(self.preferencesDict["beforefajr"]))
        self.spinBoxSunriseWarn.setValue(int(self.preferencesDict["beforesunrise"]))
        self.spinBoxDhuhrWarn.setValue(int(self.preferencesDict["beforedhduhr"]))
        self.spinBoxAsrWarn.setValue(int(self.preferencesDict["beforeasr"]))
        self.spinBoxMaghribWarn.setValue(int(self.preferencesDict["beforemaghrib"]))
        self.spinBoxIshaWarn.setValue(int(self.preferencesDict["beforeisha"]))

    def restartWarning(self):
        """
        warns user to restart application !!no use anymore!!
        """

        QtGui.QMessageBox.information(None, u"Uyarı!",
                                      u"Yeni ayarları arayüzde görmek için uygulamayı yeniden başlatmalısınız\n",
                                      u"Tamam")

    def restartApplication(self):
        """
        tries to restart application. !! doesnt Work!!!
        """
        QtCore.QProcess.startDetached(QtGui.QApplication.applicationFilePath())
        exit(12)

    def taskbarToggle(self):
        """
        hides or shows main window
        """
        if self.isVisible():
            self.setVisible(False)
        else:
            self.setVisible(True)

    def showTrayIcon(self):
        """
        shows a tray icon
        """
        # self.trayIcon.setIcon(QtGui.QIcon(self.appRootDirectory+"/data/mosque.png"))#TODO path should be specified correctly
        ####################
        # te=QtGui.QTextEdit(str(int(self.remainingTime.split(":")[0])*60+int(self.remainingTime.split(":")[1])))
        # te.resize(40, 40)
        # te.autoFillBackground()
        # pix=QtGui.QPixmap.grabWidget (te, 0,0,-1,-1)
        # pix.save("test.png")


        te = QtGui.QLCDNumber(3)
        te.display((int(self.remainingTime.split(":")[0]) * 60 + int(self.remainingTime.split(":")[1])))
        te.setSegmentStyle(QtGui.QLCDNumber.Flat)

        te.resize(40, 40)

        pix = QtGui.QPixmap.grabWidget(te, 0, 0, -3, -10)
        # pix.save("test.png")

        self.trayIcon.setIcon(QtGui.QIcon(pix))  # TODO path should be specified correctly

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
        Sets root directory of application.  !!!no use anymore !!!
        """
        chdir("../")  # for this usage pynamaz.py should be one level deep from root directory.
        self.appRootDirectory = os.getcwd()

    def printUseWarning(self, isAgain=None):

        """
        prints how the application works
        if gets called with something, shows warning for 1 time
        """
        showedIt = self.preferencesDict["howtouseshowed"]
        if not isAgain == None:
            showedIt = "False"

        if str(showedIt) == "False":
            QtGui.QMessageBox.information(None, u"Nasıl kullanılır?",
                                          u"Uygulama sistem saatinizi kullanmaktadır. Saatinizin doğru olduğundan emin olun.\n"
                                          u"Uygulamanın çalışması için gerekli vakit bilgisini PrayerTimes.txt dosyasına kaydetmelisiniz. Eğer daha önce kaydettiyseniz bu uyarıyı dikkate almayınız\n"

                                          u"\nGerekli aylık vakit bilgilerine ulaşmak için linkler bölümündeki vakit bağlantısı butonunu kullanın ve gelen tablodaki bilgileri farenizle seçip kopyalayın\n"
                                          u"Dosyayı açmak için Namaz vakitleri dosyasını aç butonunu kullanınız\nişlemi tamamladıktan sonra programı kapatıp tekrar açın\n",
                                          u"Anladım")
            self.preferencesDict["howtouseshowed"] = "True"
            self.preferencesObj.savePreferences(self.preferencesDict)
        else:
            pass

    def openPrayerTimesText(self):
        """
        opens PrayerTimes.txt file with a text editor
        """
        if self.platform == "linux":
            system('xdg-open "' + self.homedir + '/.pyNamaz/data/PrayerTimes.txt"')
        elif self.platform == "windows":
            system(
                'start notepad "' + self.homedir + r'\PrayerTimes.txt"')  # TODO this usage can cause problem. file paths should be specified in more efficient way. should be tested in windows systems
        else:
            pass

    def setCurrentTime(self):
        """sets and continually updates then prints current time"""
        # TODO Should warn the user to set his system clock properly
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
        # firstly, Current date and time must be set
        try:
            self.currentTime = QtCore.QTime().currentTime().toString("hh:mm:ss")
            self.currentDate = QtCore.QDate().currentDate().toString("dd.MM.yy")
            # print self.currentDate + " "+ self.currentTime
            # pass
        except:
            print "current time and date can't be obtained from operating system"  # should be gui warning

        currentDate = QtCore.QDate.fromString(self.currentDate, "dd.MM.yy")
        nextDate = currentDate.addDays(1)
        nextDate = nextDate.toString("dd.MM.yy")
        # Finding Current date's prayer times from the file and assigning

        if sys.platform.startswith("linux"):
            timesFileObject = open(self.homedir + "/.pyNamaz/data/PrayerTimes.txt", 'r')
        else:
            try:
                timesFileObject = open(os.path.expanduser("~/documents/PrayerTimes.txt"), 'r')
            except:
                timesFileObject = open(os.path.expanduser("~/documents/PrayerTimes.txt"), 'a+')

        # TODO prayertimes.txt path should be specified with more efficient way

        for line in timesFileObject:

            # print str(nextDate)[0:6]+"20"+str(nextDate)[6:]
            if line.split('\t')[0].strip(' ') == str(self.currentDate)[0:6] + "20" + str(self.currentDate)[6:]:
                timeArray = line.split('\t')
                self.fajrTime = timeArray[1].strip(' ')
                self.sunriseTime = timeArray[2].strip(' ')
                self.dhuhrTime = timeArray[3].strip(' ')
                self.asrTime = timeArray[4].strip(' ')
                self.maghribTime = timeArray[5].strip(' ')
                self.ishaTime = timeArray[6].strip(' ')
            elif line.split('\t')[0].strip(' ') == str(nextDate)[0:6] + "20" + str(nextDate)[
                                                                               6:]:  # TODO I didnt test this
                self.nextFajrTime = line.split('\t')[1].strip(' ')
                break

    def printPrayerTimes(self):
        """prints current date and prayer times to the gui"""
        self.labelCurrentDate.setText("<h1>" + self.currentDate + "</h>")
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

    def setAppearance(self, appereance_choice):
        """
        sets appereance (eg: qtcurve , bespin)
        """
        if appereance_choice == None:
            appereance_choice = "Cleanlooks"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(appereance_choice))

    def openLink(self, url=''):
        """
        opens a given url
        """
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))

    def calculateRemainingTime3(self):
        """
        Calculates remaining time and prints to gui , decides next time (eg: asr, fajr )
        """

        # type casting time variables from string to qtime
        fajrQtime = self.convertToQtime(self.fajrTime + ":00")
        currentQtime = self.convertToQtime(self.currentTime)
        asrQtime = self.convertToQtime(self.asrTime + ":00")
        dhuhrQtime = self.convertToQtime(self.dhuhrTime + ":00")
        sunriseQtime = self.convertToQtime(self.sunriseTime + ":00")
        maghribQtime = self.convertToQtime(self.maghribTime + ":00")
        ishaQtime = self.convertToQtime(self.ishaTime + ":00")
        nextFajrQtime = self.convertToQtime(self.nextFajrTime + ":00")
        midnightQtime = self.convertToQtime("00:00:00")

        # if   currentQtime==QtCore.QTime.fromString("23:59:59","hh:mm:ss"): #TODO midnight (00:00) must trick updating time ,date and prayer timess
        #     print "gecti"
        #     self.setCurrentTime()
        #     self.setPrayerTimes()


        if fajrQtime <= currentQtime <= ishaQtime:  # time is bigger than fajr and smaller than Isha time (after fajr before İsha)
            if fajrQtime < currentQtime <= sunriseQtime:
                self.nextTime = "Sunrise"
                seconds = abs(QtCore.QTime.secsTo(sunriseQtime, currentQtime))
                self.labelNextPrayer.setText(u"Güneşe kalan süre")
            elif sunriseQtime < currentQtime <= dhuhrQtime:
                self.nextTime = "Dhuhr"
                seconds = abs(QtCore.QTime.secsTo(dhuhrQtime, currentQtime))
                self.labelNextPrayer.setText(u"Öğleye kalan süre")
            elif dhuhrQtime < currentQtime <= asrQtime:
                self.nextTime = "Asr"
                seconds = abs(QtCore.QTime.secsTo(asrQtime, currentQtime))
                self.labelNextPrayer.setText(u"İkindiye kalan süre")
            elif asrQtime < currentQtime <= maghribQtime:
                self.nextTime = "Maghrib"
                seconds = abs(QtCore.QTime.secsTo(maghribQtime, currentQtime))
                self.labelNextPrayer.setText(u"Akşama kalan süre")
            elif maghribQtime < currentQtime <= ishaQtime:
                self.nextTime = "Isha"
                seconds = abs(QtCore.QTime.secsTo(ishaQtime, currentQtime))
                self.labelNextPrayer.setText(u"Yatsıya kalan süre")
        else:  # after isha before next fajr

            if currentQtime > ishaQtime and currentQtime > midnightQtime and currentQtime > fajrQtime:  # we are in the range ishatime-midnight (after isha before midnight )
                self.nextTime = "Fajr"
                seconds = (-1) * (QtCore.QTime.secsTo(fajrQtime, currentQtime))
                self.labelNextPrayer.setText(u"İmsağa kalan süre")
            elif currentQtime >= midnightQtime and currentQtime <= fajrQtime and currentQtime <= ishaQtime:  # we are in the range midnight-Fajrtime (after midnight before fajr)
                self.nextTime = "Fajr"
                seconds = abs(QtCore.QTime.secsTo(fajrQtime, currentQtime))
                self.labelNextPrayer.setText(u"İmsağa kalan süre")

        self.remainingTime = self.turnSecondsInto(seconds)

        # printing time into remaining time section
        self.lcdNumberNextPrayerHour.display(self.remainingTime.split(':')[0])
        self.lcdNumberNextPrayerMinute.display(self.remainingTime.split(':')[1])
        self.lcdNumberNextPrayerSecond.display(self.remainingTime.split(':')[2])
        # self.remainingTimeWarning(self.nextTime)
        self.remainingTimeWarning2(self.nextTime)
        self.showTrayIcon()  # shows a tray icon

    def remainingTimeWarning(self, forTime):
        """
        Decides if warning is necessary or not
        :param forTime: for which time we trying to warn (Asr, Fajr etc)
        """
        warningQTime = self.convertToQtime(self.warningTime)
        remainingQtime = self.convertToQtime(self.remainingTime)

        if remainingQtime <= warningQTime and self.lastWarningWasFor != forTime:
            self.printWarn()
            self.hasShown = True
            self.lastWarningWasFor = forTime

    def remainingTimeWarning2(self, forTime):
        """
        Decides if warning is necessary or not
        :param forTime: for which time we trying to warn (Asr, Fajr etc)
        """
        remainingQtime = self.convertToQtime(self.remainingTime)

        beforefajrQtime = self.convertToQtime(self.turnSecondsInto(int(self.preferencesDict["beforefajr"]) * 60))
        beforesunriseQtime = self.convertToQtime(self.turnSecondsInto(int(self.preferencesDict["beforesunrise"]) * 60))
        beforedhduhrQtime = self.convertToQtime(self.turnSecondsInto(int(self.preferencesDict["beforedhduhr"]) * 60))
        beforeasrQtime = self.convertToQtime(self.turnSecondsInto(int(self.preferencesDict["beforeasr"]) * 60))
        beforemaghribQtime = self.convertToQtime(self.turnSecondsInto(int(self.preferencesDict["beforemaghrib"]) * 60))
        beforeishaQtime = self.convertToQtime(self.turnSecondsInto(int(self.preferencesDict["beforeisha"]) * 60))

        if self.lastWarningWasFor != forTime and self.preferencesDict["showintray"] == "True":

            if self.nextTime == "Asr" and remainingQtime <= beforeasrQtime:
                self.printWarn()
                self.hasShown = True
                self.lastWarningWasFor = forTime
            elif self.nextTime == "Dhuhr" and remainingQtime <= beforedhduhrQtime:
                self.printWarn()
                self.hasShown = True
                self.lastWarningWasFor = forTime
            elif self.nextTime == "Maghrib" and remainingQtime <= beforemaghribQtime:
                self.printWarn()
                self.hasShown = True
                self.lastWarningWasFor = forTime
            elif self.nextTime == "Isha" and remainingQtime <= beforeishaQtime:
                self.printWarn()
                self.hasShown = True
                self.lastWarningWasFor = forTime
            elif self.nextTime == "Fajr" and remainingQtime <= beforefajrQtime:
                self.printWarn()
                self.hasShown = True
                self.lastWarningWasFor = forTime
            elif self.nextTime == "Sunrise" and remainingQtime <= beforesunriseQtime:
                self.printWarn()
                self.hasShown = True
                self.lastWarningWasFor = forTime
        else:
            pass

    def printWarn(self):
        """
        prints remaining time warning as notification
        """
        # QtGui.QMessageBox.information(None, u"Vakit uyarısı",
        #                               u"sıradaki vakit: "+self.nextTime+u" Son "+self.remainingTime,u"Tamam")

        dict = {'Fajr': u'İmsak', 'Sunrise': u'Güneş', 'Dhuhr': u'Öğle', 'Asr': u'İkindi', 'Isha': u'Yatsı',
                'Maghrib': u'Akşam'}  # Turkish meanings of prayer times
        self.trayIcon.showMessage(u"Bilgi", u"Sonraki vakit : " + dict[
            self.nextTime] + u"\n" + u"Kalan süre: " + self.remainingTime,
                                  self.trayIcon.Information, 6000)

    def turnSecondsInto(self, seconds):
        """turns seconds into hour minute and second . returns as string hh:mm:ss"""
        days, seconds = divmod(seconds, 24 * 60 * 60)
        hours, seconds = divmod(seconds, 60 * 60)
        minutes, seconds = divmod(seconds, 60)

        # return format must be hh:mm:ss
        # for example 0:11:59 cause problem. so it must be 00:11:59
        if hours < 10:
            hours = str(hours)
            hours = "0" + hours
        else:
            hours = str(hours)
        if seconds < 10:
            seconds = str(seconds)
            seconds = "0" + seconds
        else:
            seconds = str(seconds)
        if minutes < 10:
            minutes = str(minutes)
            minutes = "0" + minutes
        else:
            minutes = str(minutes)
        return hours + ":" + minutes + ":" + seconds

    def convertToQtime(self, timeString):
        """
        converts a given string to Qtime
        :param timeString: hh:mm:ss
        :return: timeQ  Qtime
        """
        timeQ = QtCore.QTime.fromString(timeString, "hh:mm:ss")
        return timeQ

    def centerMainWindow(self):
        self.move((QtGui.QDesktopWidget().screenGeometry().width() - self.geometry().width()) / 2, \
                  (QtGui.QDesktopWidget().screenGeometry().height() - self.geometry().height()) / 2)

    def printer(self):
        print "I got called"


if __name__ == "__main__":
    app.setApplicationName("pynamaz")  # necessary for phonon module.
    program = PyNamaz()
    program.show()
    sys.exit(app.exec_())
