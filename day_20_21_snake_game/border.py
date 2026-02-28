from turtle import Turtle

class Border(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle
        self.speed("fastest")
        self.color("white")
        self.pensize(4)
        self.penup()
        self.draw_border()
        self.draw_top_lines()
    
    def draw_border(self):
        self.goto(-290, -290)
        self.pendown()

        for _ in range (4):
            self.forward(580)
            self.left(90)

        self.penup()

    def draw_top_lines(self):
        self.hideturtle()
        self.goto(-290, 230) #below scoreboard
        self.pendown()
        self.forward(580)
        self.penup()

