# Christopher Hunt
# CS 162
# Assignment 3

import turtle
import random

class Snake:
    def __init__(self):
        """ This only runs once """
        self.head = turtle.Turtle()
        self.speed = 5
        self.body = []
        self.head.shape("triangle")
        self.head.color("red")
        self.head.penup()
        self.head.speed(0)

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

    def forward(self):
        self.position = self.head.position()
        segment = self.body.pop(0)
        segment.goto(self.position)
        segment.showturtle()
        self.body.append(segment)
        self.head.forward(self.speed)
    
    def addBody(self, scoreboard):
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple",])
        new_body.color(color)
        new_body.penup()
        self.body.append(new_body)
        scoreboard.updateScore()

    def slither(self):
        # Move head of snake
        if self.head.heading() == 0:  # Move 20 pixels right
            x = self.head.xcor()
            self.head.setx(x+20)
        if self.head.heading() == 90:  # Move 20 pixels up
            y = self.head.ycor()
            self.head.sety(y+20)
        if self.head.heading() == 180:  # Move 20 pixels left
            x = self.head.xcor()
            self.head.setx(x-20)
        if self.head.heading() == 270:  # Move 20 pixels down
            y = self.head.ycor()
            self.head.setx(y-20)

        # Move body of snake
        if(len(self.body) > 0):
            for index in range(len(self.body)-1, 0 , -1): # Cycle from last in list to first
                if index == 0:      
                    x = self.head.xcor()
                    y = self.head.ycor()
                    self.body[index].goto((x,y))

                else:
                    x = self.body[index-1].xcor()
                    y = self.body[index-1].ycor()
                    self.body[index].goto((x,y))

         

