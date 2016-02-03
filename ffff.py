from PyQt4.phonon import Phonon
class player():

    output = Phonon.AudioOutput(Phonon.MusicCategory)
    m_media = Phonon.MediaObject()
    Phonon.createPath(m_media, output)
    def play(self,fn):
        self.m_media.stop()
        self.m_media.setCurrentSource(Phonon.MediaSource("sounds/{}".format(fn)))
        self.m_media.play()




if __name__ == "__main__":
    xxx=player()
    filePath =r"/home/mnc/.pyNamaz/data/sms.wav"
    xxx.play(filePath)


    raw_input("")
# // ...
# player->setMedia(QUrl::fromLocalFile("/Users/me/Music/coolsong.mp3"));
# player->setVolume(50);
# player->play();