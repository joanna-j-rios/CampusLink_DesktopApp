# login_ui.py

import tkinter as tk
from tkinter import ttk, messagebox


class LoginUI:


    """
    Manages the user interface for the login and create account screens.
    It interacts with the DatabaseManager and the main app to change views.
    """


    def __init__(self, parent_frame, db_manager, show_main_app_callback):

        """
        Initializes the LoginUI.

        Args:
            parent_frame (ttk.Frame): The frame to place the UI widgets on.
            db_manager (DatabaseManager): An instance of the DatabaseManager for authentication.
            show_main_app_callback (function): The method in CampusLinkApp to call on successful login.
        """

        self.parent_frame = parent_frame
        self.db_manager = db_manager
        self.show_main_app_callback = show_main_app_callback
        
        self._create_login_widgets()



    def _create_login_widgets(self):

        """
        Creates and places all the login and create account widgets.
        """

        # --- Top-level frame for login content, centered ---
        main_login_frame = ttk.Frame(self.parent_frame, padding="20")
        main_login_frame.pack(expand=True)

        # --- Title ---
        title_label = ttk.Label(main_login_frame, text="CampusLink Login", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # --- Login Form Frame ---
        login_form_frame = ttk.Frame(main_login_frame)
        login_form_frame.pack(pady=10)

        # Username
        username_label = ttk.Label(login_form_frame, text="Username:")
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = ttk.Entry(login_form_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Password
        password_label = ttk.Label(login_form_frame, text="Password:")
        password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = ttk.Entry(login_form_frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Login Button
        login_button = ttk.Button(main_login_frame, text="Login", command=self._handle_login)
        login_button.pack(pady=10)

        # --- Separator and Create Account Section ---
        ttk.Separator(main_login_frame, orient="horizontal").pack(fill="x", pady=20)
        
        create_account_label = ttk.Label(main_login_frame, text="New to CampusLink?", font=("Arial", 12))
        create_account_label.pack(pady=5)
        
        create_account_button = ttk.Button(main_login_frame, text="Create Account", command=self._handle_create_account)
        create_account_button.pack()
    


    def _handle_login(self):

        """
        Handles the login button click.
        """

        username = self.username_entry.get()
        password = self.password_entry.get()
        
        """
        if self.db_manager.check_user(username, password):
            # If successful, call the callback to switch to the main app view
            self.show_main_app_callback(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
        """

        """
        Changes following...
        Handles the login process.
        
        This method now uses an if/elif/else block to handle the more
        specific return values from the database manager.
        """
        if not username or not password:
            messagebox.showwarning("Input Error", "Username and password cannot be empty.")
            return

        # Use the updated check_user method that returns a specific status string
        login_status = self.db_manager.check_user(username, password)
        
        # --- START OF HIGHLIGHTED CHANGE ---
        # The logic is now a decision tree based on the status string.
        if login_status == "success":
            # Correct username and password, so proceed with login.
            self.show_main_app_callback(username)
            self._clear_entries()
        elif login_status == "user_not_found":
            # User does not exist, show the specific message.
            messagebox.showwarning("Login Failed", "User does not exist. Please create an account by clicking 'Create Account'.")
        elif login_status == "incorrect_password":
            # User exists, but password is wrong.
            messagebox.showerror("Login Failed", "Incorrect password.")
        else:
            # An unexpected error occurred.
            messagebox.showerror("Error", "An unexpected error occurred.")

            
            
    def _handle_create_account(self):

        """
        Handles the create account button click.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Input Error", "Username and password cannot be empty.")
            return

        # Attempt to add the user to the database
        if self.db_manager.add_user(username, password):
            messagebox.showinfo("Success", f"Account for '{username}' created successfully! You can now log in.")
            self._clear_entries() # clears entries after successful creation        
        # note: The add_user method handles errors internally


    def _clear_entries(self):
        
        """
        Clears the username and password entry fields.
        """
        
        self.username_entry.delete(0, tk.END) # clears username field
        self.password_entry.delete(0, tk.END) # clears password field
 


