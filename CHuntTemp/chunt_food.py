import turtle
import utils
import random

class Food():
    def __init__(self):
        self.food = turtle.Turtle()
        self.color = random.choice(["black", "red", "blue"])
        self.shape = "turtle"
        self.food.hideturtle()
        self.food.penup()


"""
Game mechanic to detect how close the snake is to the food.
if it is then move the food to a new random location.

def checkSnakeDistFromFood(snake):
    if snake.distance(food) < 20:
    	x = random.randint(-270, 270) # these values can change, depends on how large our screen is to begin
    	y = random.randint(-270, 270) # same as above
    	food.goto(x, y) # relocate food turtle


    # This could be turned into a function and added to snake class?
    		# Adding segment
    	new_segment = turtle.Turtle()
    	new_segment.speed(0)
    	new_segment.shape("cirlce")
    	new_segment.color(snake.color) 
    	new_segment.penup()
    	snake.body.append(new_segment)
    	delay -= 0.001
    	score += 10
    	if score > high_score:
    		high_score = score
    	pen.clear()
    	pen.write("Score : {} High Score : {} ".format(
    		score, high_score), align="center", font=("candara", 24, "bold"))

"""
