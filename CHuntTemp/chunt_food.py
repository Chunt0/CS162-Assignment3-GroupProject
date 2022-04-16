# Christopher Hunt
# CS 162
# Assignment 3

import turtle
import random

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.color("black")
        self.food.shape("square")
        self.food.speed(0)
        self.food.penup()
        self.food.goto((0,200))

    def eatenFood(self, snake, scoreboard):
        """
        If the distance of the snake is less than 20 pixels from the food
        chooose random x and y coordinates and move the food to that location.
        Then run the addBody() Snake method.
        Return true, this may trigger another event in the driver.
        Else flase.
        """
        if(snake.direction(self.food) < 20):
            x_loc = random.randint(-370,370)
            y_loc = random.randint(-370, 370)
            self.food.goto(x_loc, y_loc)
            snake.addBody(scoreboard)
            return True
        else:
            return False


# 
# I think the food class really doesn't need any methods.
# It pretty much should just sit still and do nothing.
# The only time anything should happen is dependent on the snake.
# If the snake gets within a certain distance, the food should
# randomly relocate itself and that is it.

# Score board will need to be updated, and snake length with need to be updated

# perhaps this mock up of a detection function could be added to the snake class?
# or it could be apart of the driver functions


# Take a look:
# ============

# Game mechanic to detect how close the snake is to the food.
# if it is then move the food to a new random location.


#     # This could be turned into a function and added to snake class?
#     		# Adding segment
#     	new_segment = turtle.Turtle()
#     	new_segment.speed(0)
#     	new_segment.shape("cirlce")
#     	new_segment.color(snake.color) 
#     	new_segment.penup()
#     	snake.body.append(new_segment)
    	
#         delay -= 0.001
#     	score += 10 # Add score to the score board
    	
        
#         if score > high_score:
#     		high_score = score
    	
#         # This might use a "pen" created from the scoreboard class, and then use the .write function to update the score
#         pen.clear()
#     	pen.write("Score : {} High Score : {} ".format(
#     		score, high_score), align="center", font=("candara", 24, "bold"))

# 
