import time
from datetime import datetime, timedelta
from app.db_transfer import get_tasks_data
from app.constants import DUE_DATE_COLUMN, DATETIME_FORMAT, TITLE

def check_reminders():
    while True:
        tasks_data = get_tasks_data()
        current_time = datetime.now()

        for task in tasks_data:
            due_date = datetime.strptime(task[DUE_DATE_COLUMN], DATETIME_FORMAT)
            reminder_interval = timedelta(hours=task[REMINDER_INTERVAL])
            reminder_time = due_date - reminder_interval

            if reminder_time <= current_time < due_date:
                send_reminder_notification(task)

        time.sleep(60)  # Check for reminders every minute

def send_reminder_notification(task):
    print(f"Reminder: Task '{task[TITLE]}' is due at {task[DUE_DATE_COLUMN]}")
