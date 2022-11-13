from turtle import Turtle
import random

COLOR_LIST = ["Blue", "Green", "Red", "Yellow", "Violet", "Aqua", "Purple", "Pink", "Magenta", "Cyan"]
FOOD_LIST = ["circle", "turtle"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(FOOD_LIST))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR_LIST))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLOR_LIST))
        self.shape(random.choice(FOOD_LIST))
        rx = random.randint(-270, 270)
        ry = random.randint(-270, 270)
        self.goto(rx, ry)
