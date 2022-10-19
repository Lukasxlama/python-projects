"""
author: Lukas Sanz
file: quadrate2.py
catnr: 1BHIF-24
"""


### Bibliotheken
from turtle import *


### Funktion
def quadrat(color_pen, color_fill, status):
    if not status:
        pencolor(color_pen)
        fillcolor(color_fill)
        begin_fill()
        lt(45)
        for i in range(4):
            fd(200)
            lt(90)
        end_fill()
    if status:
        pencolor(color_pen)
        fillcolor(color_fill)
        begin_fill()
        rt(105)
        lt(45)
        for i in range(4):
            fd(200)
            lt(90)
        end_fill()

### Voreinstellungen
hideturtle()
pensize(5)
speed(0)

### Ausgabe
quadrat("red", "cyan", False)
quadrat("green", "magenta", True)
quadrat("blue", "yellow", True)
quadrat("cyan", "red", True)
quadrat("green", "cyan", True)
quadrat("yellow", "blue", True)

### Startposition
home()

### Programm beenden
done()