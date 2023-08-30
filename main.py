import sys
import threading

from app.db_transfer import create_tasks_table
from PyQt5.QtWidgets import QApplication
from app.window_ui import TaskManagementWindow
from app.reminder import check_reminders

if __name__ == "__main__":
    app = QApplication(sys.argv)
    create_tasks_table()
    ex = TaskManagementWindow()
    ex.show()
    reminder_thread = threading.Thread(target=check_reminders, daemon=True)
    reminder_thread.start()
    sys.exit(app.exec_())
