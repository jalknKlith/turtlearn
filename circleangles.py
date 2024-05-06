import turtle as Turtle
import time

Turtle.color('green')
Turtle.bgcolor('black')
for angle in range(0,360,10):
	Turtle.seth(angle)
	Turtle.circle(100)
