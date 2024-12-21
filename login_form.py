import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        
        # Create frame for login form
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()
        
        # Username field
        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(pady=5)
        
        # Password field
        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")  # Show * for password
        self.password_entry.pack(pady=5)
        
        # Login button
        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        
    def login(self):
        # Get entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check if fields are empty
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        # Here you would typically validate against a database
        # For demo purposes, we'll just show the entered data
        messagebox.showinfo("Login Info", f"Username: {username}\nPassword: {password}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()