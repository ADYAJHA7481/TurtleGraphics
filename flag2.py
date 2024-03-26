# Create Flag
import turtle
t=turtle.Turtle()

def rect(color):     # Create rectangle size
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(280)
        t.right(90)
        t.forward(70)
        t.right(90)
    t.end_fill()
    

    
t.up()           # Create upper rectangle
t.pensize(4)
t.goto(0,-300)
t.down()
t.goto(0,280)
rect("#FF9933")

t.goto(0,210)
t.forward(140)
t.pensize(3)
t.color("#000088")
t.circle(-35)
t.setheading(270)
t.forward(35)
t.setheading(0)

for i in range(24):   # Create Wheel
    t.forward(35)
    t.bk(35)
    t.left(15)

t.setheading(90)
t.forward(35)
t.setheading(0)

t.pensize(4)
t.color("black")
t.forward(140)
t.right(90)
t.forward(70)
t.right(90)
t.forward(280)
t.right(90)
t.forward(70)
t.right(90)



t.goto(0,140)
rect("green")




























