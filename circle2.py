import turtle as Turtle
Turtle.speed(30)
Turtle.bgcolor('black')

colors = ['red','yellow','cyan','orange','pink','purple']

for x in range(100):
	Turtle.circle(x)
	Turtle.color(colors[x%6])
	Turtle.left(60)
