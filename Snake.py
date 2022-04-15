import turtle
import utils

class Snake:
    def __init__(self, color):
        self.head     = turtle.Turtle()
        self.body     = []
        self.color    = color
        self.length   = 10  # changes based on score multiply
        self.speed    = 5
        self.position = self.head.position()
        self.path     = []
        self.head.shape('triangle')
        self.head.color(color)
        self.head.penup()

        for idx in range(self.length):
            segment = turtle.Turtle(shape="circle", visible=False)
            segment.penup()
# change colors (from colors list)
            segment.color(self.color)
            self.body.append(segment)

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

def get_color():
    prompt = "What color is your snake? "
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    idx = utils.input_options(prompt, colors)
    return colors[idx-1]

done = False

def stop():
    done = True

# Get snake color.
col = get_color()

# Initialize screen
map = turtle.Screen()
map.bgcolor("lightblue")

# Create snake.
snake = Snake(col)

# Set up keyboard inputs.
map.listen()
map.onkey(snake.up, 'w')
map.onkey(snake.down, 's')
map.onkey(snake.left, 'a')
map.onkey(snake.right, 'd')

map.onkey(snake.increase_length, 'i')

map.onkey(stop, 'q')

#print("Are you ready to play the game?")
#ready = utils.input_yes_no()
while not done:
    snake.forward()
#add code here

