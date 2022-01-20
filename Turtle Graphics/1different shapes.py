from turtle import *
t1=Turtle()

color=["purple","red","blue","green","orange"]
for x in range(200):
    t1.color(color[x%5])
    t1.pensize(x/10+1)
    t1.forward(x)
    t1.left(59)
    
