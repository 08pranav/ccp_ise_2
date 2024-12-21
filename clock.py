import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Clock")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Set up the clock face turtle
clock_face = turtle.Turtle()
clock_face.hideturtle()
clock_face.speed(0)

# Set up the hands
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

for hand in [hour_hand, minute_hand, second_hand]:
    hand.shape("arrow")
    hand.shapesize(stretch_wid=0.4, stretch_len=10)
    hand.speed(0)
    hand.penup()
    hand.color("black")

# Function to draw the clock face
def draw_clock_face():
    clock_face.penup()
    clock_face.goto(0, -250)
    clock_face.pendown()
    clock_face.circle(250)

    # Draw numbers on the clock
    clock_face.penup()
    for i in range(1, 13):
        angle = 360 * i / 12  # Divide circle into 12 sections
        clock_face.goto(0, 0)  # Reset to center
        clock_face.setheading(90 - angle)  # Adjust heading to place text correctly
        clock_face.forward(210)  # Move slightly closer to the center for the numbers
        clock_face.write(str(i), align="center", font=("Times New Roman", 18, "normal"))
        clock_face.backward(210)  # Return to the center for the next number

# Function to update the hands
def update_hands():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Calculate angles for each hand
        hour_angle = (360 / 12) * (hour % 12 + minute / 60)
        minute_angle = (360 / 60) * minute
        second_angle = (360 / 60) * second

        # Update hands
        hour_hand.setheading(90 - hour_angle)
        minute_hand.setheading(90 - minute_angle)
        second_hand.setheading(90 - second_angle)

        time.sleep(1)

# Draw the clock face and start the clock
draw_clock_face()
update_hands()

screen.mainloop()