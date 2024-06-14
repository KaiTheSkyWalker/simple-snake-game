from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Owen's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# control the direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


flag = True
while flag:
    screen.update()
    snake.move() 
    time.sleep(0.1) # refresh rate of 0.1 second

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    elif snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # flag = False

    for segment in snake.array:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # for segment in snake.array[1::]: # except for the head, check for the rest of the segments
    #     if snake.head.distance(segment) < 10:
    #         # game_is_on = False
    #         # scoreboard.game_over()
    #         scoreboard.reset()
    #         snake.reset()

screen.exitonclick()
