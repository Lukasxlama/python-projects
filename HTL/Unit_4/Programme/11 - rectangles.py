"""
author: Lukas Sanz
file: 11 - rectangles.py
catnr: 1BHIF-24
"""


### Funktion
def groessenklassen():
    seite_a, seite_b = float(input("Gib die erste Seite des Rechtecks ein (in cm): ")), float(input("Gib die zweite Seite des Rechtecks ein (in cm): "))
    print("\n")
    if seite_a == seite_b and seite_a * 4 < 100:
        print(f"Größenklasse: Kleines Quadrat\nFläche: {seite_a * seite_b} cm².")
    if seite_a == seite_b and seite_a * 4 >= 100:
        print(f"Größenklasse: Großes Quadrat\nFläche: {seite_a * seite_b} cm².")
    if seite_a != seite_b and seite_a * seite_b < 200:
        print(f"Größenklasse: Kleines Rechteck\nFläche: {seite_a * seite_b} cm².")
    if seite_a != seite_b and seite_a * seite_b >= 200:
        print(f"Größenklasse: Großes Rechteck\nFläche: {seite_a * seite_b} cm².")
    schleife()

def schleife():
    q = input("Möchtest du das Programm wiederholen? (y/n): ").lower()
    if q == "y":
        groessenklassen()
    elif q == "n":
        exit()
    else:
        schleife()

### Ausgabe
groessenklassen()