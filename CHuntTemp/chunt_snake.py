import turtle
import utils

class Snake:
    def __init__(self):
        """ This only runs once """
        self.head = turtle.Turtle()
        self.speed = 5
        self.position = self.head.position()
        self.head.shape('triangle')
        self.head.color("red")
        self.head.penup()
        self.head.direction = "Stop"
        

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