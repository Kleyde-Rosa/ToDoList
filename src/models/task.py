from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    task_name: str
    date: str
    hour: str
    week: str
    status: bool = False

    @classmethod
    def create_from_dict(cls, task_dict):
        return cls(**task_dict)

    def to_dict(self):
        return {
            "task_name": self.task_name,
            "date": self.date,
            "hour": self.hour,
            "week": self.week,
            "status": self.status
        }
