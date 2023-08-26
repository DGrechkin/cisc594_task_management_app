from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDateEdit, QComboBox, QPushButton, QMessageBox
from app.db_transfer import save_task
from app.constants import LOW, MEDIUM, HIGH

class AddTaskWindow(QDialog):
    def __init__(self, parent=None):
        super(AddTaskWindow, self).__init__(parent)
        self.setWindowTitle("Add Task")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.title_label = QLabel("Title:")
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

        self.description_label = QLabel("Description:")
        self.description_input = QLineEdit()
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)

        self.due_date_label = QLabel("Due Date:")
        self.due_date_input = QDateEdit()
        layout.addWidget(self.due_date_label)
        layout.addWidget(self.due_date_input)

        self.priority_label = QLabel("Priority:")
        self.priority_input = QComboBox()
        self.priority_input.addItem(LOW)
        self.priority_input.addItem(MEDIUM)
        self.priority_input.addItem(HIGH)
        layout.addWidget(self.priority_label)
        layout.addWidget(self.priority_input)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_task)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_task(self):
        title = self.title_input.text()
        description = self.description_input.text()
        due_date = self.due_date_input.date().toPyDate()
        priority = self.priority_input.currentText()

        if not title or not description:
            QMessageBox.warning(self, "Warning", "Title and Description cannot be empty.")
            return

        save_task(title, description, due_date, priority)
        self.close()
