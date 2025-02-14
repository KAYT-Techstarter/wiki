class Pet:
    def __init__(self, name, species, age, favorite_food):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy_level = 100

    def get_description(self):
        return f"{self.name} is a {self.age} years old {self.species}."

    def play(self, duration):
        energy_loss = duration * 5
        self.energy_level = max(self.energy_level - energy_loss, 0) # max sorg dafür das der wert nicht unter 0 Fallen kann 
        return f"{self.name} played for {duration} minutes. The energy level is now: {self.energy_level}."

    def feed(self, food):
        if food == self.favorite_food:
            self.energy_level = min(self.energy_level + 30 ,100) # min begrenzt das maximus mit der der 100 ,dass das energy level nicht mehr als 100 sein kann
            return f"{self.name}'s favorite food is {food}! The energy level quickly increased to: {self.energy_level} of 100."
        else:
            self.energy_level = min(self.energy_level + 10, 100)
            return f"{self.name} doesn't like {food} that much, so the energy level increased slowly to: {self.energy_level} of 100."

my_pet = Pet("Scrumble", "Chinchilla", 1.5, "Chocolate")

print(my_pet.get_description())
print(my_pet.play(15))
print(my_pet.feed("Chocolate"))
print(my_pet.feed("Carrot"))
print(my_pet.feed("Chocolate"))
print(my_pet.feed("Chocolate"))
print(my_pet.play(35))
print(my_pet.feed("Carrot"))
