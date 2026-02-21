import turtle
colours= ["red", "blue", "yellow", "green", "pink", "brown"]
sketch= turtle.Pen()
turtle.speed(0.1)
turtle.bgcolor("black")
for i in range(300):
    sketch.pencolor(colours[i%6])
    sketch.width(i/100 +1)
    sketch.forward(i)
    sketch.left(59)
sketch.done()
