"""
author: Lukas Sanz
file: 13 - minimum.py
catnr: 1BHIF-24
"""

### Funktionen
def zahlen_minimum():
    zahl_1, zahl_2, zahl_3 = input("Gib die erste Zahl ein: "), input("Gib die zweite Zahl ein: "), input("Gib die dritte Zahl ein: ")
    if zahl_1 == zahl_2 == zahl_3:
        print("Die 3 Zahlen sind gleich groß.")
    else:
        zahlen = [zahl_1, zahl_2, zahl_3]
        zahlen.sort()
        print(f"Die kleinste Zahl ist {zahlen[0]}.")
    schleife()

def schleife():
    q = input("Möchtest du das Programm wiederholen? (y/n): ").lower()
    if q == "y":
        minimum()
    elif q == "n":
        exit()
    else:
        schleife()

### Ausgabe
zahlen_minimum()

### Alternative Lösung:
"""
def zahlen_minimum():
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
"""