class Vehicles:
    def __init__(
        self, vehicle_brand_name, vehicle_model_name, average_consumption_in_l, tank_volume
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l 
        self.km_driven = 0  
        self.volume = tank_volume  

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven += km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100
        return cons_in_l_per_km * self.km_driven
    
    def get_total_tank_volume(self):
        return (self.volume / self.consumption) * 100

my_vehicle = Vehicles("VW", "Golf 1", 4.5, 55)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)

print(f"Der gesamte Verbrauch liegt bei: {my_vehicle.get_total_consumption()} Litern")
print(f"Die Reichweite pro Tankfüllung beträgt: {my_vehicle.get_total_tank_volume()} km")



