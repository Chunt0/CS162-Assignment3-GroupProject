from chunt_food import Food
from phoenix_scoreboard import Scoreboard
from sarah_snake import Snake
import time, turtle

def createWindow():
    """Creates a new window"""
    window = turtle.Screen()
    window.title("Snake Charmer")
    window.bgcolor("brown")
    window.setup(width=800, height=800)    
    return window

def snakeEatsItself(snake):
    """Checks to see if snake.head is too close to any snake.body"""
    collision = False
    for body in snake.body:
        if (body.distance(snake.head) < 20):
            collision = True
    if collision:
        return True
    else:
        return False

def outOfBounds(xcor, ycor):
    """Checks to see if snake.head is out of bounds"""
    if (xcor > 400 or xcor < -400 or ycor > 400 or ycor < -400):
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
        x_head = snake.head.xcor()
        y_head = snake.head.ycor()
        distance = snake.head.distance(food.food) # How far is the snake head from the food?

        # Is snake out of bounds or eatting itself?
        if(outOfBounds(x_head, y_head) or snakeEatsItself(snake)):
            # Reset Game
            time.sleep(1)
            snake.head.goto(0,0) # Move snake head back to start

            # Get ride of the snake's body
            for segment in snake.body:
                segment.goto((1000,1000))
            snake.body.clear()

            score.resetScore()


        # Is snake eatting food?
        if(food.eatenFood(distance)):
            snake.addBody()
            score.set_score()

        # Increment snake head and body    
        snake.slither()
        time.sleep(.1)