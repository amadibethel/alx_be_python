# daily_reminder.py
# A program that provides a customized reminder for a single daily task
# Demonstrates use of input, match case, and conditionals

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using match case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an undefined priority level."

# Adjust message if task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder = f"Note: {reminder} Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
