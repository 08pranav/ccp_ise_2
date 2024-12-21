import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("800x600")
        
        # Current file path
        self.current_file = None
        
        # Create the main menu
        self.create_menu()
        
        # Create the text area
        self.create_text_area()
        
        # Create the status bar
        self.create_status_bar()
        
        # Bind events
        self.bind_events()
        
        # Track changes
        self.text_modified = False
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.confirm_exit)
        
        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        edit_menu.add_command(label="Find", command=self.show_find_dialog, accelerator="Ctrl+F")
        
        # Format Menu
        format_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Word Wrap", command=self.toggle_word_wrap)
        
    def create_text_area(self):
        # Create main text area with scrollbar
        self.text_area = ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')
        
    def create_status_bar(self):
        self.status_bar = ttk.Label(self.root, text="Ready", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def bind_events(self):
        # Bind keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-a>', lambda e: self.select_all())
        self.root.bind('<Control-f>', lambda e: self.show_find_dialog())
        
        # Bind text modification
        self.text_area.bind('<<Modified>>', self.on_modify)
        
        # Bind cursor position changes
        self.text_area.bind('<KeyRelease>', self.update_status_bar)
        self.text_area.bind('<Button-1>', self.update_status_bar)
        
    def new_file(self):
        if self.text_modified:
            if not self.confirm_save():
                return
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.text_modified = False
        self.root.title("Text Editor")
        
    def open_file(self):
        if self.text_modified:
            if not self.confirm_save():
                return
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                self.current_file = file_path
                self.text_modified = False
                self.root.title(f"Text Editor - {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
                
    def save_file(self, event=None):
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, 'w') as file:
                    file.write(content)
                self.text_modified = False
                self.status_bar.config(text="File saved successfully")
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
                return False
        else:
            return self.save_as_file()
            
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            self.root.title(f"Text Editor - {os.path.basename(file_path)}")
            return self.save_file()
        return False
        
    def confirm_save(self):
        if self.text_modified:
            response = messagebox.askyesnocancel(
                "Save Changes?",
                "Do you want to save the changes?"
            )
            if response is None:  # Cancel
                return False
            elif response:  # Yes
                return self.save_file()
        return True
        
    def confirm_exit(self):
        if self.text_modified:
            if not self.confirm_save():
                return
        self.root.quit()
        
    def select_all(self, event=None):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return 'break'
        
    def show_find_dialog(self, event=None):
        find_dialog = tk.Toplevel(self.root)
        find_dialog.title("Find")
        find_dialog.transient(self.root)
        find_dialog.resizable(False, False)
        
        # Find entry
        ttk.Label(find_dialog, text="Find:").grid(row=0, column=0, padx=5, pady=5)
        find_entry = ttk.Entry(find_dialog, width=30)
        find_entry.grid(row=0, column=1, padx=5, pady=5)
        find_entry.focus_set()
        
        def find_text():
            search_text = find_entry.get()
            if search_text:
                start_pos = self.text_area.search(search_text, tk.INSERT, tk.END)
                if start_pos:
                    end_pos = f"{start_pos}+{len(search_text)}c"
                    self.text_area.tag_remove(tk.SEL, "1.0", tk.END)
                    self.text_area.tag_add(tk.SEL, start_pos, end_pos)
                    self.text_area.mark_set(tk.INSERT, end_pos)
                    self.text_area.see(tk.INSERT)
                else:
                    messagebox.showinfo("Find", "Text not found!")
        
        ttk.Button(find_dialog, text="Find Next", command=find_text).grid(row=1, column=0, columnspan=2, pady=10)
        
    def toggle_word_wrap(self):
        current_wrap = self.text_area.cget("wrap")
        new_wrap = tk.NONE if current_wrap == tk.WORD else tk.WORD
        self.text_area.configure(wrap=new_wrap)
        
    def on_modify(self, event=None):
        if self.text_area.edit_modified():
            self.text_modified = True
            title = self.root.title()
            if not title.startswith("*"):
                self.root.title("*" + title)
            self.text_area.edit_modified(False)
            
    def update_status_bar(self, event=None):
        position = self.text_area.index(tk.INSERT)
        line, column = position.split(".")
        self.status_bar.config(text=f"Line: {line} | Column: {column}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()