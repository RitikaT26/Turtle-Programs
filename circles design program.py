import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0.001)

for i in range(20):
    for colours in ["red", "magenta", "green", "blue", "white", "brown"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10.33)

turtle.hideturtle()
