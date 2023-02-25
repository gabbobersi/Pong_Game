import turtle

from paddle import Paddle
from ball import Ball

paddle_a = Paddle()
paddle_a.goto(-350, 0)

paddle_b = Paddle()
paddle_b.goto(350, 0)

ball = Ball()
ball.goto(0, 0)

score_a = 0
score_b = 0

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed("slowest")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write(f'Player A: {score_a}\tPlayer B: {score_b}', align='center', font=('Courier', 24, "normal"))

# Keyboard binding
window.listen()
window.onkeypress(paddle_a.move_up, "w")
window.onkeypress(paddle_a.move_down, "s")
window.onkeypress(paddle_b.move_up, "Up")
window.onkeypress(paddle_b.move_down, "Down")

def update_scores_board(score_a: int, score_b: int):
        pen.clear()
        pen.write(f'Player A: {score_a}\tPlayer B: {score_b}', align='center', font=('Courier', 24, "normal"))

# Main game loop
while True:
    window.update()

    ball.move()

    paddle_a.borders_check()
    paddle_b.borders_check()
    
    point_a, point_b = ball.borders_check()
    score_a += point_a
    score_b += point_b
    update_scores_board(score_a, score_b)

    # Collisions between ball and paddles
    if (340 < ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 50) and \
            (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.x *= -1

    if (-350 < ball.xcor() < - 340) and \
            (ball.ycor() < paddle_a.ycor() + 50) and \
            (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.x *= -1