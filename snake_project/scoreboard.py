from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial",24,"normal"    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                content = data.read()
                self.high_score = int(content) if content else 0
        except:
            self.high_score = 0    
                
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        
        
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,270)
        self.write(f"score:{self.score} :: high_score:{self.high_score}", align=ALIGNMENT,font=FONT)  

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)  
        self.goto(0,270)      
       
    def increase_score(self):
        self.score += 1  
        
        self.update_scoreboard()
        