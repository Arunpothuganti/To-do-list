import os
import json
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        return tasks
    return {"tasks": []}

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks, description, priority, due_date):
    task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
    }
    tasks["tasks"].append(task)
    print("Task added successfully!")

def remove_task(tasks, index):
    if 0 <= index < len(tasks["tasks"]):
        removed_task = tasks["tasks"].pop(index)
        print(f"Removed task: {removed_task['description']}")
    else:
        print("Invalid task index!")

def mark_completed(tasks, index):
    if 0 <= index < len(tasks["tasks"]):
        tasks["tasks"][index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index!")

def display_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks["tasks"]):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['description']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List App =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
            add_task(tasks, description, priority, due_date)

        elif choice == "2":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(tasks, index)

        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_completed(tasks, index)

        elif choice == "4":
            display_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Exiting. Your tasks are saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
