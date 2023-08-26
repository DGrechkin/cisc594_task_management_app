"""This file contains AddTaskWindow class"""
from datetime import datetime

from app.constants import *

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QPushButton


class AddTaskWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.width = 350
        self.height = 170
        self.resize(self.width, self.height)
        self.description_text_box = QPlainTextEdit(self)
        self.priority_drop_down = QComboBox(self)
        self.due_date_box = QDateTimeEdit(self, calendarPopup=True)
        self.save_button = QPushButton(SAVE, self)
        self.close_button = QPushButton(CLOSE, self)
        self.task_data = {}
        self.initUI()

    def initUI(self):
        """Build a pop-up window to add a task

        :return: None
        """
        self.setWindowTitle(ADD_TASK_TITLE)
        header = QLabel(ADD_TASK_DESCRIPTION, self)
        header.move(15, 5)

        self.add_description_widget()
        self.add_priority_widget()
        self.add_due_date_widget()
        self.add_save_button()
        self.add_close_button()

    def add_description_widget(self):
        """Add a text box where users can enter their task description

        :return: None
        """
        description_label = QLabel(TASK_DESCRIPTION, self)
        description_label.move(15, 30)

        self.description_text_box.resize(self.width - 30, 50)
        self.description_text_box.move(15, 50)

    def add_priority_widget(self):
        """Add a drop-down menu where users can select a priority

        There are 3 priority values: low, medium, and high

        :return: None
        """
        priority_label = QLabel(f"{PRIORITY.capitalize()}:", self)
        priority_label.move(15, 110)

        self.priority_drop_down.addItem(LOW)
        self.priority_drop_down.addItem(MEDIUM)
        self.priority_drop_down.addItem(HIGH)
        self.priority_drop_down.move(60, 106)

    def add_due_date_widget(self):
        """Add a menu where users can select due date and time

        :return: None
        """
        due_date_label = QLabel(f"{DUE_DATE_LABEL}:", self)
        due_date_label.move(155, 110)

        self.due_date_box.setDateTime(datetime.now())
        self.due_date_box.setDisplayFormat(DATETIME_FORMAT)
        self.due_date_box.move(210, 106)
        self.due_date_box.resize(125, 20)

    def collect_task_data(self):
        """The function collects user input in a dictionary

        :return: None
        """
        self.task_data[DESCRIPTION] = self.description_text_box.toPlainText()
        self.task_data[PRIORITY] = self.priority_drop_down.currentText()
        due_date = self.due_date_box.dateTime().toString(DATETIME_FORMAT)
        self.task_data[DUE_DATE_LABEL] = due_date

        self.accept()

    def add_save_button(self):
        """Add save button for task creation window

        :return: None
        """
        self.save_button.move(self.width - 170, self.height - 30)
        self.save_button.clicked.connect(self.collect_task_data)

    def add_close_button(self):
        """Add close button for task creation window

        :return: None
        """
        self.close_button.move(self.width - 85, self.height - 30)
        self.close_button.clicked.connect(self.reject)
