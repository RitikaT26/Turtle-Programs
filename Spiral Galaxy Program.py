import turtle as tt
import colorsys

t= tt.Turtle()
t.speed(0)
tt.bgcolor('black')
t.pensize(2)

colors= [colorsys.hsv_to_rgb(i/100,1,1) for i in range(100)]

for i in range(200):
    t.color(colors[i%100])
    t.forward(i*2)
    t.right(59)

tt.hideturtle()
tt.done()
