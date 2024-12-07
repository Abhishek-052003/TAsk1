import datetime

class Task:
    def __init__(self, description, due_date=None, priority=1):
        self.description = description
        self.due_date = due_date
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, 1):
                due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
                print(f"{i}. {task.description} (Priority: {task.priority}, Due: {due_date})")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def get_date_input():
    while True:
        date_str = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
        if not date_str:
            return None
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = get_date_input()
            priority = int(input("Enter priority (1-5, 1 being highest): "))
            task = Task(description, due_date, priority)
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the number of the task to delete: "))
            todo_list.delete_task(index)

        elif choice == '4':
            print("Thank you for using the To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


main()