"""
author: Lukas Sanz
file: 7 - calculate.py
catnr: 1BHIF-24
"""


### Funktion
def sqrt(x0):
    x1 = (x0 + x0 / x0) / 2
    x2 = (x1 + x0 / x1) / 2
    x3 = (x2 + x0 / x2) / 2
    print(f"Radikant = {radikant}\nWurzelexponent = 2\nWurzelwert (Näherung) ≈ {round(x3, 2)}")

### Variable
radikant = float(input("Gib eine Zahl für den Radikant ein: "))

### Ausgabe
sqrt(radikant)