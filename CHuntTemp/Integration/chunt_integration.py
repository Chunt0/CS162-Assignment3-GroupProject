from chunt_food import Food
from chunt_window import createWindow, outOfBounds, snakeEatsItself
from phoenix_scoreboard import Scoreboard
from sarah_snake import Snake
import utils

score = Scoreboard()
food = Food()
snake = Snake()
window = createWindow()


# Set up keyboard inputs.
window.listen()
window.onkey(snake.up, 'w')
window.onkey(snake.down, 's')
window.onkey(snake.left, 'a')
window.onkey(snake.right, 'd')

