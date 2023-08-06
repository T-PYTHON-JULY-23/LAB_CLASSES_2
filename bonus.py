

# define a Vehicle class . it has the following structure :
# properties

#     brand
#     name
#     color
#     capacity
#     plate_number

# methods

#     drive() prints "the vehicle_name is driving!"
#     drift() prints "the vehicle_name is drifting !!" or something else depending on the class.
#     carry_cargo() prints "the vehicle_name is carrying cargo !!" or something else depending on the class

# for each of the properties do a setter & getter (encabsulate the data).
# Create tow other subclasses (inherit from vehicle):

#     Bus
#     Truck

# Note

#     override the methods as needed for each subclass of vehicle.
#     create at least one object of each class.
#     call all the methods on each object.




class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number):
        self._brand = brand
        self._name = name
        self._color = color
        self._capacity = capacity
        self._plate_number = plate_number

    def drive(self):
        print(f"The {self._name} - {self._brand}is driving!")

    def drift(self):
        print(f"The {self._name} -  {self._brand} is drifting!")

    def carry_cargo(self):
        print(f"The {self._name} - {self._brand} is carrying cargo!")


    # Getters
    def get_brand(self):
        return self._brand

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_capacity(self):
        return self._capacity

    def get_plate_number(self):
        return self._plate_number


    # Setters
    def set_brand(self, brand):
        self._brand = brand

    def set_name(self, name):
        self._name = name

    def set_color(self, color):
        self._color = color

    def set_capacity(self, capacity):
        self._capacity = capacity

    def set_plate_number(self, plate_number):
        self._plate_number = plate_number


class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

    def drift(self):
        print(f"The {self._name} is not suitable for drifting.")


class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

    def carry_cargo(self):
        print(f"The {self._name} is carrying heavy cargo!")


# Create objects of each class
car = Vehicle("Toyota", "Car1", "Red", 4, "ABC123")
bus = Bus("Mercedes", "Bus1", "Blue", 50, "DEF456")
truck = Truck("Volvo", "Truck1", "Yellow", 10000, "GHI789")

# Call methods on each object
car.drive()
car.drift()
car.carry_cargo()
print("==="*6)
bus.drive()
bus.drift()
bus.carry_cargo()
print("==="*6)
truck.drive()
truck.drift()
truck.carry_cargo()