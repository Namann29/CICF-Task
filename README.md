TaskBot - Your Personal Terminal Task Manager
TaskBot is a simple and intuitive command-line interface (CLI) task manager written in Python. It allows you to easily add, remove, and list your daily tasks directly from your terminal, helping you stay organized and productive.

Features
Add Tasks: Quickly add new tasks to your to-do list.
Remove Tasks: Easily remove completed or unwanted tasks by their number.
List Tasks: View all your current tasks in a clear, numbered list.
User-Friendly Interface: Simple menu-driven navigation.

Code Overview
The task.py script is structured with several functions to handle different aspects of the task manager:

display_menu(): Prints the main menu options to the console.
add_task(tasks): Takes the tasks list as an argument, prompts the user for a task, and adds it to the list.
remove_task(tasks): Displays current tasks, prompts the user to select a task by number, and removes it from the list. Includes error handling for invalid input.
list_tasks(tasks): Displays all tasks currently in the tasks list, or a message if the list is empty.
main(): The primary function that initializes the task list, displays a welcome message, and runs the main loop to handle user input and call the appropriate functions.
