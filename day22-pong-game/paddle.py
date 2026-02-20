from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#ff6600")
        self.penup()
        self.goto(position * 350, 0)
        self.shapesize(5, 1)
        
    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)
    
    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)