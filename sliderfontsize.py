import tkinter as tk

class SliderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slider App - Change Label Font Size")
        
        # Create a label with an initial font size of 20
        self.label = tk.Label(self.root, text="Hello, Tkinter!", font=("Arial", 20))
        self.label.pack(pady=20)
        
        # Create a horizontal slider (scale) to adjust font size
        self.slider = tk.Scale(self.root, from_=10, to=100, orient="horizontal", label="Font Size")
        self.slider.set(20)  # Set default slider position to 20
        self.slider.pack(pady=20)
        
        # Create a button to apply the new font size
        self.button = tk.Button(self.root, text="Apply Font Size", command=self.update_font_size)
        self.button.pack(pady=20)

    def update_font_size(self):
        """Update the font size of the label based on the slider value."""
        new_font_size = self.slider.get()
        self.label.config(font=("Arial", new_font_size))


# Initialize the Tkinter application
root = tk.Tk()
app = SliderApp(root)
root.mainloop()
