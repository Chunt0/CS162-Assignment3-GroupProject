"""File: scoreboard.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Phoenix Angulo, Christopher Hunt
Date completed: 04/XX/2022
Description: Implements the scoreboard for the snake game, with methods to update and display game over
"""

import turtle


class Scoreboard:
    def __init__(self, coords=(0, 300)):
        self.score = 0

        """
        Moves to starting coords
        """
        self.cursor = turtle.Turtle()
        self.cursor.hideturtle()  # [~] You could still see the turtle shape, use this to hide it.
        self.cursor.penup()
        self.cursor.goto(coords)

        self.update()  # First write (should always be 0)

    def update(self):
        """Redraws score. Best used internally."""
        self.cursor.clear()
        self.cursor.write(
            arg=self.score,
            align="Center",
            font=("Comic Sans", 42, "normal"),
            move=False,
        )

    def set_score(self, new_score: int):
        """Accepts new score and redraws"""
        # We could separate these tasks, but let's eliminate desynchronization risk
        self.score = new_score
        self.update()

    def increment_score(self, increment: int):
        """Changes score by increment and redraws"""
        # Equivalent to iadd, just as a method instead of operator
        self.score += increment
        self.update()

    def __iadd__(self, addend: int):
        """Allows the scoreboard to be incremented by an integer"""
        # Scoreboard += 1 would increment the score variable and rewrite the board itself
        self.score += addend
        self.update()
        return self

    def game_over(self):
        """TODO: This. Need some sort of game-over routine as per requirements."""

        Y_ORIGIN = 80
        """Turtle starts here when writing the big game-over, then moves down."""

        self.cursor.clear()
        self.cursor.goto(0, Y_ORIGIN)
        self.cursor.write(
            arg="Game Over!", align="Center", font=("Comic Sans", 96, "bold")
        )
        self.cursor.goto(x=0, y=(Y_ORIGIN - 40))
        self.cursor.write(
            arg=f"Your final score was: {self.score}",
            align="Center",
            font=("Comic Sans", 24, "normal"),
        )

    # [~] Added this function. -chunt
    def resetScore(self):
        """Resets Scoreboard"""
        self.score = 0
        self.update()
        return True
