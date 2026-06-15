# To-Do List Application

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i + 1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark complete: "))
        tasks[task_num - 1]["done"] = True
        print("Task marked as completed!")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        print("Task deleted!")
    except:
        print("Invalid input.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")