import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "✔" if t["done"] else "✗"
                    print(f"{i}. {t['task']} [{status}]")

        elif choice == "3":
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print("Deleted:", removed["task"])
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting To-Do List. Bye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
