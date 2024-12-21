import turtle

class HouseDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(20)  

    def draw_house(self):
        
        self.t.penup()
        self.t.goto(-50, -50)  
        self.t.pendown()
        self.t.fillcolor("lightblue")
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(100)
            self.t.left(90)
        self.t.end_fill()

       
        self.t.fillcolor("red")
        self.t.begin_fill()
        self.t.goto(-50, 50)  
        self.t.goto(0, 100)   
        self.t.goto(50, 50)   
        self.t.goto(-50, 50)  
        self.t.end_fill()

        
        self.t.penup()
        self.t.goto(-15, -50)  
        self.t.pendown()
        self.t.fillcolor("brown")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(30)
            self.t.left(90)
            self.t.forward(50)
            self.t.left(90)
        self.t.end_fill()

        
        self.t.penup()
        self.t.goto(-40, 0)  
        self.t.pendown()
        self.t.fillcolor("yellow")
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(20)
            self.t.left(90)
        self.t.end_fill()

        
        self.t.penup()
        self.t.goto(20, 0)  
        self.t.pendown()
        self.t.fillcolor("yellow")
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(20)
            self.t.left(90)
        self.t.end_fill()


house = HouseDrawer()
house.draw_house()
turtle.done()
