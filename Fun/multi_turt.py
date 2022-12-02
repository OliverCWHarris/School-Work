import threading
import threading
from turtle import *

import turtle


tur1 = turtle.Turtle()

tur2=turtle.Turtle()

tur1.speed(6)

tur1.getscreen().bgcolor("black")
turtle.screensize(canvwidth=1000, canvheight=1000)
tur1.speed(0)
tur2.speed(0)
tur1.color("cyan")
tur2.color('Red')

tur1.penup()
tur2.penup()

tur1.goto((200, -150))
tur2.goto((-400, 200))


tur1.pendown()
tur2.pendown()


def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            

            turtle.forward(size)
            star(turtle, size/3)


            turtle.left(216)




threading._start_new_thread(star, (tur1, 360))
threading._start_new_thread(star, (tur2, 360))

#star(tur1, 360)
#star(tur2, 360)
turtle.done()