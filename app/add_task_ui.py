"""This file contains AddTaskWindow class"""
from datetime import datetime

from app.constants import *
from app.db_transfer import save_task

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSpinBox


class AddTaskWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(ADD_TASK_TITLE)
        self.width = 350
        self.height = 170
        self.resize(self.width, self.height)
        self.description_text_box = QPlainTextEdit()
        self.priority_drop_down = QComboBox()
        self.due_date_box = QDateTimeEdit(calendarPopup=True)
        self.save_button = QPushButton(SAVE)
        self.close_button = QPushButton(CLOSE)
        self.title_input = QLineEdit()
        self.box_layout = QVBoxLayout()
        self.task_data = {}
        self.reminder_interval_input = QSpinBox()
        self.category_input = QLineEdit()
        self.recurrence_interval_input = QSpinBox()
        self.initUI()

    def initUI(self):
        """Build a pop-up window to add a task

        :return: None
        """
        header = QLabel(ADD_TASK_DESCRIPTION)
        self.box_layout.addWidget(header)

        self.add_title_widget()
        self.add_description_widget()
        self.add_priority_widget()
        self.add_due_date_widget()
        self.add_save_button()
        self.add_close_button()

        self.setLayout(self.box_layout)
        self.add_reminder_interval_widget()
        self.add_category_widget()
        self.add_recurrence_interval_widget()

    def add_title_widget(self):
        """Add a text box where users can enter their task title

        :return:
        """
        title_label = QLabel(f"{TITLE.capitalize()}:")
        self.box_layout.addWidget(title_label)
        self.box_layout.addWidget(self.title_input)

    def add_description_widget(self):
        """Add a text box where users can enter their task description

        :return: None
        """
        description_label = QLabel(TASK_DESCRIPTION)

        self.description_text_box.resize(self.width - 30, 50)

        self.box_layout.addWidget(description_label)
        self.box_layout.addWidget(self.description_text_box)

    def add_priority_widget(self):
        """Add a drop-down menu where users can select a priority

        There are 3 priority values: low, medium, and high

        :return: None
        """
        priority_label = QLabel(f"{PRIORITY.capitalize()}:")

        self.priority_drop_down.addItem(LOW)
        self.priority_drop_down.addItem(MEDIUM)
        self.priority_drop_down.addItem(HIGH)

        self.box_layout.addWidget(priority_label)
        self.box_layout.addWidget(self.priority_drop_down)

    def add_due_date_widget(self):
        """Add a menu where users can select due date and time

        :return: None
        """
        due_date_label = QLabel(f"{DUE_DATE_LABEL}:")

        self.due_date_box.setDateTime(datetime.now())
        self.due_date_box.setDisplayFormat("yyyy-MM-dd HH:mm")

        self.box_layout.addWidget(due_date_label)
        self.box_layout.addWidget(self.due_date_box)

    def add_reminder_interval_widget(self):
        """Add a spin box where users can enter their reminder interval in hours

        :return: None
        """
        reminder_interval_label = QLabel(f"{REMINDER_INTERVAL.capitalize()} (hours):")
        self.box_layout.addWidget(reminder_interval_label)
        self.box_layout.addWidget(self.reminder_interval_input)

    def add_category_widget(self):
        """Add a text box where users can enter their task category

        :return: None
        """
        category_label = QLabel(f"{CATEGORY.capitalize()}:")
        self.box_layout.addWidget(category_label)
        self.box_layout.addWidget(self.category_input)

    def collect_task_data(self):
        """The function collects user input in a dictionary

        :return: None
        """
        self.task_data[DESCRIPTION] = self.description_text_box.toPlainText()
        self.task_data[PRIORITY] = self.priority_drop_down.currentText()
        due_date = self.due_date_box.dateTime().toPyDateTime().strftime(DATETIME_FORMAT)
        self.task_data[DUE_DATE_LABEL] = due_date
        self.task_data[TITLE] = self.title_input.text()
        self.task_data[REMINDER_INTERVAL] = self.reminder_interval_input.value()
        self.task_data[CATEGORY] = self.category_input.text()
        self.task_data[RECURRENCE_INTERVAL] = self.recurrence_interval_input.value()

        if not self.task_data[TITLE] or not self.task_data[DESCRIPTION]:
            QMessageBox.warning(self, WARNING, INCOMPLETE_TASK_ERROR)
            return

        save_task(self.task_data)
        self.accept()

    def add_save_button(self):
        """Add save button for task creation window

        :return: None
        """
        self.box_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.collect_task_data)

    def add_close_button(self):
        """Add close button for task creation window

        :return: None
        """
        self.box_layout.addWidget(self.close_button)
        self.task_data = {}
        self.close_button.clicked.connect(self.reject)

    def add_recurrence_interval_widget(self):
        """Add a spin box where users can enter their task recurrence interval

        :return: None
        """
        recurrence_interval_label = QLabel(f"{RECURRENCE_INTERVAL.capitalize()} (days):")
        self.box_layout.addWidget(recurrence_interval_label)
        self.box_layout.addWidget(self.recurrence_interval_input)

    def update_due_date_based_on_recurrence(task_id: int, recurrence_interval: int):
        cursor = connection.cursor()
        cursor.execute("SELECT due_date FROM tasks WHERE id=?", (task_id,))
        due_date = cursor.fetchone()[0]
        new_due_date = datetime.strptime(due_date, "%Y-%m-%d") + timedelta(days=recurrence_interval)
        cursor.execute("UPDATE tasks SET due_date=? WHERE id=?", (new_due_date.strftime("%Y-%m-%d"), task_id))
        connection.commit()
