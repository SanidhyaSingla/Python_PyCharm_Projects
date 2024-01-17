# create the __init__ function for the class car
class Car:
    def __init__(self, car, model, year, weight):
        self.car = car
        self.model = model
        self.year = year
        self.weight = weight


# initialize the car with attributes for car, model, year, and weight
current_car = Car('Honda City', 'ZX', 2017, 500)
dream_car = Car('BMW', 'Series 8', 2021, 700)

# print the car object and its attributes
print(current_car.__dict__)
print(dream_car.__dict__)
print('My current car is', current_car.car, current_car.model)
print('My dream car is', dream_car.car, dream_car.model)
