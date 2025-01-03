from services.todo_service import TodoService

class ConsoleUI:
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def display_menu(self):
        print("\n".ljust(50, "=") + " Main " + "".ljust(50, "="))
        print("1. Add Task")
        print("2. Mark as completed")
        print("3. List completed tasks")
        print("4. List uncompleted tasks")
        print("Enter 'q' to quit!")

    def print_task(self, task):
        print(f"Task Name: {task.task_name.title()}")
        print(f"Date: {task.date}")
        print(f"Time: {task.hour}H {task.week}")
        print()

    def add_task(self):
        print("\n".ljust(50, "=") + " Adding Task " + "".ljust(50, "="))
        task_name = input("Enter task name: ")
        if self.todo_service.add_task(task_name):
            print("Task added successfully!")
        else:
            print("Failed to add task.")

    def mark_completed(self):
        print("\n".ljust(50, "=") + " Mark As Completed " + "".ljust(50, "="))
        task_name = input("Enter task name: ")
        if self.todo_service.mark_as_completed(task_name):
            print("Task marked as completed!")
        else:
            print("Task not found or error occurred.")

    def show_completed_tasks(self):
        print("\n".ljust(50, "=") + " Completed Tasks " + "".ljust(50, "="))
        tasks = self.todo_service.get_completed_tasks()
        if not tasks:
            print("No completed tasks found.")
        for task in tasks:
            self.print_task(task)

    def show_uncompleted_tasks(self):
        print("\n".ljust(50, "=") + " Uncompleted Tasks " + "".ljust(50, "="))
        tasks = self.todo_service.get_uncompleted_tasks()
        if not tasks:
            print("No uncompleted tasks found.")
        for task in tasks:
            self.print_task(task)

    def run(self):
        while True:
            self.display_menu()
            option = input().lower()

            if option == 'q':
                break

            options = {
                "1": self.add_task,
                "2": self.mark_completed,
                "3": self.show_completed_tasks,
                "4": self.show_uncompleted_tasks
            }

            if option in options:
                options[option]()
            else:
                print("Invalid option. Please try again.")
