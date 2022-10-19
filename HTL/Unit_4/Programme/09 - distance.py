"""
author: Lukas Sanz
file: 09 - distance.py
catnr: 1BHIF-24
"""

### Funktionen
def distance_func(**def_status):
    status = def_status.get("with_abs", False)
    if not status:
        p1 = float(input("Gib die erste Zahl ein: "))
        p2 = float(input("Gib die zweite Zahl ein: "))
        if p1 < p2:
            distance = p2 - p1
            print(f"Die Distanz beträgt ungefähr {round(distance, 2)}")
        elif p2 > p1:
            distance = p2 - p1
            print(f"Die Distanz beträgt ungefähr {round(distance, 2)}")
    elif status:
        p1 = float(input("Gib die erste Zahl ein: "))
        p2 = float(input("Gib die zweite Zahl ein: "))
        distance = abs(p1 - p2)
        print(f"Die Distanz beträgt ungefähr {round(distance, 2)}")
    schleife()

def schleife():
    q = input("Möchtest du das Programm wiederholen? (y/n): ").lower()
    if q == "y":
        distance_func()
    elif q == "n":
        exit()
    else:
        schleife()

### Ausgabe
distance_func(with_abs=True)