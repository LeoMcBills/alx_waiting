class Drone:

    number_of_drones = 0

    def __init__(self, model=None, function=None):
        self.model = model
        self.function = function
        Drone.number_of_drones += 1

    def __str__(self):
        print("This is gonna become the best and the biggest Drone company in Uganda, just think about that.")

    def manufacture(self):
        Drone.number_of_drones += 1

vh1 = Drone("DR-21", "Drug-delivery")
vh2 = Drone("DR-22", "Delivery of clothing")
vh4 = Drone()
vh1.manufacture()
vh3 = Drone("DR-23", "Delivery of food")

print(Drone.number_of_drones)
print()

print(vh1.function)