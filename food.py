from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(0)
        self.goto(random.randint(-280,280),random.randint(-280,265))
        
    def refresh(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))       
