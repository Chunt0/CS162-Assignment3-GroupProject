from chunt_food import Food
from chunt_scoreboard import ScoreBoard
from chunt_window import createWindow, outOfBounds
from chunt_snake import Snake


score = ScoreBoard()
food = Food()
snake = Snake()
window = createWindow()


# Set up keyboard inputs.
window.listen()
window.onkey(snake.up, 'w')
window.onkey(snake.down, 's')
window.onkey(snake.left, 'a')
window.onkey(snake.right, 'd')

while True:
    window.update()
    score.updateScore()

    if(outOfBounds(snake)): # Checks to see if snake is out of bounds
        pass

    if(food.eatenFood(snake,score)): # checks to see if snake has moved within 20 pixels of "food"
        pass
    
    snake.slither()
    # Now update body


