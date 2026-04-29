"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""


import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 10  # the length of the flaming arms
num_shapes = 10

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0)

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    ...
    for i in range(25):
        t.forward(-10)
        t.right(-200)
        t.forward(30)
        t.left(-400)

for i in range(1500):
    make_a_shape(t)
    t.right(360/num_shapes)
    

t.hideturtle() 

turtle.done() 

t = ... # Create a turtle named t

# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    ...

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = ...

