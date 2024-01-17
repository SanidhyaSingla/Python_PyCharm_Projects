# create a car class
class Car():
    pass


# create a car object
redbull = Car()
mercedes = Car()

# add attributes to the car object
redbull.color = 'Black, Red, Blue'
mercedes.color = 'Black, Oceanic, Teal'

redbull.position = 'Winner'
mercedes.position = 'Second Runner-Up'

# print attributes in 2 different ways
print('Redbull Color:', redbull.color)
print('Redbull Position:', redbull.position)
print(''
      '')
print('Mercedes Color:', mercedes.color)
print('Mercedes Position:', mercedes.position)

print(''
      '')

print(redbull.__dict__)
print(mercedes.__dict__)
