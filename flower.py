import turtle

class FlowerDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(10)

    def draw_petal(self, petal_length, color):
        """Draws a single flower petal with the given length and color"""
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.circle(petal_length, 60)
            self.t.left(120)
        self.t.end_fill()

    def draw_flower(self, petal_count, petal_length, stem_length, stem_color):
        """Draws a complete flower with stem"""
        self.t.penup()
        self.t.goto(0, -stem_length // 2)
        self.t.pendown()
        self.t.pencolor(stem_color)
        self.t.forward(stem_length)
        self.t.setheading(90)  

        colors = ["red", "yellow", "orange", "pink"]
        for i in range(petal_count):
            self.draw_petal(petal_length, colors[i % len(colors)])
            self.t.left(360 / petal_count)  

flower = FlowerDrawer()
flower.draw_flower(petal_count=8, petal_length=50, stem_length=100, stem_color="green")
turtle.done()