import turtle
from chunt_food import Food

def createGameWindow():
    # move this into a screen class
    # Creating a window screen
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("light blue")
    # the width and height can be put as user's choice
    window.setup(width=600, height=600)
    window.tracer(0)
    return window

window = createGameWindow()
food = Food()
window.exitonclick()

