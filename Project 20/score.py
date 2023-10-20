from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_sc = 0
        self.r_sc = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(f"{self.l_sc}", align="center", font=("Times New Roman", 55, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.r_sc}", align="center", font=("Times New Roman", 55, 'normal'))


    def update_l(self):
        self.l_sc += 1
        self.clear()
        self.update()


    def update_r(self):
        self.r_sc += 1
        self.clear()
        self.update()