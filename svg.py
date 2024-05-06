from svg_turtle import SvgTurtle

t = SvgTurtle(500, 500)
t.forward(200)
t.dot(10)
t.save_as('example.svg')
