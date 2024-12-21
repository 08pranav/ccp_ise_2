import turtle 

screen = turtle.Screen()
screen.title("Grid Pattern")
screen.bgcolor("white")


pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


rows, cols = 8, 8  
cell_size = 40      


colors = ["lightgreen", "lightblue"]


for row in range(rows):
    for col in range(cols):
        pen.penup()
        
        x = col * cell_size - (cols * cell_size) / 2
        y = -(row * cell_size) + (rows * cell_size) / 2
        pen.goto(x, y)

        
        pen.fillcolor(colors[(row + col) % 2])
        pen.begin_fill()

        
        for _ in range(4):
            pen.pendown()
            pen.forward(cell_size)
            pen.right(90)
        pen.end_fill()

pen.pencolor("black")
for i in range(rows + 1):
    
    pen.penup()
    pen.goto(-(cols * cell_size) / 2, (rows / 2 - i) * cell_size)
    pen.pendown()
    pen.forward(cols * cell_size)

for i in range(cols + 1):
    
    pen.penup()
    pen.goto((i - cols / 2) * cell_size, (rows * cell_size) / 2)
    pen.setheading(-90)
    pen.pendown()
    pen.forward(rows * cell_size)

screen.mainloop()
