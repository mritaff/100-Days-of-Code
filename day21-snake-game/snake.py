from turtle import Turtle
class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]
        self.tail = self.body_parts[-1]
    
    def move_up(self):
        if self.body_parts[0].heading() != 270:
            self.body_parts[0].setheading(90)
        
    def move_left(self):
        if self.body_parts[0].heading() != 0:
            self.body_parts[0].setheading(180)
    
    def move_down(self):
        if self.body_parts[0].heading() != 90:
            self.body_parts[0].setheading(270)
        
    def move_right(self):
        if self.body_parts[0].heading() != 180:
            self.body_parts[0].setheading(0)
        
    def create_snake(self):
        for i in range(3):
            new_body_part = Turtle(shape="square")
            new_body_part.penup()
            new_body_part.goto(-20*i, 0)
            new_body_part.color("white")
            self.body_parts.append(new_body_part)
    
    def increase_size(self):
        last_part = len(self.body_parts) - 1
        xcor_end = self.body_parts[last_part].xcor()
        ycor_end = self.body_parts[last_part].ycor()
        
        new_body_part = Turtle(shape="square")
        new_body_part.penup()
        new_body_part.goto(xcor_end, ycor_end)
        new_body_part.color("white")
        self.body_parts.append(new_body_part)            
            
    def move(self):
        for i in range((len(self.body_parts) - 1), 0, -1):
            new_x = self.body_parts[i-1].xcor()
            new_y = self.body_parts[i-1].ycor()
            self.body_parts[i].goto(new_x, new_y)
            
        self.body_parts[0].forward(20)
                
