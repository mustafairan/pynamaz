from ConfigParser import SafeConfigParser
class preferences:
    prefDict={}
    def __init__(self):
        #TODO should look for a config.ini , if there isnt any, then call returntodefaults
        self.setPreferences()
    def readPreferences(self,key):#takes a preference key and return its value
        config = SafeConfigParser()
        config.read('config.ini')
        return config.get('main', key)
    def setPreferences(self):#reads all settings and returns them in a dictionary
        keys=["showintray" ,"playadhan","playwarn","adhansoundpath","warnsoundpath","closeaction","muteinadhantaime","beforefajr","beforesunrise","beforedhduhr","beforeasr","beforemaghrib","beforeisha","fajrwarn","dhuhrwarn","sunrisewarn","asrwarn","ishawarn","maghribwarn"]
        preferencesDictionary={}
        config = SafeConfigParser()
        config.read('config.ini')
        for key in keys:
            print key
            #preferencesDictionary+={key:str(config.get('main', key))}
            preferencesDictionary=self.merge_two_dicts(preferencesDictionary,{key:str(config.get('main', key))})

        self.prefDict=preferencesDictionary
        #print self.prefDict
    def savePreferences(self):

        config = SafeConfigParser()
        config.read('config.ini')
        config.add_section('main')
        config.set('main', 'showinTray','true')
        config.set('main', 'playAdhan','true')
        config.set('main', 'playWarn','true')
        config.set('main', 'adhanSoundPath','')
        config.set('main', 'warnSoundPath','')
        config.set('main', 'closeAction','hide')
        config.set('main', 'muteInAdhanTAime','false')
        config.set('main', 'beforeFajr','33')
        config.set('main','beforeSunrise','33' )
        config.set('main', 'beforeDhduhr','33')
        config.set('main', 'beforeAsr','33')
        config.set('main', 'beforeMaghrib','33')
        config.set('main', 'beforeIsha','33')
        config.set('main', 'fajrWarn','false')
        config.set('main', 'dhuhrWarn','false')
        config.set('main', 'sunriseWarn','false')
        config.set('main', 'asrWarn','false')
        config.set('main', 'ishaWarn','false')
        config.set('main', 'maghribWarn','false')
        with open('config.ini', 'w') as f:
            config.write(f)
    def retunToDefaults (self): #initiates preferences or sets up to defaults
        config = SafeConfigParser()
        config.read('config.ini')
        try:
            config.add_section('main')
        except:
            pass
        config.set('main', 'showinTray','true')
        config.set('main', 'playAdhan','false')
        config.set('main', 'playWarn','true')
        config.set('main', 'adhanSoundPath','')
        config.set('main', 'warnSoundPath','')
        config.set('main', 'closeAction','hide')
        config.set('main', 'muteInAdhanTAime','false')
        config.set('main', 'beforeFajr','0')
        config.set('main', 'beforeSunrise','0' )
        config.set('main', 'beforeDhduhr','0')
        config.set('main', 'beforeAsr','0')
        config.set('main', 'beforeMaghrib','0')
        config.set('main', 'beforeIsha','0')
        config.set('main', 'fajrWarn','true')
        config.set('main', 'dhuhrWarn','true')
        config.set('main', 'sunriseWarn','true')
        config.set('main', 'asrWarn','true')
        config.set('main', 'ishaWarn','true')
        config.set('main', 'maghribWarn','true')
        with open('config.ini', 'w') as f:
            config.write(f)
    def merge_two_dicts(self,x, y):
        '''Given two dicts, merge them into a new dict as a shallow copy.'''
        z = x.copy()
        z.update(y)
        return z

# if __name__ == "__main__":
#     preobj=preferences()

