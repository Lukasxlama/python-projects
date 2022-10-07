"""
author: Lukas Sanz
file: quadrate (02).py
catnr: 1BHIF-24
"""


### Bibliotheken
from turtle import *


### Voreinstellungen
pensize(8)
speed(3)

### Variablen
s = float(input("Welche Seitenlänge sollen die Quadrate haben?: "))

### Zeichnen 1
for x in range(0, 4, 1):
    fd(s)
    rt(90)

### Position einnehmen 1
pu()
fd(10)
rt(90)
fd(10)
pd()

### Zeichnen 2
for x in range(0, 4, 1):
    fd(s - 20)
    lt(90)

### Position einnehmen 2

pu()
fd(10)
lt(90)
fd(10)
pd()

### Zeichnen 3
for x in range(0, 4, 1):
    fd(s - 40)
    rt(90)
