class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index!")

    def show_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty!")

    def save_tasks(self, file_name):
        with open(file_name, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self, file_name):
        try:
            with open(file_name, "r") as file:
                self.tasks = [line.strip() for line in file]
        except FileNotFoundError:
            print("No previous to-do list found.")

def main():
    todo_list = ToDoList()
    file_name = "todo_list.txt"
    todo_list.load_tasks(file_name)

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "3":
            index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            todo_list.save_tasks(file_name)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
