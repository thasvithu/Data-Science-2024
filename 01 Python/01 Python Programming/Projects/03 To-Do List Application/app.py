""" 
Welcome to the To-Do List App!

1. Add Task
2. View Tasks
3. Remove Task
4. Quit

Choose an option (1-4): 1
Enter task description: Buy Milk
Task added!

Choose an option (1-4): 2
Tasks:
1. Buy Milk

Choose an option (1-4): 3
Enter task number to remove: 1
Task removed!

Choose an option (1-4): 4
Goodbye!
"""


import os

class ToDoListApp:
    def menu(self):
        choice = 0

        while choice != 4:
            print("\nWelcome to the To-Do List App!")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Quit")

            choice = int(input("\nChoose an option (1-4):"))

            if choice == 1:
                self.addTasks()
            elif choice == 2:
                self.viewTasks()
            elif choice == 3:
                self.removeTasks()
            elif choice == 4:
                print("Goodbye!")
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")

    def addTasks(self):
        print("\n*Add Task*")
        task = input("Enter task description:")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")  # Append a newline character after each task
        print("Task added!")

    def viewTasks(self):
        print("\n*Here are your Tasks*")
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                print(file.read())
        else:
            print("No tasks available.")

    def removeTasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
            
            if tasks:
                print("\n*Remove Task*")
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")

                task_number = int(input("Enter task number to remove:"))
                
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)

                    with open("tasks.txt", "w") as file:
                        file.writelines(tasks)

                    print(f"Task '{removed_task.strip()}' removed!")
                else:
                    print("Invalid task number. No task removed.")
            else:
                print("No tasks available to remove.")
        else:
            print("No tasks available to remove.")


obj1 = ToDoListApp()
obj1.menu()
