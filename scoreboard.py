from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.point = 0
        with open("data.txt") as file:
            high_score = file.read().strip()
            self.high_score = int(high_score)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.point}   High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def new_point(self):
        self.point += 1
        self.update_score()

    def reset(self):
        if self.point > self.high_score:
            self.high_score = self.point
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.point = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
