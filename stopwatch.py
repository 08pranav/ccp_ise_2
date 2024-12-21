import tkinter as tk
from time import time, strftime, gmtime

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch App")
        
        # Display for time
        self.time_display = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_display.pack(pady=20)
        
        # Start button
        self.start_button = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        # Stop button
        self.stop_button = tk.Button(root, text="Stop", width=10, command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        # Reset button
        self.reset_button = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Initialize stopwatch state
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

    def update_timer(self):
        """Update the displayed time while the stopwatch is running."""
        if self.running:
            current_time = time()
            self.elapsed_time = current_time - self.start_time
            formatted_time = strftime('%H:%M:%S', gmtime(self.elapsed_time))
            self.time_display.config(text=formatted_time)
            self.root.after(100, self.update_timer)  # Update every 100ms

    def start(self):
        """Start the stopwatch if it's not already running."""
        if not self.running:
            self.running = True
            self.start_time = time() - self.elapsed_time
            self.update_timer()  # Start the timer update loop

    def stop(self):
        """Stop the stopwatch if it's running."""
        if self.running:
            self.running = False

    def reset(self):
        """Reset the stopwatch to 00:00:00."""
        self.running = False
        self.elapsed_time = 0
        self.time_display.config(text="00:00:00")


if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
