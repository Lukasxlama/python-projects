"""
author: Lukas Sanz
file: triangle2.py
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
rt(180)
fd(400)
rt(90)
pendown()

# Triangel zeichnen
fd(500)  # Hypotenuse
hypotenuse = 500
rt(120)
fd(300)  # Kathete 1
kathete_1 = 300
rt(96.5)
fd(435)  # Kathete 2
kathete_2 = 435

# Rechnungen
print("1 cm = 100 px")
print("Hypotenuse =", hypotenuse, "px = 5 cm")
print("Kathete 1 =", kathete_1, "px = 3 cm")
print("Kathete 2 =", kathete_2, "px = 4,35 cm")
print("A =", kathete_1 * kathete_2 / 2, "px = 6,525 cm²")
print("U =", hypotenuse + kathete_1 + kathete_2, "px = 1,235 cm")

# Programm beenden
done()
