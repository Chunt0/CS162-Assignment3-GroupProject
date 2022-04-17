"""File: main.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Christopher Hunt, Phoenix Angulo, Sarah Mortensen
Date completed: 04/XX/2022
Description: Implements the snake game.
"""

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from window import create_window
import time

def snake_main():
    """Main Game program, intializes all variables and starts game loop."""
    window = create_window()
    window.tracer(0)
    score = Scoreboard()
    snake = Snake()
    food = Food()

    # Set up keyboard inputs.
    window.listen()
    window.onkey(snake.up, 'w')
    window.onkey(snake.down, 's')
    window.onkey(snake.left, 'a')
    window.onkey(snake.right, 'd')

    while True:
        window.update()

        # Is snake eating food?
        if(food.eaten_food(snake)):
            snake.add_body()
            score += 1 # Using Scoreboard dunder method for "+="

        # Increment snake head and body    
        snake.slither()

        # Two lose conditions: out of bounds or autocannibalism
        if (snake.out_of_bounds() or snake.ouroboros()):
            score.reset_game(snake)
        
        time.sleep(.1)

if __name__=="__main__":
    snake_main()