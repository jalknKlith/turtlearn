import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red','orange']
for number in range(300):
	t.forward(number+1)
	t.right(89)
	t.pencolor(colors [number%2])
turtle.done()

