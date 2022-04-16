# Christopher Hunt
# CS 162
# Assignment 3

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

def outOfBounds(xcor, ycor):
    if (xcor > 390 or xcor < -390 or ycor > 390 or ycor < -390):
        return True
    else:
        return False

def snakeEatsItself(snake):
    collision = False
    for bod in snake.body:
        if bod.distance(snake.head) < 20:
            collision = True
    if collision:
        return True
    else:
        return False

