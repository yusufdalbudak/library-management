from tkinter import Tk, Label, Entry, Button, ttk, messagebox
from book_management import add_book, fetch_books, delete_book

def refresh_books():
    # Clear the table
    for row in book_table.get_children():
        book_table.delete(row)
    
    # Fetch books from the database
    books = fetch_books()
    for book in books:
        book_table.insert("", "end", values=book)

def handle_add_book():
    # Get input values
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    genre = genre_entry.get()
    copies = copies_entry.get()
    
    if title and author and isbn and genre and copies:
        add_book(title, author, isbn, genre, int(copies))
        refresh_books()  # Update the table after adding the book
        # Clear input fields
        title_entry.delete(0, 'end')
        author_entry.delete(0, 'end')
        isbn_entry.delete(0, 'end')
        genre_entry.delete(0, 'end')
        copies_entry.delete(0, 'end')
    else:
        print("All fields are required!")

def handle_delete_book():
    # Get selected book's ID
    selected_item = book_table.selection()
    if selected_item:
        book_id = book_table.item(selected_item)["values"][0]  # Get the ID from the first column
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the book with ID {book_id}?"):
            delete_book(book_id)  # Delete the book
            refresh_books()  # Refresh the table
    else:
        messagebox.showwarning("No Selection", "Please select a book to delete.")

# Initialize the main window
root = Tk()
root.title("Library Management System")
root.geometry("800x600")

# Input form for adding a new book
Label(root, text="Title").grid(row=0, column=0, padx=10, pady=10)
title_entry = Entry(root)
title_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Author").grid(row=1, column=0, padx=10, pady=10)
author_entry = Entry(root)
author_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="ISBN").grid(row=2, column=0, padx=10, pady=10)
isbn_entry = Entry(root)
isbn_entry.grid(row=2, column=1, padx=10, pady=10)

Label(root, text="Genre").grid(row=3, column=0, padx=10, pady=10)
genre_entry = Entry(root)
genre_entry.grid(row=3, column=1, padx=10, pady=10)

Label(root, text="Copies").grid(row=4, column=0, padx=10, pady=10)
copies_entry = Entry(root)
copies_entry.grid(row=4, column=1, padx=10, pady=10)

Button(root, text="Add Book", command=handle_add_book).grid(row=5, column=1, pady=10)

# Table to display books
columns = ("ID", "Title", "Author", "ISBN", "Genre", "Copies", "Available")
book_table = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
book_table.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Set column headings
for col in columns:
    book_table.heading(col, text=col)

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=book_table.yview)
book_table.configure(yscroll=scrollbar.set)
scrollbar.grid(row=6, column=4, sticky="ns")

# Add delete button
Button(root, text="Delete Book", command=handle_delete_book).grid(row=7, column=1, pady=10)

# Initial table population
refresh_books()

# Run the application
root.mainloop()
