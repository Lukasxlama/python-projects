"""
author: Lukas Sanz
file: 01 - quadrate3.py
catnr: 1BHIF-24
"""


### Bibliotheken
from turtle import *


### Funktion
def quadrat(color_pen, color_fill, degree, status):
    if not status:
        pencolor(color_pen)
        fillcolor(color_fill)
        begin_fill()
        lt(45)
        for i in range(4):
            fd(200)
            lt(degree)
        end_fill()
    if status:
        pencolor(color_pen)
        fillcolor(color_fill)
        begin_fill()
        rt(105)
        lt(45)
        for i in range(4):
            fd(200)
            lt(degree)
        end_fill()

### Voreinstellungen
hideturtle()
pensize(5)
speed(0)

### Ausgabe
quadrat("red", "cyan", 90, False)
quadrat("green", "magenta", 90, True)
quadrat("blue", "yellow", 90, True)
quadrat("cyan", "red", 90, True)
quadrat("green", "cyan", 90, True)
quadrat("yellow", "blue", 90, True)

### Startposition
home()

### Programm beenden
done()