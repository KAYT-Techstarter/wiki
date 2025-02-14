ageP1 = int(input("Gib Das alter der 1. Person an:"))
ageP2 = int(input("Gib Das alter der 2. Person an:"))
sum = ageP1 + ageP2

print(f"Der datentyp der variablen ageP1 und ageP2 ist : ageP1 = {type(ageP1)} & ageP2 {type(ageP2)}")

print(f"Das alter der 1. Person ist {int(ageP1)}")
print(f"Das alter der 2. Person ist {int(ageP2)}")

print(f"Das alter zusammen beträgt = {int(sum)} Jahre")


# Vorlage Tom Schiffmann
#
#  Elegante Lösung
# note_11 = input("Gib Zahl 1 ein:")  # string
# note_11_int = int(note_11)
# print(f"Der Typ von Zahl1 ist: {type(note_11)}")
# print(f"Der Typ von Zahl1 ist: {type(note_11_int)}")
# note_12 = input("Gib Zahl 2 ein:")
# print(f"Der Typ von Zahl 2 ist: {type(note_12)}")
# addition_zahl11_12 = note_11 + note_12
# print(f"Das Ergebnis ist {addition_zahl11_12}")
#
# """