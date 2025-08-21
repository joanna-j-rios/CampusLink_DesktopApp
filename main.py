# main.py

import tkinter as tk
from tkinter import ttk, messagebox
import os


# importing the classes from other files

from database_manager import DatabaseManager
from login_ui import LoginUI
from account_ui import AccountUI
from activities_ui import ActivitiesUI
from bulletin_ui import BulletinUI
from emergency_contacts_ui import EmergencyContactsUI


class CampusLinkApp(tk.Tk):

    """
    The main application class for CampusLink Desktop App.
    This class sets up the login/create account view, main window, navigation, and integrates
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
        
        # Variables to track the applications state (if logged in and who is logged in)
        # initialized to False & None because no one is logged in when the app first starts
        self.is_logged_in = False # boolean that tells is user is logged in
        self.current_user = None # string to hold the username of the person who is logged in
        self. current_user_id = None # to store the users ID

        # Configure the grid to make the notebook expand --> crucial for making UI responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # Initialize Database Manager and create tables
        self.db_manager = DatabaseManager(os.path.join(os.getcwd(), "campuslink.db"))
        self.db_manager.create_tables()

        # Create and manage the Login/Main app views
        # Create a container frame to hold either the login view or the main window
        # note: instead of packing the ttk.Notebook directly into the main window, we put everything
        # inside this main_container. this makes it easier to switch what's visible on the screen.
        # we can either show the login set or the main app set
        self.main_container = ttk.Frame(self, padding ="10")
        self.main_container.grid(row=0, column=0, sticky="nsew")

        # Create a login frame (initially visible)
        # This is for the login and create account page. 
        # its packed into the main_container so its the only thing visible when the app starts
        self.login_frame = ttk.Frame(self.main_container)
        self.login_frame.pack(fill="both", expand=True)

        # Create the Main app view (intially hidden)
        # This Frame is for the main application
        # including the ttk.Notebook and all the tabs. its created but not packed initially, so
        # its ot visible when the app starts. its only shown after a successful login
        self.app_frame = ttk.Frame(self.main_container)


        # Create instance of LoginUI class --> passing ref to call back func (show_...)
        # note: doesnt call it right away, saves to call later after successful log in        
        self.login_ui = LoginUI(self.login_frame, self.db_manager, self.show_main_app_view)


        # Create a Notebook (tabbed interface) Widget for navigation
        # This is a simple and effective way to switch between different 
        # sections of the application for the prototype.
        self.notebook = ttk.Notebook(self.app_frame) # creates instance of notebook widget
        ##self.notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) # places notebook widget in main window
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Create Frames for each Feature Section ---
        # These frames will hold the UI elements for each part of the app.
        # For the prototype, they will initially be empty or contain basic labels.

        # Activities/Task Schedule Manager Frame
        self.activities_frame = ttk.Frame(self.notebook, padding="10") # creates frame
        ##self.activities_frame.grid_rowconfigure(0, weight=1) 
        ##self.activities_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.activities_frame, text="Activities") # adds frame as tab to notebook
        # Add a placeholder label for now -> inside frame
        # ttk.Label(self.activities_frame, text="Activities & Task Schedule Manager (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Events Calendar Frame -> removing events frame -> modified proj to meet deadline
        #self.events_frame = ttk.Frame(self.notebook, padding="10")
        ##self.events_frame.grid_rowconfigure(0, weight=1)
        ##self.events_frame.grid_columnconfigure(0, weight=1)
        #self.notebook.add(self.events_frame, text="Events")
        # Add a placeholder label for now
        #ttk.Label(self.events_frame, text="Events Calendar (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Bulletin Board Frame
        self.bulletin_frame = ttk.Frame(self.notebook, padding="10")
        ##self.bulletin_frame.grid_rowconfigure(0, weight=1)
        ##self.bulletin_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.bulletin_frame, text="Bulletin Board")
        # Add a placeholder label for now
        #ttk.Label(self.bulletin_frame, text="Community Bulletin Board (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Emergency Contacts Frame
        self.emergency_frame = ttk.Frame(self.notebook, padding="10")
        ##self.emergency_frame.grid_rowconfigure(0, weight=1)
        ##self.emergency_frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.emergency_frame, text="Emergency Contacts")
        # Add a placeholder label for now
        #ttk.Label(self.emergency_frame, text="Emergency Contacts & Quick Access (Coming Soon!)", font=("Arial", 14)).pack(pady=50)

        # Account Info Frame
        self.account_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.account_frame, text="Account Info")
        ##ttk.Label(self.account_frame, text = "User Account Information (Coming Soon!)", font=("Arial", 14)).pack(pady=50)
        

        # Create instance of AccountUI
        self.account_ui = None
        # Create instance of BulletinUI
        self.bulletin_ui = None
        # Create instance of EmergencyUI
        self.emergency_contacts_ui = EmergencyContactsUI(self.emergency_frame)


    # Create Methods to switch between views


    def show_main_app_view(self, username):


        """
        Switches from the login view to the main application view.
        This method will be called by the LoginUI upon a successful login.
        """

        self.current_user = username # stores username so the app can use it later
        self.current_user_id = self.db_manager.get_user_id(username) # get the user ID
        self.is_logged_in = True # sets boolean to true. i.e. someone is logged in
        self.login_frame.pack_forget() # key line for hiding the login screen
        self.app_frame.pack(fill="both", expand=True) # makes the main app frame visible by packing
        messagebox.showinfo("Success", f"Welcome, {username}!")

        # Create AccountUI instance after a successful login
        # We need the username to be set first before creating this UI.
        # second callback here! AccountUI will store this ref and call when logout clicked
        self.account_ui = AccountUI(self.account_frame, self.current_user, self.show_login_view)

        # Initialize the Activities UI and place it in its designated frame
        ActivitiesUI(self.activities_frame, self.current_user_id)   

        # Initialize the BulletinUI and place it in its designated frame
        self.bulletin_ui = BulletinUI(self.bulletin_frame, self.db_manager, self.current_user_id)     



    def show_login_view(self):


        """
        Switches from the main application view to the login view.
        This method will be called by the AccountUI upon logout.
        """

        self.is_logged_in = False # resets the applications state after logout
        self.current_user = None # resets user logged in to None
        self.current_user_id = None # clear the user ID

        # Destroy the AccountUI to clear the old username display -> upon logout so app resets ui
        if self.account_ui:
            for widget in self.account_frame.winfo_children():
                widget.destroy()
            self.account_ui = None

        # Destroy the BulletinUI to clear the old posts display
        if self.bulletin_ui:
            for widget in self.bulletin_frame.winfo_children():
                widget.destroy()
            self.bulletin_ui = None

        self.app_frame.pack_forget() # hides main applications tabbed interface
        self.login_frame.pack(fill="both", expand=True) # makes login screen visible again
        self.login_ui._clear_entries() # to clear previous login entries


# Entry point guard --> "Is this script currently the main program being run? Yes? Execute." 
if __name__ == "__main__":
    # Create an instance of the application
    app = CampusLinkApp()
    # Start the Tkinter event loop
    app.mainloop()
