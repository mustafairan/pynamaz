# import urllib
# veriler={}
# # veriler['countryName'] = "2"
# # veriler['stateName'] = "500"
# # veriler['name'] = "9148"
# veriler['period']='Aylik'
# veriler['Country'] = "150"
# veriler['State'] = "16275"
# veriler['City'] = "9205"
# #Country=150&State=16275&City=9205&period=Aylik
# #url = "http://www.diyanet.gov.tr/turkish/namazvakti/vakithes_namazsonuc.asp"
# #url="http://www.diyanet.gov.tr/tr/namazvakitleri"
# #{"countryName":"2","stateName":"500","name":"9148"}
# url="http://www.diyanet.gov.tr/tr/PrayerTime/WorldPrayerTimes"
# # veriler = urllib.urlencode(veriler)
# # site = urllib.urlopen(url, veriler)
# # html = site.read(9000)
# # print html
# # print "hello"
#
#
# import urllib2
# req = urllib2.Request(url)
# req.add_header('Referer', 'http://www.diyanet.gov.tr/tr/PrayerTime/PrayerTimesList')
#
# req.add_header('Cookie','Country=2; State=16275; City=9205; dynweb=ffffffff096c090745525d5f4f58455e445a4a423660')
# #req.add_header("Content-Type",'application/json')
# data={'Country':'2','State':'506','City':'9205','period':'Aylik'}
#
# data=urllib.urlencode(data)
# resp = urllib2.urlopen(req,data=data)
# content = resp.read()
# print content
import urllib,re
def test():
    
    url = str("http://www.diyanettakvimi.com/"+"turkiye" +
              "/" +"ankara"+ "-ezan-vakti.html")
    site = urllib.urlopen(url)
    html = site.read(6500)

    metin = 'td align=center class="im3">(.*?)</td><td align=center class="im3">(.*?)</td>' + \
            '<td align=center class="im3">(.*?)</td><td align=center class="im3">(.*?)</td>' + \
            '<td align=center class="im3">(.*?)</td><td align=center class="im3">(.*?)</td>'

    ara = re.search(metin, html).groups()
    saatler = ara

    imsak = saatler[0]
    gunes = saatler[1]
    ogle = saatler[2]
    ikindi = saatler[3]
    aksam = saatler[4]
    yatsi = saatler[5]
    print imsak,gunes,ogle,ikindi,aksam,yatsi

if __name__ == "__main__":
    test()




















