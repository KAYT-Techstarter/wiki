a = 5
b = 10

print("Aufgabe 1 ________________________")
print(f"Output von a {a} < b {b} = ", (a < b))  # kleiner als
print(f"Output von a {a} > b {b} = ", (a > b))  # größer als
print(f"Output von a {a} == b {b} = ", (a == b))  # gleich
print(f"Output von a {a} != b {b} = ", (a != b))  # ungleich
print(f"Output von a {a} >= b {b} = ", (a >= b))  # größer oder gleich
print(f"Output von a {a} <= b {b} = ", (a <= b))  # kleiner oder gleich

print("Aufgabe 2 ________________________")
print(f"Output von (a < b) and (a != b) = ", ((a < b) and (a != b)))  # UND-Operator (beide Bedingungen müssen wahr sein)
print(f"Output von (a > b) or (a == 5) = ", ((a > b) or (a == 5)))    # ODER-Operator (mindestens eine Bedingung muss wahr sein)
print(f"Output von not(a == b) = ", (not (a == b)))                 # NICHT-Operator (kehrt den Wahrheitswert um)