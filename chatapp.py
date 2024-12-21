import tkinter as tk

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")

        # Create the chat window (a Text widget for displaying messages)
        self.chat_window = tk.Text(self.root, width=50, height=20, state=tk.DISABLED)
        self.chat_window.pack(padx=10, pady=10)

        # Create the message entry field
        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(padx=10, pady=10)

        # Create the Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self):
        """Send the message entered by the user."""
        message = self.message_entry.get()  # Get the message from the entry widget
        if message:
            self.display_message(f"You: {message}")  # Display the user's message
            self.message_entry.delete(0, tk.END)  # Clear the entry field
            self.receive_message()  # Simulate receiving a message after sending one

    def receive_message(self):
        """Simulate receiving a message from the 'server'."""
        self.display_message("Server: Hello! How can I help you?")

    def display_message(self, message):
        """Display a message in the chat window."""
        self.chat_window.config(state=tk.NORMAL)  # Enable text widget for editing
        self.chat_window.insert(tk.END, message + "\n")  # Insert the message at the end
        self.chat_window.config(state=tk.DISABLED)  # Disable text widget after inserting the message
        self.chat_window.yview(tk.END)  # Scroll to the end of the chat window

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()

# Create the Tkinter root window
root = tk.Tk()
app = ChatApp(root)
app.run()
