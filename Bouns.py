class Vehicle:
    def __init__(self,brand : str , name :str , color:str,capacity:int,plate_number:int) -> None:
        self.__brand = brand
        self.__name=name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    def drive(self):
        return f"the {self.__name} is driving !!" 

    def drift(self):
        return f"the {self.__name} is drifting !!"
    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!"
    def set_brand(self,brand):
        self.__brand=brand
    def set_name(self,name):
        self.__name=name
    def set_color(self,color):
        self.__color=color
    def set_capacity(self,capacity):
        self.__capacity=capacity
    def set_plate_number(self,plate_number):
        self.__plate_number=plate_number
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
class Bus(Vehicle):
    def _init_(self, brand, name, color, capacity, plate_number):
        super()._init_(brand, name, color, capacity, plate_number)

    def drift(self):
        return f"The {self.__name} is not  for drifting at all!!"

class Truck (Vehicle):
    def _init_(self, brand, name, color, capacity, plate_number):
        super()._init_(brand, name, color, capacity, plate_number)

    def carry_cargo(self):
        return f"The {self.__name} is a good choice to carry cargo!"
car = Vehicle("Hyundi", "sonata", "Blue", 60, "MAQ505")
bus = Bus("mercedes", "Bus", "white", 200, "AHM303")
truck = Truck("ford", "ranger", "Black", 1022, "ACS505")
car.drive()
car.drift()
car.carry_cargo()
bus.drift()
bus.carry_cargo()
truck.carry_cargo()