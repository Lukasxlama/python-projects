"""
author: Lukas Sanz
file: 8 - calculate.py
catnr: 1BHIF-24
"""


### Funktion
def sqrt(x0):
    x1 = (x0 + x0 / x0) / 2
    x2 = (x1 + x0 / x1) / 2
    x3 = (x2 + x0 / x2) / 2
    print(f"Radikant = {x0}\nWurzelexponent = 2\nWurzelwert (Näherung) = {round(x3, 2)}")

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

### Ausgabe
frage = int(input("Wähle eine Option aus:\n1 = sqrt\n2 = minimum\n--> "))
while frage != 1 or frage != 2:
    match frage:
        case 1:
            sqrt(float(input("Gib eine Zahl für den Radikant ein: ")))
        case 2:
            minimum()
        case _:
            print("Ungültige Eingabe: Gib 1 oder 2 ein!")
            frage = int(input("\nWähle eine Option aus:\n1 = sqrt\n2 = minimum\n--> "))