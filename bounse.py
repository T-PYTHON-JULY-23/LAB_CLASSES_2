
class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print(f"The {self.__name} : {self.__brand} is driving!!")

    def drift(self):
        print(f"The {self.__name} : {self.__brand} is drifting !!")

    def carry_cargo(self):
        print(f"The {self.__name} : {self.__brand} is carrying cargo!!")

    def get_brand(self):
        return self.__brand

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_capacity(self):
        return self.__capacity

    def get_plate_number(self):
        return self.__plate_number

    def set_brand(self, brand):
        self.__brand = brand

    def set_name(self, name):
        self.__name = name

    def set_color(self, color):
        self.__color = color

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number


class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

    def drift(self):
        print(f"The {self.get_name()} is not for drifting!!")


class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

    def carry_cargo(self):
        print(f"The {self.get_name()}  is carrying cargo !!")

car = Vehicle("Ford", "Car1", "black", 56, "FJK453")
bus = Bus("Kia", "Bus1", "green", 47, "DFH321")
truck = Truck("BMW", "Truck1", "red", 12000, "IEJ987")

car.drive()
car.drift()
car.carry_cargo()
bus.drive()
bus.drift()
bus.carry_cargo()
truck.drive()
truck.drift()
truck.carry_cargo()