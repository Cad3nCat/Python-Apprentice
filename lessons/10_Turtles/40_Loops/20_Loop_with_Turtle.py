"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(10000000)                           # Make the turtle move as fast, but not too fast. 

for i in range(100):
    tina.forward(150)                       # Move tina forward by the forward distance
    tina.left(78)                           # Turn tina left by the left turn


turtle.exitonclick()                    # Close the window when we click on it