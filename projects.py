# build — Simple To-Do List CLI using a list (add/remove/view) — no persistence yet
tasks = []

def add_task(task):
    """Add a task to the list."""
    tasks.append(task)
    print(f'Task added: "{task}"')

def remove_task(task):
    """Remove a task from the list."""
    if task in tasks:
        tasks.remove(task)
        print(f'Task removed: "{task}"')
    else:
        print(f'Task not found: "{task}"')

def view_tasks():
    """View all tasks in the list."""
    if tasks:
        print("Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f" {i}. {t}")
    else:
        print("No tasks to display.")

def main():
    while True:
        print("\n...To-Do List CLI...")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == "2":
            task_description = input("Enter task description to remove: ")
            remove_task(task_description)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def food():
    print("I love food")

food()

if __name__ == "__main__":
    main() 