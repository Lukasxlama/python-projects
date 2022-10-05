"""
author: Lukas Sanz
file: wabe01.py
catnr: 1BHIF-24
"""

# Bibliotheken | library's
from turtle import *

# Seitenlänge der Waben | Side length of the honeycombs
s = 60

# Zähler, wie viel Seiten gezeichnet wurden | Counter how many sides were drawn
side_counter = 1

# Drehungsmultiplikation | Rotation multiplication
rm = 2

# Turtle Einstellungen | turtle settings
pencolor("brown")
shape("turtle")
pensize(2)
speed(5)

# Funktion: Sechseck malen | function: paint hexagon
def draw_hex(color, side_length):
    side_counter = 1
    fillcolor(color)
    begin_fill()
    while side_counter <= 6:
        fd(side_length)
        rt(side_length)
        side_counter += 1
    end_fill()

# "draw_hex" Funktion starten + Parameter übergeben | Start "draw_hex" function + pass parameters
draw_hex('yellow', s)

# Wie viele Sechsecke gemacht werden sollen | how many orange hex should be made
while side_counter <= 6:
    rt(s * rm)
    if rm == 1:
        rt(s)
        fd(s)
        lt(s)
        rm == 2
    draw_hex('orange', s)
    side_counter += 1  # Fügt 1 zu Made Hex hinzu | add 1 to made hex
    if side_counter == 3:
        rt(s * 2)
        fd(s)
        lt(s)
        draw_hex('orange', s)
        side_counter += 1
        rm = 1

# Zurück in die Ausgangsposition | back to the starting position
penup()
fd(s - s * 2)
pendown()

# Turtle beenden | close turtle
done()
