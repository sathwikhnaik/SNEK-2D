from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.adds(position)

    def adds(self, position):
        t = Turtle()
        t.shape("square")
        t.color("White")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def yum(self):
        self.adds(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            nx = self.turtles[i - 1].xcor()
            ny = self.turtles[i - 1].ycor()
            self.turtles[i].goto(nx, ny)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def nono(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            if self.turtles[i].distance(self.head) < 15:
                return True
