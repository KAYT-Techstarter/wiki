# Aufgaben für den Nachmittag: Python-Code in Arbeitsschritte beschreiben

**Abgabe**: Text ()

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf.

### Antwort 

1. Fordere den Benutzer auf, eine Zahl einzugeben.

2. Wandle die Benutzereingabe von einem String in eine ganze Zahl um.

3. Prüfe, ob die eingegebene Zahl größer als 10 ist.

   Wenn ja, gib „Die Zahl ist größer als 10.“ aus.

   Wenn nein, gib „Die Zahl ist 10 oder kleiner.“ aus.

---

## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf.

### Antwort 

1. Erstelle eine Liste von Zahlen.

2. Gebe die Erste Zahl der Liste aus. (0)

3. gebe die Letzte Zahl aus der Liste aus (-1)

**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.

### Antwort Zusatzaufgabe

```python
wochentag = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
print("Die erste Wochentag ist:", wochentage[0])
print("Die letzte Wochentag ist:", wochentage[-1])
```

1. Erstelle eine Liste von Wochentagen.

2. Gebe den ersten Wochentag der Liste aus. (0)

3. gebe den Letzten Wochentag aus der Liste aus (-1)

---

## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf.

### Antwort

1. Fordere den Benutzer auf, eine Zahl einzugeben.

2. Wandle die Benutzereingabe von einem String in eine ganze Zahl um.

3. Prüfe ist die Zahl Positiv (Großer als 0)

4. Prüfe ist die Zahl Negativ (Kleiner als 0)

5. Wenn nichts zutrifft soll ausgeben werden das die Zahl 0 ist.

---

## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf.

### Antwort

1. Definiere einen Funktion ist-gerade 

2. Teile die Zahl durch 2 und prüfe ob ein Rest bleibt.

3. Definiere einen Benutzer eingabe für eine Zahl.

4. Rufe die Funktion ist_gerade auf und egbe die Zahl mit.

5. Wenn die Zahl gerade ist gebe "Die Zahl ist gerade." aus.

6. Wenn die Zahl ungerade ist gebe "Die Zahl ist ungerade." aus.

---

## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.

### Antwort

1. Frage den Nutzer nach den Namen

2. Frage den Nutzer nach den Alter

3. Gebe den Nutzer seinen Namen und das alter aus in 10 Jahren
   Als satz "Hallo ***Nutzername***, in 10 Jahren wirst du ***Alter + 10*** Jahre alt sein!"

---

Diese Aufgaben sind auf den bisherigen Stand der Vorlesung abgestimmt und bieten eine gute Balance zwischen Verständnis und Anwendung. Punkte sind proportional zur Komplexität der Aufgabe verteilt.