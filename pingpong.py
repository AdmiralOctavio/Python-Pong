import turtle
import random as r
wn = turtle.Screen()
wn.title("aaaaaaaaaaaaaaaaaaaaa")
wn.bgcolor("#4400FF")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# moving
ymoveA = 0
ymoveB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(10, 0.5, 3)
paddleA.color("#B0C9FF")
paddleA.penup()
paddleA.setx(350)
paddleA.sety(0)

# Paddle B

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(10, 0.5, 3)
paddleB.color("#B0C9FF")
paddleB.penup()
paddleB.setx(-350)
paddleB.sety(0)

# Ball
ball = turtle.Turtle()

ball.speed(0)
ball.shape("circle")
ball.color("#B0C9FF")

ball.penup()
ball.dx = 2
ball.dy = 2

# Pen DO NOT CHANGE
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier New", 24, "normal"))

# Functions


def paddle_a_up():
    y = paddleA.ycor() + 10
    paddleA.sety(y)


def paddle_a_down():
    y = paddleA.ycor() - 10
    paddleA.sety(y)


def paddle_b_up():
    y = paddleB.ycor() + 10
    paddleB.sety(y)


def paddle_b_down():
    y = paddleB.ycor() - 10
    paddleB.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

yvelBall = 0.3
xvelBall = 0.3

# Main game loop
while True:

    wn.update()

    # Move the ball
    x = ball.xcor() + xvelBall
    ball.setx(x)
    y = ball.ycor() - yvelBall
    ball.sety(y)
    # Border checking

    # Top and bottom
    if ball.ycor() > 600 / 2 - 10:
        ball.sety(270)
        yvelBall = -yvelBall
        y = ball.ycor() - yvelBall
        ball.sety(y)

    elif ball.ycor() < - (600 / 2 - 10):
        ball.sety(-270)
        yvelBall = -yvelBall
        y = ball.ycor() - yvelBall
        ball.sety(y)

    # Left and right
    if ball.xcor() > 800 / 2 - 20:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))
        yvelBall = -yvelBall
        xvelBall = -xvelBall
        ball.setx(0)
        ball.sety(0)

    elif ball.xcor() < -(800 / 2 - 10):
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))
        yvelBall = -yvelBall
        xvelBall = -xvelBall
        ball.setx(0)
        ball.sety(0)

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddleB.ycor() + 100 and ball.ycor() > paddleB.ycor() - 100:
        xvelBall = -xvelBall
        xvelBall += 0.02
        x = ball.xcor() + xvelBall
        ball.setx(x)
        print("Bounce P1 \n", xvelBall, x)

    elif ball.xcor() > 340 and ball.ycor() < paddleA.ycor() + 100 and ball.ycor() > paddleA.ycor() - 100:
        xvelBall = -xvelBall
        xvelBall -= 0.02
        x = ball.xcor() + xvelBall
        ball.setx(x)
        print("Bounce P1 \n", xvelBall, x)
