"""
author: Lukas Sanz
file: calculator.py
catnr: 1BHIF-24
"""


### Bibliotheken
from math import sqrt


### Funktionen
def calculator():  # Rechner
    calculation = input("Gib deine Rechnung ein: ")  # Rechnungseingabe
    print(eval(calculation))  # Rechnung wird ausgerechnet und ausgegeben. | Sicherheitslücke!!
    print(query())  # Die Funktion "query" wird gestartet

def manual():  # Anleitung
    print("Hier eine kurze Anleitung, wie du die Rechenoperationen richtig verwendest:")
    print("Addition = +")
    print("Subtraktion = -")
    print("Multiplikation = *")
    print("Ganzzahlige Division = //")
    print("Rest bei der ganzzahligen Division = %")
    print("Gleitkommazahldivision = /")
    print("Potenz = **")
    print("Quadratwurzel = sqrt(number)")
    print("")
    print(calculator())  # Die Funktion "calculator" wird gestartet

def query():  # Abfrage/Entscheidung
    dec = input("Möchtest du noch eine Rechnung eingeben? (y/n): ")
    if dec == "y" or dec == "Y":
        print(calculator())  # Die Funktion "calculator" wird gestartet
    elif dec == "n" or dec == "N":
        exit()  # Programm wird geschlossen
    else:
        print("Ungültige Eingabe.")
        print(query())  # Wiederholung der Abfrage

### Code
print(manual())  # Die Funktion "manual" wird gestartet
