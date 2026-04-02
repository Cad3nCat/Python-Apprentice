"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help
"""

import turtle, random                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
turtle.bgcolor('black')
tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'tan', 'magenta']

for  i in range(random.randint(500, 1000)):
    randomForward = random.randint(1, 100)
    randomLeft = random.randint(1, 100)
    tina.color(random.choice(colors))
    tina.forward(randomForward)
    tinaX = tina.xcor()
    tinaY = tina.ycor()
   
    if tinaX >= 300 or tinaX <=-300:
        tina.undo()
    if tinaY >= 300 or tinaY <= -300:
        tina.undo()
    tina.left(randomLeft)
turtle.exitonclick()  