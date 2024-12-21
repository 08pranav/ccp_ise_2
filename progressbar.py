import tkinter as tk
from tkinter.ttk import Progressbar
import time

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Bar App")

        # Label to indicate the purpose of the progress bar
        self.label = tk.Label(self.root, text="Simulating Loading...", font=("Arial", 14))
        self.label.pack(pady=10)

        # Progress bar widget
        self.progress_bar = Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=20)

        # Button to start the loading process
        self.start_button = tk.Button(self.root, text="Start Loading", command=self.start_loading)
        self.start_button.pack(pady=10)

    def start_loading(self):
        """Simulates a loading process with a progress bar."""
        self.progress_bar["value"] = 0  # Reset progress bar
        self.label.config(text="Simulating Loading...")  # Reset label text
        self.root.update_idletasks()

        # Simulate loading progress
        for i in range(101):  # Loop from 0 to 100 (percentage)
            time.sleep(0.05)  # Simulate a task delay
            self.progress_bar["value"] = i  # Update the progress bar value
            self.root.update_idletasks()  # Update the GUI to reflect changes

        # Update label text once loading is complete
        self.label.config(text="Loading Complete!")

    def run(self):
        """Runs the Tkinter main loop."""
        self.root.mainloop()


# Create the main Tkinter window and start the application
root = tk.Tk()
app = ProgressBarApp(root)
app.run()
