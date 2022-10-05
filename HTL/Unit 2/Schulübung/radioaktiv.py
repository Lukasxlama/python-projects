"""
author: Lukas Sanz
file: radioaktiv.py
catnr: 1BHIF-24
"""


# Bibliotheken
from turtle import *


# Voreinstellungen
hideturtle()
speed(8)

# Position einnehmen
penup()
rt(180)
fd(200)
lt(90)
fd(230)
lt(90)
pendown()

# Quadrat Einstellungen
pensize(5)
pencolor("black")
fillcolor("yellow")

# Quadrat Zeichnen
begin_fill()
for count in range(0, 5, 1):
    fd(400)
    lt(90)
end_fill()

# Sektorpositionsfunktion
def home_position(degree):
    penup()
    home()
    lt(90)
    back(30)
    lt(degree)
    pendown()

# Sektorfunktion
def sector():
    fillcolor("black")
    begin_fill()
    forward(100)
    left(90)
    circle(100, 60)
    left(90)
    forward(100)
    left(120)
    end_fill()

# Kreissektoren zeichnen
home_position(25)
sector()
home_position(150)
sector()
home_position(270)
sector()
home_position(0)

# Kreisfunktion
def paint_circle():
    pencolor("yellow")
    pensize(3)
    fillcolor("black")
    begin_fill()
    circle(15)
    end_fill()

# Position einnehmen
penup()
rt(90)
fd(15)
lt(90)
pendown()

# Kreis zeichnen
paint_circle()

# Programm beenden
done()
