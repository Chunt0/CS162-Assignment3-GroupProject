from chunt_food import Food
from phoenix_scoreboard import Scoreboard
from sarah_snake import Snake
import time, turtle

def createWindow():
    # Creating a window screen
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("brown")
    window.setup(width=800, height=800)    
    return window

def snakeEatsItself(snake):
    collision = False
    for bod in snake.body:
        if bod.distance(snake.head) < 20:
            collision = True
    if collision:
        return True
    else:
        return False


def outOfBounds(xcor, ycor):
    if (xcor > 390 or xcor < -390 or ycor > 390 or ycor < -390):
        return True
    else:
        return False

def snakeMain():
    window = createWindow()
    #window.tracer(0)
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
        distance = int(snake.head.distance(food.food)) # How far is the snake head from the food?

        # Is snake out of bounds or eatting itself?
        if(outOfBounds(x_head, y_head) or snakeEatsItself(snake)):
            # Reset Game
            time.sleep(1)
            snake.head.goto((0,0)) # Move snake head back to start

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
