import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os

class FileUploader:
    def __init__(self, root):
        self.root = root
        self.root.title("File Uploader")
        
        # Set minimum window size
        self.root.minsize(400, 500)
        
        # Configure main window scaling
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(padx=20, pady=20, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        
        # Label for instructions with system font
        self.instruction_label = ttk.Label(
            self.main_frame,
            text="Upload an image to display it here.",
            font=("Arial", 14)
        )
        self.instruction_label.grid(row=0, column=0, pady=10)
        
        # Button to upload image - using ttk for native look
        self.upload_button = ttk.Button(
            self.main_frame,
            text="Upload Image",
            command=self.upload_image
        )
        self.upload_button.grid(row=1, column=0, pady=10)
        
        # Frame for image display with border
        self.image_frame = ttk.Frame(
            self.main_frame,
            borderwidth=2,
            relief="solid"
        )
        self.image_frame.grid(row=2, column=0, pady=10, sticky="nsew")
        
        # Label to display the uploaded image
        self.image_label = ttk.Label(self.image_frame)
        self.image_label.pack(expand=True, padx=10, pady=10)
        
        # Status label
        self.status_label = ttk.Label(
            self.main_frame,
            text="No image selected",
            font=("Arial", 12)
        )
        self.status_label.grid(row=3, column=0, pady=5)

    def upload_image(self):
        """Handles the image upload process and displays the image."""
        # Open a file dialog to select an image - simplified file types
        file_types = [
            ('Image files', '.png'),
            ('Image files', '.jpg'),
            ('Image files', '.jpeg'),
            ('Image files', '.gif'),
            ('Image files', '.bmp'),
            ('All files', '.')
        ]
        
        try:
            file_path = filedialog.askopenfilename(
                parent=self.root,
                title='Select an Image',
                filetypes=file_types
            )
            
            if file_path:
                # Open the selected image
                img = Image.open(file_path)
                
                # Calculate resize dimensions while maintaining aspect ratio
                display_size = (300, 300)
                img.thumbnail(display_size, Image.Resampling.LANCZOS)
                
                # Convert the image to RGB mode if necessary
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Convert the image to a PhotoImage object for Tkinter
                photo_img = ImageTk.PhotoImage(img)
                
                # Display the image in the image label
                self.image_label.configure(image=photo_img)
                
                # Keep a reference to avoid garbage collection
                self.image_label.image = photo_img
                
                # Update status with file name
                file_name = os.path.basename(file_path)
                self.status_label.configure(
                    text=f"Loaded: {file_name}",
                    foreground="green"
                )
                
        except Exception as e:
            # Handle any errors during image loading
            self.status_label.configure(
                text=f"Error: {str(e)}",
                foreground="red"
            )

    def run(self):
        """Runs the main Tkinter event loop."""
        # Center the window on the screen
        self.center_window()
        self.root.mainloop()
    
    def center_window(self):
        """Centers the window on the screen."""
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate window size and position
        window_width = 400
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Set window position
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileUploader(root)
    app.run()