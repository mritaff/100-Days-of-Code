from turtle import Turtle

class ScoreBoard(Turtle):    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()
        
    def increase(self):
        self.score +=1
        self.display_score()
        

