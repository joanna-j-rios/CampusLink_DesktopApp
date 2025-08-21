# emergency_contacts_ui.py

import tkinter as tk
from tkinter import ttk

class EmergencyContactsUI:
    """
    Manages the user interface for the Emergency Contacts tab.
    This class displays a static list of important contact numbers.
    """

    def __init__(self, parent_frame):
       
        """
        Initializes the EmergencyContactsUI.

        Args:
            parent_frame (ttk.Frame): The frame to place the UI widgets on.
        """
       
        self.parent_frame = parent_frame
        self._create_widgets()

    def _create_widgets(self):
       
        """
        Creates and places all the widgets for the Emergency Contacts tab.
        """
       
        # Main header
        header = ttk.Label(self.parent_frame, text="Emergency Contacts", font=("Arial", 18, "bold"))
        header.pack(pady=10)

        # Content frame for contacts
        content_frame = ttk.Frame(self.parent_frame, padding="20")
        content_frame.pack(fill="both", expand=True)

        # --- Emergency Services ---
        emergency_label = ttk.Label(content_frame, text="Campus & General Emergency Services", font=("Arial", 12, "bold"))
        emergency_label.pack(anchor="w", pady=(10, 5))

        # Example Contact 1
        police_label = ttk.Label(content_frame, text="University Police: (956)882-4911", font=("Arial", 10))
        police_label.pack(anchor="w")

        # Example Contact 2
        medical_label = ttk.Label(content_frame, text="Student Health Center: (956)665-2511", font=("Arial", 10))
        medical_label.pack(anchor="w")

        # --- University Services ---
        services_label = ttk.Label(content_frame, text="\nUniversity Services", font=("Arial", 12, "bold"))
        services_label.pack(anchor="w", pady=(10, 5))

        # Example Contact 3
        counseling_label = ttk.Label(content_frame, text="Counseling Center: (956)665-2574", font=("Arial", 10))
        counseling_label.pack(anchor="w")

        # Example Contact 4
        helpdesk_label = ttk.Label(content_frame, text="IT Help Desk: (956)665-2020", font=("Arial", 10))
        helpdesk_label.pack(anchor="w")

        # Example Contact 4
        ucentral_label = ttk.Label(content_frame, text="UCentral: (956)882-4026", font=("Arial", 10))
        ucentral_label.pack(anchor="w")