# import 2 modules - Turtle & Time
import turtle, time

# reference the documentation for both modules
print(help(turtle))
turtle.speed(1)
for i in range(0, 4):
    turtle.forward(200)
    turtle.right(90)

# draw a shape and have it remain on the screen
time.sleep(10)
