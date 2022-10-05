"""
author: Lukas Sanz
file: olympic_rings.py
catnr: 1BHIF-24
"""


### Bibliotheken
from turtle import *


### Voreinstellungen
speed(0)
hideturtle()
pensize(5)

### Schwarzer Ring
pencolor("black")
circle(80)

### Blauer Ring
pu()
fd(-200)
pd()
pencolor("blue")
circle(80)

### Roter Ring
pu()
fd(400)
pd()
pencolor("red")
circle(80)

### Gelber Ring
pu()
goto(-100, -100)
pd()
pencolor("yellow")
circle(80)

### Grüner Ring
pu()
goto(100, -100)
pd()
pencolor("green")
circle(80)

### Programm beenden
done()