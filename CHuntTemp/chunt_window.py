import turtle
import random
import time

def createWindow():
    # Creating a window screen
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("brown")
    window.setup(width=800, height=800)    
    return window

def outOfBounds(snake, scoreboard, food):
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor > 390 or snake.head.ycor < -390:
        time.sleep(1)
        snake.head.goto((0,0))
        for bod in snake.body:
            bod.goto((1000,1000))
        snake.body.clear()
        scoreboard.resetScore()
        food.goto((0,200))

def snakeEatsItself(snake):
    for bod in snake.body:
        if bod.distance(snake.head) < 20:
            time.sleep(1)
            snake.head.goto((0,0))
            for bod in snake.body:
                bod.goto((1000,1000))
            snake.body.clear()
