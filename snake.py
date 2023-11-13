from turtle import Turtle
class Snake:

    def __init__(self,l=3,col='white'):
        """Create a Sanke object with l segments of col color"""
        self.snake=[]
        x=0
        for _ in range(l):
            s=Turtle(shape="square")
            s.penup()
            s.color(col)
            s.goto(x,0)
            x-=20
            self.snake.append(s)
            self.alive=True
        
    def move(self,dis=20): 
        """Moves the self object i.e. a sanke object by dis distance"""
        for s in range(len(self.snake)-1,0,-1):
            if(s!=0):
                self.snake[s].goto(self.snake[s-1].xcor(),self.snake[s-1].ycor())
        self.snake[0].forward(dis)
        self.snake_alive()
        self.colllison()

    def snake_up(self):
        if self.snake[0].heading() != 270:
            
            self.snake[0].setheading(90)
        
        
    def snake_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
        
    
    def snake_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
        

    def snake_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

            
    def snake_alive(self):
        head=self.snake[0]
        if(-290<head.xcor()<290 and -290<head.ycor()<270):
            self.alive= True
        else:
            self.alive= False
            
    def add_seg(self):
        temp=Turtle()
        tail=self.snake[-1]
        temp.color(tail.pencolor())
        temp.shape('square')
        temp.penup()
        if(tail.heading()==0):
            temp.goto(tail.xcor()-20,tail.ycor())
        elif(tail.heading()==90):
            temp.goto(tail.xcor(),tail.ycor()-20)
        elif(tail.heading()==180):
            temp.goto(tail.xcor()+20,tail.ycor())
        elif(tail.heading()==270):
            temp.goto(tail.xcor(),tail.ycor()+20)
        self.snake.append(temp)
        
    def colllison(self):
        for s in self.snake:
            if(s!=self.snake[0] and self.snake[0].distance(s)< 10):
                self.alive=False