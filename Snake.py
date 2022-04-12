import turtle
import utils

#Screen
map = turtle.Screen()
map.bgcolor("lightblue")

#Turtle Player
snake = turtle.Turtle()
snake.color("green")
snake.penup()

#trying to control snake length
erase = turtle.Turtle()
erase.color("lightblue")
erase.hideturtle()


#Constant
speed = 1
length = 10
path = []

def up():
    if snake.heading() != 270:
        snake.setheading(90)

def down():
    if snake.heading() != 90:
        snake.setheading(270)
    
def left():
    if snake.heading() != 0:
        snake.setheading(180)

def right():
    if snake.heading() != 180:
        snake.setheading(0)

map.listen()
map.onkey(up, 'w')
map.onkey(down, 's')
map.onkey(left, 'a')
map.onkey(right, 'd')


#print("Are you ready to play the game?")
#ready = utils.input_yes_no()
snake.pendown()
path.append(snake.position())
erase.pendown()
while True:
    snake.forward(speed)
    path.append(snake.position()) #trying to get position for erase turtle to follow
    if len(path) > length:
        erase.goto(path[0])
        path.pop(0)
        print(path)
