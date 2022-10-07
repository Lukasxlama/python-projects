"""
author: Lukas Sanz
file: kmh2ms.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
ges_km_h = float(input("Bitte die Geschwindigkeit in km/h eingeben: "))
ges_m_s = ges_km_h / 3.6

### Ausgabe
print(str(ges_km_h) + "km/h = " + str(ges_m_s))
