import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1000000000000000000000)                           # Make the turtle move as fast, but not too fast. 


for i in range (1000000):
    tina.forward(.1)
    tina.right (360/1000000)