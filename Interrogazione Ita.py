import os
from termcolor import colored
from bs4 import BeautifulSoup
import requests

def getText(number):
    url = f"https://divinacommedia.weebly.com/inferno-canto-{number}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    pars = soup.findAll("div", {"class": "paragraph"})
    par1 = pars[1].get_text()
    par2 = pars[-4].get_text()
    os.system('clear')

    print(colored(f'\u2794  Canto {number}', 'green'))
    print('\n')
    print(par1)
    print('\n')
    print(par2)

def menu():
    print(f"{colored('1.', 'red')} Canti Dante")
    print(f"{colored('0.', 'red')} Esci")
    choice = input()
    os.system('clear')
    if choice=='1':
        print(colored('\u2794  Dante','green'))
        number = input('Numero canto con numeri romani minuscoli:\n')
        getText(number)
        print('\n')
        menu()
    elif choice=='0':
        global go
        go = False


os.system('clear')

menu()

os.system('clear')