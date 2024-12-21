import turtle

class ShapeDrawer:
    def __init__(self):
        self.t = turtle.Turtle()

    def draw_square(self, side_length):
        for _ in range(4):
            self.t.forward(side_length)
            self.t.right(90)

    def draw_rectangle(self, width, height):
        for _ in range(2):
            self.t.forward(width)
            self.t.right(90)
            self.t.forward(height)
            self.t.right(90)

    def draw_triangle(self, side_length):
        for _ in range(3):
            self.t.forward(side_length)
            self.t.right(120)

drawer = ShapeDrawer()
drawer.draw_square(100) 

drawer.t.penup()
drawer.t.goto(-150, 0)  
drawer.t.pendown()

drawer.draw_rectangle(150, 100) 


drawer.t.penup()
drawer.t.goto(50, -150) 
drawer.t.pendown()

drawer.draw_triangle(120)

turtle.done()