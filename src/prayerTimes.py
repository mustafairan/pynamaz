#!/usr/bin/env python3
import urllib
import json

#
# from pprint import pprint
# from xml.etree import ElementTree as ET

from platform import system as sysname#for system type
from os import popen

class prayerTimes:
    def __init__(self):

        pass
    def getTimes(self): #Gets prayer times from https://muezzin.herokuapp.com/. Its the api for diyanet.gov.tr
        req = urllib.Request('https://muezzin.herokuapp.com/countries')
        response = urllib.urlopen(req)
        the_page = response.read()
        #print(the_page)

        with open("deneme.txt","w+") as fileobj:
            fileobj.write(the_page)

        data = json.load(file("deneme.txt"))

        #pprint (data)/home/mnc
        #print data["countries"]
        country={}
        for dict in data["countries"]:
            print (dict)
            print (dict['trName'])
            print (dict ['id'])
            #country =country+{dict["trName"]:dict['id']}

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





        #
        # self.printCountries()
        # self.comboBoxSelectCountry.activated.connect(lambda: self.printCities())
        # self.getCities(2)
        # self.getDistricts(540)
        # self.comboBoxSelectCity.activated.connect(self.printer)
        # self.comboBoxSelectDistrict.activated.connect(self.printer)
        # print self.comboBoxSelectCountry.itemData(1,32)
        #
#         #
#     def getCountries(self): #get all countries and prints it to countries.json file
#
#         req = urllib.Request('https://muezzin.herokuapp.com/countries')
#         response = urllib.urlopen(req)
#         the_page = response.read()
#         with open("countries.json","w+") as fileobj:
#             fileobj.write(the_page)
#     def printCountries(self): #reads countries.json file and prints countries to relative combobox.
#         self.getCountries()
#         data = json.load(file("countries.json"))
#         self.comboBoxSelectCountry.clear()
#
#         for dict in data["countries"]:
#             # print dict
#             # print dict['trName']
#             # print dict ['id']
#             self.comboBoxSelectCountry.addItem(dict['trName'],dict['id'])
#
#
#
#         #self.comboBoxSelectCountry.activated.connect(lambda : self.getCities (str(166))) #TODO
#     def getCities(self,countryId): #get all cities for a given country id and prints it to cities.json file
#         req = urllib.Request('https://muezzin.herokuapp.com/'+str(countryId)+'/cities')
#         response = urllib.urlopen(req)
#         the_page = response.read()
#         with open("cities.json","w+") as fileobj:
#             fileobj.write(the_page)
#     def printCities(self): #reads countries.json file and prints countries to relative combobox.
#
#
# #todo if not -1 and == current
#         data = json.load(file("cities.json"))
#         self.comboBoxSelectCity.clear()
#
#         for dict in data["cities"]:
#             # print dict
#             # print dict['trName']
#             # print dict ['id']
#
#             self.comboBoxSelectCity.addItem(dict['name'],QtCore.QVariant(dict['id']))
#
#             #self.comboBoxSelectCountry.activated.connect(lambda : self.getCities (str(166))) #TODO
#     def getDistricts(self,cityId): #get all cities for a given country id and prints it to cities.json file
#         req = urllib.Request('https://muezzin.herokuapp.com/'+str(cityId)+'/districts')
#         response = urllib.urlopen(req)
#         the_page = response.read()
#         with open("districts.json","w+") as fileobj:
#             fileobj.write(the_page)
#     def printDistricts(self): #reads countries.json file and prints countries to relative combobox.
#
# #todo if not -1 and == current
#         data = json.load(file("districts.json"))
#         self.comboBoxSelectDistrict.clear()
#
#         for dict in data["districts"]:
#             # print dict
#             # print dict['trName']
#             # print dict ['id']
#             self.comboBoxSelectDistrict.addItem(dict['name'],QtCore.QVariant(dict['id']))
#
#
#         #self.comboBoxSelectCountry.activated.connect(lambda : self.getCities (str(166))) #TODO
#
