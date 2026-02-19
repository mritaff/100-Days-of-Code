from turtle import Turtle

class ScoreBoard(Turtle):    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.pencolor("red")
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))
        
    def increase(self):
        self.score +=1
        self.display_score()
