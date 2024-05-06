import turtle as Turtle
import random
Turtle.speed(0)
Turtle.bgcolor('Black')

colors=['red','yellow','pink','orange','blue','green','cyan','white']

for x in range(300):
	
	Turtle.color(colors[random.randint(0,7)])
	Turtle.forward(x)
	Turtle.left(90)
