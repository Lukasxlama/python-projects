"""
author: Lukas Sanz
file: 11 - rectangles.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
seite_a = float(input("Gib die erste Seite des Rechtecks ein (in cm): "))
seite_b = float(input("Gib die zweite Seite des Rechtecks ein (in cm): "))

### Ausgabe
print()
if seite_a == seite_b and seite_a * 4 < 100:
    print(f"Größenklasse: Kleines Quadrat\nFläche: {seite_a * seite_b} cm².")
if seite_a == seite_b and seite_a * 4 >= 100:
    print(f"Größenklasse: Großes Quadrat\nFläche: {seite_a * seite_b} cm².")
if seite_a != seite_b and seite_a * seite_b < 200:
    print(f"Größenklasse: Kleines Rechteck\nFläche: {seite_a * seite_b} cm².")
if seite_a != seite_b and seite_a * seite_b >= 200:
    print(f"Größenklasse: Großes Rechteck\nFläche: {seite_a * seite_b} cm².")