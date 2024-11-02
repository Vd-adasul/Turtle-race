from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Add available colors to the prompt
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you bet on? Choose from red, green, blue, yellow, violet:").lower()
colors = ['red', 'green', 'blue', 'yellow', 'violet']

# Create turtles and set their starting positions
turtles = []
y_positions = [-100, -50, 0, 50, 100]

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

# Start the race if user placed a bet
if user_bet:
    is_race_on = True

# Main loop to move the turtles
while is_race_on:
    for turtle in turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Print the result of the race
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

            break  # Stop the loop once we have a winner

        # Move the turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
