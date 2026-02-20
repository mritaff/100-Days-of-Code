from turtle import Turtle

class Score:
    def __init__(self):
        self.scores = []
        self.score_one = 0
        self.score_two = 0
        self.create_scores()
        
    def create_scores(self):
        coordinates = [(-140, 270), (140, 270)]
        for i in range(2):
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.color("white")
            t.goto(coordinates[i])
            self.scores.append(t)
    
    def display_score(self):
        self.scores[0].clear()
        self.scores[1].clear()
        self.scores[0].write(f"{self.score_one}", align="center", font=("Arial", 20, "normal"))
        self.scores[1].write(f"{self.score_two}", align="center", font=("Arial", 20, "normal"))
    
    def increase_score_one(self):
        self.score_one += 1
    
    def increase_score_two(self):
        self.score_two += 1