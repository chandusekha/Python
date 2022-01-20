from turtle import *
t=Turtle()

t.up()

t.goto(-100,-300)
t.down()
t.pensize(5)
t.goto(-100,300)
def rect(color):
    t.begin_fill()
    t.fillcolor(color)
    t.forward(300)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(300)
    t.end_fill()
    t.setheading(360)
    
    
color=["orange","white","green"]
for x in color:
    rect(x)
t.up()
t.goto(55,161)
t.down()
t.circle(34)



