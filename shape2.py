import turtle
t=turtle.Turtle()
turtle.Screen().bgcolor('purple')
t.pensize(2)
t.speed(0)

#Create "D"

t.begin_fill()
t.fillcolor("red")
t.up()
t.pensize(4)
t.goto(-200,-70)
t.down()
t.left(90)
t.forward(150)
t.right(90)
t.circle(-75,180)
t.end_fill()

# Create "I"

t.up()
t.goto(-90,-70)
t.down()
t.right(90)
t.forward(140)
t.left(90)
t.forward(40)
t.backward(80)
t.up()
t.goto(-90,-70)
t.down()
t.forward(40)
t.backward(80)

# Create "V"

t.up()
t.goto(-30,70)
t.down()
t.begin_fill()
t.fillcolor("yellow")
t.left(110)
t.forward(150)
t.left(140)
t.forward(150)
t.end_fill()

# Create "Y"

t.up()
t.goto(90,70)
t.down()
t.right(140)
t.forward(75)
t.left(140)
t.forward(75)
t.backward(150)

# Create "A"

t.up()
t.goto(170,70)
t.down()
t.right(170)
t.forward(150)
t.up()
t.goto(170,70)
t.down()
t.left(25)
t.forward(150)
t.backward(60)
t.right(100)
t.forward(40)
t.hideturtle()




































