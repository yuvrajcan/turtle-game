import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics")
screen.bgcolor("white")
screen.setup(width=1000 , height=1000)

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)  # Set the turtle speed

# Set up the floor size
floor_size = 20
square_size = 20

# Draw the grid
for i in range(floor_size + 1):
    t.penup()
    t.goto(-floor_size * square_size // 2, (i - floor_size // 2) * square_size)
    t.pendown()
    t.forward(floor_size * square_size)

t.right(90)
for i in range(floor_size + 1):
    t.penup()
    t.goto((i - floor_size // 2) * square_size, floor_size * square_size // 2)
    t.pendown()
    t.backward(floor_size * square_size)

# Reset turtle position
t.penup()
t.goto(0,0)
t.setheading(90)  # Face upwards

# Commands for the turtle
commands = [
    "forward 100",
    "right 90",
    "forward 100",
    "left 90",
    "forward 50",
    "penup",
    "forward 50",
    "pendown",
    "left 90",
    "forward 100",
]

# Execute commands
for command in commands:
    cmd = command.split()
    action = cmd[0]

    if action == "forward":
        t.forward(int(cmd[1]))
    elif action == "backward":
        t.backward(int(cmd[1]))
    elif action == "right":
        t.right(int(cmd[1]))
    elif action == "left":
        t.left(int(cmd[1]))
    elif action == "penup":
        t.penup()
    elif action == "pendown":
        t.pendown()

# Close the window when clicked
screen.exitonclick()
