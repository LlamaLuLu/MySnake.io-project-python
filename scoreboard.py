from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.point = 0
        self.color("white")
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.point}", align=ALIGNMENT, font=FONT)

    def new_point(self):
        self.point += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
