
class Vehicle :

    def __init__(self, brand:str, name:str, color:str, capacity:str, plate_number:str) -> None:
        self.__brand = brand
        self.__name = name 
        self.__color =color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print( f"the {self.__name} is driving!")

    def drift(self):
        print(f"the {self.__name} is drifting !!")

    def carry_cargo(self):
         print (f"the {self.__name} is carrying cargo !!")

    def set_brand(self, brand):
        self.__brand = brand 
    
    def set_name(self,name):
        self.__name = name
    
    def set_color(self, color):
        self.__color = color

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number


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

    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        super().__init__(brand, name, color, capacity, plate_number)



class Truck(Vehicle):
    
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

 


car = Vehicle(" Mercedes", "A-Class Sedan", "black", 70 , 4246)
bus = Bus("Hyundai ","van", "white", 100, 3930)
truck= Truck("Truck", "Tractor", "gray", 200, 2295)

car.drive()
car.drift()
car.carry_cargo()
bus.drift()
bus.carry_cargo()
truck.carry_cargo()
