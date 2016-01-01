from platform import system as sysname#for system type
from os import popen

class prayerTimes:
    def __init__(self):

        pass
    def getTimes(self): #Gets prayer times from www.diyanet.gov.tr
        pass
    def saveTimes(self): #saves Prayer times to PrayerTimes.txt
        pass
    def getTimesManuelly(self):
        if sysname()=="Linux":
            popen("kate ./PrayerTimes.txt")

        elif sysname()=="Windows":
            popen("notepad.exe ./PrayerTimes.txt")
        else :
            pass