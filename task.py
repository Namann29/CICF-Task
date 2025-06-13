def display_menu():
    print("\n--- Task Manager Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task you want to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: \"{task}\"")
    else:
        print("No task entered. Please try again.")

def remove_task(tasks):
    if not tasks:
        print("No tasks available to remove.")
        return

    print("\nCurrent Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

    try:
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"Removed: \"{removed_task}\"")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def list_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def main():
    tasks = []
    print("Welcome to TaskBot, your personal terminal task manager.")

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            print("Exiting TaskBot. Have a productive day!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()