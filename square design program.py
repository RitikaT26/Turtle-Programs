import turtle
turtle.bgcolor("black")
turtle.pensize(4)
turtle.speed(0.001)

for i in range(100):
    for colour in ['red','pink','magenta','orange','yellow','green','blue','violet','brown','grey','white']:
        turtle.color(colour)
        turtle.forward(100)
        turtle.left(90)
        turtle.right(20)
        

turtle.hideturtle()
    
