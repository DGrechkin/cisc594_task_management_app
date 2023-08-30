"""This file contains TaskManagementWindow class"""
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QLineEdit

from app import add_task_ui
from app import db_transfer
from app.constants import *


class TaskManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = TASK_MANAGEMENT_TOOL
        self.left = 150
        self.right = 150
        self.width = 700
        self.height = 600
        self.tasks_table = QTableWidget(self)
        self.sort_drop_down = QComboBox(self)
        self.category_filter_input = QLineEdit(self)
        self.initUI()

    def initUI(self):
        """Build main window elements

        :return: None
        """
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.build_add_button()

        sort_label = QLabel(LIST_TASKS_BY, self)
        sort_label.move(200, 25)

        self.build_sort_menu()
        self.sort_tasks(ID)
        self.build_category_filter_input()

    def build_add_button(self):
        """Setup Add button that is creating a new task

        After the button is pressed a new pop window will appear with a form to create a new task

        :return: None
        """
        add_button = QPushButton(ADD, self)
        add_button.move(40, 25)
        add_button.clicked.connect(self.add_task)

    def build_sort_menu(self):
        """Setup drop down Sort menu.

        Sort menu has 3 parameters to choose: ID, Priority, and Due Date.
        Once one of them is chosen the list of tasks get correspondingly sorted and rebuild
        "ID" is a default value

        :return: None
        """
        self.sort_drop_down.addItem(ID.upper())
        self.sort_drop_down.addItem(PRIORITY.capitalize())
        self.sort_drop_down.addItem(DUE_DATE_LABEL)
        self.sort_drop_down.move(280, 25)
        self.sort_drop_down.activated[str].connect(self.sort_tasks)

    def sort_tasks(self, sort_by):
        """Sort and rebuild the list of tasks by the selected parameter

        :param sort_by: str, parameter by which list should be sorted
        :return: None
        """
        tasks_data = db_transfer.get_tasks_data()

        if sort_by == ID.upper():
            tasks_data = sorted(tasks_data, key=lambda task: task[ID])
        elif sort_by == PRIORITY.capitalize():
            tasks_data = sorted(
                tasks_data, key=lambda task: PRIORITY_MAPPING.get(task[PRIORITY])
            )
        elif sort_by == DUE_DATE_LABEL:
            tasks_data = sorted(tasks_data, key=lambda task: task[DUE_DATE_COLUMN])

        self.build_tasks_list(tasks_data)

    def build_tasks_list(self, tasks_data: list):
        """List all tasks that still need to be completed.

        List of tasks is a table that has the following columns:
        +----+-------+------------------+----------+--------------+----------+
        | ID | Title | Task Description | Priority | Created Date | Due Date |
        +----+-------+------------------+----------+--------------+----------+

        :param tasks_data: list, sorted list of tasks
        :return: None
        """
        self.tasks_table.setColumnCount(len(TASKS_COLUMNS))
        self.tasks_table.setRowCount(len(tasks_data))
        self.tasks_table.move(15, 70)
        self.tasks_table.resize(self.width - 30, self.height - 85)
        for row_index, row in enumerate(tasks_data):
            self.tasks_table.setItem(row_index, 0, QTableWidgetItem(1))
            for column_index, key in enumerate(TASKS_COLUMNS):
                self.tasks_table.setItem(
                    row_index, column_index, QTableWidgetItem(row.get(key))
                )
            completed_button = QPushButton(COMPLETED)
            completed_button.clicked.connect(lambda _, row_id=row.get(ID): self.completed_task(row_id))
            self.tasks_table.setCellWidget(
                row_index, len(TASKS_COLUMNS) - 1, completed_button
            )
        self.tasks_table.setHorizontalHeaderLabels(TASKS_LABELS)
        header = self.tasks_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Fixed)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.tasks_table.resizeRowsToContents()

    def add_task(self):
        """Triggers "Add Task" window to pop up

        Once task is added, refresh and sort the table view to display the new task

        :return: None
        """
        add_window = add_task_ui.AddTaskWindow()
        add_window.exec_()
        self.sort_tasks(ID)

    def completed_task(self, task_id: str):
        """Task is completed. Remove record from the DB and refresh the table view

        :param task_id: str, Task ID string
        :return: None
        """
        db_transfer.remove_task(int(task_id))
        current_sort_option = self.sort_drop_down.currentText()
        self.sort_tasks(current_sort_option)

    def filter_tasks_by_category(self, category):
        tasks_data = db_transfer.get_tasks_data()
        filtered_tasks = [task for task in tasks_data if task[CATEGORY] == category]
        self.build_tasks_list(filtered_tasks)

    def build_category_filter_input(self):
        """Add a text box where users can enter a category to filter tasks

        :return: None
        """
        category_filter_label = QLabel(f"Filter by {CATEGORY.capitalize()}:", self)
        category_filter_label.move(400, 25)

        self.category_filter_input.move(520, 25)
        self.category_filter_input.textChanged.connect(self.apply_category_filter)

    def apply_category_filter(self):
        category = self.category_filter_input.text()
        if category:
            self.filter_tasks_by_category(category)
        else:
            self.sort_tasks(ID)

