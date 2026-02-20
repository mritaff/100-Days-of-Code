from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#b405ff")
        self.shapesize(0.7, 0.7)
        self.penup()
        self.y_move = 3
        self.x_move = 3
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def returning_center(self):
        self.home()
        self.move_speed = 0.1
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed = 0.1