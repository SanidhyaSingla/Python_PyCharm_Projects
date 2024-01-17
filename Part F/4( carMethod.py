class Car:
    def __init__(self, car, model, year, weight, max_speed):
        self.car = car
        self.model = model
        self.year = year
        self.weight = weight
        self.max_speed = max_speed
        self.speed = 0

    def acceleration(self, speed_added=0):
        self.speed += speed_added
        if self.speed > self.max_speed:
            self.speed = self.max_speed


my_car = Car('Honda City', 'ZX', 2017, 500, 220)
my_car.acceleration(231)
print(my_car.__dict__)

# create new attributes for speed (value not set via parameter) and max speed
# DONE

# create an accelerate method with a default acceleration
# DONE
