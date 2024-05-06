import turtle as Turtle
import random

Turtle.speed(10)
Turtle.bgcolor('black')
turns = 100
distance = 10

for x in range(turns):
	right = Turtle.right(random.randint(0, 360)
	left = Turtle.left(random.randint(0, 360)
	Turtle.color(random.choice(['Blue','Red','Green','Cyan','Magenta','Pink','Violet']))
	random.choice([right, left])
	Turtle.forward(distance)
	
