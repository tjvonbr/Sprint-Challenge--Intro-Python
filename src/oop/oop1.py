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

# Because all other classes and instances stem from this class, this is the base class
class Vehicle:
    def __init__(self, name, material, movement):
        self.name = name
        self.material = material
        self.movement = movement

class GroundVehicle(Vehicle):
    def __init__(num_wheels, doors):
        super().__init__(name, material, movement)
        self.num_wheels = num_wheels
        self.doors = doors

motorcycle = GroundVehicle

print(car)

    


