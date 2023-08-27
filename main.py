import sys

from app.db_transfer import create_tasks_table
from PyQt5.QtWidgets import QApplication
from app.window_ui import TaskManagementWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    create_tasks_table()
    ex = TaskManagementWindow()
    ex.show()
    sys.exit(app.exec_())
