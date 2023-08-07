
class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print(f"The {self.__name} is driving!")

    def drift(self):
        print(f"The {self.__name} is drifting!")

    def carry_cargo(self):
        print(f"The {self.__name} is carrying cargo!")

    # getters and setters for each property
    def get_brand(self):
        return self.__brand

    def set_brand(self,brand):
        self.__brand = brand

    def get_name(self):
        return self.__name

    def set_name(self,__name):
        self.name = name

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

    def get_capacity(self):
        return self.capacity

    def set_capacity(self,capacity):
        self.capacity = capacity

    def get_plate_number(self):
        return self.plate_number

    def set_plate_number(self,plate_number):
        self.plate_number = plate_number


class Bus(Vehicle):
   

    def drive(self):
        print(f"The {self.get_name()} is driving safely with passengers!")

    def carry_cargo(self):
        print(f"The {self.get_name()} is carrying passengers!")


class Truck(Vehicle):
    def drift(self):
        print(f"The {self.get_name()} is not drifting, it's carrying heavy cargo!")

    def carry_cargo(self):
        print(f"The {self.get_name()} is carrying heavy cargo!")


# create objects
car = Vehicle("Ford", "Mustang", "Red", 4, "1234")
bus = Bus("Volvo", "B7L", "Yellow", 50, "5678")
truck = Truck("Kenworth", "T680", "White", 40000, "9012")

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