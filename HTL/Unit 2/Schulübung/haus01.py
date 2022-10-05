"""
author: Lukas Sanz
file: haus01.py
catnr: 1BHIF-24
"""

### Bibliotheken
from turtle import *

### Voreinstellungen
reset()
pensize(5)
speed(5)
hideturtle()
pencolor("red")

### Dach zeichnen
lt(120)
fd(200)
lt(120)
fd(200)
lt(120)
fd(200)

### Positon für Wände
back(20)
rt(90)

### Wände Voreinstellungen
pensize(3)
pencolor("black")

### Wände zeichnen
fd(110)
rt(90)
fd(160)
rt(90)
fd(110)
rt(90)