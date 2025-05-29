# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case for priority level
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unrecognized priority level"

# Time-sensitive logic
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have free time."

# Final output
print(message)