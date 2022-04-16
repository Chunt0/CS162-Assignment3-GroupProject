import turtle
import time

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto((0,300))
        self.pen.write("****SNAKE CHARMER****\nScore : 0", align="center", font=("arial", 24, "bold"))
    
    def updateScore(self):
        self.score += 10 
        self.pen.clear()
        self.pen.write(f"*****SNAKE CHARMER****\nScore : {self.score}", align="center", font=("arial", 24, "bold"))

    def resetScore(self):
        self.score = 0
        self.pen.clear()
        self.pen.write("****SNAKE CHARMER****\nScore : 0", align="center", font=("arial", 24, "bold"))       
       