import turtle as Turtle
Turtle.speed(0)
Turtle.bgcolor('Black')

colors=['red','yellow','orange','green','cyan','white']

for x in range(300):
	
	
	Turtle.color(colors[x%6])
	Turtle.forward(x)
	Turtle.left(59)
