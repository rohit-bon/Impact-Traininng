from abc import *


class Vehicle(ABC):
    def number_of_tyres(self):
        pass

class Bus(Vehicle):
    def number_of_tyres(self,tyres):
        print("Number of tyres: ",tyres)  
        
class Truck(Vehicle):
    def number_of_tyres(self,tyres):
        print("Number of tyres: ",tyres)
        
class Auto(Vehicle):
    def number_of_tyres(self,tyres):
        print("Number of tyres: ",tyres)
    
class Cycle(Vehicle):
    def number_of_tyres(self,tyres):
        print("Number of tyres: ",tyres)    
        
class Bike(Vehicle):
    def number_of_tyres(self,tyres):
        print("Number of tyres: ",tyres)
        
class JCB(Vehicle):
    def number_of_tyres(self,tyres):
        print("Number of tyres: ",tyres)
        

bus_obj = Bus()
bus_obj.number_of_tyres(4)

truck_obj =Truck()
truck_obj.number_of_tyres(24)

auto_obj = Auto()
auto_obj.number_of_tyres(3)

cycle_obj =Cycle()
cycle_obj.number_of_tyres(2)

bike_obj = Bike()
bike_obj.number_of_tyres(2)

jcb_obj = JCB()
jcb_obj.number_of_tyres(4)


# o/p:
# Number of tyres:  4
# Number of tyres:  24
# Number of tyres:  3
# Number of tyres:  2
# Number of tyres:  2
# Number of tyres:  2