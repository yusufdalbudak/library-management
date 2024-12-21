import os
import sqlite3

# Function to get the absolute path of the database
def get_db_path():
    """
    Returns the absolute path to the library.db file.
    This is useful to avoid hardcoding paths and make the app more portable.
    """
    base_dir = os.path.dirname(__file__)  # Get the directory of this script
    db_path = os.path.join(base_dir, 'database', 'library.db')
    return db_path

# Function to create a database connection
def create_connection():
    """
    Establishes a connection to the SQLite database.
    Returns the connection object, or None if connection fails.
    """
    db_path = get_db_path()  # Get the path to the database
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error while connecting to database: {e}")
        return None

# Function to execute a query (e.g., SELECT, INSERT)
def execute_query(query, params=None):
    """
    Executes a SQL query (e.g., SELECT, INSERT) and returns the result.
    """
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()  # Commit the changes (useful for INSERT, UPDATE, DELETE)
            return cursor.fetchall()  # For SELECT queries
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            conn.close()
    else:
        print("Database connection failed.")
        return None

# Function to initialize the database (create necessary tables)
def initialize_db():
    """
    Initializes the database by creating necessary tables.
    This function should be called at the start to set up the database structure.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_date TEXT,
        isbn TEXT UNIQUE
    );
    """
    execute_query(create_table_query)

# Function to check if the database file exists
def db_exists():
    """
    Checks if the database file exists in the specified path.
    """
    return os.path.exists(get_db_path())

# Utility function to clean the database (optional, for testing purposes)
def reset_db():
    """
    Resets the database by dropping all tables. Use with caution!
    """
    drop_tables_query = """
    DROP TABLE IF EXISTS books;
    """
    execute_query(drop_tables_query)
    initialize_db()
