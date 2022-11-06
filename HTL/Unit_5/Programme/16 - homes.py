"""
author: Lukas Sanz
file: 16 - homes.py
catnr: 1BHIF-24
"""


### Bibliotheken
from turtle import *


### Funktion
def haus(seite, seite_dach, p1, p2):
    for count in range(2):
        fd(seite)  # länge
        rt(90)
        fd(seite - 30)  # breite
        rt(90)
    lt(45)
    fd(seite_dach)
    rt(90)
    fd(seite_dach)
    lt(45)
    pu()
    goto(p1, p2)
    pd()

### Voreinstellungen
pensize(5)
speed(10)
hideturtle()

### Ausgabe
haus(200, 141.5, 270, -50)
haus(150, 106, 470, -100)
haus(100, 70, 0, 0)
done()