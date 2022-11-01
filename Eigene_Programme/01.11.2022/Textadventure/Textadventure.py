# Bibliotheken
from random import uniform


# Wichtige Variablen
j_n = ["ja", "nein"]
nosw = ["links", "rechts", "vor", "zurück"]
name = input("Wie lautet dein Name, tapferer Recke? --> ")

# Einleitung
print(f"\nSei gegrüßt, {name}. Dein Abenteuer startet jetzt!")
print(f"Du befindest dich am rande eines düsteren Waldes, auf der suche nach einem mysteriösen Zauberstab.")
print("Kannst du ihn durchqueren und den Stab finden?")

# Beginn
antwort = ""
while antwort not in j_n:
    antwort = input("Möchtest du den Wald betreten? [Ja|Nein] --> ").lower()
if antwort == "ja":
    print("\nDu betrittst den Wald.")
elif antwort == "nein":  # TODO
    print(f"\nDu bist wohl noch nicht bereit, {name}.\nLebe wohl!")
    input("Drücke ENTER, um das Programm zu beenden.")
    exit("Aufgegeben")

else:
    print("Tut mir leid, das habe ich nicht verstanden!\n")

# Entscheidung
antwort = ""
while antwort not in nosw:
    print("\nLinks lauert ein hungriger Wolf.")
    print("Rechts geht es tiefer in den Wald hinein.")
    print("Vor dir befindet sich eine hohe Felswand.")
    print("Hinter dir befindet sich der Ausgang.")
    antwort = input("In welche Richtung gehst du? [Links|Rechts|Vor|Zurück] --> ").lower()

# Entscheidung | Linker Weg
if antwort == "links":
    antwort = input("\nDu willst also den Wolf bezwingen?\nDie Chance auf einen Sieg liegt nur bei 40%!\nBist du dir sicher? [Ja|Nein] --> ").lower()
    if antwort == "ja":
        chance = uniform(0, 1)  # Zufallszahlen zwischen 0 und 1
        if chance <= 0.6:
            print(f"\nDer Wolf hat dich gefressen.")
            input("Drücke ENTER, um das Programm zu beenden.")
            exit(f"Du bist gestorben, {name}!")
        else:
            print(f"\nDu hast den Wolf bezwungen und den Stab gefunden!")
            input("Drücke ENTER, um das Programm zu beenden.")
            exit(f"Du hast gewonnen, {name}!")
    elif antwort == "nein":
        print("\nDie Flucht ist gescheitert.")
        input("Drücke ENTER, um das Programm zu beenden.")
        exit(f"Du bist gestorben, {name}!")

# Entscheidung | Rechter Weg
elif antwort == "rechts":
    print("\nDu hast dich im dunklen Nebel verlaufen und findest dort deinen Tod.")
    input("Drücke ENTER, um das Programm zu beenden.")
    exit(f"Du bist gestorben, {name}!")

# Entscheidung | Nach vorne gehen
elif antwort == "vor":
    while antwort not in j_n:
        antwort = input("\nMöchtest du die hohe Felswand erklimmen?\nDie Chance, dass du abrutscht liegt bei 40%!\n[Ja|Nein] --> ").lower()
        if antwort == "ja":
            chance = uniform(0, 1)
            if chance <= 0.4:
                print("\nDu bist abgerutscht und hinuntergefallen.")
                input("Drücke ENTER, um das Programm zu beenden.")
                exit(f"Du bist gestorben, {name}!")
            else:
                print("\nDu hast die Felswand erfolgreich erklommen und den Stab gefunden.")
                input("Drücke ENTER, um das Programm zu beenden.")
                exit(f"Du hast gewonnen, {name}!")
        elif antwort == "nein":
            print(f"\nOk, {name}")
            input("Drücke ENTER, um das Programm zu beenden.")
            exit("Aufgegeben")

# Entscheidung | Nach hinten gehen
elif antwort == "zurück":
    print("\nDu hast den Wald verlassen.")
    input("Drücke ENTER, um das Programm zu beenden.")
    exit("Aufgegeben")