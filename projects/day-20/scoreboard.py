from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highscore = int(f.read())
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f"GAME OVER YOUR SCORE : {self.score}",False,"center",("Courier",15,"normal"))

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High score : {self.highscore}",False ,"center",("Courier",15,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as f:
                f.write(f"{self.highscore}")
        self.score = 0
        
 