from turtle import *
t1=Turtle()
t1.speed(3)
t1.begin_fill()
t1.fillcolor("red")
for  x in range(4):
    t1.forward(100)
    t1.left(90)
t1.end_fill()
t1.hideturtle()


# 'fastest' :  0
#       'fast'    :  10
#        'normal'  :  6
 #       'slow'    :  3
  #      'slowest' :  1


# for screen
# ws=screen()
#ws.bgcolor("red")
#ws.bgpic('.gif')


