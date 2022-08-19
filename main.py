import time
import turtle
import math
import logging


window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


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
ball.speed("slowest")
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball_x = math.sin(2)
ball_y = math.cos(2)

# Scores
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed("slowest")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write(f'Player A: {score_a}\tPlayer B: {score_b}', align='center', font=('Courier', 24, "normal"))


def paddle_up(obj: turtle.Turtle):
    y = obj.ycor()
    y += 20
    obj.sety(y)


def paddle_down(obj: turtle.Turtle):
    y = obj.ycor()
    y -= 20
    obj.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(lambda paddle=paddle_a: paddle_up(paddle), "w")
window.onkeypress(lambda paddle=paddle_a: paddle_down(paddle), "s")

window.onkeypress(lambda paddle=paddle_b: paddle_up(paddle), "Up")
window.onkeypress(lambda paddle=paddle_b: paddle_down(paddle), "Down")


# Main game loop
while True:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Border check - If ball hits a certain point, it bounces.
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1

    if ball.xcor() > 390:
        ball_x *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a}\tPlayer B: {score_b}', align='center', font=('Courier', 24, "normal"))

    if ball.xcor() < - 390:
        logging.debug("Hit!")
        ball_x *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}\tPlayer B: {score_b}', align='center', font=('Courier', 24, "normal"))

    # Collision between ball and paddle
    if (340 < ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 50) and \
            (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball_x *= -1

    if (-350 < ball.xcor() < - 340) and \
            (ball.ycor() < paddle_a.ycor() + 50) and \
            (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball_x *= -1

    time.sleep(0.0002)      # "Fixed extra ugly FPS on my machine..." It can be remove maybe. Turtle doesn't handles FPS?
