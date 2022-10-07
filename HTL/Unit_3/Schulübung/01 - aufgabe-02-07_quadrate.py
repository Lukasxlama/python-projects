"""
author: Lukas Sanz
file: aufgabe-02-07_quadrate (01).py
catnr: 1BHIF-24
"""


### Bibliotheken
from turtle import *


### Einstellungen vor dem Zeichnen
reset()
pensize(5)
speed(10)
degree = 105

### Quadrat 1 zeichnen
pencolor("red")
fillcolor("cyan")
begin_fill()
lt(45)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
end_fill()

### Quadrat 2 zeichnen
pencolor("green")
fillcolor("magenta")
begin_fill()
rt(degree)
lt(45)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
end_fill()

### Quadrat 3 zeichnen
pencolor("blue")
fillcolor("yellow")
begin_fill()
rt(degree)
lt(45)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
end_fill()

### Quadrat 4 zeichnen
pencolor("cyan")
fillcolor("red")
begin_fill()
rt(degree)
lt(45)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
end_fill()

### Quadrat 5 zeichnen
pencolor("green")
fillcolor("cyan")
begin_fill()
rt(degree)
lt(45)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
end_fill()

### Quadrat 6 zeichnen
pencolor("yellow")
fillcolor("blue")
begin_fill()
rt(degree)
lt(45)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
fd(200)
lt(90)
end_fill()

### Startposition
home()
