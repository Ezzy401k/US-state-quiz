import turtle


class FetchName(turtle.Turtle):
    def __init__(self, answer, x, y):
        super().__init__()  # Initialize the turtle object
        self.penup()  # Lift the pen to avoid drawing while moving
        self.hideturtle()  # Hide the turtle cursor
        self.goto(x, y)  # Move the turtle to the specified coordinates (x, y)
        # Write the provided state name on the screen at the current position
        self.write(f"{answer}", False, font=("Arial", 7, "bold"))
