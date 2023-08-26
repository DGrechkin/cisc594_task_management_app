"""This file contains database read, write, delete functions"""
import sqlite3

def create_tasks_table():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_task(title, description, due_date, priority):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, due_date, priority)
        VALUES (?, ?, ?, ?)
    """, (title, description, due_date, priority))

    conn.commit()
    conn.close()

def get_tasks_data():
    """Read all tasks from the database and return it in list format
    :return: List
    """
    print("DB read is called")
    pass
