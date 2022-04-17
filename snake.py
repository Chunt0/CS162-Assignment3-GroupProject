"""File: snake.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Sarah Mortensen, Christopher Hunt
Date completed: 04/XX/2022
Description: Implements snake object. Handles movements and segmentation.
"""

import turtle
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
        """Adds a turtle object to self.body and increases self.length by 1"""
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
        """Increments each body segments from last to first and then increments the head"""
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

    def ouroboros(self):
        """Checks to see if snake.head is too close to any snake.body"""
        collision = False
        for i in range(0, self.length):
            if (self.body[i].distance(self.head) < 10):
                collision = True
        if collision:
            return True
        else:
            return False

    def out_of_bounds(self):
        """Checks to see if snake.head is out of bounds"""
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if (xcor < -380 or xcor > 380 or ycor < -380 or ycor > 380):
            return True
        else:
            return False