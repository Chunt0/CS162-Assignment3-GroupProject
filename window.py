"""File: food.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Christopher Hunt
Date completed: 04/19/2022
Description: Function that creates and returns the game window.
"""

import turtle

def create_window():
    """Create a new window for the snake game."""
    window = turtle.Screen()
    window.title("Snake Charmer")
    window.bgcolor("light blue")
    window.setup(width=800, height=800)    
    return window

