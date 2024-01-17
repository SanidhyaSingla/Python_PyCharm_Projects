"""
    ATTRIBUTES:
    Occupants attribute which is 0 by default
    Floor attribute which is 0 by default

    METHODS:
    add_occupants
    go_to_floor

    PROPERTIES:
    Occupants can only be added if the occupants limit hasn't been exceeded i.e. 8 people.
    Only floors from -5 to 50 exist
"""


class Elevator:
    occupants = 0
    floor = 0

    def add_occupants(self):
        Elevator.occupants += 1
        if Elevator.occupants > 8:
            Elevator.occupants = 8
            print('Sorry! The elevator has reached it limit of 8 people.')

    def go_to_floor(self):
        Elevator.floor = int(input('Please enter the floor no. :'))
        if Elevator.floor > 50:
            Elevator.floor = 0
            print('Sorry! In this building, there are only floors from -5 to 50.')
        if Elevator.floor < -6:
            Elevator.floor = 0
            print('Sorry! In this building, there are only floors from -5 to 50.')


Elevator1 = Elevator()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
Elevator1.add_occupants()
print(Elevator.occupants)

Elevator1.go_to_floor()