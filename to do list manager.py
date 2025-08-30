# To-Do List Manager in Python

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!\n")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1] += " ✅"
                    save_tasks(tasks)
                    print("Task marked as done!\n")
                else:
                    print("Invalid task number!\n")
            except ValueError:
                print("Enter a valid number!\n")

        elif choice == "4":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' deleted!\n")
                else:
                    print("Invalid task number!\n")
            except ValueError:
                print("Enter a valid number!\n")

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-5.\n")

# Run the program
if __name__ == "__main__":
    main()
