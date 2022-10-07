"""
author: Lukas Sanz
file: 04.py
catnr: 1BHIF-24
"""


### Variablen
geschwindigkeit = 50  # km/h
beschleunigung = -2 * 3.6  # = -7.2 km/h
sekunden = 0
strecke = 0

### Rechnung
while geschwindigkeit > 0:
    geschwindigkeit += beschleunigung
    sekunden += 1
    strecke = sekunden * 2

### Ausgabe
print("Das Auto benötigt ungefähr " + str(sekunden) + " Sekunden, um bei einer Strecke von " + str(strecke) + "m zum Stillstand zu kommen.")