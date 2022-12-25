from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.write(f"Score: {self.score}", False, 'center', ("Consolas", 12, "bold"))
    
    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, 'center', ("Consolas", 12, "bold"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER :P", False, 'center', ("Consolas", 17, "bold"))