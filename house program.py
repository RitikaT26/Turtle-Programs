import turtle as tt

t= tt.Turtle()
t.pensize(3)

#Base of House
t.penup()
t.goto(0,0)
t.pendown()
for i in range(4):
    t.forward(150)
    t.left(90)

#Roof
t.penup()
t.goto(0,150)
t.pendown()
t.goto(75,220)
t.goto(150,150)
'''
t.forward(150)
t.left(45)
t.forward(106)
t.left(90)
t.forward(106)
t.left(45)
'''

#Door
t.penup()
t.goto(55,0)
t.pendown()
t.begin_fill()

for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

#Left Window
t.penup()
t.goto(20,90)
t.pendown()
for i in range(4):
    t.forward(40)
    t.left(90)

#Right Window
t.penup()
t.goto(90,90)
t.pendown()
for i in range(4):
    t.forward(40)
    t.left(90)

'''
#Chimney
t.penup()
t.goto(110,190)
t.pendown()
t.setheading(90)
for i in range(2):
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.right(90)
'''

t.hideturtle()
tt.done()
