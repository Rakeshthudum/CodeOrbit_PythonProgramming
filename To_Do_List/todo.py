tasks = []


# Function to add a task
def add_task():
    task = input("Enter a new task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")


# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n===== YOUR TASKS =====")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Function to remove a task
def remove_task():
    if len(tasks) == 0:
        print("No tasks available to remove.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter the task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
