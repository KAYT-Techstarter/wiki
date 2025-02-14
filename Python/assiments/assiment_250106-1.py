# Schreibe ein Programm, das die Häufigkeit eines Buchstabens in einem Text zählt.
# 1. Der Benutzer gibt einen Text und einen Buchstaben ein.
# 2. Dein Programm zählt mit einer Schleife, wie oft dieser Buchstabe im Text vorkommt.

def count_letter_occurrences(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

text = input("Enter a text: ")
letter = input("Enter a letter to count its occurrences: ")

occurrences = count_letter_occurrences(text, letter)

print(f"The letter '{letter}' appears {occurrences} times in the text.")
