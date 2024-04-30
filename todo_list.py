import pickle

def load_tasks(filename='tasks.pkl'):
    try:
        with open(filename, 'rb') as f:
            tasks = pickle.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename='tasks.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(tasks, f)

def add_task(title, description, tasks=None):
    if tasks is None:
        tasks = load_tasks()
    task = {'title': title, 'description': description}
    tasks.append(task)
    save_tasks(tasks)

def display_tasks(tasks=None):
    if tasks is None:
        tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task["title"]} - {task["description"]}')

def delete_task(task_number, tasks=None):
    if tasks is None:
        tasks = load_tasks()
    try:
        del tasks[task_number - 1]
        save_tasks(tasks)
    except IndexError:
        print('Invalid task number.')

def modify_task(task_number, title=None, description=None, tasks=None):
    if tasks is None:
        tasks = load_tasks()
    try:
        task = tasks[task_number - 1]
        if title:
            task['title'] = title
        if description:
            task['description'] = description
        save_tasks(tasks)
    except IndexError:
        print('Invalid task number.')

def todo_list():
    print("Welcome to TODO list!")
    while True:
        print("\nSelect a program:")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Delete task")
        print("4. Modify task")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == 2:
            display_tasks()
        elif choice == 3:
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == 4:
            task_number = int(input("Enter task number to modify: "))
            title = input("Enter new task title (or press enter to keep current): ")
            description = input("Enter new task description (or press enter to keep current): ")
            if title:
                modify_task(task_number, title, description)
            else:
                modify_task(task_number, description=description)
        elif choice == 5:
            print("Thank you for using TODO list!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list()