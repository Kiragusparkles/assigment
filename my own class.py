# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Encapsulation: Battery life is a private attribute
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life  # Private attribute

    # Getter method for battery_life
    def get_battery_life(self):
        return self.__battery_life

    # Setter method for battery_life
    def set_battery_life(self, new_battery_life):
        if 0 <= new_battery_life <= 100:
            self.__battery_life = new_battery_life
        else:
            print("Invalid battery life. It should be between 0 and 100.")

    # Method to make a call
    def make_call(self, phone_number):
        print(f"Dialing {phone_number}...")

    # Method to send a message
    def send_message(self, phone_number, message):
        print(f"Sending message to {phone_number}: {message}")


# Subclass: SmartphoneWithCamera (inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_resolution):
        # Initialize parent class (Smartphone) attributes
        super().__init__(brand, model, battery_life)
        self.camera_resolution = camera_resolution  # New attribute for camera resolution

    # Overriding make_call method (Polymorphism)
    def make_call(self, phone_number):
        print(f"Making a high-definition call to {phone_number} with enhanced audio!")

    # Method to take a picture
    def take_picture(self):
        print(f"Taking a photo with {self.camera_resolution} MP camera!")


# Create objects of both classes
smartphone1 = Smartphone("Samsung", "Galaxy S22", 85)
smartphone2 = SmartphoneWithCamera("Apple", "iPhone 14", 90, 48)

# Interact with the Smartphone object
print(f"{smartphone1.brand} {smartphone1.model}")
smartphone1.make_call("123-456-7890")
smartphone1.send_message("123-456-7890", "Hey, how are you?")
print(f"Battery life: {smartphone1.get_battery_life()}%")

# Interact with the SmartphoneWithCamera object
print(f"\n{smartphone2.brand} {smartphone2.model}")
smartphone2.make_call("987-654-3210")  # Demonstrates polymorphism
smartphone2.send_message("987-654-3210", "Let's catch up!")
smartphone2.take_picture()
print(f"Battery life: {smartphone2.get_battery_life()}%")
