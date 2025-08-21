# database_manager.py


import sqlite3 # imports library for working with SQLite databases
import hashlib # Used for securely hashing passwords
import os
import datetime # for timestamps on posts

class DatabaseManager:
    """
    Manages all database interactions for the CampusLink app, including
    creating tables, adding users, and verifying credentials.
    """
  
    def __init__(self, db_path):
        
        """
        Constructor. Initializes the database connection.
        
        Args:
            db_path (str): The full file path to the SQLite database file.
        """
        
        # Create variable to hold database connection
        self.conn = None # initializes instance variable None
        
        # Define error handling block to catch any problems that might occur when trying to connect
        # to the database. if something goes wrong we'll print error message
        try:
            # Connect to the database file
            self.conn = sqlite3.connect(db_path)
            # Create a cursor object to execute SQL commands
            self.cursor = self.conn.cursor()
            print(f"Database connection established to {db_path}")

        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")




    def create_tables(self):
        
        """
        Creates the necessary tables for the application if they don't exist.
        This includes a 'users' table for authentication.
        """
        
        # Check connection to db, if none stop
        if self.conn is None:
            print("Database connection is not active.")
            return


        try:

            # ----- Table for user authentication ---

            # SQL to create the users table
            # We store a hashed password instead of the plain-text password 
            # for security.
            
            # 1. creates table named "users" only if doesnt exist already
            # columns:
            # 2. id : creates a unique id for each user --> auto increments 
            # for every user
            #    note: serves as "primary key". identifies each row (user)
            # 3. username: stores the username as text
            #    note: NOT NULL means it cant be empty 
            #    note: UNIQUE means no two users can have same username
            # 4. password_hash: stores the hased password as non empty text


            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                )
            ''')



            # --- Table for the user's activities and tasks ---
            
            # SQL to crete table for users actvities and tasks
            # Defining tasks table (linked to the users table via user id)

            # 1. creates table named "tasks" only if it doesnt exist already
            # columns: 
            # 2. id: unique identifier for each task ("name" of first column)
            # 3. user_id: will store the ID of the user who "owns" the task
            # thus linking this task back to a specific entry in the users table
            # 4. task_name: will store the title or name of the task
            #    note: stored as text with rule preventing empty task entry
            # 5. description: for storing details of task
            #    note: stored as text but optional (can be left empty)
            # 6. due_date: for storing the due data of a task
            # 7. is_completed: track the completion status of the task
            #    note: 0 - false (not completed)
            #    note: 1 - true (completed)
            #    note: every task must have a completion status
            #    note: each task is auto set to 0 (not completed)
            # 8. declares user_id as 'FOREIGN_KEY'
            #    note: links tables
            #    note: tells db that user_id in this table must coorespond to
            # existing id in the users table. preventing tasks from being
            # created by users that dont exist


            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    task_name TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT,
                    is_completed BOOLEAN NOT NULL DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')


            
            # ----- Table for bulletin board posts -----
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')
        

            self.conn.commit() # commits changes to table
            print("Tables created successfully.")
        
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")


    
    def get_user_id(self, username):
    
        """
        Retrieves the user ID for a given username.
        
        Args:
            username (str): The username to find.
        
        Returns:
            int: The user's ID, or None if the user is not found.
    
        """

        if self.conn is None:
            return None
        
        try:
            self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            result = self.cursor.fetchone()
            return result[0] if result else None

        except sqlite3.Error as e:
            print(f"Error getting user ID: {e}")
            return None



    def get_username_by_id(self, user_id):
        """
        Retrieves the username for a given user ID.
        
        Args:
            user_id (int): The ID of the user.
        
        Returns:
            str: The username, or None if the ID is not found.
        """
        if self.conn is None:
            return None
        try:
            self.cursor.execute("SELECT username FROM users WHERE id = ?", (user_id,))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Error getting username by ID: {e}")
            return None


    def add_user(self, username, password):
        
        """
        Adds a new user to the database (USERS table). The password is first hashed
        for security before being stored.
        
        Args:
            username (str): The new user's username.
            password (str): The new user's plain-text password.
            
        Returns:
            bool: True if the user was added, False otherwise.
        """
        
        # Check if connection is active
        if self.conn is None:
            print("Database connection is not active.")
            return False

        # Hash the password using a secure hashing algorithm (SHA-256)
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Insert and commit data (new user) into db
        try:
            self.cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            self.conn.commit()
            print(f"User '{username}' added successfully.")
            return True
        
        # Handle if someone tries to create an account with username that already exists
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
            return False
        
        # Catches any other errors
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            return False




    def check_user(self, username, password):
        
        """
        Checks if a user's credentials are correct by hashing the provided
        password and comparing it to the stored hash.
        
        Args:
            username (str): The username to check.
            password (str): The plain-text password to check.
            
        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        
        # Check if connection has been lost
        if self.conn is None:
            return False

        # Hash the provided password to compare with the stored hash
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Query db for password of username provided and gets data from one row (password hash, if found)
        try:
            self.cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            result = self.cursor.fetchone() # attempts to retrieve stored hash for given username
            # note: result will return either return tuple i.e. user found or false i.e not found
            #       result[0] gets actual hash string from tuple            

            """
            # Check if a user was found and if the password hashes match
            if result and result[0] == password_hash:
                return True
            else:
                return False
            """
            
            if not result:
                # This means the query returned no rows, so the user doesn't exist.
                return "user_not_found"
            
            if result[0] == password_hash:
                # The password hash matches the one in the database.
                return "success"
            else:
                # The user exists, but the password hashes don't match.
                return "incorrect_password"

        
        except sqlite3.Error as e:
            print(f"Error checking user credentials: {e}")
            return False




    def close(self):

        """
        Closes the database connection.
        """
        
        # Checks if connected
        if self.conn:
            self.conn.close() # closes connection
            print("Database connection closed.")




    def add_task(self, user_id, task_name, description, due_date):

        """
        Adds a new task to the tasks table for a specific user.
        
        Args:
            user_id (int): The ID of the user who owns the task.
            task_name (str): The name of the new task.
            description (str): A description for the task.
            due_date (str): The due date of the task (e.g., 'YYYY-MM-DD').
        """

        if self.conn is None:
            print("Database connection is not active.")
            return
        
        try:
            self.cursor.execute(
                "INSERT INTO tasks (user_id, task_name, description, due_date) VALUES (?, ?, ?, ?)",
                (user_id, task_name, description, due_date)
            )
            self.conn.commit()
            print(f"Task '{task_name}' added successfully for user ID {user_id}.")
        except sqlite3.Error as e:
            print(f"Error adding task: {e}")




    def get_tasks(self, user_id):

        """
        Retrieves all tasks for a specific user.
        
        Args:
            user_id (int): The ID of the user whose tasks to retrieve.
            
        Returns:
            list: A list of task dictionaries, or an empty list if no tasks are found.
        """

        if self.conn is None:
            print("Database connection is not active.")
            return []
            
        try:
            self.cursor.execute(
                "SELECT id, task_name, description, due_date, is_completed FROM tasks WHERE user_id = ?",
                (user_id,)
            )
            tasks = []
            for row in self.cursor.fetchall():
                task_data = {
                    "id": row[0],
                    "task_name": row[1],
                    "description": row[2],
                    "due_date": row[3],
                    "is_completed": bool(row[4])
                }
                tasks.append(task_data)
            return tasks
        except sqlite3.Error as e:
            print(f"Error getting tasks: {e}")
            return []




    def mark_task_complete(self, task_id):

        """
        Marks a task as completed in the database.
        
        Args:
            task_id (int): The ID of the task to update.
        """

        if self.conn is None:
            print("Database connection is not active.")
            return
            
        try:
            self.cursor.execute(
                "UPDATE tasks SET is_completed = 1 WHERE id = ?",
                (task_id,)
            )
            self.conn.commit()
            print(f"Task ID {task_id} marked as complete.")
        except sqlite3.Error as e:
            print(f"Error marking task as complete: {e}")



    def delete_task(self, task_id):

        """
        Deletes a task from the database.
        
        Args:
            task_id (int): The ID of the task to delete.
        """

        if self.conn is None:
            print("Database connection is not active.")
            return
        
        try:
            self.cursor.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,)
            )
            self.conn.commit()
            print(f"Task ID {task_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting task: {e}")



    def add_post(self, user_id, title, content):
        
        """
        Adds a new post to the posts table.
        """
        
        if self.conn is None:
            print("Database connection is not active.")
            return
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                "INSERT INTO posts (user_id, title, content, timestamp) VALUES (?, ?, ?, ?)",
                (user_id, title, content, timestamp)
            )
            self.conn.commit()
            print(f"Post '{title}' added successfully for user ID {user_id}.")
        except sqlite3.Error as e:
            print(f"Error adding post: {e}")



    def get_posts(self):
        
        """
        Retrieves all posts from the database, sorted by timestamp.
        
        Returns:
            list: A list of post dictionaries, or an empty list.
        """
        
        if self.conn is None:
            print("Database connection is not active.")
            return []
        try:
            self.cursor.execute("SELECT id, user_id, title, content, timestamp FROM posts ORDER BY timestamp DESC")
            posts = []
            for row in self.cursor.fetchall():
                post_data = {
                    "id": row[0],
                    "user_id": row[1],
                    "title": row[2],
                    "content": row[3],
                    "timestamp": row[4]
                }
                posts.append(post_data)
            return posts
        except sqlite3.Error as e:
            print(f"Error getting posts: {e}")
            return []



    def delete_post(self, post_id):
       
        """
        Deletes a post from the database.
        """
       
        if self.conn is None:
            print("Database connection is not active.")
            return
        try:
            self.cursor.execute(
                "DELETE FROM posts WHERE id = ?",
                (post_id,)
            )
            self.conn.commit()
            print(f"Post ID {post_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting post: {e}")

