from turtle import Turtle
ALIGNMENT='center'
FONT=('Arial', 15, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.current_hs=0
        with open(r"C:\Coding\Python\PRACTISE\UdemyCouse\SnakeGame\highScore.txt") as hs:
            self.current_hs=hs.read()
            
        self.text=f"Score: {self.score}   High Score: {self.current_hs}"
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        
    def Score_update(self):
        self.goto(0,270)
        self.score+=1
        self.text=f"Score: {self.score}   High Score: {self.current_hs}"
        self.clear()
        self.score_write()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",True,ALIGNMENT,FONT)
    
    def score_write(self):
        self.write(self.text,True,ALIGNMENT,FONT)
        
    def highScore(self):
        if(self.score > int(self.current_hs)):
            with open(r"C:\Coding\Python\PRACTISE\UdemyCouse\SnakeGame\highScore.txt","w") as hs:
                hs.write(f"{self.score}")