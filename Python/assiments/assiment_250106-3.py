# Erstelle ein Muster mit einer verschachtelten Schleife. Beispiel:
# Der Benutzer gibt die Anzahl der Zeilen ein, und das Programm gibt folgendes Muster aus:
# Beispiel:
# Eingabe: 5
# Ausgabe:
# *
# **
# ***
# ****
# *****

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
