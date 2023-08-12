from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_Board
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score_Board()

sc.listen()
sc.onkey(snake.up, "w")
sc.onkey(snake.down, "s")
sc.onkey(snake.left, "a")
sc.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # DEtect collision With Foood

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with Walls
    if snake.head.xcor() > 281 or snake.head.xcor() < -281 or snake.head.ycor() > 281 or snake.head.ycor() < -281:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision With Tail
    for tail in snake.new_segments: ## for tail in snake.new_segments[1:]:
        if tail == snake.head: #{
            pass                 #    }
        elif snake.head.distance(tail) < 10:
            game_is_on = False
            scoreboard.game_over()

sc.exitonclick()
