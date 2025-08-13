# account_ui.py

import tkinter as tk
from tkinter import ttk

class AccountUI:

    """
    Manages the user interface for the user's account tab.
    This includes displaying user information and a logout button.
    """

    def __init__(self, parent_frame, current_user, logout_callback):

        """
        Initializes the AccountUI.

        Args:
            parent_frame (ttk.Frame): The frame to place the UI widgets on.
            current_user (str): The username of the currently logged-in user.
            logout_callback (function): A method in the main app to call when logging out.
            * note: will referrence show_login_view in main when logout button is clicked
        """

        # Instance Variables
        self.parent_frame = parent_frame # store parent frame in var so its accessible
        self.current_user = current_user # stores logged in users name as an instance var.
        self.logout_callback = logout_callback # stores callback func so _handle_logout
                                               # can call it later
        # Create Widget
        self._create_widgets() # calls helper method to create visual elements for tab



    def _create_widgets(self):

        """
        Creates and places all the widgets for the Account tab.
        """

        # Top-level frame for centered content
        content_frame = ttk.Frame(self.parent_frame, padding="20") # frame is created to
                                                                   # contain all widgets
        content_frame.pack(expand=True) # packed to keep contents centered in the tab

        # Create welcome message label --> f string to dynamically insert username 
        welcome_label = ttk.Label(
            content_frame, 
            text=f"Hello, {self.current_user}!", 
            font=("Arial", 16, "bold")
        )

        welcome_label.pack(pady=10) # pack to place inside parent

        # A label to show this is the account page --> provides description of tab
        info_label = ttk.Label(
            content_frame, 
            text="This is your account page.",
            font=("Arial", 12)
        )

        info_label.pack(pady=5)

        # Logout button
        logout_button = ttk.Button(
            content_frame, 
            text="Logout", 
            command=self._handle_logout # button will call specified method whenever clicked
        )

        logout_button.pack(pady=20)


    
    def _handle_logout(self):

        """
        Method is called when logout button is pressed.
        Calls the logout callback provided by the main application.
        """

        self.logout_callback()
        # note: essentially jumps back to main.py file and runs all the code inside
        # the show_login_view method (which hides the main application window, clears
        # the user information, and shows the login window again)

