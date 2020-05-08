# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#VEHICLE = BASE CLASS
class Vehicle:
        pass

class FlightVehicle(Vehicle): #flightvehicle inherit from vehicle
        pass
class Starship(FlightVehicle): #starship inherit from flightvechile
        pass

class Airplane(FlightVehicle): #Airplane inherit from flight vehicle
        pass

class GroundVehicle(Vehicle):
        pass
#ground vehicle inherit from vehicle

#car/motorcycle both inhjerit from ground vehicle
class Car(GroundVehicle):
        pass

class Motorcycle(GroundVehicle):
        pass