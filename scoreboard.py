from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(2, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Constantia", 20, "normal"))

    def updatesc(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Constantia", 20, "normal"))

    def eat(self):
        self.score += 1
        self.clear()
        self.goto(2, 270)
        self.updatesc()

    def game_over(self):
        self.goto(0, 20)
        self.color("Red")
        self.write("GAME OVER", move=False, align="center", font=("Chiller", 40, "normal"))
        self.goto(0, -20)
        self.write(f"Your Score is {self.score}", move=False, align="center", font=("Chiller", 40, "normal"))
        self.goto(0, -280)
        self.write("Made by Zikron", move=False, align="center", font=("Comic Sans MS", 15, "normal"))
