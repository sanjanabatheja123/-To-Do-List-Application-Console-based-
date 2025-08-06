#  Console-Based To-Do List Application (Python)

This is a simple command-line To-Do List application written in Python. It allows users to add, remove, and view tasks from a persistent task list stored in a local file. Tasks are saved to a file (`tasks.txt`), so they remain even after the program is closed and restarted.

## Objective
To implement a basic to-do list manager using Python that supports persistent storage and common task operations like:

- Adding tasks
- Removing tasks
- Viewing all tasks

## Files
- `todo.py` — The main Python file containing the application logic
- `tasks.txt` — Auto-generated file that stores your to-do tasks

## How It Works
1. **Startup**:  
   On launch, the program attempts to read existing tasks from `tasks.txt`. If the file doesn’t exist, it starts with an empty task list.

2. **Main Loop**:  
   The program runs in a loop and asks the user what action they want to perform:
   - `add`: Prompts for a new task and adds it to the list.
   - `remove`: Prompts for a task to remove and deletes it if it exists.
   - `view`: Displays the current list of tasks.
   - `exit`: Exits the program.

3. **Persistent Storage**:  
   All changes are saved to `tasks.txt` immediately after each add or remove operation, ensuring persistence between sessions.

## Code Flow
1. Try to open and read existing tasks from 'tasks.txt'.
2. Enter a loop:
    a. Ask the user for an operation (add/remove/view/exit).
    b. If 'add':
        - Take input and append task to list.
        - Save updated list to file.
    c. If 'remove':
        - Take input and remove task from list if it exists.
        - Save updated list to file.
    d. If 'view':
        - Print all tasks in a numbered list.
    e. If 'exit':
        - Break the loop and end program.
    f. Else:
        - Show invalid input message.
