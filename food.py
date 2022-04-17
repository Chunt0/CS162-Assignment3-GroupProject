"""File: food.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Christopher Hunt
Date completed: 04/XX/2022
Description: Implements food object. Detects collision.
"""

import turtle
import random

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.color("black")
        self.food.shape("turtle")
        self.food.speed(0)
        self.food.penup()
        self.food.goto((0,200))

    def eaten_food(self, distance):
        """
        If the distance of the snake is less than 20 pixels from the food
        chooose random x and y coordinates and move the food to that location.
        Then run the add_body() Snake method.
        Return true, this may trigger another event in the driver.
        Else flase.
        """
        if(distance < 20):
            x_loc = random.randint(-370, 370)
            y_loc = random.randint(-370, 370)
            self.food.goto(x_loc, y_loc)
            return True
        else:
            return False