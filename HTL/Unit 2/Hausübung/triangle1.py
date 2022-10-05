"""
author: Lukas Sanz
file: triangle1.py
catnr: 1BHIF-24
"""


from turtle import *


# Turtle Einstellungen
hideturtle()
pensize(5)
speed(5)

# Position einnehmen
penup()
fd(150)
lt(90)
fd(115)
rt(90)
pendown()

# Triangel zeichnen
for triangle in range(0, 3, 1):
    rt(120)
    fd(300)

# Programm beenden
done()