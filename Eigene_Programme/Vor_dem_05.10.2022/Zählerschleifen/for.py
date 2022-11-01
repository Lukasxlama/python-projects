number_1 = (input("Gib die Zahl ein, bei der die Zählung gestartet werden soll: "))
number_2 = (input("Gib die Zahl ein, bei der die Zählung beendet werden soll: "))
number_3 = (input("Gib an, in welchen Schritten gezählt werden soll (z.B. 2, 4, 6, 8, usw.): "))

print("Gut, soll ich die Zahlen " + number_1 + " " "bis " + number_2 + " " + "ausgeben? Es wird in " + number_3 + "er Schritten gezählt.")
yo = (input("Ja/Nein: "))

if yo == "Ja" or "ja" or "JA":
    print("Passt, ich starte die Zählung.")
    for counter in range(int(number_1), int(number_2), int(number_3)):
        print(counter)

elif yo == "Nein" or "nein" or "NEIN":
    print("Soll ich die Zahlen ändern?")
    yo_2 = input("Ja/Nein: ")
    if yo_2 == "Ja" or "ja":
        number_1 = (input("Gib die Zahl ein, bei der die Zählung gestartet werden soll: "))
        number_2 = (input("Gib die Zahl ein, bei der die Zählung beendet werden soll: "))
        number_3 = (input("Gib an, in welchen Schritten gezählt werden soll (z.B. 2, 4, 6, 8, usw.): "))
        print("Passt, ich starte die Zählung.")
        for counter in range(int(number_1), int(number_2), int(number_3)):
            print(counter)
    else:
        print("Gut, bis Bald")