# Library Management System

## Overview
The Library Management System is a Python-based project designed to help manage books in a library. This application allows for performing basic operations such as adding, deleting, updating, and viewing books in the library's database. The system utilizes SQLite to store and manage the data, ensuring fast and efficient handling of records.

### Features
- **Add Books**: Add new books to the library's database.
- **Update Books**: Modify the details of existing books.
- **Delete Books**: Remove books from the database.
- **View Books**: Display the list of books currently in the library.

## Installation

### Prerequisites
To run this project, you will need to have Python 3.6 or later installed, along with the required Python packages. It's recommended to use a virtual environment to manage dependencies.

1. Clone the repository:
   ```bash
   git clone git@github.com:yusufdalbudak/library-management.git



library-management/
├── .venv/               # Virtual environment folder
├── assets/               # Folder for any assets (images, etc.)
├── src/                  # Main source code
│   ├── database/         # SQLite database file
│   ├── __init__.py       # Package initialization file
│   ├── book_management.py # Book management logic
│   ├── utils.py          # Utility functions
│   └── main.py           # Main entry point for the application
├── Readme.md             # This file
└── requirements.txt      # Python dependencies
