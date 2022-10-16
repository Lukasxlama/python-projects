"""
author: Lukas Sanz
file: 08 - salary3.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
monat_gehalt = int(input("Gib ein Anfangsgehalt ein (Integer): "))
erhoehung_pro_jahr = (monat_gehalt / 100) * 3

### Ausgabe
print(f"Anfangsgehalt: {monat_gehalt}")
print(f"Gehalt nach einem Jahr: {monat_gehalt + erhoehung_pro_jahr * 1}")
print(f"Gehalt nach zwei Jahr: {monat_gehalt + erhoehung_pro_jahr * 2}")
print(f"Gehalt nach drei Jahren: {monat_gehalt + erhoehung_pro_jahr * 3}")
print(f"Gehalt nach vier Jahren: {monat_gehalt + erhoehung_pro_jahr * 4}")
print(f"Gehalt nach fünf Jahren: {monat_gehalt + erhoehung_pro_jahr * 5}")
