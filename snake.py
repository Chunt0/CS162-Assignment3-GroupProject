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
    def __init__(self):
        self.head     = turtle.Turtle()
        self.body     = []
        """List of turtle objects representing each body segment."""
        self.length   = 0
        """Length of body segments. Does not count head."""
        self.head.shape('triangle')
        self.head.color("red")
        self.head.penup()
        self.head.direction = "Stop"

#         for idx in range(self.length):
#             segment = turtle.Turtle(shape="circle", visible=False)
#             segment.penup()
# # change colors (from colors list)
#             segment.color("purple")
#             self.body.append(segment)


#[~] I'm not too sure what's going on here, like what is the significance of increasing by 4?
#[~] I think it might be cleaner if we just add one segment for each food eaten and increment the score by 1.
#[~] See addBody() for my suggested method.
#     def increase_length(self, amt=4):
#         self.length += amt
# #        print("Snake length is now:", self.length)
#         for idx in range(amt):
#             segment = turtle.Turtle(shape="circle", visible=False)
#             segment.penup()
#             # change colors (from colors list)
#             segment.color(self.color)
#             self.body.insert(0, segment)
#         self.speed += 1
#         return self.length

#[~]
    def addBody(self):
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple",])
        new_body.color(color)
        new_body.penup()

        # code below may be glitchy #
        # if(self.length > 0):
        #     location = self.body[(self.length-1)].position()
        # else:
        #     location = self.head.position()
        # #############################

        # new_body.goto(location)
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

#[~] It might be that I don't know how the forward() method works in the turtle module
#[~] But in my tests I have found that using the while loop to increment the head and body 
#[~] by a set amount of pixels is more effective when having to also compare the distances
#[~] between the snake, itself, the border, and the food bit. Check my solution in slither()
    # def forward(self):
    #     self.position = self.head.position()
    #     segment = self.body.pop(0)
    #     segment.hideturtle()
    #     segment.goto(self.position)
    #     segment.showturtle()
    #     self.body.append(segment)
    #     self.head.forward(self.speed)

#[~]
    def slither(self):
        
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