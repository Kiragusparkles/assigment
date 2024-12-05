# Base class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name  # Adding a name attribute to each vehicle
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print(f"The {self.name} is driving 🚗.")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print(f"The {self.name} is flying ✈️.")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print(f"The {self.name} is sailing ⛵.")

# Function to demonstrate polymorphism
def demonstrate_move(vehicle):
    vehicle.move()

# Creating instances of each class with specific names
car = Car("Toyota")
plane = Plane("Boeing 747")
boat = Boat("Yacht")

# Demonstrating polymorphism with the name and movement behavior
print("Vehicle Actions:")
demonstrate_move(car)   # Calls Car.move()
demonstrate_move(plane) # Calls Plane.move()
demonstrate_move(boat)  # Calls Boat.move()
