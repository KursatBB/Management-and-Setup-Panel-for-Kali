import os
import time
import pyfiglet
import colorama
from colorama import Fore
import ktoolsetup
import kuserconf
ascii_banner=pyfiglet.figlet_format("KeK Setup")

def updateUpgrade():
    print(Fore.YELLOW + "Python Güncelleniyor.")
    os.system("sudo apt install python3 python3-pip")
    print(Fore.YELLOW + "Sistem güncellemeleri başlıyor.")
    os.system("sudo apt update -y && sudo apt upgrade -y")
    distUpg=input(Fore.YELLOW + "Genel güncelleme ve geliştirme bitti\nDağıtımın güncellenmesini ister misiniz(E veya H) : " + Fore.WHITE)
    if distUpg=="E" or "e":
        os.system("sudo apt update && sudo dist-upgrade -y")
        print(Fore.GREEN + "\nDağıtım güncellemesi bitti, gerekli olmayan paketler siliniyor\n" + Fore.WHITE)
        os.system("sudo apt autoremove -y")
    elif distUpg=="H" or "h":
        print(Fore.GREEN + "\nDağıtım güncellemesi olmayacak, gerekli olmayan paketler siliniyor\n" + Fore.WHITE)
        os.system("sudo apt autoremove -y")

if __name__ =="__main__":
    print(ascii_banner)
    name=os.getlogin()
    print (Fore.MAGENTA + "Giriş yaptığınız kullanıcı : "+ name + Fore.WHITE)
    while(True):
        deger= int(input(Fore.CYAN + "Ne yapmak istediğiniz seçin : \n1)Sistemi Güncelleştir ve Yükselt\n2)Kullanıcı işlemleri\n3)Araç yükle\n4)Çıkış Yap\n"))
        if deger > 0 and deger < 5:
            if deger==1:
                updateUpgrade()
            elif deger==2:
                kuserconf.menu()
            elif deger==3:
                ktoolsetup.menu()
            elif deger==4:
                break
        else:
            print(Fore.RED + "Geçerli bir değer girin.\n" + Fore.WHITE)