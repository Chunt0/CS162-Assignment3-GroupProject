import turtle

def createWindow():
    # Creating a window screen
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("brown")
    window.setup(width=800, height=800)    # the width and height can be put as user's choice
    return window
        # # Set up keyboard inputs.
        # window.listen()
        # window.onkey(snake.up, 'w')
        # window.onkey(snake.down, 's')
        # window.onkey(snake.left, 'a')
        # window.onkey(snake.right, 'd')
    
