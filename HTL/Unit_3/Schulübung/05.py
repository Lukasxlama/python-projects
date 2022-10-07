"""
author: Lukas Sanz
file: 05.py
catnr: 1BHIF-24
"""

### Variablen und Rechnungen
kuchenstuecke = 12
gaeste = 5
aufgeteilte_stuecke = kuchenstuecke // gaeste
rest = kuchenstuecke % gaeste

### Ausgabe
print("Jeder Gast bekommt " + str(aufgeteilte_stuecke) + " Stücke und es bleiben " + str(rest) + " Stücke übrig.")
