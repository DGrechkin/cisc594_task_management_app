"""This file contains the back-end functions of the Task Manager App"""
from app.add_task_ui import AddTaskWindow

def add_task():
    """Triggers "Add Task" window to pop up

    :return:
    """
    add_task_window = AddTaskWindow()
    add_task_window.exec_()
    print("Add button is pressed")
    pass


def completed_task(row):
    """Task is completed. Remove record from the DB and refresh the table view

    :param row: dict, Task record that is completed
    :return:
    """
