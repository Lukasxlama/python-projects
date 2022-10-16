"""
author: Lukas Sanz
file: wabe2.py
catnr: 1BHIF-24
"""


from turtle import *


### Einstellungen
hideturtle()
pencolor("brown")
pensize(5)
speed(0)

### Position 1
def position_1(x, y):
    pu()
    fd(x)
    lt(y)
    pd()

### Position 2
def position_2(y):
    pu()
    rt(y)
    pd()

### Funktion
def hexagon(color_fill, status):
    fillcolor(color_fill)
    begin_fill()
    fd(60)
    if not status:
        lt(60)
    elif status:
        rt(60)
    fd(60)
    lt(60)
    fd(60)
    lt(60)
    fd(60)
    lt(60)
    fd(60)
    lt(60)
    fd(60)
    if status:
        lt(60)
        fd(60)
    end_fill()

### Ausgabe
position_1(60, 120)
hexagon("yellow", False)
for i in range(2):
    position_2(60)
    hexagon("orange", False)
for i in range(4):
    position_2(-60)
    hexagon("orange", True)

### Zum Anfang
pu()
home()
pd()

### Programm beenden
done()