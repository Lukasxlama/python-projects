"""
author: Lukas Sanz
file: arithmean.py
catnr: 1BHIF-24
"""


def mittelwert_berechnen(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    mittelwert = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10) / 10
    return mittelwert


try:
    zahl1 = float(input("Gib die erste Zahl ein: "))
    zahl2 = float(input("Gib die zweite Zahl ein: "))
    zahl3 = float(input("Gib die dritte Zahl ein: "))
    zahl4 = float(input("Gib die vierte Zahl ein: "))
    zahl5 = float(input("Gib die fünfte Zahl ein: "))
    zahl6 = float(input("Gib die sechste Zahl ein: "))
    zahl7 = float(input("Gib die siebte Zahl ein: "))
    zahl8 = float(input("Gib die achte Zahl ein: "))
    zahl9 = float(input("Gib die neunte Zahl ein: "))
    zahl10 = float(input("Gib die zehnte Zahl ein: "))
    ergebnis = mittelwert_berechnen(zahl1, zahl2, zahl3, zahl4, zahl5, zahl6, zahl7, zahl8, zahl9, zahl10)
    print(f"Der Mittelwert ist: {ergebnis}")
except BaseException as Error:
    exit(f"Ungültige Eingabe!\nFehlermeldung: {Error}")
