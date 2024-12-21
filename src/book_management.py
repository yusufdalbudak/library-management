import sqlite3
import os

# Database connection setup
db_path = os.path.join('database', 'library.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Function to add a new book
def add_book(title, author, isbn, genre, copies):
    available = copies  # Initially, all copies are available.
    cursor.execute('''
    INSERT INTO books (title, author, isbn, genre, copies, available)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, author, isbn, genre, copies, available))
    conn.commit()
    print(f'Book "{title}" added successfully!')

# Function to fetch all books from the database
def fetch_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return books

# Function to delete a book from the database by its ID
def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
    conn.commit()
    print(f'Book with ID {book_id} deleted successfully!')
