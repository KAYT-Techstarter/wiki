# Implementiere einen Algorithmus, der als Git-Befehle Wörterbuch genutzt werden
# soll. Also zum Beispiel soll der Nutzer pull eingeben und dazu soll eine Beschreibung
# zu dem pull Befehl ausgegeben werden. Nutze dazu folgende Zeichnung als
# Orientierung.

def git_befehle_lexikon():

    git_befehle = {
        "pull": "Holt Änderungen von einem entfernten Repository und integriert sie in das lokale Repository.",
        "push": "Überträgt lokale Commits auf ein entferntes Repository.",
        "clone": "Erstellt eine Kopie eines entfernten Git-Repositories auf dem lokalen Rechner.",
        "commit": "Speichert Änderungen im lokalen Repository mit einer Nachricht.",
        "status": "Zeigt den aktuellen Status des Repositories an, einschließlich ungestagter Änderungen und nicht verfolgter Dateien.",
        "add": "Fügt Änderungen zur Staging-Area hinzu, sodass sie beim nächsten Commit berücksichtigt werden.",
        "checkout": "Wechselt zwischen Branches oder stellt eine bestimmte Version einer Datei wieder her.",
        "branch": "Zeigt eine Liste der lokalen Branches an oder erstellt einen neuen Branch.",
        "merge": "Fügt die Änderungen eines anderen Branches in den aktuellen Branch ein.",
        "log": "Zeigt die Historie der Commits im aktuellen Branch an.",
        "diff": "Zeigt die Unterschiede zwischen den Änderungen im Arbeitsverzeichnis und dem Staging-Bereich.",
    }

    print("Verfügbare Git-Befehle:")
    for befehl, beschreibung in git_befehle.items():
        print(f"- {befehl.capitalize()}")

    befehl = input("\nGib einen Git-Befehl ein (z. B. pull, push, commit): ").lower()

    if befehl in git_befehle:
        print(f"\n{befehl.capitalize()} Befehl: {git_befehle[befehl]}")
    else:
        print("\nBefehl nicht gefunden. Bitte gib einen gültigen Git-Befehl ein.")

git_befehle_lexikon()
