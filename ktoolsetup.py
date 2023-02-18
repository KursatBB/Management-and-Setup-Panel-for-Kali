import os
import signal
import requests
import urllib.request
from bs4 import BeautifulSoup
import colorama
from colorama import Fore
from configparser import SafeConfigParser

config_file = "cmsmap.conf"
parser = SafeConfigParser()
parser.optionxform = str
parser.read(config_file)

def handler(signum, frame):
    exit(1)
signal.signal(signal.SIGINT, handler)

def menu():
    while(True):
        deger= input("Hangi aracı/araçları indirmek istersiniz aralarında virgül olacak şekilde girin (1,3 vb.) :\nAraç Listesi : \n1)openVAS\n2)GoBuster\n3)CMSmap\n4)Beef\n5)Snap\n6)VSCode(snap ile kurulur)\n7)Tor Browser(Şuanlık sadece tar dosyası)\n8)Geri Git\n")
        dizi=deger.split(",")
        for a in dizi:
            print(a)
            if a=="1":
                openVAS()
            elif a=="2":
                goBuster()
            elif a=="3":
                CMSMap()
            elif a=="4":
                Beef()
            elif a=="5":
                Snap()
            elif a=="6":
                VSCode()
            elif a=="7":
                torBrowser()
            elif a=="8":
                break
        input(Fore.GREEN + "Kurulumlar yapıldı.\nDevam etmek için Enter'a basın.")
        break

def openVAS():
    print(Fore.YELLOW + "openVAS indiriliyor.")
    os.system("sudo apt install openvas")
    #print(Fore.GREEN + "openVAS kuruldu ayarlamalara başlanıyor.\nBu işlem biraz uzun sürecek lütfen bekleyin.")
    os.system("gvm-setup")
    print(Fore.GREEN + "gvm kuruldu lütfen UDID ve password değerlerini bir yere kaydedin.")
    input(Fore.YELLOW + "Devam etmek için Enter'a basın.")
    os.system("gvm-check-setup")
    #print(Fore.GREEN + "openVAS tamamen kuruldu kullanmaya başlayabilirsiniz.")

def goBuster():
    print(Fore.YELLOW + "GoBuster indiriliyor.")
    os.system("sudo apt install gobuster -y")
    #print(Fore.GREEN + "Gobuster kuruldu.")

#---------------------- CMSmap -------------------------------
def CMSMap():
    print(Fore.YELLOW + "CMSmap indiriliyor.")
    os.system("git clone https://github.com/Dionach/CMSmap")
    set_config_CMSMap("exploitdb","edbtype","APT")
    set_config_CMSMap("exploitdb","edbpath","/usr/share/exploitdb/")
    os.system("cd CMSmap")
    os.system("pip3 install .")
def set_config_CMSMap(section,option,value):
    if parser.has_section(section,option,value):
        parser.set(section, option,value)
        with open(config_file,"w") as conf_file:
            parser.write(conf_file)
            return True
#-------------------------------------------------------------
def Beef():
    userF="user:"
    passwdF="passwd:"
    print(Fore.YELLOW + "Beef indiriliyor.")
    os.system("git clone https://github.com/beefproject/beef")
    os.system("sudo apt install software-properties-common -y")
    os.system("sudo apt-add-repository -y ppa:brightbox/ruby-ng")
    os.chdir("./beef/")
    os.system("./install")
    file = open("config.yaml","r+")
    text= file.read()
    print(Fore.GREEN + "Beef kuruldu\nBeef'in varsayılan giriş bilgilerini değiştirmek için kullanıcı adı ve şifresini girin :\n")
    username=input("Kullanıcı adı : ")
    passwd = input("Şifre : ")
    if '"beef"' in text:
        file.seek(0)
        file.truncate()
        new_text=text.replace('"beef"',"")
        file.write(new_text)
        if userF in new_text:
            file.seek(0)
            file.truncate()
            new_text=new_text.replace(userF,userF+ ' "'+username + '"')
            file.write(new_text)
            if passwdF in new_text:
                file.seek(0)
                file.truncate()
                new_text=new_text.replace(passwdF,passwdF+ ' "'+passwd + '"')
                file.write(new_text)
                file.close()
    print("Beef giriş bilgileri ayarlandı, yeni giriş bilgilerinizle beef'i kullanabilirsiniz (./beef)")

    

def Snap():
    file = open("/etc/environment","r+")
    text= file.read()
    snapbin=":/snap/bin"
    usrgames=":/usr/games"
    
    print("Snap kuruluyor.")
    os.system("sudo apt install python3 python3-pip")
    os.system("sudo apt update")
    os.system("sudo apt install snapd")
    os.system("systemctl enable --now snapd apparmor")
    if snapbin in text:
        print("Snap kuruldu Kullanabilmek için sistemi yeniden başlatın.")
    else:
        if usrgames in text:
            file.seek(0)
            file.truncate()
            new_text= text.replace(usrgames, usrgames + snapbin)
            file.write(new_text)
            file.close()
            print("Snap kuruldu Kullanabilmek için sistemi yeniden başlatın.")
def VSCode():
    print("Visual Studio Code kuruluyor.")
    os.system("sudo snap install code --classic")

def torBrowser():
    url = "https://www.torproject.org/download/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    download_links = soup.find_all('a', href=True, string="Download for Linux")

    if len(download_links) == 0:
        print("Could not find download link")
    else:
        download_url = download_links[0]['href']
        print(f"Downloading from {download_url}")
        urllib.request.urlretrieve(download_url, "torbrowser-install.tar.xz")
