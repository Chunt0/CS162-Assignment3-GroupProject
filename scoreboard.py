"""File: scoreboard.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Phoenix Angulo, Christopher Hunt
Date completed: 04/16/2022
Description: Implements the scoreboard for the snake game, with methods to update and display game over
"""

import turtle


class Scoreboard:
    """Handles score-keeping, writing, and game-over display for Snake."""

    def __init__(self, coords: turtle.Vec2D = (0, 300)):
        """Initialize invisible turtle and write score at given coordinates.

        Args:
        coords (Tuple/Vec2D): Ordered pair of signed ints as (x,y).
            Score will be written near here, but game_over doesn't care.
        """
        self.score = 0
        """The games' score. Intended to be natural numbers only."""

        self.cursor = turtle.Turtle()
        """Invisible Turtle. Written text is created nearby it."""

        # Ready & Move to Starting Co-ordinates
        self.cursor.hideturtle()  # [~] You could still see the turtle shape, use this to hide it.
        self.cursor.penup()
        self.cursor.goto(coords)

        self.update()  # First write (should always be 0)

    def update(self):
        """Redraw score. Best used internally."""
        self.cursor.clear()
        self.cursor.write(
            arg=self.score,
            align="Center",
            font=("Comic Sans", 42, "normal"),
            move=False,
        )

    def set_score(self, new_score: int):
        """Accept new score and redraw the board.

        Args:
        new_score (int): Should be a natural number. Can be a signed int.
        """
        # We could separate these tasks, but let's eliminate desynchronization risk
        self.score = new_score
        self.update()

    def increment_score(self, increment: int):
        """Change score by increment and redraw the board.

        Args:
        increment (int): Any integer. Negatives will decrease score.
        """
        # Equivalent to iadd, just as a method instead of operator
        self.score += increment
        self.update()

    def __iadd__(self, addend: int):
        """Incremental-add Operator equivalent to increment_score."""
        """Scoreboard += 1 would increment the score variable and rewrite the board itself"""
        self.score += addend
        self.update()
        return self

    def game_over(self):
        """Erase scoreboard and draw game-over screen."""
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

    def reset_score(self):  # [~] Added this function. -chunt
        """Set score to 0 and redraw board. Equivalent to set_score(0)."""
        self.score = 0
        self.update()
        return True
