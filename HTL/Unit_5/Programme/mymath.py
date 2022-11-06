"""
author: Lukas Sanz
file: mymath.py
catnr: 1BHIF-24
"""


### Funktionen
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

def grading():
    points = float(input("Wie viele Punkte von 0-100 hast du?: "))
    if points <= 50:
        print(f"Deine Note ist:\n0-50 Punkte ---> Nicht genügend")
    elif points <= 62:
        print(f"Deine Note ist:\n50-62 Punkte ---> Genügend")
    elif points <= 78:
        print(f"Deine Note ist:\n63-78 Punkte ---> Befriedigend")
    elif points <= 90:
        print(f"Deine Note ist:\n79-90 Punkte ---> Gut")
    elif points <= 100:
        print(f"Deine Note ist:\n91-100 Punkte ---> Sehr gut")
    else:
        print("Ungültige Punktzahl, bitte gib eine Zahl zwischen 0 und 100 ein!")