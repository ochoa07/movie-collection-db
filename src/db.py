# db.py — manages the SQLite database and Barbie movies table
import os
import sqlite3

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DB_PATH = os.path.join(DB_DIR, "barbie_movies.db")

def connect():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database and create the Barbie movies table if it doesn't exist."""
    os.makedirs(DB_DIR, exist_ok=True)
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS barbie_movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year INTEGER,
                genre TEXT,
                theme TEXT,
                character TEXT,
                rating REAL,
                watch_link TEXT,
                added_at TEXT DEFAULT (datetime('now'))
            );
            """
        )
        conn.commit()