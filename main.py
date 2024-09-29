import alllfunc as af

# Main CLI loop
while True:
        print("\n-- FocusFlow CLI --")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Start Pomodoro Timer")
        print("6. Track Productivity")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low, Medium, High): ")
            category = input("Enter task category (e.g., Work, Study, Personal): ")
            due_date = input("Enter task due date (YYYY-MM-DD HH:MM): ")
            af.add_task(description, priority, category, due_date)
        elif choice == "2":
            af.list_tasks()
        elif choice == "3":
            af.list_tasks()
            task_number = int(input("Enter task number to complete: "))
            af.complete_task(task_number)
        elif choice == "4":
            af.list_tasks()
            task_number = int(input("Enter task number to delete: "))
            af.delete_task(task_number)
        elif choice == "5":
            af.list_tasks()
            task_number = int(input("Enter task number to start Pomodoro for: "))
            tasks = af.load_tasks()
            if 0 < task_number <= len(tasks):
                af.start_pomodoro(tasks[task_number - 1]['description'])
            else:
                print("Invalid task number.")
        elif choice == "6":
            af.track_productivity()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
