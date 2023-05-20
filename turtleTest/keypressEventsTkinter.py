import turtle
turtle.setup(400,500)
wn = turtle.getscreen()
wn.title("Hello")
wn.bgcolor("white")
t = turtle.Turtle()
t.color("red")
t.shape("turtle")
def move():
  t.forward(2)
def turn_left():
  t.left(90)
def turn_right():
  t.right(90)
def exit():
  wn.bye()
wn.onkey(move, "space")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(exit, "q")
wn.listen()
wn.mainloop()
