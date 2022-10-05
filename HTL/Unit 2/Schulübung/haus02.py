"""
author: Lukas Sanz
file: haus02.py
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
fillcolor("red")
pencolor("black")
pensize(4)
begin_fill()
lt(120)
fd(200)
lt(120)
fd(200)
lt(120)
fd(200)
end_fill()

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

### Tür Position einnehmen
penup()
home()
rt(90)
fd(110)
rt(90)
fd(40)
rt(90)
pendown()

### Tür zeichnen
pencolor("black")
pensize(4)
fillcolor("brown")
begin_fill()
fd(80)
lt(90)
fd(55)
lt(90)
fd(80)
end_fill()

### Fenster Position einnehmen
penup()
rt(90)
fd(35)
rt(90)
fd(25)
pendown()

### Fenster zeichnen
pensize(3)
fillcolor("yellow")
begin_fill()
fd(40)
lt(90)
fd(40)
lt(90)
fd(40)
lt(90)
fd(40)
lt(90)
end_fill()

### Programm beenden
done()