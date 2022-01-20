from turtle import *
t1=Turtle()
def m1(x,y,color,rad):
    t1.up()
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.fillcolor(color)
    t1.circle(rad)
    t1.end_fill()
    t1.up()
    t1.home()
    
                       
               
m1(0,-100,'green',100)
m1(-200,-200,'red',-100)
m1(-200,200,'orange',100)
m1(200,-200,'yellow',-100)
m1(200,200,'blue',100)



