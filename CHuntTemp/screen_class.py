# CHRISTOPHER HUNT
# CS 162
# Assignment 3
# screen_class.py
import turtle

class Screen():
    def __init__(self):
        self.width = 600
        self.height = 800
    
        screen = turtle.Screen()
        screen.title("Snake Charmers")
        screen.bgcolor("purple")
        screen.screensize(width=self.width, height=self.height)

window = Screen()