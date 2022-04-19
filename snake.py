"""File: snake.py
Team No.: 1. THE SNAKE CHARMERS
Author name: Sarah Mortensen, Christopher Hunt
Date completed: 04/19/2022
Description: Implements snake object. Handles movements and segmentation.
"""

import turtle
import random

class Snake:
    """Handle snake creation, movement, and expansion. Detect lose conditions. Assist in ending game with poweroff."""
    def __init__(self,initial_segments:int = 2):
        """Create a snake moving east at origin, with given initial body segments."""
        self.head     = turtle.Turtle()
        self.body     = []
        """List of turtle objects representing each body segment."""
        self.length   = 0  # Only add_body should change this!
        """Length of body segments. Does not count head."""
        self.head.shape('triangle')
        self.head.color("red")
        self.head.penup()
        self.power = turtle.Turtle()
        """Boolean: have we hit the power off button to stop the game?"""
        self.power.hideturtle()

        while (self.length < initial_segments):
            self.add_body()

    def up(self):
        """Sets snake head to 90* (upwards)"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Sets snake heading to 270* (downwards)"""
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        """Sets snake heading to 180* (leftwards)"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Sets snake heading to 0* (right..wards)"""
        if self.head.heading() != 180:
            self.head.setheading(0)

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
        if (xcor < -400 or xcor > 400 or ycor < -400 or ycor > 400):
            return True
        else:
            return False
            
    def power_button(self):
        """Moves self.power to 1000,1000 which will trigger self.power_off()"""
        self.power.goto(1000,1000)
    
    def power_off(self):
        """If self.power was moved then return true, else false. Will be used in snake_main to exit while loop."""
        if (self.power.xcor() > 800):
            return True
        else:
            return False