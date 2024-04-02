from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_file()
        self.color("white")
        self.penup()
        self.goto(0, 475)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score:  {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def read_file(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())
            return self.high_score

    def write_file(self, high_score):
        with open("data.txt", mode="w") as data:
            data.write(str(high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
