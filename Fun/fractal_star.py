from turtle import *

import turtle
  

tur = turtle.Turtle()
  

tur.speed(0)
  
tur.getscreen().bgcolor("black")
turtle.screensize(canvwidth=5000, canvheight=5000)
tur.color("cyan")

tur.penup()
  
tur.goto((-1500, 0))
  

tur.pendown()
  

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            

            turtle.forward(size)
            star(turtle, size/1.2)
  

            turtle.left(216)
  
 
star(tur, 600)
turtle.done()