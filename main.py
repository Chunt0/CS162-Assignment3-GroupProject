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

def createWindow():
    """Creates a new window"""
    window = turtle.Screen()
    window.title("Snake Charmer")
    window.bgcolor("light blue")
    window.setup(width=800, height=800)    
    return window

def snakeEatsItself(snake):
    """Checks to see if snake.head is too close to any snake.body"""
    collision = False
    for i in range(0, snake.length):
        if (snake.body[i].distance(snake.head) < 10):
            collision = True
    if collision:
        return True
    else:
        return False

def outOfBounds(head_position):
    """Checks to see if snake.head is out of bounds"""
    xcor = head_position[0]
    ycor = head_position[1]
    
    if (xcor > 370 or xcor < -370 or ycor > 370 or ycor < -370):
        return True
    else:
        return False

def snakeMain():
    """Main Game program, intializes all variables and starts game loop."""
    window = createWindow()
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

        # Is snake out of bounds?
        if(outOfBounds(head_position)):
            # Reset Game
            time.sleep(1)
            snake.head.goto(0,0) # Move snake head back to start

            # Get ride of the snake's body
            for index in range(0, snake.length):
                snake.body[index].goto(1000,1000)
            snake.body.clear()
            snake.length = 0

            score.reset_score()

        # Is snake eatting food?
        if(food.eatenFood(distance)):
            snake.addBody()
            score += 1 # Using Scoreboard dunder method for "+="

        # Increment snake head and body    
        snake.slither()
        
        if (snakeEatsItself(snake)):
            time.sleep(1)
            snake.head.goto(0,0) # Move snake head back to start

            # Get ride of the snake's body
            for index in range(0,snake.length):
                snake.body[index].goto(1000,1000)
            snake.body.clear()
            snake.length = 0

            score.reset_score()
        
        time.sleep(.1)

if __name__=="__main__":
    snakeMain()