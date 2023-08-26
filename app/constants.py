"""This file contains constants for our project"""

ADD = "Add"
ADD_TASK_DESCRIPTION = "Please fill all fields to add the task:"
ADD_TASK_TITLE = "Add Task"
CLOSE = "Close"
COMPLETED = "Completed"
CREATED_DATE_COLUMN = "created_date"
CREATED_DATE_LABEL = "Created Date"
DATETIME_FORMAT = "yyyy-MM-dd HH:mm"
DESCRIPTION = "description"
DUE_DATE_COLUMN = "due_date"
DUE_DATE_LABEL = "Due Date"
HIGH = "high"
ID = "id"
LIST_TASKS_BY = "List Tasks by:"
LOW = "low"
MEDIUM = "medium"
PRIORITY = "priority"
SAVE = "Save"
TASK_DESCRIPTION = "Task Description"
TASK_MANAGEMENT_TOOL = "Task Management Tool"
TIME = "Time"


TASKS_LABELS = [
    ID.upper(),
    DESCRIPTION.capitalize(),
    PRIORITY.capitalize(),
    CREATED_DATE_LABEL,
    DUE_DATE_LABEL,
    "",
]
TASKS_COLUMNS = [ID, DESCRIPTION, PRIORITY, CREATED_DATE_COLUMN, DUE_DATE_COLUMN, ""]
