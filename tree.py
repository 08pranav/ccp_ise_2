import turtle
class TreeDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)  
        self.t.left(90)
        self.t.penup()
        self.t.goto(0, -250)  
        self.t.pendown()

    def draw_tree(self, branch_length):
        if branch_length > 5:
    
            self.t.pensize(branch_length / 10)
            self.t.pencolor("brown")

            self.t.forward(branch_length)
            self.t.right(20)

            
            self.draw_tree(branch_length - 15)
            
            self.t.left(40)

        
            self.draw_tree(branch_length - 15)
            
            self.t.right(20)
            
            
            self.t.backward(branch_length)

        else:
            
            self.t.pencolor("green")
            self.t.pensize(1)
            self.t.dot(10)  

tree = TreeDrawer()
tree.draw_tree(100)
turtle.done()
