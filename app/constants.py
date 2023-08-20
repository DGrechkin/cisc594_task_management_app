"""This file contains constants for our project"""

TASK_MANAGEMENT_TOOL = "Task Management Tool"
ADD = "Add"
LIST_TASKS_BY = "List Tasks by:"
PRIORITY = "priority"
DUE_DATE_LABEL = "Due Date"
ID = "id"
DESCRIPTION = "description"
LOW = "low"
MEDIUM = "medium"
HIGH = "high"
CREATED_DATE_COLUMN = "created_date"
DUE_DATE_COLUMN = "due_date"
CREATED_DATE_LABEL = "Created Date"
COMPLETED = "Completed"


TASKS_LABELS = [
    ID.upper(),
    DESCRIPTION.capitalize(),
    PRIORITY.capitalize(),
    CREATED_DATE_LABEL,
    DUE_DATE_LABEL,
    "",
]
TASKS_COLUMNS = [ID, DESCRIPTION, PRIORITY, CREATED_DATE_COLUMN, DUE_DATE_COLUMN, ""]
