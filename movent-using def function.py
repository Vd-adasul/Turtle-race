from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Move forward by 10 units
def move_forward():
    tim.forward(10)

# Move backward by 10 units
def move_backwards():
    tim.backward(10)

# Turn counterclockwise by 5 degrees
def move_ccwise():
    tim.left(5)

# Turn clockwise by 5 degrees
def move_cwise():
    tim.right(5)

# Clear the screen and reset turtle position
def clr_screen():
    tim.clear()  # Clear the drawing, keep turtle and screen listeners
    tim.penup()  # Lift the pen to move without drawing
    tim.home()   # Move to the center (home position)
    tim.pendown()  # Put the pen down to resume drawing

# Setting up the screen to listen for key presses
screen.listen()

# Associating keys with functions
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_ccwise)
screen.onkey(key='d', fun=move_cwise)
screen.onkey(key='c', fun=clr_screen)

# Keep the window open until clicked
screen.exitonclick()
