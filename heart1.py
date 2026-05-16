import turtle

screen = turtle.Screen()
screen.title("Heart ❤️")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color("cyan")
pen.pensize(3)
pen.speed(3)

pen.penup()
pen.goto(0, -50)
pen.pendown()

pen.begin_fill()
pen.left(140)
pen.forward(100)
pen.circle(-50, 200)
pen.left(120)
pen.circle(-50, 200)
pen.forward(100)
pen.end_fill()

pen.hideturtle()

turtle.done()