class Vehicle ():
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:str) -> None:
        self.brand = brand
        self.name = name
        self.color =color
        self.capacity = capacity
        self.plate_number = plate_number
    # def drive(self):
    #     print(f"The {self.name} id driving !")
    # def drif(self):
    #     pass
    # def carry_cargo():
    #     pass
class Bus(Vehicle):
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
    def drive(self):
        print(f"The {self.name} id driving !")
    def drift(self):
        print(f"the {self.name} is not drifting !!")
    def carry_cargo(self):
        print(f"the {self.name} is not carrying cargo !!")

bus1 = Bus("Marcedes","Benz Bus","white",182,"ksa 2030")
print("------- Bus -------")
bus1.drive()
bus1.drift()
bus1.carry_cargo()
print()
class Truck(Vehicle):
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
    def drive(self):
        print(f"The {self.name} id driving !")
    def drift(self):
        print(f"the {self.name} is not drifting !!")
    def carry_cargo(self):
        print(f"the {self.name} is carrying cargo !!")
truck1 = Truck("Foton","Tunland","Black",185,"ksa 2000")
print("------- Truck -------")
truck1.drive()
truck1.drift()
truck1.carry_cargo()
print()