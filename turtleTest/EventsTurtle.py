import turtle

# Set up the turtle window
turtle.setup(400, 500)
wn = turtle.getscreen()
wn.title("Hello")
wn.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.color("red")
t.shape("turtle")

# Define movement functions
def move():
    t.forward(2)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

def gotoPosition(x, y):
    print("You clicked at {0},{1}".format(x, y))
    t.goto(x, y)

def spin():
    for i in range(4):
        t.right(90)

def exit():
    wn.bye()

# Set up event handlers
wn.onkey(move, "space")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(spin, "s")
wn.onclick(gotoPosition)
wn.onkey(exit, "q")

# Start listening for events
wn.listen()

# Start the main event loop
wn.mainloop()
