import tkinter as tk
from tkinter import messagebox
import re

class FormValidator:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        # Create form labels and entry widgets
        self.name_label = tk.Label(self.root, text="Name")
        self.name_label.pack(padx=10, pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack(padx=10, pady=5)

        self.email_label = tk.Label(self.root, text="Email")
        self.email_label.pack(padx=10, pady=5)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack(padx=10, pady=5)

        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.pack(padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(padx=10, pady=5)

        self.confirm_password_label = tk.Label(self.root, text="Confirm Password")
        self.confirm_password_label.pack(padx=10, pady=5)
        self.confirm_password_entry = tk.Entry(self.root, width=30, show="*")
        self.confirm_password_entry.pack(padx=10, pady=5)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.validate_form)
        self.submit_button.pack(padx=10, pady=20)

    def validate_form(self):
        """Validate the form fields"""
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not name:
            self.show_error("Name is required.")
        elif not self.is_valid_email(email):
            self.show_error("Please enter a valid email address.")
        elif len(password) < 6:
            self.show_error("Password must be at least 6 characters long.")
        elif password != confirm_password:
            self.show_error("Passwords do not match.")
        else:
            self.show_success("Registration successful!")

    def is_valid_email(self, email):
        """Check if the email has a valid format using regular expression"""
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def show_error(self, message):
        """Display an error message in a messagebox"""
        messagebox.showerror("Error", message)

    def show_success(self, message):
        """Display a success message in a messagebox"""
        messagebox.showinfo("Success", message)

    def run(self):
        """Start the Tkinter main loop"""
        self.root.mainloop()

# Create the Tkinter root window
root = tk.Tk()
app = FormValidator(root)
app.run()
