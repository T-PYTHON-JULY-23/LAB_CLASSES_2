class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number):
        self._brand = brand
        self._name = name
        self._color = color
        self._capacity = capacity
        self._plate_number = plate_number

    # Getters
    def get_brand(self):
        return self._brand

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_capacity(self):
        return self._capacity

    def get_plate_number(self):
        return self._plate_number

    # Setters
    def set_brand(self, brand):
        self._brand = brand

    def set_name(self, name):
        self._name = name

    def set_color(self, color):
        self._color = color

    def set_capacity(self, capacity):
        self._capacity = capacity

    def set_plate_number(self, plate_number):
        self._plate_number = plate_number

    def drive(self):
        print(f"The {self._name} is driving!")

    def drift(self):
        print(f"The {self._name} is drifting!")

    def carry_cargo(self):
        print(f"The {self._name} is carrying cargo!")


class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number, passengers):
        super().__init__(brand, name, color, capacity, plate_number)
        self._passengers = passengers

    def carry_cargo(self):
        print(f"The {self._name} is carrying passengers: {self._passengers} people.")


class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number, cargo_type):
        super().__init__(brand, name, color, capacity, plate_number)
        self._cargo_type = cargo_type

    def carry_cargo(self):
        print(f"The {self._name} is carrying {self._cargo_type}.")


# Creating objects
vehicle1 = Vehicle("Generic", "Car", "Red", 5, "ABC123")
bus1 = Bus("Mercedes", "Bus", "Blue", 50, "XYZ789", passengers=30)
truck1 = Truck("Volvo", "Truck", "White", 5000, "DEF456", cargo_type="Furniture")

# Calling methods on each object
vehicle1.drive()
vehicle1.drift()
vehicle1.carry_cargo()

bus1.drive()
bus1.carry_cargo()

truck1.drive()
truck1.carry_cargo()