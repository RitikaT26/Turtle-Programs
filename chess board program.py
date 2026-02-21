import turtle
sc= turtle.Screen()
pen= turtle.Turtle()

def draw():
    
 for j in range(4):
    pen.forward(30)
    pen.left(90)
 pen.forward(30)

if __name__== "__main__":
    sc.setup(600,600)
    pen.speed(100)
    
    for i in range(8):
       pen.up()
       pen.setpos(0,30 * i)
       pen.down()
       for r in range(8):
           for d in range(8):
              if (i+r)% 2==0:
                 pen.fillcolor("black")
              else:
                 pen.fillcolor("white")
        
           pen.begin_fill()
           draw()
           pen.end_fill()
       
      
    pen.hideturtle()

