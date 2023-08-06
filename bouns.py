"""
# Bonus

## define a Vehicle class . it has the following structure :

#### properties
- brand
- name
- color
- capacity
- plate_number


#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class


### for each of the properties do a setter & getter (encabsulate the data).

### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck


### Note
- override  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 

"""


class Vehicle ():

    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int) -> None:
        
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number

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

    
    
    
    
    
    
    
    def drive(self):
        print(f"the {self.__name} is driving !!".title()) 
    
    def drift(self):
        print(f"the {self.__name} is drifting !!".title()) 
    
    def carrry_cargo(self):
         print(f'the {self.__name} is carring a cargo !'.title())


class Bus(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

    def drift(self):
        print(f"You cant drift with a bus ({self.get_name()})".title())

    def carrry_cargo(self):
        print(f'Bus cant carry a cargo '.title())


class Truck (Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int ,cargos:int) -> None:
        super().__init__(brand, name, color, capacity, plate_number) 
        self.__cargos=cargos

    def set_cargos(self,cargos):
        self.__cargos=cargos
    def get_cargos(self):
        return self.__cargos
    def drift(self):
        print(f"You cant drift with a truck ({self.get_name()})".title())

    def carrry_cargo(self):
        print(f'The {self.get_name()} truck is carrying {self.__cargos} cargos')



bus1 = Bus('BENZ','big bus101','black',20,123)
truck1 = Truck('mitsubishi','big mitsubishi','red',3,123,2)

print("**** Bus obj ****")
bus1.drive()
bus1.drift()
bus1.carrry_cargo()
print('')
print("**** Truck obj ****")
truck1.drive()
truck1.drift()
truck1.carrry_cargo()
