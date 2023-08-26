"""This file contains the back-end functions of the Task Manager App"""
from app import add_task_window


def add_task():
    """Triggers "Add Task" window to pop up

    :return:
    """
    add_window = add_task_window.AddTaskWindow()
    add_window.exec_()
    print(add_window.task_data)
    pass


def completed_task(row):
    """Task is completed. Remove record from the DB and refresh the table view

    :param row: dict, Task record that is completed
    :return:
    """
    pass
