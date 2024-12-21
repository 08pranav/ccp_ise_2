import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Entry field for displaying numbers
        self.display = tk.Entry(root, width=20, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Buttons for calculator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(root, text=button, width=5, command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.display.delete(0, tk.END)
        elif key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

# Create and run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()