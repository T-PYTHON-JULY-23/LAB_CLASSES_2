class Vehicle:

    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_num:str) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_num = plate_num
    
    # setters >
    def set_brand(self, newBrand):
        self.__brand = newBrand
    
    def set_name(self, newName):
        self.__name = newName
    
    def set_color(self, newColor):
        self.__color = newColor
    
    def set_capacity(self, newCapacity):
        self.__capacity = newCapacity
    
    def set_plate_num(self, newPlateNum):
        self.__plate_num = newPlateNum
    
    # grtters >
    def get_brand(self):
        return self.__brand
    
    def get_name(self):
        return self.__name
    
    def get_color(self):
        return self.__color
    
    def get_capacity(self):
        return self.__capacity
    
    def get_plate_num(self):
        return self.__plate_num

    # methods >
    def drive(self):
        print(f"the {self.__name} is driving!")
    

    def drift(self):
        print(f"the {self.__name} is drifting")




class Bus(Vehicle):

    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_num:str, seats:int) -> None:
        super().__init__(brand, name, color, capacity, plate_num)
        self.seats = seats
    
    def drift(self):
        print(f"no one drift with a BUS !!")



class Truck(Vehicle):

    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_num:str, payload_kg:int, towing_kg:int) -> None:
        super().__init__(brand, name, color, capacity, plate_num)
        self.payload_kg = payload_kg
        self.towing_kg = towing_kg
   
    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo it can load more than {self.payload_kg}kg  and can !!")