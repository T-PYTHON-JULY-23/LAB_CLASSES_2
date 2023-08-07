# define a Vehicle class . it has the following structure :
class Vehicle:
    def __init__(self,Brand:str,name:str,color:str,capacity:int,plate_number:str) -> None:
        self.__Brand = Brand
        self.__name = name 
        self.__color = color 
        self.__capacity = capacity
        self.__plate_number = plate_number
    def drive(self):
         print(f"the {self.__name} is driving!")
    def drift(self):
             print(f"the {self.__name} is drifting !!")
    def carry_cargo(self):
          print(f"the {self.__name} is carrying cargo !!")
         
# for each of the properties do a setter & getter (encabsulate the data).
    def get_Brand(self):
         return self.__Brand
    def set_Brand(self,Brand):
          self.__Brand = Brand

    def get_name(self):
         return self.__name
    def set_name(self,name):
          self.__name = name

    def get_color(self):
         return self.__color
    def set_color(self,color):
          self.__color = color

    def get_capacity(self):
         return self.__capacity
    def set_capacity(self,capacity):
          self.__capacity = capacity
    def get_plate_number(self):
         return self.__plate_number
    def set_plate_number(self,plate_number):
          self.__plate_number = plate_number

# Create tow other subclasses (inherit from vehicle):
class Bus(Vehicle) :
     def drive(self):
        print(f"the {self.get_name()} bus is driving!")
     def drift(self):
             print(f"the {self.get_name()} buscis drifting !!")
     def carry_cargo(self):
          print(f"the {self.get_name()} bus is carrying cargo !!")
     

class Truck(Vehicle) :
     def drive(self):
            print(f"the {self.get_name()} Truck is driving!")
     def drift(self):
            print(f"the {self.get_name()} Truck drifting !!")
     def carry_cargo(self):
         print(f"the {self.get_name()} Truck is carrying cargo !!")
     
My_Vehicle = Vehicle("Toyota" , "Camray" , "Bluesky" ,3 ,"MK111")
My_Bus = Bus("Mercedes" , "V-class" , "Black" , 5 ,"MK000")
My_Truck = Truck("Ford" , "F-150" , "RED" ,6 ,"MK111")
# Bus

print(My_Vehicle.get_name())
My_Vehicle.drive()
My_Vehicle.drift()
My_Vehicle.carry_cargo()
print("")
print(My_Bus.get_name())
My_Bus.drive()
My_Bus.drift()
My_Bus.carry_cargo()
print("")
print(My_Truck.get_name())
My_Truck.drive()
My_Truck.drift()
My_Truck.carry_cargo()
