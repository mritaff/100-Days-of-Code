from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("#6cff04")
        self.speed("fastest")
        xcor = random.randint(-250, 250)
        ycor = random.randint(-250, 250)
        self.goto(xcor, ycor)
        self.refresh()
        
    def refresh(self):
        xcor = random.randint(-250, 250)
        ycor = random.randint(-250, 250)
        self.goto(xcor, ycor)
