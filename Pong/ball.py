from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.shapesize(1, 1, 0)
        self.velocity = 10

    def move(self):
        self.forward(self.velocity)

    def fast(self):
        self.velocity += 0.1

    def set_direction(self):
        self.velocity = 10
        self.setheading(random.choice([45, 135, 225, 315]))
        time.sleep(0.5)
