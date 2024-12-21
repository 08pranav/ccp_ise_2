import turtle
class StarDrawer:
    def __init__(self):
        self.t = turtle.Turtle()

    def draw_star(self, points, size):
        angle = 180 - (180 / points)
        for _ in range(points):
            self.t.forward(size)
            self.t.right(angle)

star = StarDrawer()
star.draw_star(5, 100)
turtle.done()