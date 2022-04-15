"""File: test_scoreboard.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Phoenix Angulo, Sarah Mortensen
Date completed: 04/XX/2022
Description: Sloppy testbed for the scoreboard object outside game context
"""
import turtle, utils, time, scoreboard as sb


board = sb.Scoreboard((40, 200))

for i in range(0, 1000 // 10):  # If the player goes above the 1000s I will eat my hat
    time.sleep(0.1)
    board += 11


"""Mostly made with Sarah's code I've hacked together"""


def stop():
    done = True


# Initialize screen
done = False
map = turtle.Screen()
map.bgcolor("green")

# Set up keyboard inputs.
map.onkey(stop, "q")
map.listen()

map.mainloop()
