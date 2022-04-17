"""File: main.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Christopher Hunt
Date completed: 04/XX/2022
Description: Implements the snake game.
"""

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time, turtle

def create_window():
    """Creates a new window"""
    window = turtle.Screen()
    window.title("Snake Charmer")
    window.bgcolor("light blue")
    window.setup(width=800, height=800)    
    return window

def ouroboros(snake):
    """Checks to see if snake.head is too close to any snake.body"""
    collision = False
    for i in range(0, snake.length):
        if (snake.body[i].distance(snake.head) < 10):
            collision = True
    if collision:
        return True
    else:
        return False

def out_of_bounds(head_position):
    """Checks to see if snake.head is out of bounds"""
    xcor = head_position[0]
    ycor = head_position[1]
    
    if (xcor > 370 or xcor < -370 or ycor > 370 or ycor < -370):
        return True
    else:
        return False

def reset_game(snake: Snake, score: Scoreboard):
    """Destroy the snake body, set it to origin, and set score to 0."""
    time.sleep(1)
    snake.head.goto(0,0) # Move snake head back to start

    # Get rid of the snake's body
    for index in range(0,snake.length):
        snake.body[index].goto(1000,1000)
    snake.body.clear()
    snake.length = 0

    score.reset_score()

def reset_game(snake, score):
    """Destroy the snake body, set it to origin, add two bodies, and set score to 0."""
    time.sleep(1)
    snake.head.goto(0,0) # Move snake head back to start

    # Get rid of the snake's body
    for index in range(0,snake.length):
        snake.body[index].goto(1000,1000)
    snake.body.clear()
    snake.length = 0
    score.reset_score()
    for _ in range(2):
        snake.add_body()

def snake_main():
    """Main Game program, intializes all variables and starts game loop."""
    window = create_window()
    window.tracer(0)
    food = Food()
    snake = Snake()
    score = Scoreboard()

    # Set up keyboard inputs.
    window.listen()
    window.onkey(snake.up, 'w')
    window.onkey(snake.down, 's')
    window.onkey(snake.left, 'a')
    window.onkey(snake.right, 'd')

    while True:
        window.update()

        # Get Location of the snake's head 
        head_position = snake.head.position()
        distance = snake.head.distance(food.food) # How far is the snake head from the food?

        # Is snake eating food?
        if(food.eaten_food(distance)):
            snake.add_body()
            score += 1 # Using Scoreboard dunder method for "+="

        # Increment snake head and body    
        snake.slither()

        #Two lose conditions: out of bounds or autocannibalism
        if (out_of_bounds(head_position) or ouroboros(snake)):
            reset_game(snake, score)
        
        time.sleep(.1)

if __name__=="__main__":
    snake_main()