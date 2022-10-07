"""
author: Lukas Sanz
file: 02.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
semmeln = 2735  # Stück
netz = 24  # Stück pro Netz
benoetigte_netze = semmeln // netz
rest = semmeln % netz

### Ausgabe
print("Es werden " + str(benoetigte_netze) + " Netze benötigt und es bleiben " + str(rest) + " Semmeln übrig.")