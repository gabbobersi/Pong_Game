from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize_turtle()

    def initialize_turtle(self):
        super().speed(0)
        super().shape('square')
        super().shapesize(5, 1)
        super().color('white')
        super().penup()

    def borders_check(self):
        # If a paddle hits a certain point, it stops.
        if self.ycor() <= - 230:
            self.sety(self.ycor() + 10)
            
        if self.ycor() <= - 230:
            self.sety(self.ycor() + 10)

        if self.ycor() >= 230:
            self.sety(self.ycor() - 10)
            
        if self.ycor() >= 230:
            self.sety(self.ycor() - 10)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)
