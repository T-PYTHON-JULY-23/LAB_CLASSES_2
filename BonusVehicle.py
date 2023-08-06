
class Vehicle:

    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:str) -> None:
        
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

   
    def set_brand(self,brand:str):
        if isinstance(brand, str):
             self.__brand = brand
        else:
            raise ValueError("please input valid brand for the car\n")
        
   
    def get_brand(self):
        return self.__brand
    
     
    def set_name(self,name:str):
        if isinstance(name, str):
             self.__name = name
        else:
            raise ValueError("please input valid name for the car\n")
        

    def get_name(self):
        return self.__name
    

    def set_color(self,color:str):
        if isinstance(color, str):
             self.__color = color
        else:
            raise ValueError("please input valid color for the car\n")
        
   
    def get_color(self):
        return self.__color
    


    def set_capacity(self,capacity:int):
        if isinstance(capacity, int):
             self.__capacity = capacity
        else:
            raise ValueError("please input valid capacity number for the car\n")
        
   
    def capacity(self):
        return self.__capacity
    

     
    def set_plate_number(self,plate_number:str):
        if isinstance(plate_number, str) and len(plate_number)== 6 :
             self.__plate_number = plate_number
        else:
            raise ValueError("please input valid plate number for the car\n")
        
   
    def plate_number(self):
        return self.__plate_number

    def drive(self):

        print(f"The {self.__name} is driving!!")
    
    def drift(self):

        print(f"The {self.__name} is drifting!!")
        
        
    def carry_cargo(self):

        print(f"The {self.__name} is carrying cargo !!")

    
class Bus(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.name= name
        
    def drift(self):

        print(f"The {self.name} is drifting!!")
    
    def carry_cargo(self):

        print(f"The {self.name} can't carry cargo !!")


class Truck(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.name= name

    def drift(self):

        print(f"The {self.name} can't drift!!")
    
    def carry_cargo(self):

        print(f"The {self.name} is carrying cargo !!")

print("_"*30)
truck = Truck("Toyota","A3","blue",4,"123ASD")
truck.carry_cargo()
truck.drift()
truck.drive()

print("_"*30)
bus = Bus("ford","SS","red",15,"456yYHN")

bus.carry_cargo()
bus.drift()
bus.drive()