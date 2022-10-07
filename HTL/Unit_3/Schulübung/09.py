"""
author: Lukas Sanz
file: 09.py
catnr: 1BHIF-24
"""


### Variablen und Rechnungen
weg = 500  # m
niedergetreten = 20 * 10**-2  # m
gesamte_flaeche = (weg * niedergetreten) * 2  #  = 200m²
erntbares_heu = 0.25  # pro m²
verlorengegangenes_heu = gesamte_flaeche * erntbares_heu
verlorengegangenes_heu = int(verlorengegangenes_heu)

### Ausgabe
print("Es sind insgesamt " + str(verlorengegangenes_heu) + "kg Heu durch das Niedertreten der Fußgänger verlorengegangen.")