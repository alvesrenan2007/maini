import sqlite3

DB_FILE = "finance.db"


def initialize_db():
    """
    Sets up the essential database tables, by executing SQLite queries.

    Args:
        none

    Returns
        none
    """


with sqlite3.connect(DB_FILE) as conn:
    conn.execute("""
                    CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        value INTEGER,
                        currency TEXT,
                        counterpart TEXT,
                        tags TEXT
                    )
                    """)
