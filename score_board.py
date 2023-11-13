from turtle import Turtle
ALIGNMENT='center'
FONT=('Arial', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.text=f"Score: {self.score}"
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        
    def Score_update(self):
        self.goto(0,270)
        self.score+=1
        self.text=f"Score: {self.score}"
        self.clear()
        self.score_write()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",True,ALIGNMENT,FONT)
    
    def score_write(self):
        self.write(self.text,True,ALIGNMENT,FONT)