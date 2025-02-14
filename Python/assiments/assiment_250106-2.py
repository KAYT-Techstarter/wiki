# Schreibe ein Programm, das:
# 1. Den Benutzer auffordert, 5 Zahlen einzugeben.
# 2. Mit einer Schleife die Summe und den Durchschnitt der Zahlen berechnet.
# 3. Die Ergebnisse ausgibt.

input_numbers = input("Enter 5 numbers separated by commas: ")
numbers = [float(number.strip()) for number in input_numbers.split(",")]

total_sum = sum(numbers)
average = total_sum / len(numbers)

print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")

