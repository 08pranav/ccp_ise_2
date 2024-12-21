import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo App")
        self.root.geometry("600x400")
        
        # Load saved tasks
        self.tasks = self.load_tasks()
        
        # Create main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create input fields
        self.create_input_fields()
        
        # Create task list
        self.create_task_list()
        
        # Create buttons
        self.create_buttons()
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
    def create_input_fields(self):
        # Task title
        ttk.Label(self.main_frame, text="Task:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.task_entry = ttk.Entry(self.main_frame, width=40)
        self.task_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Priority
        ttk.Label(self.main_frame, text="Priority:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.priority_var = tk.StringVar(value="Medium")
        self.priority_combo = ttk.Combobox(self.main_frame, textvariable=self.priority_var, 
                                         values=["Low", "Medium", "High"], 
                                         state="readonly", width=10)
        self.priority_combo.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
    def create_task_list(self):
        # Create treeview
        columns = ("Task", "Priority", "Status", "Date Added")
        self.tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid the treeview and scrollbar
        self.tree.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=2, column=3, pady=5, sticky=(tk.N, tk.S))
        
        # Bind double-click event for marking tasks as complete
        self.tree.bind("<Double-1>", self.toggle_task_status)
        
        # Load existing tasks
        self.refresh_task_list()
        
    def create_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear Completed", command=self.clear_completed).pack(side=tk.LEFT, padx=5)
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            priority = self.priority_var.get()
            date_added = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # Add to tasks dictionary
            task_id = str(len(self.tasks) + 1)
            self.tasks[task_id] = {
                "task": task,
                "priority": priority,
                "status": "Pending",
                "date_added": date_added
            }
            
            # Clear entry
            self.task_entry.delete(0, tk.END)
            
            # Refresh list and save
            self.refresh_task_list()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
            
    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = selected_item[0]
            if task_id in self.tasks:
                del self.tasks[task_id]
                self.refresh_task_list()
                self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            
    def clear_completed(self):
        completed_tasks = [task_id for task_id, task in self.tasks.items() 
                         if task["status"] == "Completed"]
        for task_id in completed_tasks:
            del self.tasks[task_id]
        self.refresh_task_list()
        self.save_tasks()
        
    def toggle_task_status(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = selected_item[0]
            if task_id in self.tasks:
                current_status = self.tasks[task_id]["status"]
                new_status = "Completed" if current_status == "Pending" else "Pending"
                self.tasks[task_id]["status"] = new_status
                self.refresh_task_list()
                self.save_tasks()
                
    def refresh_task_list(self):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Add all tasks to the treeview
        for task_id, task_info in self.tasks.items():
            self.tree.insert("", tk.END, task_id, values=(
                task_info["task"],
                task_info["priority"],
                task_info["status"],
                task_info["date_added"]
            ))
            
    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)
            
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()