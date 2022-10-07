"""
author: Lukas Sanz
file: 01.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
bier_liter = 780  # Liter
bier_faesser = 25  # Liter pro Fass
gefuellte_faesser = bier_liter // bier_faesser

### Ausgabe
print("Es können mit 780l Bier " + str(gefuellte_faesser) + " Fässer abgefüllt werden.")