"""File: test_scoreboard.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Phoenix Angulo, Sarah Mortensen
Date completed: 04/XX/2022
Description: Sloppy testbed for the scoreboard object outside game context
"""
import turtle, time, scoreboard as sb

"""Mostly made with Sarah's code I've hacked together"""
# Initialize screen
map = turtle.Screen()
map.setup(width=800, height=800)
map.bgcolor("red")

board = sb.Scoreboard((40, 200))
# What's this even do?
# map.mainloop()

# ugly tests of set_score, increment score
board.set_score(42000)
time.sleep(2)
board.increment_score(-40000)
time.sleep(2)
board.increment_score(8000)
time.sleep(2)

# Longer draw test
board.set_score(0)
for i in range(0, 1000 // 10):  # If the player goes above the 1000s I will eat my hat
    time.sleep(0.1)
    board += 11
time.sleep(3)

# Gameovertest
board.game_over()
time.sleep(3)
board.set_score(50000)  # Big score test. Will it look okay still?
board.game_over()

map.bgcolor("green")  # Done!
time.sleep(5)
