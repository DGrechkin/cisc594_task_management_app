"""This file contains the back-end functions of the Task Manager App"""
from app import add_task_ui
from app.db_transfer import save_task
from app.db_transfer import get_tasks_data
from app.db_transfer import remove_task


def add_task():
    """Triggers "Add Task" window to pop up

    Once task is added, refresh and sort the table view to display the new task

    :return: None
    """
    add_window = add_task_ui.AddTaskWindow()
    add_window.exec_()
    save_task(add_window.task_data)
    # TODO: Need to send task data to the main window and refresh the table, so new records get displayed
    print(get_tasks_data())


def completed_task(row):
    """Task is completed. Remove record from the DB and refresh the table view

    :param row: dict, Task record that is completed
    :return: None
    """
    pass
