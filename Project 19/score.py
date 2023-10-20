from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 245)
        self.pendown()
        self.hideturtle()
        self.color("white")
        self.score = 0
        file = open("data.txt")
        self.high_score = int(file.read())
        self.b()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.b()

    def b(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", move=False, align="center", font=('Times New Roman', 20, 'normal'))

    def increase(self):
        self.score += 1
        self.b()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER!!", move=False, align="center", font=('Algerian', 18, 'normal'))