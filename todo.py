
# Load existing tasks from file if it exists
tasks = []

try:
    with open('tasks.txt', 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    pass  # No existing file, start with empty list

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

while True:
    opr = input("\nWhat would you like to do? (add / remove / view / exit): ").strip().lower()

    if opr == 'add':
        task = input("Enter task to add: ").strip()
        tasks.append(task)
        save_tasks()
        print(f"Task added: {task}")

    elif opr == 'remove':
        task = input("Enter task to remove: ").strip()
        if task in tasks:
            tasks.remove(task)
            save_tasks()
            print(f"Task removed: {task}")
        else:
            print("Task not found.")

    elif opr == 'view':
        if not tasks:
            print("📭 No tasks in your to-do list.")
        else:
            print("\n📝 Your To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    elif opr == 'exit':
        print("Exiting... Have a productive day!")
        break

    else:
        print(" Invalid operation. Try add, remove, view, or exit.")
