import turtle as Turtle

Turtle.speed(0)
Turtle.bgcolor('Black')

colors=['red','yellow','pink','orange']

for x in range(300):
	Turtle.color(colors[x%4])
	Turtle.forward(x)
	Turtle.left(90)
