import json
from typing import List
from pathlib import Path
from models.task import Task

class TaskRepository:
    def __init__(self, filename: str):
        self.filename = Path(filename)
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """Ensure the tasks file exists, create if it doesn't"""
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        if not self.filename.exists():
            self.save_tasks([])

    def load_tasks(self) -> List[Task]:
        """Load tasks from file"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task.create_from_dict(task_dict) for task_dict in data]
        except json.JSONDecodeError:
            print("Error reading tasks file. File might be corrupted.")
            return []
        except Exception as e:
            print(f"Unexpected error loading tasks: {e}")
            return []

    def save_tasks(self, tasks: List[Task]):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in tasks], f, indent=4)
        except Exception as e:
            print(f"Error saving tasks: {e}")
