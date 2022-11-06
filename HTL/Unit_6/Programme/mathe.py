"""
author: Lukas Sanz
file: mathe.py
catnr: 1BHIF-24
"""


### Bibliotheken
from mathelib import *


### arithmetisches Mittel berechnen
def option_1():
    zahl_1, zahl_2, zahl_3 = float(input("\nZahl 1: ")), float(input("Zahl 2: ")), float(input("Zahl 3: "))
    ergebnis = arith_mean(zahl_1, zahl_2, zahl_3)
    print(f"Das arithmetische Mittel lautet: {ergebnis}")
    exit()

### geometrisches Mittel berechnen
def option_2():
    zahl_1, zahl_2 = float(input("\nZahl 1: ")), float(input("Zahl 2: "))
    ergebnis = geom_mean(zahl_1, zahl_2)
    if ergebnis == -1:
        print(f"Negativer Radikant: Das geometrische Mittel von {zahl_1} und {zahl_2} konnte nicht berechnet werden.")
        exit()
    print(f"Das geometrische Mittel lautet: {ergebnis}")
    exit()

def option_3():
    frage2 = int(input("\n1 = Zahlen addieren\n2 = Strings konkatenieren\n---> "))
    if frage2 == 1:
        zahl_1, zahl_2 = float(input("\nZahl 1: ")), float(input("Zahl 2: "))
        ergebnis_float = sum(zahl_1, zahl_2)
        print(f"Die Summe lautet: {ergebnis_float}")
        exit()
    elif frage2 == 2:
        string_1, string_2 = input("\nString 1: "), input("String 2: ")
        ergebnis_str = string_1 + string_2
        print(f"Die Strings wurden konkateniert: {ergebnis_str}")
        exit()
    else:
        print("Ungültige Eingabe!")
        exit()

def option_4():
    time = float(input("\nGib ein, wielange der Körper fällt (in Sekunden): "))
    v = velocity(time)
    print(f"Der Körper fällt nach {time} Sekunden mit {v} km/h")
    exit()

def option_5():
    time = float(input("\nGib ein, wielange der Körper fällt (in Sekunden): "))
    s = space(time)
    print(f"Der Körper legt nach {time} Sekunden {s} Kilometer zurück")
    exit()

def option_6():
    dividend = int(input("\nGib den Dividend ein: "))
    divisor = int(input("Gib den Divisor ein: "))
    ergebnis = mod(dividend, divisor)
    print(f"Der Rest von {dividend} / {divisor} ist {ergebnis}")
    exit()

def option_7():
    radikant = float(input("Gib eine Zahl für den Radikant ein: "))
    ergebnis = square_root(radikant)
    print(f"Die Wurzel aus {radikant} ist {ergebnis}")
    exit()

def option_8():
    dividend = float(input("Gib den Dividend ein: "))
    divisor = float(input("Gib den Divisor ein: "))
    quotient = div(dividend, divisor)
    print(f"{dividend} / {divisor} = {quotient}")
    exit()

### Ausgabe
frage = int(input("Wähle eine Option aus:\n1 = arithmetisches Mittel berechnen\n2 = geometrisches Mittel berechnen\n3 = Summe berechnen / Strings konkatenieren\n4 = Geschwindigkeit berechnen\n5 = Strecke berechnen\n6 = Rest einer Division berechnen\n7 = Wurzel ziehen\n8 = Quotienten berechnen\n--> "))
while frage != 1 or frage != 2:
    match frage:
        case 1:
            option_1()
        case 2:
            option_2()
        case 3:
            option_3()
        case 4:
            option_4()
        case 5:
            option_5()
        case 6:
            option_6()
        case 7:
            option_7()
        case 8:
            option_8()
        case _:
            print("Ungültige Eingabe: Gib eine Zahl zwischen 1 und 8 ein!\n")
            frage = int(input("Wähle eine Option aus:\n1 = arithmetisches Mittel berechnen\n2 = geometrisches Mittel berechnen\n3 = Summe berechnen / Strings konkatenieren\n5 = Strecke berechnen\n6 = Rest einer Division berechnen\n7 = Wurzel ziehen\n8 = Quotienten berechnen\n--> "))