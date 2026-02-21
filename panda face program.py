import turtle as t

t.bgcolor("white")
t.title("Panda Face")

def drawcircle (c, x,y, rad):
    t.penup()
    t.goto(x,y-rad)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

#Face
drawcircle("white",0,0,100)

#Ears
drawcircle("black",-70,120,40)
drawcircle("black",70,120,40)

#Eyes
drawcircle("white",-40,40,20)
drawcircle("white",40,40,20)

#Pupils
drawcircle("black",-40,40,7)
drawcircle("black",40,40,7)

#Nose
drawcircle("black",0,0,10)

#mouth
t.penup()
t.goto(-35,-40)
t.pendown()
t.setheading(-60)
t.circle(40,120)

t.hideturtle()
t.done()
