import turtle

t= turtle.Turtle()
t.pensize(5)
cs= ['blue','black','red','yellow','green']
p= [(-120,0),(0,0),(120,0),(-60,-60),(60,-60)]

for i in range(len(cs)):
    t.penup()
    t.goto(p[i])
    t.pendown()
    t.color(cs[i])
    t.circle(60)

turtle.done()
