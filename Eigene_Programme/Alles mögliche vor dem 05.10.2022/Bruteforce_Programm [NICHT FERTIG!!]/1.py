import itertools
import string
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def bruteforce_attack_letters():
    print(
        f"{Fore.RED}{Style.BRIGHT}Hinweis: Wenn andere Zeichen benutzt werden als die, die in der  Klammer [] stehen, wird das Programm zwar suchen, aber nichts finden.")
    password = input(f"{Fore.GREEN}[Buchstaben]: Gib ein Passwort ein. (Max. 6 Stellen): ")
    start_counter = time.perf_counter()
    letters = string.ascii_letters
    num_bruteforce = 0
    for num in range(1, 7):
        for bruteforce in itertools.product(letters, repeat=num):
            bruteforce = "".join(bruteforce)
            num_bruteforce += 1
            print(bruteforce)
            if bruteforce == password:
                end_counter = time.perf_counter()
                time_needed = end_counter - start_counter
                print(
                    f"""{Fore.MAGENTA}Das Passwort lautet: "{bruteforce}". {num_bruteforce} Versuch/Versuche wurde/n bei {round(time_needed, 2)} Sekunden benötigt.""")
                ifelse = str(input(f"{Fore.GREEN}Möchtest du noch ein Passwort eingeben? [Y/N]: "))
                if ifelse == "Y" or ifelse == "y":
                    print(bruteforce_attack_letters())

                elif ifelse == "N" or ifelse == "n":
                    exit()

                else:
                    while ifelse != "Y" or ifelse != "y" or ifelse != "N" or ifelse != "n":
                        print(f"{Fore.RED}Ungültige Eingabe!")
                        ifelse = str(input(f"{Fore.GREEN}Möchtest du noch ein Passwort eingeben? [Y/N]: "))
                        if ifelse == "Y" or ifelse == "y":
                            print(bruteforce_attack_letters())

                        elif ifelse == "N" or ifelse == "n":
                            exit()


def bruteforce_attack_numbs():
    print("das ist 1")


def bruteforce_attack_special_characters():
    print("das ist 2")


def head_code():
    print(
        f"{Fore.RED}P{Fore.GREEN}R{Fore.YELLOW}O{Fore.BLUE}G{Fore.MAGENTA}R{Fore.LIGHTBLUE_EX}A{Fore.RED}M{Fore.GREEN}M{Fore.YELLOW}E{Fore.BLUE}D {Fore.MAGENTA}B{Fore.LIGHTBLUE_EX}Y{Fore.RED}: {Fore.RED}L{Fore.GREEN}U{Fore.YELLOW}K{Fore.BLUE}A{Fore.MAGENTA}S{Fore.LIGHTBLUE_EX}X{Fore.RED}L{Fore.GREEN}A{Fore.YELLOW}M{Fore.BLUE}A")
    print("")
    print(f"{Fore.YELLOW}Wilkommen in meinem Brute Force Programm! Welche Zeichen sollen gesucht werden?")
    print("")
    print(f"{Fore.CYAN}0 = Nur Groß und Kleinbuchstaben [{string.ascii_letters}]")
    print(f"{Fore.CYAN}1 = Nur Zahlen [{string.digits}]")
    print(f"{Fore.CYAN}2 = Nur Sonderzeichen [{string.punctuation}]")
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
        while number != 0 or number != 1 or number != 2:
            invalid_error = input(f"{Fore.RED}Ungültige Eingabe. Soll das Programm neu gestarted werden? [Y/N]: ")
            if invalid_error == "Y" or invalid_error == "y":
                number = int(input(f"{Fore.GREEN}Gib eine Zahl von 0-2 ein: "))
                if number == 0:
                    print(bruteforce_attack_letters())
                elif number == 1:
                    print(bruteforce_attack_numbs())
                elif number == 2:
                    print(bruteforce_attack_special_characters())
            elif invalid_error == "N" or invalid_error == "n":
                exit()
            else:
                while invalid_error != "Y" or invalid_error == "y" or invalid_error == "N" or invalid_error == "n":
                    invalid_error = input(
                        f"{Fore.RED}Ungültige Eingabe. Soll das Programm neu gestarted werden? [Y/N]: ")
                    if invalid_error == "Y" or invalid_error == "y":
                        number = int(input(f"{Fore.GREEN}Gib eine Zahl von 0-2 ein: "))
                        if number == 0:
                            print(bruteforce_attack_letters())
                        elif number == 1:
                            print(bruteforce_attack_numbs())
                        elif number == 2:
                            print(bruteforce_attack_special_characters())
                    elif invalid_error == "N" or invalid_error == "n":
                        exit()