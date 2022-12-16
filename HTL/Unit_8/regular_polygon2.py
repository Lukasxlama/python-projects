"""
author: Lukas Sanz
file: regular_polygon2.py
catnr: 1BHIF-24
"""


from turtle import *


def regular_polygon1(length, colors, corners):
    speed(0)
    pensize(3)
    pencolor(colors[0])

    for i in range(corners):
        pencolor(colors[i % len(colors)])
        fd(length)
        lt(360 / corners)
    done()


try:
    length_ = int(input("Gib die Länge der Seiten ein: "))
    corners_ = int(input("Gib die Anzahl der Seiten ein: "))
    color1 = input(f"Gib die Farbe der ersten Seite ein: ")
    color2 = input(f"Gib die Farbe der zweiten Seite ein: ")
    color3 = input(f"Gib die Farbe der dritten Seite ein: ")
except ValueError as Error:
    exit(f"Ungültige Eingabe!\nFehlermeldung: {Error}")

try:
    regular_polygon1(length_, (color1, color2, color3), corners_)
except BaseException as Error:
    exit(f"Fehler beim zeichnen!\nFehlermeldung: {Error}")