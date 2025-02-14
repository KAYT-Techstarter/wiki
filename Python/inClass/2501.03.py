# Python-Programm zur Erstellung und Abfrage eines Wörterbuchs

def main():
    # Grundwörterbuch erstellen
    dictionary = {
        "haus": "house",
        "baum": "tree",
        "katze": "cat",
        "hund": "dog",
        "stuhl": "chair",
        "tisch": "table",
        "fenster": "window",
        "tür": "door",
        "buch": "book",
        "auto": "car"
    }

    print("Willkommen zum Wörterbuchprogramm!")

    while True:
        print("\nMenü:") # Lasse einen lücke zwischen Willkommen und Menü \n
        print("1. Wort übersetzen")
        print("2. Wörterbuch erweitern")
        print("3. Beenden")

        auswahl = input("\nWählen Sie eine Option (1/2/3): ")

        if auswahl == "1":  # Aufgabe 1 Nutzer abfrage für die Übesetzung
            wort = input("Geben Sie ein deutsches Wort ein, das übersetzt werden soll: ").lower()
            if wort in dictionary:
                print(f"Die englische Übersetzung von '{wort}' ist '{dictionary[wort]}'.")
            else:
                print(f"Das Wort '{wort}' ist nicht im Wörterbuch enthalten.")

        elif auswahl == "2": # Aufgabe 2 Erweiterung des Dictionarys
            print("Wörterbucherweiterung: Geben Sie 'exit' ein, um den Modus zu verlassen.")
            while True:
                deutsches_wort = input("Geben Sie ein deutsches Wort ein: ").lower()
                if deutsches_wort == "exit":
                    print("Erweiterungsmodus beendet.")
                    break
                englisches_wort = input("Geben Sie die englische Übersetzung ein: ").lower()
                dictionary[deutsches_wort] = englisches_wort
                print(f"Das Wortpaar '{deutsches_wort} : {englisches_wort}' wurde hinzugefügt.")

        elif auswahl == "3":
            break

        else:
            print("Ungültige Auswahl. Bitte wählen Sie erneut.")

if __name__ == "__main__":
    main()

# # Aufgabe: Wörterbuch erstellen und Abfragen

# ## Hauptaufgabe:

# 1. Erstelle ein Python-Programm, in dem die Teilnehmer ein Dictionary erstellen. Das Dictionary soll mindestens 10 deutsche Wörter mit ihren englischen Übersetzungen enthalten.
# 2. Danach soll das Programm den Benutzer per Eingabe (input) fragen, welches deutsche Wort ins Englische übersetzt werden soll.
#    Falls das Wort nicht im Dictionary ist, soll eine entsprechende Fehlermeldung angezeigt werden.

# ## Zusatzaufgabe:

# 1. Einheitliche Eingaben: Stelle sicher, dass die Eingaben unabhängig von der Groß- und Kleinschreibung erkannt werden (arbeite mit .lower()).
# 2. Erweiterung des Wörterbuchs: Implementiere eine Funktion, mit der Benutzer das Wörterbuch erweitern können:
#    Verwende eine while True-Schleife mit einer Abbruchbedingung (z. B. Eingabe von „exit“), um neue Übersetzungen hinzuzufügen.