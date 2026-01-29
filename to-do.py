

import os


def main():
    todo_file = "todo.txt"
    if not os.path.exists(todo_file):
        with open(todo_file, "w") as f:
            f.write("")
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(todo_file)
        elif choice == "2":
            view_tasks(todo_file)
        elif choice == "3":
            remove_task(todo_file)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def add_task(todo_file):
    task = input("Enter a new task: ")
    with open(todo_file, "a") as f:
        f.write(task + "\n")

def view_tasks(todo_file):
    with open(todo_file, "r") as f:
        tasks = f.readlines()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def remove_task(todo_file):
    view_tasks(todo_file)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        with open(todo_file, "r") as f:
            tasks = f.readlines()
        if 0 <= index < len(tasks):
            with open(todo_file, "w") as f:
                for i, task in enumerate(tasks):
                    if main ()
                    if i != index:
                        f.write(task)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()