import sys

from PyQt5.QtWidgets import QApplication
from app.window_ui import TaskManagementWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TaskManagementWindow()
    ex.show()
    sys.exit(app.exec_())
