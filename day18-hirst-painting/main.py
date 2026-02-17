from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

t = Turtle()
t.speed("fastest")
t.hideturtle()

screen = Screen()
screen.colormode(255)
screen.title("Hirst painting")

height = screen.window_height()
width = screen.window_width()

for y in range(((-1) * (height//2) + 70), (height//2), 70):
    for x in range (((-1) * (width//2) + 70), (width//2), 70):
        # If the python's version is 3.12 can use t.teleport()
        t.color(random.choice(rgb_colors))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(20)
    
screen.exitonclick()
