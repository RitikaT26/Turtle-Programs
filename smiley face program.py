import turtle as tt

t= tt.Turtle()
t.pensize(3)

#Face Circle
t.penup()
t.goto(0,-100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

#Eyes
for i in [-35,35]:
    t.penup()
    t.goto(i,10)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

#Smile
t.penup()
t.goto(-40,-40)
t.pendown()
t.setheading(-60)
t.circle(50,120)

tt.done()
