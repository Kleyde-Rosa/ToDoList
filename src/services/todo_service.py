from datetime import datetime
from typing import List
from models.task import Task
from repositories.task_repository import TaskRepository

class TodoService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, task_name: str) -> bool:
        """Add a new task"""
        try:
            now = datetime.now()
            task = Task(
                task_name=task_name,
                date=now.strftime("%d/%m/%Y"),
                hour=now.strftime('%H:%M'),
                week=now.strftime('%A')
            )
            tasks = self.repository.load_tasks()
            tasks.append(task)
            self.repository.save_tasks(tasks)
            return True
        except Exception as e:
            print(f"Error adding task: {e}")
            return False

    def mark_as_completed(self, task_name: str) -> bool:
        """Mark a task as completed"""
        try:
            tasks = self.repository.load_tasks()
            for task in tasks:
                if task.task_name.lower() == task_name.lower():
                    now = datetime.now()
                    task.status = True
                    task.hour = now.strftime('%H:%M')
                    task.date = now.strftime('%d/%m/%Y')
                    task.week = now.strftime('%A')
                    self.repository.save_tasks(tasks)
                    return True
            return False
        except Exception as e:
            print(f"Error marking task as completed: {e}")
            return False

    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks"""
        return [task for task in self.repository.load_tasks() if task.status]

    def get_uncompleted_tasks(self) -> List[Task]:
        """Get all uncompleted tasks"""
        return [task for task in self.repository.load_tasks() if not task.status]
