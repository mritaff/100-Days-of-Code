from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.cars_move = 5
    
    def create_car(self):
        random_chance = random.randint(1 ,6)
        if random_chance == 1:
            ycor = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, ycor)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.cars_move)
            
    def increase_speed(self):
        self.cars_move += MOVE_INCREMENT