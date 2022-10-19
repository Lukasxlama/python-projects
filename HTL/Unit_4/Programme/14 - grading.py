"""
author: Lukas Sanz
file: 14 - grading.py
catnr: 1BHIF-24
"""


### Funktionen
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
    schleife()

def schleife():
    q = input("Möchtest du das Programm wiederholen? (y/n): ").lower()
    if q == "y":
        grading()
    elif q == "n":
        exit()
    else:
        print("Ungültige Eingabe!")
        schleife()

### Ausgabe
grading()