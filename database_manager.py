# database_manager.py


import sqlite3 # imports library for working with SQLite databases
import hashlib # Used for securely hashing passwords
import os

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
        
        if self.conn is None:
            print("Database connection is not active.")
            return

        try:
            # SQL to create the users table
            # We store a hashed password instead of the plain-text password for security.
            
            # 1. creates table named USERS only if doesnt exist already
            # 2. creates a unique id for each user, which auto increments for every user
            #    note: serves as "primary key". identifies each row "user"
            # 3. stores the username as text
            #    note: NOT NULL means it cant be empty 
            #    note: UNIQUE means no two users can have same username
            # 4. stores the hased password as text (again, cant be empty)


            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                )
            ''')
        
            self.conn.commit() # commits changes to table
            print("Tables created successfully.")
        
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")




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

            # Check if a user was found and if the password hashes match
            if result and result[0] == password_hash:
                return True
            else:
                return False
        
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


