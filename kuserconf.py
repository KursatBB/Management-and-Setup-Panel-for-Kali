import os
import time
import pyfiglet
import colorama
from colorama import Fore

def menu():
    while(True):
        deger= int(input("Ne yapacağınızı seçin : \n1)Yeni Kullanıcı Ekle\n2)Kullanıcı Şifresi Değiştir\n3)Geri git"))
        for a in deger:
            if a=="1":
                addNewUser()
            elif a=="2":
                changePasswd()
            elif a=="3":
                break
        break

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