class Vehicle :
    def __init__(self, brand, name , color,capacity, pate_number ) -> None:
       self._brand=brand
       self._name=name
       self._color=color
       self._capacity=capacity
       self._pate_number=pate_number

       ##setter

    def set_brand(self, brand):
        self._brand=brand
    
    def set_name(self, name ):
        self._name=name
    
    def set_color(self, color):
        self._color=color
    
    def set_capacity(self, capacity):
        self._capacity=capacity
    
    def set_pate_number(self, pate_number ):
        self._pate_number=pate_number
    
    ###gettr

    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color
    
    def get_capacity(self):
        return self._capacity
    
    def get_pate_number(self):
        return self._pate_number
    
    ###methods

    def drive(self):
        print(f"the{self._name} is driving")

    def drift(self):
        print(f"the {self._name} is drifting !!")    

    def carry_cargo(self):
        print (f"the {self._name} is carrying cargo !!" )


class Bus(Vehicle):
    def __init__(self, brand, name, color, capability, plate_number):
        super().__init__(brand, name, color, capability, plate_number)

    def drift(self):
        print(f"The {self.get_name()} is drifting ")


class Truck(Vehicle):
    def __init__(self, brand, name, color, capability, plate_number):
        super().__init__(brand, name, color, capability, plate_number)

    def carry_cargo(self):
        print(f"The {self.get_name()} is carrying cargo 11")



Vehicle1 = Vehicle("Ford", "Car", "Blue", "300", "fkrfj4")
bus = Bus("Volvo", "bus", "black", "800", "4r4kdd")
truck = Truck("Toyota", "trick", "Red", "500", "2k3okr")


Vehicle1.drive()
Vehicle1.drift()
Vehicle1.carry_cargo()

print()

bus.drive()
bus.drift()
bus.carry_cargo()

print()

truck.drive()
truck.drift()
truck.carry_cargo()
     
  


        
        
        
        