"""
author: Lukas Sanz
file: 05 - rectangles2.py
catnr: 1BHIF-24
"""


### Funktionen
def perimeter(a, b):
    calc = 2 * a + 2 * b
    round(calc, 2)
    return calc

def area(a, b):
    calc = a * b
    round(calc, 2)
    return calc

def class_(a, b):
    if a == b and a * 4 < 100:
        print(f"Größenklasse: Kleines Quadrat")
    if a == b and a * 4 >= 100:
        print(f"Größenklasse: Großes Quadrat")
    if a != b and a * b < 200:
        print(f"Größenklasse: Kleines Rechteck")
    if a != b and a * b >= 200:
        print(f"Größenklasse: Großes Rechteck")

### Abfrage
seite_a = float(input("Gib die erste Seite des Rechtecks ein (in cm): "))
seite_b = float(input("Gib die zweite Seite des Rechtecks ein (in cm): "))

### Ausgabe
class_(seite_a, seite_b)
print(f"Umfang: {perimeter(seite_a, seite_b)} cm")
print(f"Fläche: {area(seite_a, seite_b)} cm²")