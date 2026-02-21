import turtle as tt
import random

tt.bgcolor('black')
t= tt.Turtle()
t.speed(0)
tt.colormode(255)

def fireworks(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    color= (random.randint(100,255),random.randint(100,255),random.randint(100,255))
    t.color(color)
    for i in range(36):
        t.forward(50)
        t.backward(50)
        t.right(10)

tt.onscreenclick(fireworks)
tt.done()
