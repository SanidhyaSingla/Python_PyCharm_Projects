import math


# Define the Circle class and the Circle constructor method
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return math.pi * 2 * self.radius


while True:
    radius1 = float(input('Please give the radius of the circle:'))
    circle = Circle(radius1)
    print('Area of the circle:', circle.area())
    print('Area of the circumference:', circle.circumference())

# Create the area calculation method, which returns the circle's area


# Create the circumference method, which return the circle's circumference


# After the class definition, add the code that requests for user input for the radius


# Create a while loop requesting user input, changing the circle object's radius and then printing out the area
# and the circumference
