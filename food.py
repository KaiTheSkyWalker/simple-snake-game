from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")

    def refresh(self):
        new_x = randint(-270, 270)
        new_y = randint(-270, 270)
        self.goto(new_x, new_y)
