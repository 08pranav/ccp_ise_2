import turtle
class SpiralDrawer:
    def __init__(self):
        self.t = turtle.Turtle()

    def draw_spiral(self, length=5, angle=30, increment=5, turns=50):
        for _ in range(turns):
            self.t.forward(length)
            self.t.right(angle)
            length += increment

spiral = SpiralDrawer()
spiral.draw_spiral()
turtle.done()