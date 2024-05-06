import turtle

tim = turtle.Turtle()

import turtle

tim = turtle.Turtle()
tim.color("red")  
tim.pensize(5)
tim.shape("turtle")

import turtle

tim = turtle.Turtle()
tim.color("red")  
tim.pensize(5)
tim.shape("turtle") 

tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)

import turtle

tim = turtle.Turtle()
tim.color("red")  
tim.pensize(5)
tim.shape("turtle") 

tim.forward(100)
tim.left(90)
tim.penup()  # Lifts the pen
tim.forward(100)
tim.left(90)  
tim.pendown()  # Puts the pen back down
tim.forward(100)
tim.left(90)
tim.forward(100)

import turtle

tim = turtle.Turtle()
tim.speed(5)  

import turtle

tim = turtle.Turtle()
tim.color("red", "blue")  # Blue is the fill color

tim.width(5)

tim.begin_fill()
tim.circle(50)
tim.end_fill()  

import turtle

tim = turtle.Turtle()
tim.color("red", "blue")  # Blue is the fill color

tim.width(5)

tim.begin_fill()
for x in range(4):  # This will draw a square filled in
    tim.forward(100)
    tim.right(90)

tim.end_fill()

tim.setpos(100, -50)

import turtle
import random

colors = ["red", "blue","green", "purple", "yellow", "orange", "black"]

tim = turtle.Turtle()
tim.color("red", "blue")

for x in range(5):
    randColor = random.randrange(0, len(colors))
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
   
    tim.color(colors[randColor], colors[random.randrange(0, len(colors))])

    tim.penup()
    tim.setpos((rand1, rand2))
    tim.pendown()
    
    tim.begin_fill()
    tim.circle(random.randrange(0,80))
    tim.end_fill()
    ```
