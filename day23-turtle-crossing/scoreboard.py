from turtle import Turtle
FONT = ("Courier", 20, "normal")
GAME_OVER = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_score()
        
    def create_score(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-220, 265)
    
    def display_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font = FONT)
        
    def increase_score(self):
        self.score += 1
        
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font = GAME_OVER)