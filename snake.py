"""File: snake.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Sarah Mortensen, Christopher Hunt
Date completed: 04/XX/2022
Description: Implements snake object. Handles movements and segmentation.
"""

import turtle
import utils
import random

class Snake:
    def __init__(self,initial_segments:int = 2):
        self.head     = turtle.Turtle()
        self.body     = []
        """List of turtle objects representing each body segment."""
        self.length   = 0  #Only add_body should change this!
        """Length of body segments. Does not count head."""
        self.head.shape('triangle')
        self.head.color("red")
        self.head.penup()

        while (self.length < initial_segments):
            self.add_body()

    def add_body(self):
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple",])
        new_body.color(color)
        new_body.penup()
        self.body.append(new_body)
        self.length += 1

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def slither(self):
        # Move body of snake
        for index in range(self.length-1, 0, -1): # Cycle from last in list to first
            x = self.body[index-1].xcor()
            y = self.body[index-1].ycor()
            self.body[index].goto(x, y)
        if self.length > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.body[0].goto(x, y)
        # Move head of snake
        self.head.forward(20)

