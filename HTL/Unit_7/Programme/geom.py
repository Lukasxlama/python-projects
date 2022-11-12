"""
author: Lukas Sanz
file: geom.py
catnr: 1BHIF-24
"""


### Bibliotheken
from geomlib import *


### Begrüßung + Abfrage
print("Willkommen beim geometrischen Wunderzwerg!\n")
choice = int(input("Bitte wählen Sie:\n(1) Berechnung der Entfernung: eindimensional\n(2) Berechnung der Entfernung: zweidimensional\n(3) Berechnung der Entfernung: dreidimensional\n(4) Zeichnung eines n-Eck's\n(5) Zeichnung eines Polygon's\n(6) Zeichnung von Sternen\n---> "))

if choice == 1:
    try:
        p1 = input("\nBitte geben Sie den x-Wert von Punkt 1 ein: ")
        p2 = input("Bitte geben Sie den x-Wert von Punkt 2 ein: ")
    except ValueError:
        exit("Ungültige Eingabe")
    ergebnis = distance1(p1, p2)
    print(f"\nDie Entfernung zwischen dem Punkt {p1} und dem Punkt {p2} beträgt {ergebnis}.")

elif choice == 2:
    try:
        p1x = int(input("\nBitte geben Sie den x-Wert von Punkt 1 ein: "))
        p1y = int(input("Bitte geben Sie den y-Wert von Punkt 1 ein: "))
        p2x = int(input("Bitte geben Sie den x-Wert von Punkt 2 ein: "))
        p2y = int(input("Bitte geben Sie den y-Wert von Punkt 2 ein: "))
    except ValueError:
        exit("Ungültige Eingabe")
    ergebnis = distance2(p1x, p2x, p1y, p2y)
    print(f"Die Entfernung zwischen dem Punkt ({p1x}, {p1y}) und dem Punkt ({p2x}, {p2y}) beträgt {ergebnis}.")

elif choice == 3:
    try:
        p1x = int(input("\nBitte geben Sie den x-Wert von Punkt 1 ein: "))
        p1y = int(input("Bitte geben Sie den y-Wert von Punkt 1 ein: "))
        p1z = int(input("Bitte geben Sie den z-Wert von Punkt 1 ein: "))
        p2x = int(input("Bitte geben Sie den x-Wert von Punkt 2 ein: "))
        p2y = int(input("Bitte geben Sie den y-Wert von Punkt 2 ein: "))
        p2z = int(input("Bitte geben Sie den z-Wert von Punkt 2 ein: "))
    except ValueError:
        exit("Ungültige Eingabe")
    ergebnis = distance3(p1x, p2x, p1y, p2y, p1z, p2z)
    print(f"Die Entfernung zwischen dem Punkt ({p1x}, {p1y}, {p1z}) und dem Punkt ({p2x}, {p2y}, {p2z}) beträgt {ergebnis}.")

elif choice == 4:
    try:
        x = float(input("\nGib die Koordinate von x für die Startposition ein: "))
        y = float(input("Gib die Koordinate von y für die Startposition ein: "))
        corner = int(input("Gib ein, wie viele Ecken das n-Eck haben soll: "))
        side_length = float(input("Gib die Seitenlänge des n-Eck's ein (cm): "))
    except ValueError:
        exit("Ungültige Eingabe")
    U = regular_polygon(x, y, corner, side_length)
    print(f"Der Umfang des {corner}-Eck's beträgt {U} cm")

elif choice == 5:
    try:
        p1x = float(input("\nGib eine Zahl für die x Koordinate von Punkt 1 ein: "))
        p1y = float(input("Gib eine Zahl für die y Koordinate von Punkt 1 ein: "))
        p2x = float(input("Gib eine Zahl für die x Koordinate von Punkt 2 ein: "))
        p2y = float(input("Gib eine Zahl für die y Koordinate von Punkt 2 ein: "))
        p3x = float(input("Gib eine Zahl für die x Koordinate von Punkt 3 ein: "))
        p3y = float(input("Gib eine Zahl für die y Koordinate von Punkt 3 ein: "))
        choice2 = input("Möchtest du noch zwei zusätzliche Punkte eingeben? (Y/N): ").lower()
        if choice2 == "y":
            p4x = float(input("Gib eine Zahl für die x Koordinate von Punkt 4 ein: "))
            p4y = float(input("Gib eine Zahl für die y Koordinate von Punkt 4 ein: "))
            p5x = float(input("Gib eine Zahl für die x Koordinate von Punkt 5 ein: "))
            p5y = float(input("Gib eine Zahl für die y Koordinate von Punkt 5 ein: "))
            print("Beende das Turtle Fenster, damit das Programm weiterläuft")
            U = polygon(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y)
            print(f"Der Umfang des Polygons beträgt {U} cm")
        elif choice2 == "n":
            print("Beende das Turtle Fenster, damit das Programm weiterläuft")
            U = polygon(p1x, p1y, p2x, p2y, p3x, p3y)
            print(f"Der Umfang des Polygons beträgt {U} cm")
        else:
            exit("Ungültige Eingabe")
    except ValueError:
        exit("Ungültige Eingabe")

elif choice == 6:
    try:
        numb = int(input("\nGib ein, wie viele Sterne gezeichnet werden sollen: "))
    except ValueError:
        exit("Ungültige Eingabe")
    stars_triangle(numb)

else:
    exit("Ungültige Eingabe")