class Vehicle :
    def __init__(self,brand,name,color,capacity,plate_number) -> None:
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number

    def drive(self):
        return f"the {self.__name} is driving!"
    def drift(self):
       return f"the {self.__name} is drifting!"
    def carry_cargo(self) :
        return f"the {self.__name} is not carrying cargo!"
    
    
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
  def drift(self):
      return f"the {self.get_name()} is not drifting!"
  def carry_cargo(self) :
        return f"the {self.get_name()} is not carrying cargo!"
  
class Truck(Vehicle):
  def drift(self):
      return f"the {self.get_name()} is not drifting!"
  def carry_cargo(self) :
        return f"the {self.get_name()} carrying cargo!"

car1=Vehicle("mercedes","G-class","Black",96,"H R B")
car2=Bus("mercedes","Benz Buses","white",530,"H J J")
car3=Truck("Scania","GP38","Red",3500,"H T U")
print("-"*20)
print("car")
print("-"*20)
print("the brand is ", car1.get_brand())
print("name of car is",car1.get_name())
print("the capacity of foil is :",car1.get_capacity())
print("the color is:",car1.get_color())
print("the plate number is ", car1.get_plate_number())
print (car1.drive())
print(car1.drift())
print(car1.carry_cargo())
print("-"*20)
print("Bus")
print("-"*20)
print("the brand is ", car2.get_brand())
print("name of car is",car2.get_name())
print("the capacity of foil is :",car2.get_capacity())
print("the color is:",car2.get_color())
print("the plate number is ", car2.get_plate_number())
print (car2.drive())
print(car2.drift())
print(car2.carry_cargo())
print("-"*20)
print("Truck")
print("-"*20)
print("the brand is ", car3.get_brand())
print("name of car is",car3.get_name())
print("the capacity of foil is :",car3.get_capacity())
print("the color is:",car3.get_color())
print("the plate number is ", car3.get_plate_number())
print (car3.drive())
print(car3.drift())
print(car3.carry_cargo())