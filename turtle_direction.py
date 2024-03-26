# By Default turtle faces east . To change the heading(DIRECTION) the turtle then we need to set heading method. 
#forward(distance):- move the turtle forward by the specified distance.
#backward(distance):- move the turtle backward by the specified distance.

import turtle
obj=turtle.Turtle()
obj.setheading(90)           #north
obj.setheading(180)          #west
obj.setheading(270)           #south
obj.setheading(360)             #east
obj.forward(100)          # to move the turtle
obj.fd(200)             #[forward,fd are same]
obj.fd(-100)
obj.backward(50) # [backward,back,bk are same]
obj.back(50)
obj.bk(50)
obj.left(45)          #turn turtle left by angle units  [left,lt are same]
obj.right(60)         #turn turtle right by angle units  [right,rt are same]  


