import os
print os.getcwd()
os.system("mkdir ~/.pyNamaz")
os.system("cp -HR ./* ~/.pyNamaz/")

os.system("cp -HR ./applications/pyNamaz.desktop ~/.local/share/applications/")
