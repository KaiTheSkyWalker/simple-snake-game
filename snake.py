from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.array = []
        self.create_snake()
        self.head = self.array[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)
            
    def add_segment(self, position):
            box = Turtle()
            box.color("white")
            box.shape("square")
            box.penup()
            box.goto(position)
            self.array.append(box)

    def reset(self):
        for seg in self.array: # there are still snake segments at the screen
            seg.goto(1000, 1000)
        self.array.clear() # clear the contents of the screen
        self.create_snake()
        self.head = self.array[0]

    
    def extend(self):
        self.add_segment(self.array[-1].position())
    
    def move(self):
        for i in range(len(self.array) - 1, 0, -1):
            x_cor = self.array[i - 1].xcor()
            y_cor = self.array[i - 1].ycor()
            # goto the position of the coordinates by storing them into an array
            self.array[i].goto(x_cor, y_cor)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
            