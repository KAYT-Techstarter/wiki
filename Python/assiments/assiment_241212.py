print("Augabe 1 ________Namensabfrage mit Input__________")

firstName = input("Gebe deinen Vornamen an :")
famalyName = input("Gebe deinen Familen Namen an :")

print(f"Dein voller name Lautet {firstName} {famalyName}.")

print("Augabe 2 ________Addition von Zahlen______________")

zahl1 = int(input("gebe die 1. Zahl Zummenrechnen an : "))
zahl2 = int(input("gebe die 2. Zahl Zummenrechnen an : "))
sum = zahl1 + zahl2 

print(f"Die Summer vom {int(zahl1)} + {int(zahl2)} = {int(sum)}")

print("Augabe 3 ________Einfache If-Bedingung____________")

negativquestion = int(input("gebe eine zahl an die überprüft werden soll ob sie negativ ist ="))

if negativquestion > 0:
  print("Die angebene zahl ist nicht negativ :)")
elif negativquestion == 0:
  print("Die zahl ist 0 :|")
else :
  print("Die angebene zahl ist negativ :(")