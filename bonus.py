
class Vehicle:
    def _init_(self, brand, name, color, capacity, plate_number):
        self.brand = brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

    def drive(self):
        print(f"The {self.name} is driving!")

    def drift(self):
        print(f"The {self.name} is drifting!")

    def carry_cargo(self):
        print(f"The {self.name} is carrying cargo!")

    # getters and setters for each property
    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_plate_number(self):
        return self.plate_number

    def set_plate_number(self, plate_number):
        self.plate_number = plate_number


class Bus(Vehicle):
    def _init_(self, brand, name, color, capacity, plate_number):
        super()._init_(brand, name, color, capacity, plate_number)

    def drive(self):
        print(f"The {self.name} is driving safely with passengers!")

    def carry_cargo(self):
        print(f"The {self.name} is carrying passengers!")


class Truck(Vehicle):
    def _init_(self, brand, name, color, capacity, plate_number):
        super()._init_(brand, name, color, capacity, plate_number)

    def drift(self):
        print(f"The {self.name} is not drifting, it's carrying heavy cargo!")

    def carry_cargo(self):
        print(f"The {self.name} is carrying heavy cargo!")


# create objects
    car = Vehicle("Ford", "Mustang", "Red", 4, "1234")
    bus = Bus("Volvo", "B7L", "Yellow", 50, "5678")
    truck = truck("Kenworth", "T680", "White", 40000, "9012")

    # call methods
    car.drive()
    car.drift()
    car.carry_cargo()
    bus.drive()
    bus.drift()
    bus.carry_cargo()
    truck.drive()
    truck.drift()
    truck.carry_cargo()