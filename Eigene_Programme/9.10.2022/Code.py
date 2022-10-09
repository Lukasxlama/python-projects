"""
author: Lukas Sanz
file: bruteforce.py
catnr: 1BHIF-24
"""


### Bibliotheken
import itertools
import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


### Funktionen
def bruteforce_attack_letters():
    password = input(f"{Fore.GREEN}[Buchstaben]: Gib ein Passwort ein. (Max. 6 Stellen): ")
    letters = string.ascii_letters
    num_bruteforce = 0
    for num in range(1, 7):
        for bruteforce in itertools.product(letters, repeat=num):
            bruteforce = "".join(bruteforce)
            num_bruteforce += 1
            print(bruteforce)
            if bruteforce == password:
                print(f"""{Fore.MAGENTA}Das Passwort lautet: "{bruteforce}" {num_bruteforce} Versuch/Versuche wurde/n benötigt.""")
                input(f"""{Fore.GREEN}"Strg + C" drücken, um das Fenster zu schließen..""")

def bruteforce_attack_numbs():
    password = input(f"{Fore.GREEN}[Zahlen]: Gib ein Passwort ein. (Max. 8 Stellen): ")
    letters = string.digits
    num_bruteforce = 0
    for num in range(1, 9):
        for bruteforce in itertools.product(letters, repeat=num):
            bruteforce = "".join(bruteforce)
            num_bruteforce += 1
            print(bruteforce)
            if bruteforce == password:
                print(f"""{Fore.MAGENTA}Das Passwort lautet: "{bruteforce}" {num_bruteforce} Versuch/Versuche wurde/n benötigt.""")
                input(f"""{Fore.GREEN}"Strg + C" drücken, um das Fenster zu schließen..""")

def bruteforce_attack_special_characters():
    password = input(f"{Fore.GREEN}[Sonderzeichen]: Gib ein Passwort ein. (Max. 6 Stellen): ")
    letters = string.punctuation
    num_bruteforce = 0
    for num in range(1, 7):
        for bruteforce in itertools.product(letters, repeat=num):
            bruteforce = "".join(bruteforce)
            num_bruteforce += 1
            print(bruteforce)
            if bruteforce == password:
                print(
                    f"""{Fore.MAGENTA}Das Passwort lautet: "{bruteforce}" {num_bruteforce} Versuch/Versuche wurde/n benötigt.""")
                input(f"""{Fore.GREEN}"Strg + C" drücken, um das Fenster zu schließen..""")

### Ausgabe
print(f"{Fore.RED}P{Fore.GREEN}R{Fore.YELLOW}O{Fore.BLUE}G{Fore.MAGENTA}R{Fore.LIGHTBLUE_EX}A{Fore.RED}M{Fore.GREEN}M{Fore.YELLOW}E{Fore.BLUE}D {Fore.MAGENTA}B{Fore.LIGHTBLUE_EX}Y{Fore.RED}: {Fore.RED}L{Fore.GREEN}U{Fore.YELLOW}K{Fore.BLUE}A{Fore.MAGENTA}S{Fore.LIGHTBLUE_EX}X{Fore.RED}L{Fore.GREEN}A{Fore.YELLOW}M{Fore.BLUE}A")
print(f"{Fore.YELLOW}Wilkommen in meinem Brute Force Programm! Welche Zeichen sollen gesucht werden?")
print("")
print(f"{Fore.CYAN}0 = Nur Groß und Kleinbuchstaben: {string.ascii_letters}")
print(f"{Fore.CYAN}1 = Nur Zahlen: {string.digits}")
print(f"{Fore.CYAN}2 = Nur Sonderzeichen: {string.punctuation}")
print("")
print(f"{Fore.RED}Hinweis: Die Suche kann bei vielen Zeichen mehrere Stunden bis Tage dauern!")
print("")
number = int(input(f"{Fore.GREEN}Gib eine Zahl von 0-2 ein: "))

if number == 0:
    print(bruteforce_attack_letters())
elif number == 1:
    print(bruteforce_attack_numbs())
elif number == 2:
    print(bruteforce_attack_special_characters())

else:
    var = input(f"{Fore.RED}Ungültige Eingabe. Soll das Programm neu gestarted werden? [Y/N]: ")
    if var == "Y" or "y" or "yes" or "Yes" or "YES" or "YEs" or "YeS" or "yES":
        number = int(input(f"{Fore.GREEN}Gib eine Zahl von 0-3 ein: "))
        if number == 0:
            print(bruteforce_attack_letters())
        elif number == 1:
            print(bruteforce_attack_numbs())
        elif number == 2:
            print(bruteforce_attack_special_characters())
    else:
        input(f"{Fore.GREEN}Drücke Enter um das Programm zu beenden..")