import turtle as t
t.pen()
colors=["yellow","red","green","purple"]
t.bgcolor("black")
for x in range(450):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left
