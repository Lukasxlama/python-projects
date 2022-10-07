"""
author: Lukas Sanz
file: 19 - distance.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
t = float(input("Gib eine Zahl für die dauer des Falles in Sekunden ein: "))
g = 9.81  # m/s²
s = (g / 2) * t ** 2

### Ausgabe
print("Der fallende Gegenstand legt", round(s, 2), "m in", t, "Sekunde/n zurück.")
