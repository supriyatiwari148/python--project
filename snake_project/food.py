from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("pink")
        self.speed(0)

    def refresh(self):
        ramdom_x =random.randint(-280,280) 
        random_y = random.randint(-280,280) 
        self.goto(ramdom_x,random_y)  