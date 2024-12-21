## Question 2: Pattern Generator
import turtle
class PatternGenerator:
    def __init__(self):
        self.t = turtle.Turtle()

    def draw_concentric_circles(self, radius_increment, count):
        for i in range(1, count + 1):
            self.t.circle(radius_increment * i)
            self.t.penup()
            self.t.goto(0, -radius_increment * i)
            self.t.pendown()

# Example usage
generator = PatternGenerator()
generator.draw_concentric_circles(20, 5)
turtle.done()