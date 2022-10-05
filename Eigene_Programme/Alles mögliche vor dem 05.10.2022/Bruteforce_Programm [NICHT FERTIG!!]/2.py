import itertools
import string
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


#
#
#
def bruteforce_attack_special_characters():
    print(
        f"{Fore.RED}{Style.BRIGHT}Hinweis: Wenn andere Zeichen benutzt werden als die, die in der  Klammer [] stehen, wird das Programm zwar suchen, aber nichts finden.")
    password = input(f"{Fore.GREEN}[Sonderzeichen]: Gib ein Passwort ein. (Max. 6 Stellen): ")
    start_counter = time.perf_counter()
    letters = string.punctuation
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
                    print(bruteforce_attack_special_characters())

                elif ifelse == "N" or ifelse == "n":
                    exit()

                else:
                    while ifelse != "Y" or ifelse != "y" or ifelse != "N" or ifelse != "n":
                        print(f"{Fore.RED}Ungültige Eingabe!")
                        ifelse = str(input(f"{Fore.GREEN}Möchtest du noch ein Passwort eingeben? [Y/N]: "))
                        if ifelse == "Y" or ifelse == "y":
                            print(bruteforce_attack_special_characters())

                        elif ifelse == "N" or ifelse == "n":
                            exit()
#
#
#

