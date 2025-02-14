class Zutat:
    def __init__(self, name, kalorien_pro_100g, zubereitungszeit):
        self.name = name
        self.kalorien_pro_100g = kalorien_pro_100g
        self.zubereitungszeit = zubereitungszeit

class Zutatenliste:
    def __init__(self):
        self.zutatenliste = {}

    def zutat_hinzufügen(self, zutat, menge):
        self.zutatenliste[zutat] = menge

    def kalorien(self):
        total_kalorien = 0
        for zutat in self.zutatenliste:
            total_kalorien += zutat.kalorien_pro_100g  
        print(f"Gesamtkalorien: {total_kalorien} kcal")

    def kochzeit(self):
        max_kochzeit = 0
        for zutat in self.zutatenliste:
            if zutat.zubereitungszeit > max_kochzeit:
                max_kochzeit = zutat.zubereitungszeit
        print(f"Maximale Kochzeit: {max_kochzeit} Minuten")

class Rezept(Zutatenliste):
    def __init__(self, name, beschreibung):
        super().__init__()
        self.name = name
        self.beschreibung = beschreibung

    def rezept_anzeigen(self):
        print(f"Rezept: {self.name}")
        print("Zutaten:")
        for zutat, menge in self.zutatenliste.items():
            print(f"- {zutat.name}: {menge}")
        print(f"Beschreibung: {self.beschreibung}")


def test():
    z1 = Zutat("Tomate", 18, 5)
    z2 = Zutat("Zwiebel", 40, 3)
    z3 = Zutat("Knoblauch", 150, 2)

    rezept = Rezept("Tomatensauce", "Eine leckere Sauce für Pasta.")
    rezept.zutat_hinzufügen(z1, "200g")
    rezept.zutat_hinzufügen(z2, "100g")
    rezept.zutat_hinzufügen(z3, "1 Prise")

    rezept.rezept_anzeigen()
    rezept.kalorien()
    rezept.kochzeit()

test()
