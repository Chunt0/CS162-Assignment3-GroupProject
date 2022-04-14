import turtle
from chunt_food import Food
from chunt_scoreboard import ScoreBoard

def createGameWindow():
    # move this into a screen class
    # Creating a window screen
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("light blue")
    # the width and height can be put as user's choice
    window.setup(width=800, height=800)
    return window

window = createGameWindow()
score = ScoreBoard()
food = Food()
window.exitonclick()

