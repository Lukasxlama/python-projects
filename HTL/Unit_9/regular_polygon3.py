"""
author: Lukas Sanz
file: regular_polygon3.py
catnr: 1BHIF-24
"""


from turtle import *


def regular_polygon3(length, colors, colorindex_):
    pensize(4)
    winkel = 360 / (seitenanzahl_ := len(colors))

    for i2 in range(seitenanzahl_):
        pencolor(colors[colorindex_])
        fd(length)
        lt(winkel)
        colorindex_ += 1

    print("Schließe die Turtle, um das Programm zu beenden..")
    exitonclick()


### Start
colorindex=0
seitenlaenge = int(input("Gib eine Seitenlänge an: "))
seitenanzahl = int(input("Gib die Seitenanzahl an: "))
farben = []

for seite in range(seitenanzahl):
    farbe_r = int(input(f"Gib den ersten Farbwert der Seite {seite + 1} an: "))
    farbe_g = int(input(f"Gib den zweiten Farbwert der Seite {seite + 1} an: "))
    farbe_b = int(input(f"Gib den dritten Farbwert der Seite {seite + 1} an: "))
    farbtupel = (farbe_r, farbe_g, farbe_b)
    farben.append(farbtupel)

regular_polygon3(seitenlaenge, farben, colorindex)