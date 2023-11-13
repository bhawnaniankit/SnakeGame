from snake import Snake
from turtle import Screen
import time
from food import Food
from score_board import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
snake1=Snake()
score_board=ScoreBoard()
screen.listen()
food=Food()
score_board.score_write()
while snake1.alive:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    screen.onkey(snake1.snake_up,"Up")
    screen.onkey(snake1.snake_down,"Down")
    screen.onkey(snake1.snake_left,"Left")
    screen.onkey(snake1.snake_right,"Right")
    if snake1.snake[0].distance(food)<15:
        food.refresh()
        score_board.Score_update()
        snake1.add_seg()
else:
    score_board.highScore()
    score_board.game_over()
        
screen.exitonclick()   