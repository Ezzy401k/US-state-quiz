import turtle


class FetchName(turtle.Turtle):
    def __init__(self, answer, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{answer}", False, font=("Arial", 7, "bold"))
