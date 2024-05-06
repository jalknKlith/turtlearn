import turtle as Turtle

Turtle.speed(0)
Turtle.bgcolor('Black')

colors=['red','yellow','pink','orange','blue','green','cyan','white']

for x in range(300):
	Turtle.color(colors[x%8])
	Turtle.forward(x)
	Turtle.left(90)
