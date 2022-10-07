"""
author: Lukas Sanz
file: 12 - rectangle4.py
catnr: 1BHIF-24
"""


U = float(input("Gib den Umfang des Rechtecks ein: "))
a = float(input("Gib die Seite a des Rechtecks ein: "))
x = str(input("Gib ein Längenmaß ein (z.B. cm, m): "))
b = (U - 2 * a) / 2
A = a * b
print("Die Seite b ist " + str(b) + " " + x + " lang und die Fläche beträgt " + str(A) + " " + x + "².")
