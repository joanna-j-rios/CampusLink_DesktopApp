# activities_ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from database_manager import DatabaseManager

class ActivitiesUI:
    
    """
    Manages the user interface for the Activities tab, including displaying tasks
    and handling the "Add Task" functionality. This class populates a given frame.
    """
    
    def __init__(self, parent_frame, user_id):
        self.parent_frame = parent_frame
        self.user_id = user_id
        self.db_manager = DatabaseManager(db_path="campuslink.db")
        
        self.create_widgets()
        self.refresh_task_list()




    def create_widgets(self):
        """
        Sets up the UI elements for the activities tab.
        """
        # Main header
        header = ttk.Label(self.parent_frame, text="My Tasks", font=("Arial", 18, "bold"))
        header.pack(pady=10)

        # Frame for task list
        self.task_list_frame = ttk.Frame(self.parent_frame)
        self.task_list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Add Task button
        self.add_task_button = ttk.Button(self.parent_frame, text="Add Task", command=self.open_add_task_dialog)
        self.add_task_button.pack(pady=10)




    def open_add_task_dialog(self):
        """
        Opens a new dialog window to add a task.
        """
        AddTaskDialog(self.parent_frame, self.user_id, self.refresh_task_list)




    def refresh_task_list(self):

        """
        Refreshes the displayed list of tasks by fetching them from the database.
        """

        # Clear existing tasks
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        tasks = self.db_manager.get_tasks(self.user_id)
        
        if tasks:
            for task in tasks:
                #Create a frame for each task to hold the label and buttons
                task_container = ttk.Frame(self.task_list_frame)
                task_container.pack(fill="x", padx=10, pady=5)
                
                # Use a style to show completed tasks differently
                style = ttk.Style()
                if task['is_completed']:
                    style.configure("Completed.TLabel", foreground="gray", font=("Arial", 10, "italic"))
                    # Combined all task info into one label
                    task_text = f"✓ Task: {task['task_name']} | Due: {task['due_date']} | Description: {task['description']}"
                    task_label = ttk.Label(task_container, text=task_text, style="Completed.TLabel")
                else:
                    # Combined all task info into one label
                    task_text = f"☐ Task: {task['task_name']} | Due: {task['due_date']} | Description: {task['description']}"
                    task_label = ttk.Label(task_container, text=task_text, font=("Arial", 10))


                task_label.pack(side="left", padx=(0, 10))
                

                # --- Complete Button ---
                if not task['is_completed']:
                    complete_button = ttk.Button(
                        task_container, 
                        text="Complete", 
                        command=lambda task_id=task['id']: self.mark_task_as_complete(task_id)
                    )
                    complete_button.pack(side="right")

                # --- Delete Button ---
                delete_button = ttk.Button(
                    task_container, 
                    text="Delete", 
                    command=lambda task_id=task['id']: self.delete_task(task_id)
                )
                delete_button.pack(side="right", padx=(0, 5))
                

        else:
            no_tasks_label = ttk.Label(self.task_list_frame, text="You don't have any tasks yet.")
            no_tasks_label.pack(padx=10, pady=10)




    def mark_task_as_complete(self, task_id):

        """
        Calls the database manager to mark a task as complete and refreshes the list.
        """

        self.db_manager.mark_task_complete(task_id)
        self.refresh_task_list()
        messagebox.showinfo("Success", "Task marked as complete!")




    def delete_task(self, task_id):

        """
        Calls the database manager to delete a task and refreshes the list.
        """

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            self.db_manager.delete_task(task_id)
            self.refresh_task_list()
            messagebox.showinfo("Success", "Task deleted!")




class AddTaskDialog(tk.Toplevel):

    """
    A dialog window for adding a new task.
    """

    def __init__(self, parent, user_id, on_task_added):
        super().__init__(parent)
        self.parent = parent
        self.user_id = user_id
        self.on_task_added = on_task_added
        self.db_manager = DatabaseManager(db_path="campuslink.db")

        self.title("Add New Task")
        self.geometry("400x250")
        self.resizable(False, False)
        self.grab_set()  # Make this dialog modal

        self.create_widgets()



    def create_widgets(self):

        """
        Creates the input fields and buttons for the form.
        """

        # --- Task Name Input ---
        ttk.Label(self, text="Task Name:").pack(pady=(10, 0))
        self.task_name_entry = ttk.Entry(self, width=40)
        self.task_name_entry.pack()

        # --- Description Input ---
        ttk.Label(self, text="Description:").pack(pady=(10, 0))
        self.description_entry = ttk.Entry(self, width=40)
        self.description_entry.pack()

        # --- Due Date Input ---
        ttk.Label(self, text="Due Date (YYYY-MM-DD):").pack(pady=(10, 0))
        self.due_date_entry = ttk.Entry(self, width=40)
        self.due_date_entry.pack()

        # --- Add Task Button ---
        add_button = ttk.Button(self, text="Add Task", command=self.add_task)
        add_button.pack(pady=(20, 0))

    def add_task(self):

        """
        Handles the form submission and saves the new task.
        """

        task_name = self.task_name_entry.get().strip()
        description = self.description_entry.get().strip()
        due_date = self.due_date_entry.get().strip()

        if not task_name:
            messagebox.showerror("Input Error", "Task Name is required.")
            return

        try:
            self.db_manager.add_task(self.user_id, task_name, description, due_date)
            messagebox.showinfo("Success", "Task added successfully!")
            self.on_task_added() # Call the refresh function
            self.destroy() # Close the dialog
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add task: {e}")
