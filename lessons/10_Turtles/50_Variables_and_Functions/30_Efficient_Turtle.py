
"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.left (angle)
        tina.forward(angle)
draw_polygon(999)                        # Draw a square

                   # Move tina to another spot on the screen

                        # Draw a pentagon

                                      # Move tina to another spot on the screen

                     # Draw a hexagon

turtle.exitonclick()                     # Close the window when we click on it