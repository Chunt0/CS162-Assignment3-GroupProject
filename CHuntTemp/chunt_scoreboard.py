import turtle
import utils

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto((0,300))
        self.pen.write("****SNAKE CHARMER****\nScore : 0 High Score : 0", align="center", font=("arial", 24, "bold"))

    def rewrite(self):
        self.pen.clear()
        self.pen.write("CHANGED", align="center", font=("arial", 24, "bold"))
       