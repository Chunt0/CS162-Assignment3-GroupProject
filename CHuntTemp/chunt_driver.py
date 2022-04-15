from chunt_food import Food
from chunt_scoreboard import ScoreBoard
from chunt_snake import Snake
from chunt_create_window import createGameWindow
import time

window = createGameWindow()
score = ScoreBoard()
food = Food()
snake = Snake()


# Set up keyboard inputs.
window.listen()
window.onkey(snake.up, 'w')
window.onkey(snake.down, 's')
window.onkey(snake.left, 'a')
window.onkey(snake.right, 'd')


score.rewrite()

window.exitonclick()