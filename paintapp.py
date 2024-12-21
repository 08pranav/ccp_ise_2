import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        # Canvas for drawing
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        self.canvas.pack()

        # Default shape is "line"
        self.shape = "line"

        # Store start position for dynamic drawing
        self.start_x = None
        self.start_y = None

        # Initialize buttons
        self.setup_buttons()

    def setup_buttons(self):
        """Create and place control buttons."""
        self.line_button = tk.Button(self.root, text="Draw Line", command=self.set_line)
        self.line_button.pack(side=tk.LEFT, padx=5)

        self.rectangle_button = tk.Button(self.root, text="Draw Rectangle", command=self.set_rectangle)
        self.rectangle_button.pack(side=tk.LEFT, padx=5)

        self.oval_button = tk.Button(self.root, text="Draw Oval", command=self.set_oval)
        self.oval_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def set_line(self):
        """Set shape to line."""
        self.shape = "line"

    def set_rectangle(self):
        """Set shape to rectangle."""
        self.shape = "rectangle"

    def set_oval(self):
        """Set shape to oval."""
        self.shape = "oval"

    def clear_canvas(self):
        """Clear all shapes from the canvas."""
        self.canvas.delete("all")

    def mouse_click(self, event):
        """Record starting position of the mouse click."""
        self.start_x = event.x
        self.start_y = event.y

    def mouse_release(self, event):
        """Draw the selected shape when the mouse is released."""
        end_x, end_y = event.x, event.y

        if self.shape == "line":
            self.canvas.create_line(self.start_x, self.start_y, end_x, end_y, fill="black")
        elif self.shape == "rectangle":
            self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline="black")
        elif self.shape == "oval":
            self.canvas.create_oval(self.start_x, self.start_y, end_x, end_y, outline="black")

    def run(self):
        """Bind mouse events and start the Tkinter main loop."""
        self.canvas.bind("<Button-1>", self.mouse_click)  # On mouse press
        self.canvas.bind("<B1-Motion>", lambda event: None)  # Optional: for dragging feedback (not implemented here)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)  # On mouse release
        self.root.mainloop()


# Run the Paint App
root = tk.Tk()
app = PaintApp(root)
app.run()
