"""
author: Lukas Sanz
file: power8.py
catnr: 1BHIF-24
"""


def oktal_in_dezimal(oktal):
    ergebnis = 0
    hochzahl = 0
    for ziffer in oktal[::-1]:
        if ziffer.isdigit():
            ergebnis += int(ziffer) * (8 ** hochzahl)
            hochzahl += 1
        else:
            break
    return ergebnis


oktalzahl = input("Bitte gib eine Zahl im Oktalsystem ein: ")

try:
    oktalzahl_int = int(oktalzahl)
except ValueError:
    exit(f"Deine Eingabe ist keine Zahl!")
if "8" in oktalzahl or "9" in oktalzahl:
    exit(f"Deine Eingabe ist keine Oktalzahl!")

dezimal = oktal_in_dezimal(oktalzahl)

print(f"{oktalzahl} im Oktalsystem entspricht {dezimal} im Dezimalsystem.")