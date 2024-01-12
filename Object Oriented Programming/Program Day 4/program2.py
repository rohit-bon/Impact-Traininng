from abc import *

class Car(ABC):
    def __init__(self,reg_no):
        self.reg_no = reg_no
    def open_tank(self):
        print("Fill the tank with Reg. no: ", self.reg_no)
    def steering(self):
        pass
    def break_system(self):
        pass

class Audi(Car):
    def steering(self):
        print("Power Steering.")
    def break_system(self):
        print("Hydraulic Break.")

class BMW(Car):
    def steering(self):
        print("BMW Power Steering.")
    def break_system(self):
        print("Air Break.")

audi_obj = Audi("MH31AUDI40")
audi_obj.open_tank()
audi_obj.steering()
audi_obj.break_system()

bmw_obj = BMW("MH31BMW40")
bmw_obj.open_tank()
bmw_obj.steering()
bmw_obj.break_system()


# o/p:
# Fill the tank with Reg. no:  MH31AUDI40
# Power Steering.
# Hydraulic Break.
# Fill the tank with Reg. no:  MH31BMW40
# BMW Power Steering.
# Air Break.