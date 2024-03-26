#to use background pic ,
# we should remember two thing. 1.the image file should be in the GIF format 
# 2. the python file and the image file should be in the same folder.

import turtle
obj=turtle.Turtle()
obj.color("red")
obj.shape("triangle")
window_screen=turtle.Screen()    # Create object of screen class
window_screen.bgcolor("blue")    # Change background color
turtle.colormode()              # to know the colormode
turtle.colormode(255)
window_screen.bgcolor(30,60,90)
window_screen.title("Adya")       # Change title
window_screen.bgpic("2.gif")       # Background pic


