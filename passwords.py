import random
from colorama import Fore
from os import system, name

system('cls' if name == 'nt' else 'clear')

title = """

▒█▀▀█ ░█▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▒█░░▒█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▄ ▒█▀▀▀█ 
▒█▄▄█ ▒█▄▄█ ░▀▀▀▄▄ ░▀▀▀▄▄ ▒█▒█▒█ ▒█░░▒█ ▒█▄▄▀ ▒█░▒█ ░▀▀▀▄▄ 
▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄█
                                                |by NYOXS|
"""
print(Fore.BLUE + title + Fore.WHITE)



harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numaralar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ozelKarakterler = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '.']

def new_password():
    password = ''
    length_password = int(input(Fore.MAGENTA+"Şifre Uzunluğunu Giriniz(0-100):"))
    how_many_passwords = int(input(Fore.MAGENTA+"Kaç Adet Şifre Oluşturulsun(0-100):"))

    for i in range(how_many_passwords):
        password = ''
        for i in range(length_password):
             password += random.choice(harfler+numaralar+ozelKarakterler)

        print(password)

new_password()