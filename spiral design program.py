import turtle as tt

t= tt.Turtle()
t.speed(10)
cs= ['red','blue','green','yellow','purple']
for i in range(100):
    t.color(cs[i%5])
    t.forward(i*2)
    t.right(59)
tt.done()
