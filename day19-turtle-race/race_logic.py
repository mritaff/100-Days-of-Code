from turtle import Turtle, Screen
import random

class TurtleRace:
    def __init__(self):
        self.colors = ["red", "yellow", "green", "blue", "black", "pink"]
        self.finish_line = 600
        self.turtles = []
        self.create_runners()
        
    def create_runners(self):
        for i, color in enumerate(self.colors):
            t = Turtle(shape="turtle")
            t.color(color)
            t.penup()
            t.goto(-600, (i-2)*70)
            t.pendown()
            t.speed("fast")
            self.turtles.append(t)
    
    def running(self):
        is_on_race = True
        while is_on_race:
            for turtle in self.turtles:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)
                if turtle.xcor() >= self.finish_line:
                    is_race_over = True
                    winner = turtle.pencolor()
                    return winner, is_race_over
                    
    def results(self, winner, user_bet):
        if user_bet.lower() == winner:
            print(f"Congratulations! The {winner} turtle won the race!")
        else:
            print(f"Too bad... Your bet lost. The {winner} turtle was the winner!")