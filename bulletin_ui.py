# bulletin_ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from database_manager import DatabaseManager # Import the DatabaseManager

class BulletinUI:
    
    """
    Manages the user interface for the Bulletin Board tab.
    This class handles displaying posts and opening a dialog to create new ones.
    """
    
    def __init__(self, parent_frame, db_manager, user_id):
      
        """
        Initializes the BulletinUI.

        Args:
            parent_frame (ttk.Frame): The frame to place the UI widgets on.
            db_manager (DatabaseManager): An instance of the DatabaseManager.
            user_id (int): The ID of the currently logged-in user.
        """
       
        self.parent_frame = parent_frame
        self.db_manager = db_manager
        self.user_id = user_id
        
        # Call the method to set up the UI
        self._create_widgets()
        self.refresh_post_list()



    def _create_widgets(self):
        
        """
        Sets up the UI elements for the bulletin board tab.
        """
        
        # Main header
        header = ttk.Label(self.parent_frame, text="Community Bulletin Board", font=("Arial", 18, "bold"))
        header.pack(pady=10)

        # Frame for post list
        self.post_list_frame = ttk.Frame(self.parent_frame)
        self.post_list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Add Post button
        self.add_post_button = ttk.Button(self.parent_frame, text="Create New Post", command=self._open_add_post_dialog)
        self.add_post_button.pack(pady=10)



    def _open_add_post_dialog(self):
        """
        Opens a new dialog window to add a post.
        """
        AddPostDialog(self.parent_frame, self.db_manager, self.user_id, self.refresh_post_list)

    def refresh_post_list(self):
       
        """
        Refreshes the displayed list of posts by fetching them from the database.
        """
       
        # Clear existing posts
        for widget in self.post_list_frame.winfo_children():
            widget.destroy()

        posts = self.db_manager.get_posts() # Note: We get all posts, not just for one user.
        
        if posts:
            for post in posts:
                # Create a frame for each post
                post_container = ttk.Frame(self.post_list_frame, relief="solid", borderwidth=1, padding=10)
                post_container.pack(fill="x", padx=10, pady=5)

                # Fetch username for the post
                username = self.db_manager.get_username_by_id(post['user_id'])
                
                # Post Title and Author
                title_label = ttk.Label(post_container, text=f"Title: {post['title']}", font=("Arial", 12, "bold"))
                title_label.pack(anchor="w")

                author_label = ttk.Label(post_container, text=f"By: {username or 'Unknown User'}", font=("Arial", 10, "italic"))
                author_label.pack(anchor="w")
                
                # Post Content
                content_label = ttk.Label(post_container, text=post['content'], wraplength=500)
                content_label.pack(anchor="w", pady=(5, 10))

                # Delete button for the post author only --> only you can delete your posts not someone else
                if post['user_id'] == self.user_id:
                    delete_button = ttk.Button(
                        post_container,
                        text="Delete",
                        command=lambda post_id=post['id']: self._delete_post(post_id)
                    )
                    delete_button.pack(side="right")
        else:
            no_posts_label = ttk.Label(self.post_list_frame, text="No posts on the bulletin board yet.")
            no_posts_label.pack(padx=10, pady=10)



    def _delete_post(self, post_id):
        
        """
        Calls the database manager to delete a post and refreshes the list.
        """
       
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this post?"):
            self.db_manager.delete_post(post_id)
            self.refresh_post_list()
            messagebox.showinfo("Success", "Post deleted!")




class AddPostDialog(tk.Toplevel):
    
    """
    A dialog window for adding a new bulletin board post.
    """

    def __init__(self, parent, db_manager, user_id, on_post_added):
        super().__init__(parent)
        self.parent = parent
        self.db_manager = db_manager
        self.user_id = user_id
        self.on_post_added = on_post_added

        self.title("Create New Post")
        self.geometry("500x350")
        self.resizable(False, False)
        self.grab_set()  # Make this dialog modal --> to display over Toplevel window (bulletin tab)

        self._create_widgets()



    def _create_widgets(self):
        
        """
        Creates the input fields and buttons for the form.
        
        """
        frame = ttk.Frame(self, padding="10")
        frame.pack(fill="both", expand=True)

        # --- Post Title Input ---
        ttk.Label(frame, text="Post Title:", font=("Arial", 10, "bold")).pack(pady=(5, 0), anchor="w")
        self.title_entry = ttk.Entry(frame, width=60)
        self.title_entry.pack(pady=(0, 10), fill="x")

        # --- Post Content Input ---
        ttk.Label(frame, text="Content:", font=("Arial", 10, "bold")).pack(pady=(5, 0), anchor="w")
        self.content_text = tk.Text(frame, width=60, height=10)
        self.content_text.pack(pady=(0, 10), fill="both", expand=True)

        # --- Create Post Button ---
        create_button = ttk.Button(frame, text="Create Post", command=self._add_post)
        create_button.pack(pady=(10, 0))



    def _add_post(self):
        
        """
        Handles the form submission and saves the new post.
        """
        
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not title or not content:
            messagebox.showerror("Input Error", "Title and content are required.")
            return

        try:
            self.db_manager.add_post(self.user_id, title, content)
            messagebox.showinfo("Success", "Post created successfully!")
            self.on_post_added()  # Call the refresh function
            self.destroy() # Close the dialog
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add post: {e}")
