"""
author: Lukas Sanz
file: 08.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
kosten = 420  #€
a = 24  # Personen
a_ergebnis = kosten / a
b = 27  # Personen
b_ergebnis = kosten / b
c = 36  # Personen
c_ergebnis = kosten / c

### Ausgabe
print("Bei 24 Personen und 420€ Autobuskosten muss jede Person mindestens " + str(round(a_ergebnis, 2)) + "0€ zahlen.")
print("Bei 27 Personen und 420€ Autobuskosten muss jede Person mindestens " + str(round(b_ergebnis, 2)) + "€ zahlen.")
print("Bei 36 Personen und 420€ Autobuskosten muss jede Person mindestens " + str(round(c_ergebnis, 2)) + "€ zahlen.")