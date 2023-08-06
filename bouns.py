class Vehicle:

    def __init__(self,brand:str , name:str, color:str, capacity:int, plate_number:int)->None:
        self.__brand = brand 
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print(f"the {self.__name} is driving!")

    def drift(self):
        print(f"the {self.__name} is drifting")

    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo!!")
    
    def set_brand(self,brand): 
        self.__brand = brand 
        
    def get_brand(self):
       return self.__brand
    
    def set_name(self,name): 
        self.__name = name 
        
    def get_name(self):
       return self.__name

    def set_color(self,color): 
        self.__color = color 
        
    def get_color(self):
       return self.__color
    
    def set_capacity(self,capacity): 
        self.__capacity = capacity 
        
    def get_capacity(self):
       return self.__capacity
    
    def set_plate_number(self,plate_number): 
        self.__plate_number = plate_number
        
    def get_plate_number(self):
       return self.__plate_number


class Bus(Vehicle):
    def __init__(self,brand:str , name:str, color:str, capacity:int, plate_number:int)->None:
       super().__init__(brand,name,color,capacity,plate_number)
    
    def carry_cargo(self):
        print(f"the {self.get_name()} is carrying people!!")


class Truck(Vehicle):
    def __init__(self,brand:str , name:str, color:str, capacity:int, plate_number:int)->None:
       super().__init__(brand,name,color,capacity,plate_number)
      
    def drift(self):
        print(f"the {self.get_name()} is slipping")
    


bus1 = Bus("Blue Bird","Minibus","white",10,1234)
bus2 = Bus("IC","school bus","Yellow and white",20,4321)

truck1 = Truck("Kenworth","Tractor","white",2,2020)
truck2 = Truck("Volovo","Pickup","black",5,7986)


print(bus1.drift())
print(bus1.drive())
print(bus1.carry_cargo())

print(bus2.drift())
print(bus2.drive())
print(bus2.carry_cargo())


print(truck1.drift())
print(truck1.drive())
print(truck1.carry_cargo())

print(truck2.drift())
print(truck2.drive())
print(truck2.carry_cargo())




