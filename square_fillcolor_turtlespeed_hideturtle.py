# create a square shape without the help of loop
'''import turtle
obj=turtle.Turtle()
obj.forward(150)
obj.left(90)
obj.forward(150)
obj.left(90)
obj.forward(150)
obj.left(90)
obj.forward(150)
'''
#speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning
#If input is a number greater than 10 or smaller than 0.5, speed is set to 0.
#Speedstrings  are mapped to speedvalues in the following way:
#           'fastest' :  0
#           'fast'    :  10
#           'normal'  :  6
#           'slow'    :  3
#           'slowest' :  1

# create a square shape with the help of loop
import turtle
obj=turtle.Turtle()
obj.begin_fill()
obj.fillcolor("purple")
#obj.hideturtle()      #to hide the turtle
for i in range(4):
    obj.left(90)
    obj.forward(150)
obj.end_fill()
obj.hideturtle()      #to hide the turtle
obj.speed(0)        # increase speed of turtle
