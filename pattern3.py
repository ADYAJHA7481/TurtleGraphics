import turtle
t=turtle.Turtle()
list1=["yellow","red","blue","green","aqua"]
for i in range(150):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
