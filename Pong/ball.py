from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.shapesize(1, 1, 0)
        self.velocit = 10

    def move(self):
        self.forward(self.velocit)

    def fast(self):
        self.velocit += 0.1
