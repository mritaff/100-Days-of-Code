from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_size = []
        self.create_snake()
    
    def move_up(self):
        if self.snake_size[0].heading() != 270:
            self.snake_size[0].setheading(90)
        
    def move_left(self):
        if self.snake_size[0].heading() != 0:
            self.snake_size[0].setheading(180)
    
    def move_down(self):
        if self.snake_size[0].heading() != 90:
            self.snake_size[0].setheading(270)
        
    def move_right(self):
        if self.snake_size[0].heading() != 180:
            self.snake_size[0].setheading(0)
        
    def create_snake(self):
        for i in range(3):
            t = Turtle(shape="square")
            t.penup()
            t.goto(-20*i, 0)
            t.color("white")
            self.snake_size.append(t)
            
    def move(self):
        for i in range((len(self.snake_size) - 1), 0, -1):
            new_x = self.snake_size[i-1].xcor()
            new_y = self.snake_size[i-1].ycor()
            self.snake_size[i].goto(new_x, new_y)
            
        self.snake_size[0].forward(20)
                