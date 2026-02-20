from turtle import Turtle

class Decoration(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("#90fc03")
        self.pensize(5)
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.create_line()
        
    def create_line(self):
        for _ in range(0, 561):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)