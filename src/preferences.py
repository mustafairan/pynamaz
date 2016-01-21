# -*- coding: utf-8 -*-
#/usr/bin/env python
from os.path import  isfile,expanduser
from os import getcwd,chdir
from sys import platform

from ConfigParser import SafeConfigParser
class preferences:
    prefDict={}
    homedir=expanduser('~') #coz  python doesnt understand tilda. this is the prefix location for main folder. default tilda is for linux.

    def __init__(self):
        """
        looks for /home/mnc/pynamaz-development--------------------------/app/config.ini
            if not exist, creates and with default values
            if exist pass
        puts current main settings to prefDict dictionary of class

        """
        self.findOutPlatform()
        self.setHomedir()

        if self.platform=="linux":
            if not isfile(self.homedir+'/.pyNamaz/config/config.ini'):
                f=open(self.homedir+'/.pyNamaz/config/config.ini',"w")

                f.close()
                self.reprintDefaults()
                self.retunToDefaults()

            else:
                config = SafeConfigParser()
                config.read(self.homedir+'/.pyNamaz/config/config.ini')
                if not config.has_section("MAIN"):
                    config.add_section("MAIN")
                    self.retunToDefaults()
                else:
                    pass
        elif self.platform=="windows":
            if not isfile(self.homedir+'\config\config.ini'):
                f=open(self.homedir+'\config\config.ini',"w")

                f.close()
                self.reprintDefaults()
                self.retunToDefaults()

        else:
            config = SafeConfigParser()
            config.read(self.homedir+'\config\config.ini')
            if not config.has_section("MAIN"):
                config.add_section("MAIN")
                self.retunToDefaults()
            else:
                pass


        self.prefDict=self.getPreferences()



    def setHomedir(self):
        if self.platform=="linux":
            self.homedir=expanduser('~')
        elif self.platform=="windows":
            chdir("..\\")
            self.homedir=getcwd() #TODO should check it
        elif self.platform=="mac":
            self.homedir=expanduser('~')
        else:
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


        if platform.startswith("linux"):
            self.platform="linux"
        elif platform.startswith("win32"):
            self.platform="windows"
        elif platform.startswith("cygwin"):
            self.platform="windows"
        elif platform.startswith("darwin"):
            self.platform="mac"
        elif platform.startswith("os2"):
            self.platform="mac"
        elif platform.startswith("os2emx"):
            self.platform="mac"
        else:
            self.platform="unknown"



    def getValue(self, key):
        """takes a preference key and returns its value"""
        config = SafeConfigParser()
        if self.platform=="linux":
            config.read(self.homedir+'/.pyNamaz/config/config.ini')
        elif self.platform=="windows":
            config.read(self.homedir+'\config\config.ini')


        return config.get("MAIN", key)
    def getPreferences(self):
        """reads all settings and returns them in a dictionary. at the same time ,refreshes class dictionary"""
        config = SafeConfigParser()
        if self.platform=="linux":
            config.read(self.homedir+'/.pyNamaz/config/config.ini')
        elif self.platform=="windows":
            config.read(self.homedir+'\config\config.ini')
        self.prefDict=dict(config.items("MAIN"))
        return dict(config.items("MAIN"))
    def savePreferences(self,dict):
        """
        Saves or changes given key value pair to config file (MAIN SECTION)
        Refreshes classes preference dictionary
        """

        config = SafeConfigParser()
        if self.platform=="linux":

            config.read(self.homedir+'/.pyNamaz/config/config.ini')
        elif self.platform=="windows":
            config.read(self.homedir+'\config\config.ini')
        try:
            config.add_section("MAIN")
        except:
            pass
        for element in dict:
            config.set("MAIN", element,dict[element])
        if self.platform=="linux":

            with open(self.homedir+'/.pyNamaz/config/config.ini', 'w') as f:
                config.write(f)
        elif self.platform=="windows":
            with open(self.homedir+'\config\config.ini', 'w') as f:
                config.write(f)

        self.getPreferences()
    def retunToDefaults (self,option=None):
        """initiates preferences or sets up MAIN preferences to defaults"""
        config = SafeConfigParser()
        if self.platform=="linux":
            config.read(self.homedir+'/.pyNamaz/config/config.ini')
        elif self.platform=="windows":
            config.read(self.homedir+'\config\config.ini')
        if option==None:# all setting will be restored to default

            config.remove_section("MAIN")
            config.add_section("MAIN")

            defList= config.items('DEFAULTS')
            for pair in defList:
                config.set("MAIN",pair[0],pair[1])

        else:

            if option=="prefs":
                config.set("MAIN", 'showinTray','True')
                config.set("MAIN", 'playAdhan','False')
                config.set("MAIN", 'playWarnSound','True')
                config.set("MAIN", 'adhanSoundPath','')
                config.set("MAIN", 'warnSoundPath','')
                config.set("MAIN", 'closeAction','hide')
                config.set("MAIN", 'muteInAdhanTime','False')
                config.set("MAIN", 'showSystemNotifications','True')

            elif option=="warns":

                config.set("MAIN", 'beforeFajr','50')
                config.set("MAIN", 'beforeSunrise','30' )
                config.set("MAIN", 'beforeDhduhr','10')
                config.set("MAIN", 'beforeAsr','35')
                config.set("MAIN", 'beforeMaghrib','60')
                config.set("MAIN", 'beforeIsha','35')
                config.set("MAIN", 'fajrWarn','True')
                config.set("MAIN", 'fajrWarn','True')
                config.set("MAIN", 'dhuhrWarn','True')
                config.set("MAIN", 'sunriseWarn','True')
                config.set("MAIN", 'asrWarn','True')
                config.set("MAIN", 'ishaWarn','True')
                config.set("MAIN", 'maghribWarn','True')

            else:
                print "ERROR: returnToDefaults got an invalid parameter"
        if self.platform=="linux":
            with open(self.homedir+'/.pyNamaz/config/config.ini', 'w') as f:
                config.write(f)
        elif self.platform=="windows":
            with open(self.homedir+'\config\config.ini', 'w') as f:
                config.write(f)
        self.getPreferences()
    def reprintDefaults(self):
        """
        prints default section to file from scratch.
        """
        config = SafeConfigParser()
        if self.platform=="linux":
            config.read(self.homedir+'/.pyNamaz/config/config.ini')
        elif self.platform=="windows":
            config.read(self.homedir+'\config\config.ini')
        config.remove_section('DEFAULTS')
        config.add_section('DEFAULTS')
        config.set('DEFAULTS', 'showinTray','True')
        config.set('DEFAULTS', 'howToUseShowed','False')
        config.set('DEFAULTS', 'playAdhan','False')
        config.set('DEFAULTS', 'playWarnSound','True')
        config.set('DEFAULTS', 'adhanSoundPath','')
        config.set('DEFAULTS', 'warnSoundPath','')
        config.set('DEFAULTS', 'closeAction','hide')
        config.set('DEFAULTS', 'muteInAdhanTime','False')
        config.set('DEFAULTS', 'showSystemNotifications','True')
        config.set('DEFAULTS', 'beforeFajr','50')
        config.set('DEFAULTS', 'beforeSunrise','30' )
        config.set('DEFAULTS', 'beforeDhduhr','10')
        config.set('DEFAULTS', 'beforeAsr','35')
        config.set('DEFAULTS', 'beforeMaghrib','60')
        config.set('DEFAULTS', 'beforeIsha','35')
        config.set('DEFAULTS', 'fajrWarn','True')
        config.set('DEFAULTS', 'fajrWarn','True')
        config.set('DEFAULTS', 'dhuhrWarn','True')
        config.set('DEFAULTS', 'sunriseWarn','True')
        config.set('DEFAULTS', 'asrWarn','True')
        config.set('DEFAULTS', 'ishaWarn','True')
        config.set('DEFAULTS', 'maghribWarn','True')

        if self.platform=="linux":
            with open(self.homedir+'/.pyNamaz/config/config.ini', 'w') as f:
                config.write(f)
        elif self.platform=="windows":

            with open(self.homedir+'/config/config.ini', 'w') as f:
                config.write(f)


    def merge_two_dicts(self,x, y):
        '''Given two dicts, merge them into a new dict as a shallow copy.'''
        z = x.copy()
        z.update(y)
        return z


if __name__ == "__main__":
    pass
    # pass
    #  preobj=preferences()
    # preobj.reprintDefaults()
    #  preobj.retunToDefaults(option="prefs")
    # preobj.getPreferences()
#
#