"""This file contains TaskManagementWindow class"""
import datetime

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

from app import db_transfer
from app import utils
from app.constants import *


class TaskManagementWindow(QMainWindow):
    def __init__(self):
        super(TaskManagementWindow, self).__init__()
        self.title = TASK_MANAGEMENT_TOOL
        self.left = 150
        self.right = 150
        self.width = 700
        self.height = 600
        self.initUI()

    def initUI(self):
        """Build main window elements

        :return: None
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.width, self.height)

        self.build_add_button()

        sort_label = QLabel(LIST_TASKS_BY, self)
        sort_label.move(200, 25)

        self.build_sort_menu()
        self.sort_tasks(ID)

    def build_add_button(self):
        """Setup Add button that is creating a new task

        After the button is pressed a new pop window will appear with a form to create a new task

        :return: None
        """
        add_button = QPushButton(ADD, self)
        add_button.move(40, 25)
        add_button.clicked.connect(utils.add_task)

    def build_sort_menu(self):
        """Setup drop down Sort menu.

        Sort menu has 3 parameters to choose: ID, Priority, and Due Date.
        Once one of them is chosen the list of tasks get correspondingly sorted and rebuild
        "ID" is a default value

        :return: None
        """
        sort_drop_down = QComboBox(self)
        sort_drop_down.addItem(ID.upper())
        sort_drop_down.addItem(PRIORITY.capitalize())
        sort_drop_down.addItem(DUE_DATE_LABEL)
        sort_drop_down.move(280, 25)
        sort_drop_down.activated[str].connect(self.sort_tasks)

    def sort_tasks(self, sort_by):
        """Sort and rebuild the list of tasks by the selected parameter

        :param sort_by: str, parameter by which list should be sorted
        :return: None
        """
        print(f"{sort_by} is selected")
        tasks_data = db_transfer.get_tasks_data()

        # TODO: Add sorting algorithm for tasks

        self.build_tasks_list(tasks_data)

    def build_tasks_list(self, tasks_data):
        """List all tasks that still need to be completed.

        List of tasks is a table that has the following columns:
        +----+------------------+----------+--------------+----------+
        | ID | Task Description | Priority | Created Date | Due Date |
        +----+------------------+----------+--------------+----------+

        :param tasks_data: list, sorted list of tasks
        :return: None
        """
        print("Build tasks list in the main window")

        # Temporary task placeholder
        tasks_data = [
            {
                ID: str(1),
                DESCRIPTION: "Task Placeholder",
                PRIORITY: LOW,
                CREATED_DATE_COLUMN: str(datetime.datetime.utcnow()),
                DUE_DATE_COLUMN: str(datetime.datetime.utcnow() + datetime.timedelta(days=10)),
            }
        ]

        tasks_table = QTableWidget(self)
        tasks_table.setColumnCount(len(TASKS_COLUMNS))
        tasks_table.setRowCount(len(tasks_data))
        tasks_table.move(15, 70)
        tasks_table.resize(self.width - 30, self.height - 85)
        for row_index, row in enumerate(tasks_data):
            tasks_table.setItem(row_index, 0, QTableWidgetItem(1))
            for column_index, key in enumerate(TASKS_COLUMNS):
                tasks_table.setItem(row_index, column_index, QTableWidgetItem(row.get(key)))
            completed_button = QPushButton(COMPLETED)
            completed_button.clicked.connect(lambda: utils.completed_task(row))
            tasks_table.setCellWidget(row_index, len(TASKS_COLUMNS) - 1, completed_button)
        tasks_table.setHorizontalHeaderLabels(TASKS_LABELS)
        tasks_table.resizeColumnsToContents()
        tasks_table.resizeRowsToContents()
