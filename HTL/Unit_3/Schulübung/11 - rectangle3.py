"""
author: Lukas Sanz
file: 11 - rectangle3.py
catnr: 1BHIF-24
"""


a = input("Gib die Seitenlänge a ein: ")
b = input("Gib die Seitenlänge b ein: ")
x = input("Gib ein Längenmaß ein (z.B. cm, m): ")
U = float(a) * 2 + float(b) * 2
A = float(a) * float(b)
print("Der Umfang des Quadrats beträgt " + str(U) + str(x) + " und die Fläche " + str(A) + str(x) + "².")
