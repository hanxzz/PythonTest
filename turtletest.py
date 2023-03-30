import turtle
s = turtle.getscreen()  #for the screen window
t = turtle.Turtle()
turtle.title("My turtle")

t.speed(2)#to control the turtle's speed
t.shape("turtle")
t.forward(100)          #moves forward or backwards
t.right(90)             #can change direction by left() or right() at a certain angle
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.home()
turtle.bgcolor("light blue")
t.penup()
t.left(100)
t.forward(100)
t.pendown()
t.circle(20)
t.penup()
t.left(90)
t.forward(100)
t.pendown()
t.pencolor("purple")
t.fillcolor("yellow")
t.pensize(9)
t.begin_fill()
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()
t.reset()
t.home()
n = 10
while n <= 40:
    t.circle(n)
    n = n+10