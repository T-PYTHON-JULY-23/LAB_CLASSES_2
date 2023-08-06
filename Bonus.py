


class Vehicle:

    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int) -> None:
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number

    def drive(self):
        print ("the vehicle_name is driving!")

    def drift(self):
        print ("the vehicle_name is drifting !!")

    def carry_cargo(self):
        print("the vehicle_name is carrying cargo !!")

    


    def set_brand (self,brand:str):
        self.__brand=brand 

    def get_brand (self):
        return self.__brand  
        
    def set_name(self,name:str):
        self.__name=name


    def get_name(self):
        return self.__name
    
    def set_color(self,color:str):
        self.__color=color 

    def get_color (self):
        return self.__color  
    
    def set_capacity (self,capacity:str):
        self.__bcapacity=capacity

    def get_capacity (self):
        return self.__capacity 
    
    def set_plate_number (self,plate_number:str):
        self.__brand=plate_number 

    def get_plate_number (self):
        return self.__plate_number 
  

class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int,rent:str) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.rent=rent

    def  rent(self,rent:str):
        print (f"the rent of bus is {self.rent}") 


class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int,rent:str ) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.rent=rent

    def  rent(self,rent:str):
        print (f"the rent of bus is {self.rent}") 
    



