"""
author: Lukas Sanz
file: 9 - calculate2.py
catnr: 1BHIF-24
"""


### Bibliotheken
from mymath import sqrt, minimum


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