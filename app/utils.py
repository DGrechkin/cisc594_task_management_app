"""This file contains the back-end functions of the Task Manager App"""
from app import add_task_ui
from app.db_transfer import save_task


def add_task():
    """Triggers "Add Task" window to pop up

    :return:
    """
    add_window = add_task_ui.AddTaskWindow()
    add_window.exec_()
    save_task(add_window.task_data)


def completed_task(row):
    """Task is completed. Remove record from the DB and refresh the table view

    :param row: dict, Task record that is completed
    :return:
    """
    pass
