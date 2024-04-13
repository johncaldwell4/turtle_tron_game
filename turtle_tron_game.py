import turtle

# Create the screen
screen = turtle.Screen()
screen.setup(width=1600, height=900)
screen.bgcolor("black")

# Create the turtles
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.turtlesize(3, 3, 3)
turtle1.penup()
turtle1.goto(-750, -0)

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("blue")
turtle2.turtlesize(3, 3, 3)
turtle2.penup()
turtle2.goto(750, 0)
turtle2.left(180)

# Create the game loop
while True:

    # Move the turtles
    turtle1.forward(10)
    turtle2.forward(10)

    # Check if the turtles have collided
    if turtle1.distance(turtle2) < 20:
        break

# End the game
screen.exitonclick()
