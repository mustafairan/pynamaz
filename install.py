import os
print os.getcwd()
from sys import platform

class install:
    platform=""

    def __init__(self):
        self.findOutPlatform()

        if self.platform=="linux":
            os.system("mkdir ~/.pyNamaz")
            os.system("cp -HR ./* ~/.pyNamaz/")
            os.system("cp -HR ./applications/pyNamaz.desktop ~/.local/share/applications/")

        elif self.platform=="windows":

            #os.system("mkdir %ProgramFiles%\pyNamaz\ ")
            #os.system("echo %programfiles% ")



            #os.system("xcopy "+ os.getcwd()+"\* "+os.getenv("programfiles")+"\pyNamaz\  ")
            #print "xcopy '"+ os.getcwd()+"\ ' '"+os.getenv("programfiles")+"\pyNamaz\ '  "
            #os.system('mkdir "'+str(os.getenv('programfiles')+'\pyNamaz"' ))

            ax=( ' xcopy /I /E "'+str(os.getcwd())+'" "' +str(os.getenv('programfiles')+'\pyNamaz" '))
            os.system("powershell")
            print("""powershell -Command "Start-Process '"""+ax+ """"' -Verb runAs""")
            os.system("Start-process powershell -Verb runAs")



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
            self.platform = "linux"
        elif platform.startswith("win32"):
            self.platform = "windows"
        elif platform.startswith("cygwin"):
            self.platform = "windows"
        elif platform.startswith("darwin"):
            self.platform = "mac"
        elif platform.startswith("os2"):
            self.platform = "mac"
        elif platform.startswith("os2emx"):
            self.platform = "mac"
        else:
            self.platform = "unknown"
if __name__=="__main__":
    xxx=install()




