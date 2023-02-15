import os
import time
import pyfiglet
import colorama
from colorama import Fore
import ktoolsetup
ascii_banner=pyfiglet.figlet_format("KeK Setup")


def addNewUser():
    newUserName=input(Fore.YELLOW + "Yeni kullanıcının ismini girin : " + Fore.WHITE)
    os.system("sudo adduser " + newUserName)
    os.system("sudo usermod -aG sudo " + newUserName)
    os.system("sudo chsh -s /bin/bash " + newUserName)
    print(Fore.GREEN +"\nYeni kullanıcı oluşturuldu ve sudo erişimi verildi.\n" + Fore.WHITE)

def changePasswd():
    nameforChange=input(Fore.YELLOW + "Şifresini değiştirmek istediğiniz kullanıcının adını girin : " + Fore.WHITE)
    os.system("sudo passwd {}".format(nameforChange))
    print(Fore.GREEN + "\nKullanıcının şifresi başarıyla değiştirildi.\n" + Fore.WHITE)

def updateUpgrade():
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
        deger= int(input(Fore.CYAN + "Ne yapmak istediğiniz seçin : \n1)Yeni kullanıcı oluştur\n2)İsmini girdiğiniz bir kullanıcının şifresini değiştir\n3)Sistemi güncelleştir ve yükselt.\n4)Araç yükle\n5)Çıkış Yap\n"))
        if deger > 0 and deger < 6:
            if deger==1:
                addNewUser()
            elif deger==2:
                changePasswd()
            elif deger==3:
                updateUpgrade()
            elif deger==4:
                ktoolsetup.menu()
            elif deger==5:
                break
        else:
            print(Fore.RED + "Geçerli bir değer girin.\n" + Fore.WHITE)