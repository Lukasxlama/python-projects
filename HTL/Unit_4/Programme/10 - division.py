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
        print("ZeroDivisionError ---> Der Nenner ist 0!")
        division()
    else:
        print(f"({int(a)} * {int(b)}) / ({int(a)} - {int(b)}) = {int(rechnung)}")

### Ausgabe
division()