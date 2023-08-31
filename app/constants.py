"""This file contains constants for our project"""

ADD = "Add"
ADD_TASK_DESCRIPTION = "Please fill all fields to add the task:"
ADD_TASK_TITLE = "Add Task"
CLOSE = "Close"
COMPLETED = "Completed"
CREATED_DATE_COLUMN = "created_date"
CREATED_DATE_LABEL = "Created Date"
DATETIME_FORMAT = "%Y-%m-%d %H:%M"
DESCRIPTION = "description"
DUE_DATE_COLUMN = "due_date"
DUE_DATE_LABEL = "Due Date"
HIGH = "high"
ID = "id"
INCOMPLETE_TASK_ERROR = "Title and Description cannot be empty."
LIST_TASKS_BY = "List Tasks by:"
LOW = "low"
MEDIUM = "medium"
PRIORITY = "priority"
SAVE = "Save"
TASKS_DB = "tasks.db"
TASK_DESCRIPTION = "Task Description"
TASK_MANAGEMENT_TOOL = "Task Management Tool"
TIME = "Time"
TITLE = "title"
WARNING = "Warning"
REMINDER_INTERVAL = "reminder_interval"
CATEGORY = "category"

TASKS_LABELS = [
    ID.upper(),
    TITLE.capitalize(),
    DESCRIPTION.capitalize(),
    PRIORITY.capitalize(),
    CREATED_DATE_LABEL,
    DUE_DATE_LABEL,
    "",
]
TASKS_COLUMNS = [
    ID,
    TITLE,
    DESCRIPTION,
    PRIORITY,
    CREATED_DATE_COLUMN,
    DUE_DATE_COLUMN,
    "",
]
PRIORITY_MAPPING = {
    HIGH: 1,
    MEDIUM: 2,
    LOW: 3,
}
