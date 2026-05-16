import turtle

screen = turtle.Screen()
screen.title("Five-Pointed Star")
t = turtle.Turtle()
t.speed(3) 

t.color("black")  
t.fillcolor("turquoise")      

t.begin_fill()

for _ in range(5):
    t.forward(200)       
    t.right(144)         

t.end_fill()

t.hideturtle()
screen.mainloop()