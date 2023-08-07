class Vehicle:
    def __init__(self,brand:str, name:str , color:str, capacity:int, plate_number:int) -> None:
        self.__name = name
        self.__brand = brand
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        return f"the {self.__name} is driving!"
    
    def drift(self):
        return f"the {self.__name} is drifting !!"
    
    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!" 
    

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_brand(self,brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand
    
    def get_color(self,color):
        self.__color = color
    
    def set_color(self):
        return self.__color
    
    def set_capacity(self,capacity):
        self.__capacity = capacity

    def set_capacity(self):
        return self.__capacity
    
    def set_plate_number(self,plate_number):
        self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number
    

class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

    def carry_cargo(self):
        return f"the {self.get_name} is carries a lot of people"
    
class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
    
    def drive(self):
        return f" the {self.get_name} is driving too slow"
    

bus1 = Bus("golden dragon","coach","green",5000,3224)
bus2 = Bus("Marcopolo","Scania","Yellow",4000,5563)

truck1 = Truck("ford","f-150","black",6000,7458)
truck2 = Truck("Ram","Ram 1500","red",7000,6578)

print(bus1.drive())
print(bus1.drift())
print(bus1.carry_cargo())

print(bus2.drive())
print(bus2.drift())
print(bus2.carry_cargo())


print(truck1.drive())
print(truck1.drift())
print(truck1.carry_cargo())

print(truck2.drive())
print(truck2.drift())
print(truck2.carry_cargo())








