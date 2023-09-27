import turtle
import time

# Create the game window
window = turtle.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Turns off the screen updates

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=10)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # Ball's x-axis movement speed
ball.dy = 1  # Ball's y-axis movement speed

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for row in range(5):
    for col in range(10):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.penup()
        brick.shapesize(stretch_wid = 1, stretch_len = 2)
        brick.goto(-390 + col * 80, 250 - row * 25)
        bricks.append(brick)

# Create the score display
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))


# Function to move the paddle left
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)


# Function to move the paddle right
def move_paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)


# Keyboard bindings
window.listen()
window.onkeypress(move_paddle_left, "Left")
window.onkeypress(move_paddle_right, "Right")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for border collisions
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    elif ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Check for paddle collision
    if (ball.ycor() < -240) and (ball.ycor() > -310) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    # Check for brick collisions
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)  # Move the brick off-screen
            bricks.remove(brick)  # Remove the brick from the list
            ball.dy *= -1  # Reverse the ball's y-axis direction
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
							

    # Check for game over
    if len(bricks) == 0 or ball.ycor() < -310:
      break

