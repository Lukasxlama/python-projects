"""
author: Lukas Sanz
file: geomlib.py
catnr: 1BHIF-24
"""


### Bibliotheken
from math import sqrt
from turtle import fd, lt, pu, pd, goto, home, done


### Funktionen
def distance1(x1: float, x2: float):
    distance = round(abs(x1 - x2), 2)
    return distance

def distance2(x1: float, x2: float, y1: float, y2: float):
    distance = round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    return distance

def distance3(x1: float, x2: float, y1: float, y2: float, z1: float, z2: float):
    distance = round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 + z1) ** 2), 2)
    return distance

def regular_polygon(x_start, y_start, corners, length):
    angle_sum = 180 - (360 / corners)
    pu()
    lt(180)
    goto(x_start, y_start)
    pd()
    for count in range(corners):
        fd(length)
        lt(angle_sum)
    pu()
    home()
    lt(0)
    pd()
    done()
    perimeter = round(corners * length, 2)
    return perimeter

def sum(num1: float = 0, num2: float = 0, num3: float = 0, num4: float = 0, num5: float = 0,):
    sum_return = num1 + num2 + num3 + num4 + num5
    return sum_return

def polygon(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float = None, y4: float = None, x5: float = None, y5: float = None):
    pu()
    goto(x1, y1)
    pd()
    goto(x2, y2)
    goto(x3, y3)
    if x4 is not None and y4 is not None:
        goto(x4, y4)
        U = round(distance2(x1, x2, y1, y2) + distance2(x2, x3, y2, y3) + distance2(x3, x4, y3, y4) + distance2(x4, x1, y4, y1), 2)
        if x5 is not None and y5 is not None:
            goto(x5, y5)
            U = round(distance2(x1, x2, y1, y2) + distance2(x2, x3, y2, y3) + distance2(x3, x4, y3, y4) + distance2(x4, x5, y4, y5) + distance2(x5, x1, y5, y1), 2)
    goto(x1, y1)
    if x4 is None and y4 is None and x5 is None and y5 is None:
        U = round(distance2(x1, x2, y1, y2) + distance2(x2, x3, y2, y3) + distance2(x3, x1, y3, y1), 2)
    done()
    return U

def stars_triangle(number: int):
    for count in range(number):
        print("*" * (count + 1))