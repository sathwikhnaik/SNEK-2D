from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNEK")
screen.tracer(0)
user_input = screen.textinput(title="Difficulty", prompt="Easy, Medium or Hard")

snake = Snake()
food = Food()
sc = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    if user_input.lower() == "medium":
        time.sleep(0.05)
    elif user_input.lower() == "hard":
        time.sleep(0.03)
    else:
        time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        sc.eat()
        snake.yum()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        sc.game_over()
        break
    if snake.nono():
        game_is_on = False
        sc.game_over()
        break
print(f"Your Score is {sc.score}")

screen.exitonclick()
