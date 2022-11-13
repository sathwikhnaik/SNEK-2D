from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(2, 270)
        self.hideturtle()
        self.pendown()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Constantia", 20, "normal"))

    def updatesc(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Constantia", 20, "normal"))

    def eat(self):
        self.score += 1
        self.clear()
        self.goto(2, 270)
        self.updatesc()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" , move=False, align="center", font=("Chiller", 40, "normal"))


