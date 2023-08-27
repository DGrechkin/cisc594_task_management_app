"""This file contains database read, write, delete functions"""
import sqlite3

from app.constants import *


def create_tasks_table():
    """This function creates a table where all tasks data are stored

    :return: None
    """
    conn = sqlite3.connect(TASKS_DB)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT,
            created_date DATETIME default (strftime('%Y-%m-%d %H:%M', 'now', 'localtime'))
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
    conn = sqlite3.connect(TASKS_DB)
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

    :return: List of tasks
    """
    conn = sqlite3.connect(TASKS_DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.commit()

    tasks_list = []
    for row in rows:
        task = dict()
        (
            task[ID],
            task[TITLE],
            task[DESCRIPTION],
            task[DUE_DATE_COLUMN],
            task[PRIORITY],
            task[CREATED_DATE_COLUMN],
        ) = row
        task[ID] = f"{task[ID]:02}"
        tasks_list.append(task)

    cursor.close()
    conn.close()

    return tasks_list


def remove_task(task_id: int):
    """This function deletes a task record by unique ID

    :param task_id: Unique ID integer value
    :return: None
    """
    conn = sqlite3.connect(TASKS_DB)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM tasks WHERE id = {task_id}")
    conn.commit()
    cursor.close()
    conn.close()
