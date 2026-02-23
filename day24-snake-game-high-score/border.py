from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("red")
        self.penup()
        self.goto(-260, -260)
        self.pendown()
        for _ in range (4):
            self.forward(520)
            self.left(90)