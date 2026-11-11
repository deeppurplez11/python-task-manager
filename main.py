
print("================================")
print("       MY TASK MANAGER")
print("================================")

print("1. Add a task")
print("2. View tasks")
print("3. Exit")
tasks = []
choice = input("Enter your choice: ")
if choice == "1":
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully!")
elif choice == "2":
    print("You selected: View tasks")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice. Please try again.")
