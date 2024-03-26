# Draw a circle
import turtle
t=turtle.Turtle()
t.circle(20)      #Draw a circle  of radius 20 & radius is +ve so draw circle counter clockwise direction
t.circle(-50)
t.reset()               # to reset the turtle
t.circle(100,90)    # if we give second parameter then turtle will be stop at that angle
t.reset()
t.circle(200,steps=7)  # it will divide radius into given steps

