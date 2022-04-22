"""File: main.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Christopher Hunt, Phoenix Angulo, Sarah Mortensen
Date completed: 04/19/2022
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
    power_on = True

    # Set up keyboard inputs.
    window.listen()
    window.onkey(snake.up, 'w')
    window.onkey(snake.down, 's')
    window.onkey(snake.left, 'a')
    window.onkey(snake.right, 'd')
    window.onkey(snake.power_button, 'q') # Press 'q' to exit game cleanly

    while power_on:
        window.update()

        # Is snake eating food?
        if(food.eaten_food(snake)):
            score += 1 # Using Scoreboard dunder method for "+="

        # Increment snake head and body    
        snake.slither()

        # Two lose conditions: out of bounds or autocannibalism
        if (snake.out_of_bounds() or snake.ouroboros()):
            score.game_over()
            time.sleep(2)
            score.reset_game(snake)

        # Checks to see if 'q' was pressed. If so, exit program cleanly.
        if(snake.power_off()):
            score.game_over()
            time.sleep(2)
            power_on = False

        time.sleep(.1) # Helps to make the game play at a reasonable speed

if __name__=="__main__":
    snake_main()
