class Fahrzeug:
    def __init__(self, name, motor, restreichweite, kilometerzahl):
        self.name = name
        self.motor = motor
        self.restreichweite = restreichweite
        self.kilometerzahl = kilometerzahl

    def fahren(self, gefahrene_kilometer):
        self.kilometerzahl += gefahrene_kilometer
        self.restreichweite -= gefahrene_kilometer
        print(f"{gefahrene_kilometer} Kilometer gefahren. Neue Kilometerzahl: {self.kilometerzahl}, Restreichweite: {self.restreichweite}")

    def tanken(self, hinzugefügte_reichweite):
        alte_reichweite = self.restreichweite
        self.restreichweite += hinzugefügte_reichweite
        prozentsteigerung = (hinzugefügte_reichweite / alte_reichweite) * 100 if alte_reichweite > 0 else 0
        print(f"{hinzugefügte_reichweite} Reichweite hinzugefügt. Neue Restreichweite: {self.restreichweite}")
        print(f"Die Reichweite des {self.name} ist um {prozentsteigerung:.2f}% gestiegen beim erhöhen der reichweite.")

#Fahrzeuge 
auto1 = Fahrzeug("BMW", "Verbrenner", 500, 200)
auto2 = Fahrzeug("Tesla", "Elektro", 300, 150)

print("______________________________________________")
auto1.fahren(125)
auto1.tanken(100)
print("______________________________________________")
auto2.fahren(50)
auto2.tanken(100)
print("______________________________________________")

