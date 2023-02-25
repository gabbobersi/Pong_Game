import math

from turtle import Turtle

class Ball(Turtle):
    x = math.sin(2)
    y = math.cos(2)
    
    def __init__(self):
        super().__init__()
        self.initialize_turtle()

    def initialize_turtle(self):
        super().speed("slowest")
        super().shape("circle")
        super().color("red")
        super().penup()

    def borders_check(self):
        # If ball hits a certain point, it bounces.
        a_score = 0
        b_score = 0
        if self.ycor() > 290:
            self.sety(290)
            self.y *= -1

        if self.ycor() < -290:
            self.sety(-290)
            self.y *= -1

        if self.xcor() > 390:
            self.x *= -1
            a_score = 1

        if self.xcor() < - 390:
            self.x *= -1
            b_score = 1
        
        return a_score, b_score

    def move(self):
        self.setx(self.xcor() + self.x)
        self.sety(self.ycor() + self.y)
