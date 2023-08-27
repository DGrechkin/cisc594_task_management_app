"""This file contains database read, write, delete functions"""
import sqlite3

from app.constants import *


def create_tasks_table():
    """This function creates a table where all tasks data are stored

    :return: None
    """
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT,
            created_date DATETIME default current_timestamp
        )
    """
    )

    conn.commit()
    conn.close()


def save_task(task_data: dict):
    """This function saves tasks data in database

    :param task_data: Dictionary with a task data
    :return: None
    """
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, due_date, priority)
        VALUES (?, ?, ?, ?)
    """,
        (
            task_data[TITLE],
            task_data[DESCRIPTION],
            task_data[DUE_DATE_LABEL],
            task_data[PRIORITY],
        ),
    )

    conn.commit()
    conn.close()


def get_tasks_data():
    """Read all tasks from the database and return it in list format

    :return: List
    """
    print("DB read is called")
    pass
