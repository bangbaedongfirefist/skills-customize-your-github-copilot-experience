import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    """Return saved tasks, or an empty list when the data file is unavailable."""
    pass


def save_tasks(tasks):
    """Save the task list to DATA_FILE."""
    pass


def add_task(tasks, title):
    """Add a task with a new integer ID and return the task."""
    pass


def complete_task(tasks, task_id):
    """Mark a task complete and return True, or return False if not found."""
    pass


def display_tasks(tasks):
    """Print every task with its status."""
    pass


def main():
    tasks = load_tasks()

    while True:
        print("\\n1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ").strip()
            # Add the task, save the list, and confirm the result.
            pass
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            # Convert the user's ID safely, complete the task, and save it.
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
