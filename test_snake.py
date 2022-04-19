"""File: test_snake.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Phoenix Angulo, Sarah Mortensen, Christopher Hunt
Date completed: 04/19/2022
Description: Sloppy testbed for snake movement and segments outside game context
"""

import turtle, snake, time

# Copy-pasting some setup from main in case it changes later
"""Creates a new window"""
window = turtle.Screen()
window.title("Snake Charmer")
window.bgcolor("light blue")
window.setup(width=800, height=800)

window.tracer(0)  # TODO: Evaluate utility
snake = snake.Snake()

# Set up keyboard inputs.
window.listen()
window.onkey(snake.up, "w")
window.onkey(snake.down, "s")
window.onkey(snake.left, "a")
window.onkey(snake.right, "d")

# for incr in range(0, 128):
#    snake.add_body()

while True:
    N = 0.1
    """Tick rate. For now?"""

    window.update()
    # Increment snake head and body
    snake.slither()
    time.sleep(N)
