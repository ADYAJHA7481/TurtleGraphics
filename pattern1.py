'''import turtle
t=turtle.Turtle()
t.up()
t.goto(0,-50)
t.down()
t.begin_fill()
t.fillcolor("green")
t.circle(50)
t.end_fill()
t.up()
t.home()        # go to the home position

t.goto(300,170)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.circle(50)
t.end_fill()
t.up()
t.home()

t.goto(-300,170)
t.down()
t.begin_fill()
t.fillcolor("purple")
t.circle(50)
t.end_fill()
t.up()
t.home()

t.goto(-300,-190)
t.down()
t.begin_fill()
t.fillcolor("blue")
t.circle(50)
t.end_fill()
t.up()
t.home()

t.goto(300,-190)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(50)
t.end_fill()
t.up()
t.home()
'''
# Draw pattern with the help of function

def draw_circle(x,y,color,radius):
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()
    t.up()
    t.home()


import turtle
t=turtle.Turtle()
t.pensize(4)   # turtle will be bold
t.up()
draw_circle(0,-50,"green",50)
draw_circle(0,240,"orange",50)
draw_circle(300,170,"yellow",50)
draw_circle(-300,170,"purple",50)
draw_circle(-300,-190,"blue",50)
draw_circle(300,-190,"red",50)
draw_circle(0,-280,"black",50)





















