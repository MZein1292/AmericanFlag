#american flag



import turtle
import time
import random



########################################################################
A = 100
length = A * 1.9 #B
height = A/13    #width of strip
C = A*(7/13)
D = length*(2/5)
L = A/13
red = 1,0,0 #red
########################################################################


#draw the stars


def drawStars(l, h):
    for z in range(50):
        if z < 7:
            row = 90
            drawRows(row)
        if z < 14:
            row = row - 10
            drawRows(row)
        if z < 21:
            row = row - 10
            drawRows(row)
        if z < 28:
            row = row - 10
            drawRows(row)
        if z < 35:
            row = row - 10
            drawRows(row)
        break

def drawRows(row):
    x = -75 + D
    y = 155 - C
    for z in range(10):
        x += 7
        turtle.up()
        turtle.speed(100)
        turtle.color(1,1,1)
        turtle.setpos(x,row)
        turtle.begin_fill()
        turtle.down()
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.end_fill()
    turtle.bye

##############################################


#draws the stripes
for i in range(13):
    if i % 2 == 0:
        red = 1,0,0
    else:
        red = 1,1,1
    turtle.pencolor(red)
    turtle.speed(100)
    turtle.fillcolor(red)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(height)
    turtle.right(90)


#draw the union blue box
    
x2 = -75 + D
y2 = 155-C
turtle.up()
turtle.setpos(x2,y2)
turtle.down()
turtle.color(0,0,1)
turtle.begin_fill()
turtle.forward(D)
turtle.right(90)
turtle.forward(C)
turtle.right(90)
turtle.forward(D)
turtle.right(90)
turtle.forward(C)
turtle.end_fill()
turtle.up()
drawStars(-length, height)          #call the draw stars



            

    
    
    
    

