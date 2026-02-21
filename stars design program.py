import turtle
spiral= turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(0.01)
spiral.color("yellow")
for i in range(50):
    spiral.forward(i* 10)
    spiral.right(144)
turtle.done()
