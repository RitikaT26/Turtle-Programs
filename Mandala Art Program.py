import turtle as tt

t= tt.Turtle()
t.speed(0)
tt.bgcolor('black')

colors=['red','orange','yellow','pink','green','blue','purple','brown','grey']

for i in range(12*len(colors)):
    t.color(colors[i%len(colors)])
    t.circle(120)
    t.left(5)

tt.done()
