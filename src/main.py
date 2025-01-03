from repositories.task_repository import TaskRepository
from services.todo_service import TodoService
from ui.console_ui import ConsoleUI

def main():
    try:
        repository = TaskRepository('../resources/tasks.json')
        service = TodoService(repository)
        ui = ConsoleUI(service)
        ui.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
