
# TURTLE GRAPHICS :- turtle graphics refers to controling a graphical entity in a graphics window with X,Y coordinates.
#this was developed for kids to attract them towards the programming .
# 6 shape in turtle ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
# The default shape is "classic"
# The Default colormode is 1 if we want RGB color mode then we write colormode(255)

import turtle                    # import module 
create_object=turtle.Turtle()     # create object of Turtle class
create_object.shape("square")     # Change shape
create_object.color("red")        # Change color
create_object.forward(100)
create_object.color("blue","green")
turtle.colormode(255)                 # Change the colormode
create_object.color(120,30,70)
