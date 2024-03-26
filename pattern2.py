import turtle
t=turtle.Turtle()
list1=["yellow","red","blue","green","aqua"]
t.up()
t.goto(200,0)
for i in range(5):
    t.down()
    t.begin_fill()
    t.fillcolor(list1[i])
    t.circle(50)
#    t.circle(100)         # this will overlap
    t.end_fill()
    t.up()
    t.bk(100)    
