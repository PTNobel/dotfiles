#!/usr/bin/python
"""
In the following code, draw_triangle() will take 3 coordinaltes for inputs,
and draw through those the 3 points making a triangle.
snowflake() will calculate the coordinates and call draw_tiangle(). The only
way to properly call snowflake() is call_snowflake().

Have a function that draws the line and then the triangle...
"""
import turtle 
import math
import time 


def draw_triangle(x1, y1, x2, y2, x3, y3):
    turtle.pensize(3)
    turtle.ht()
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)

def fill_triangle(x1, y1, x2, y2, x3, y3,depth):
    turtle.pensize(0)
    turtle.ht()
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    #turtle.colors={1:'black', 2:'purple', 3:'pink', 4:'yellow', 5:'red', 6:'green', 7:'orange'}
    #turtle.begin_fill()
    #turtle.fillcolor(colors[randint(1,7)])
    #turtle.goto(x2,y2)
    #turtle.goto(x3,y3)
    #turtle.goto(x1,y1)
    #turtle.end_fill()
    if (depth % 2)==1:
        
        turtle.begin_fill()
        turtle.fillcolor('yellow')
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        turtle.end_fill()
    else:
        turtle.begin_fill()
        turtle.fillcolor('red')
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        turtle.end_fill()

def call_snowflake(x1,y1,x2,y2,x3,y3,maxdepth):
    small_x=min([x1,x2,x3])
    large_x=max([x1,x2,x3])
    offset_x=(large_x-small_x)*.1
    small_y=min([y1,y2,y3])
    large_y=max([y1,y2,y3])
    offset_y=(large_y-small_y)*.1
    turtle.setworldcoordinates((small_x-offset_x),(small_y-offset_y),(large_x+offset_x),(large_y+offset_y))
    turtle.mode("world") 
    #draw_triangle(x1,y1,x2,y2,x3,y3)
    snowflake(x1, y1, x2, y2, x3, y3, maxdepth)

def snowflake(x1,y1,x2,y2,x3,y3,maxdepth,depth=0):
    
    if depth > maxdepth:
        
        return
    
    call_fill_x1=(((x1+x2)/3)/(maxdepth-depth))
    call_fill_x2=(((x1+x3)/3)/(maxdepth-depth))
    call_fill_x3=(((x2+x3)/3)/(maxdepth-depth))
    call_fill_y1=y1
    call_fill_y2=(((y1+y3)/3)/(maxdepth-depth))

    print(str(int(call_fill_x1)) + " " + str(int(call_fill_x2))  + " " + str(int(call_fill_x3)))
    """
    call_fill_x1=((x1+x2)/2)
    call_fill_y1=y1
    call_fill_x2=((x1+x3)/2)
    call_fill_y2=((y1+y3)/2)
    call_fill_x3=((x2+x3)/2)
    call_fill_y3=((y2+y3)/2)
    #if depth % 2 == 0:
    fill_triangle(call_fill_x1, call_fill_y1, call_fill_x2, call_fill_y2, call_fill_x3, call_fill_y3,depth)

    call1_x1=((x1+x2)/2)
    call1_y1=y1
    call1_x2=x2
    call1_y2=y2
    call1_x3=((x2+x3)/2)
    call1_y3=((y2+y3)/2)
    depth+=1
    triangle(call1_x1,call1_y1,call1_x2,call1_y2,call1_x3,call1_y3,maxdepth,depth)

    call2_x1=x1
    call2_y1=y1
    call2_x2=((x1+x2)/2)
    call2_y2=y2
    call2_x3=((x1+x3)/2)
    call2_y3=((y1+y3)/2)
    triangle(call2_x1,call2_y1,call2_x2,call2_y2,call2_x3,call2_y3,maxdepth,depth)

    call3_x1=((x1+x3)/2)
    call3_y1=((y1+y3)/2)
    call3_x2=((x2+x3)/2)
    call3_y2=((y2+y3)/2)
    call3_x3=x3
    call3_y3=y3
    triangle(call3_x1,call3_y1,call3_x2,call3_y2,call3_x3,call3_y3,maxdepth,depth)
    """


def snowflake(iterations):
    koch_flake = "FRFRF"
 
    for i in range(iterations):
        koch_flake = koch_flake.replace("F","FLFRFLF")
 
    turtle.down()
 
    for move in koch_flake:
        if move == "F":
            turtle.forward(100.0 / (3 ** (iterations - 1)))
        elif move == "L":
            turtle.left(60)
        elif move == "R":
            turtle.right(120)

snowflake(3)
time.sleep(10000000)
