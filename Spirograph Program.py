import turtle as tt
import colorsys

t= tt.Turtle()
t.speed(0)
tt.bgcolor("black")

colors= [colorsys.hsv_to_rgb(i/36,1,1) for i in range(36)]

for i in range(36):
    t.color(colors[i%36])
    t.circle(120)
    t.right(10)

tt.hideturtle()
tt.done()
