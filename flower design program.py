import turtle
turtle.bgcolor("black")
turtle.speed(0.01)
turtle.color("light blue")
def flower():
    for i in range(200):
        turtle.circle(190-i, 90)
        turtle.left(90)
        turtle.circle(190-i, 90)
        turtle.left(18)

flower()
