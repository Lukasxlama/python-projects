"""
author: Lukas Sanz
file: 13 - minimum.py
catnr: 1BHIF-24
"""


### Funktionen
def minimum():
    zahl_1 = input("Gib die erste Zahl ein: ")
    zahl_2 = input("Gib die zweite Zahl ein: ")
    zahl_3 = input("Gib die dritte Zahl ein: ")
    if zahl_1 < zahl_2 and zahl_1 < zahl_3:
        print(f"Die kleinste Zahl ist {zahl_1}")
    elif zahl_2 < zahl_1 and zahl_2 < zahl_3:
        print(f"Die kleinste Zahl ist {zahl_2}")
    elif zahl_3 < zahl_2 and zahl_3 < zahl_1:
        print(f"Die kleinste Zahl ist {zahl_3}")
    elif zahl_1 == zahl_2 == zahl_3:
        print("Die 3 Zahlen sind gleich groß.")
    frage()

def frage():
    q = input("Möchtest du noch eine Zahl eingeben? (y/n): ").lower()
    if q == "y":
        minimum()
    elif q == "n":
        exit()
    else:
        frage()

### Ausgabe
minimum()