# main.py

import tkinter as tk
from tkinter import ttk
import os


class CampusLinkApp(tk.Tk):

    """
    The main application class for CampusLink Desktop App.
    This class sets up the main window, navigation, and integrates
    the different feature modules.
    """


    # note: 'self' is equivalent of 'this' from c++/java in python
    # referrence to specific object you're working with so you can set or access 
    # attributes that belong to particular instance
    # like saying "the object i'm currently working on"
    # note: 'def __init__' is equivalent to a constructor in c++/java
    # automatic set up routine thats run when instance of class is created/called 
    # --> meant to setup initial state of app

    def __init__(self):
        # Ensure parent class 'tk.Tk' window is correctly set up before CampusLinkApp class
        # adds its specific features 
        super().__init__()
        self.title("CampusLink Desktop App") # Set window title
        self.geometry("800x600") # Set initial window size

        # Configure the grid to make the notebook expand --> crucial for making UI responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a Notebook (tabbed interface) Widget for navigation
        # This is a simple and effective way to switch between different 
        # sections of the application for the prototype.
        self.notebook = ttk.Notebook(self) # creates instance of notebook widget
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) # places notebook widget in main window

        # --- Create Frames for each Feature Section ---
        # These frames will hold the UI elements for each part of the app.
        # For the prototype, they will initially be empty or contain basic labels.

        # Activities/Task Schedule Manager Frame
        self.activities_frame = ttk.Frame(self.notebook, padding="10") # creates frame
        self.activities_frame.grid_rowconfigure(0, weight=1) 
        self.activities_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.activities_frame, text="Activities") # adds frame as tab to notebook
        # Add a placeholder label for now -> inside frame
        ttk.Label(self.activities_frame, text="Activities & Task Schedule Manager (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Events Calendar Frame
        self.events_frame = ttk.Frame(self.notebook, padding="10")
        self.events_frame.grid_rowconfigure(0, weight=1)
        self.events_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.events_frame, text="Events")
        # Add a placeholder label for now
        ttk.Label(self.events_frame, text="Events Calendar (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Bulletin Board Frame
        self.bulletin_frame = ttk.Frame(self.notebook, padding="10")
        self.bulletin_frame.grid_rowconfigure(0, weight=1)
        self.bulletin_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.bulletin_frame, text="Bulletin Board")
        # Add a placeholder label for now
        ttk.Label(self.bulletin_frame, text="Community Bulletin Board (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Emergency Contacts Frame
        self.emergency_frame = ttk.Frame(self.notebook, padding="10")
        self.emergency_frame.grid_rowconfigure(0, weight=1)
        self.emergency_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.emergency_frame, text="Emergency Contacts")
        # Add a placeholder label for now
        ttk.Label(self.emergency_frame, text="Emergency Contacts & Quick Access (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

# Entry point guard --> "Is this script currently the main program being run? Yes? Execute." 
if __name__ == "__main__":
    # Create an instance of the application
    app = CampusLinkApp()
    # Start the Tkinter event loop
    app.mainloop()
