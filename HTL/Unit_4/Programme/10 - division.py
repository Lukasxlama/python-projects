"""
author: Lukas Sanz
file: 10 - division.py
catnr: 1BHIF-24
"""


### Funktion
def division():
    a = float(input("Gib eine Zahl für a ein: "))
    b = float(input("Gib eine Zahl für b ein: "))
    try:
        rechnung = (a * b) / (a - b)
    except ZeroDivisionError:
        print(f"ZeroDivisionError ---> Der Nenner ergibt 0:\n{a} - {b} = 0")
        division()
    else:
        print(f"({a} * {b}) / ({a} - {b}) ≈ {round(rechnung)}")
    schleife()

def schleife():
    q = input("Möchtest du das Programm wiederholen? (y/n): ").lower()
    if q == "y":
        division()
    elif q == "n":
        exit()
    else:
        schleife()
### Ausgabe
division()