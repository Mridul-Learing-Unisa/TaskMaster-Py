import json
import os
import time
from datetime import datetime

# Constants for Pomodoro (25-minute work session, 5-minute break)
WORK_DURATION = 25 * 60
BREAK_DURATION = 5 * 60
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to add a task with priority and category
def add_task(description, priority, category):
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "priority": priority,
        "category": category,
        "completed": False,
        "created_at": str(datetime.now())
    })
    save_tasks(tasks)
    print(f"Task added: '{description}' with priority {priority} and category '{category}'.")

# Function to list tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available!")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{task['priority']}] {task['description']} [{task['category']}] [{status}]")

# Function to complete a task
def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: '{deleted_task['description']}'")
    else:
        print("Invalid task number.")

# Pomodoro timer function (work and break)
def start_pomodoro(task_description):
    print(f"Starting Pomodoro for: {task_description}")
    print("Work session for 25 minutes!")
    countdown(WORK_DURATION)
    print("Time for a break! 5 minutes.")
    countdown(BREAK_DURATION)
    print("Break over, back to work!")

# Countdown function for Pomodoro
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end="\r")
        time.sleep(1)
        seconds -= 1

# Function to track productivity (show completed tasks for today)
def track_productivity():
    tasks = load_tasks()
    today = datetime.now().date()
    completed_today = [task for task in tasks if task["completed"] and datetime.strptime(task["created_at"], "%Y-%m-%d %H:%M:%S.%f").date() == today]
    
    print(f"\n-- Productivity Report for {today} --")
    if completed_today:
        print(f"Tasks completed today: {len(completed_today)}")
        for task in completed_today:
            print(f"- {task['description']} [{task['category']}]")
    else:
        print("No tasks completed today!")

