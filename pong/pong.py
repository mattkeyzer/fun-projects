# Pong Game
# By: Matt Keyzer


import turtle
import os

player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")

window = turtle.Screen()

window.title("Pong by: Matt")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Background styling
# circle
fieldcenter = turtle.Turtle()
fieldcenter.goto(0, -75)
fieldcenter.speed(0)
fieldcenter.color("white")
fieldcenter.hideturtle()
fieldcenter.circle(75)
# midline
midline = turtle.Turtle()
midline.goto(0, -300)
midline.speed(0)
midline.color("white")
midline.hideturtle()
midline.setheading(90)
midline.fd(600)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.2
ball.dy = -1.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: {}     {}: {}".format(player1, score_a, player2, score_b), align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


# Keyboard binding
window.onkeyrelease(paddle_a_up, "w")
window.onkeyrelease(paddle_a_down, "s")
window.onkeyrelease(paddle_b_up, "Up")
window.onkeyrelease(paddle_b_down, "Down")
window.listen()

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = 1.2
        ball.dy = -1.2
        ball.dx *= 1
        score_a += 1
        pen.clear()
        pen.write("{}: {}     {}: {}".format(player1, score_a, player2, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay pong/hooray.mp3&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 1.2
        ball.dy = -1.2
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}: {}     {}: {}".format(player1, score_a, player2, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay pong/hooray.mp3&")

    if paddle_a.ycor() > 250:
        paddle_a.goto(-350, 250)

    if paddle_a.ycor() < -250:
        paddle_a.goto(-350, -240)

    if paddle_b.ycor() > 250:
        paddle_b.goto(350, 250)

    if paddle_b.ycor() < -250:
        paddle_b.goto(350, -240)

    # Paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 340) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        # Speed modifier
        ball.dx += -0.2
        os.system("afplay pong/spring.mp3&")

    if (ball.xcor() < -330 and ball.xcor() > -340) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1
        # Speed modifier
        ball.dx += 0.2
        os.system("afplay pong/spring.mp3&")



