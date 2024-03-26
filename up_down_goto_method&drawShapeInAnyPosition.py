import turtle
t=turtle.Turtle()    
#t=turtle.Pen()            # Turtle is also called Pen
'''t.circle(100) 
t.undo()               #It Will undo the last turtle action
t.circle(100)           
t.reset()               #It will clear all things
t.goto(0,-100)      #in goto we need to mention that x coordinate as well as y,Here x=0,y=-100 [setpos,setposition,goto are same]
t.circle(100)'''
t.up()    # if we use t.up then while turtle moving it won't draw the line [penup,pu,up are same]
t.circle(50)  #You can't see any line because turtle is up now,if you want to draw the line now,you need to do it t.down
t.down()         #[pendown,pd,down are same]
t.circle(60)
