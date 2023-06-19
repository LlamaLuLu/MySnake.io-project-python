# 18/6/2023

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My_Snake_Game.io")
screen.tracer(0)

# TODO: 1. create snake body
snake = Snake()  # new turtle: 20x20 pixels
food = Food()
score = Score()  # TODO: 5. create scoreboard

# TODO: 3. control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()  # TODO: 2. move snake

    # TODO: 4. detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.new_point()

    # TODO: 6. detect collision with wall
    if not ((-305 < snake.head.xcor() < 290) and (-290 < snake.head.ycor() < 305)):
        game_is_on = False
        score.game_over()

    # TODO: 7. detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
