"""
author: Lukas Sanz
file: regular_polygon2.py
catnr: 1BHIF-24
"""


from turtle import *
from random import randint


def regular_polygon1(length: float = 50, colors: tuple = ("red", "green", "blue"), corners: int = 3):
    angle_sum = ((corners - 2) * 180 / corners + 180) * (-1)
    pensize(5)
    speed(5)
    for count in range(corners):
        pencolor(colors[randint(0, 2)])
        fd(length)
        lt(angle_sum)
    pu()
    home()
    pd()
    done()


try:
    length_ = float(input("Gib die Länge der Seiten ein: "))
    corner = int(input("Gib ein, wieviele Ecken das Polygon haben soll: "))
    color1 = input(f"Gib die Farbe der ersten Seite ein: ")
    color2 = input(f"Gib die Farbe der zweiten Seite ein: ")
    color3 = input(f"Gib die Farbe der dritten Seite ein: ")
except ValueError as Error:
    exit(f"Ungültige Eingabe!\nFehlermeldung: {Error}")

try:
    regular_polygon1(length_, (color1, color2, color3), corner)
except BaseException as Error:
    exit(f"Fehler beim zeichnen!\nFehlermeldung: {Error}")