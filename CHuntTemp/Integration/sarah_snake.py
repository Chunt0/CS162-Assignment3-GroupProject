import turtle
import utils

class Snake:
    def __init__(self):
        self.head     = turtle.Turtle()
        self.body     = []
        self.length   = 10  # changes based on score multiply
        self.speed    = 5
        self.position = self.head.position()
        self.path     = []
        self.head.shape('triangle')
        self.head.color("red")
        self.head.penup()

#         for idx in range(self.length):
#             segment = turtle.Turtle(shape="circle", visible=False)
#             segment.penup()
# # change colors (from colors list)
#             segment.color(self.color)
#             self.body.append(segment)

    def increase_length(self, amt=4):
        self.length += amt
#        print("Snake length is now:", self.length)
        for idx in range(amt):
            segment = turtle.Turtle(shape="circle", visible=False)
            segment.penup()
            # change colors (from colors list)
            segment.color(self.color)
            self.body.insert(0, segment)
        self.speed += 1
        return self.length

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
        segment.hideturtle()
        segment.goto(self.position)
        segment.showturtle()
        self.body.append(segment)
        self.head.forward(self.speed)