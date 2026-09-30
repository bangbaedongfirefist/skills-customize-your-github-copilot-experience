# 📘 Assignment: File-Based Task Manager

## 🎯 Objective

Build a command-line task manager that saves tasks in a JSON file. You will practice reading and writing files, handling invalid input safely, organizing code into functions, and testing Python code with the standard library only.

## 📝 Tasks

### 🛠️ Load and Save Tasks

#### Description
Complete the functions that load tasks from `tasks.json` and save them back to the file. The program should continue with an empty task list when the file does not exist yet.

#### Requirements
Completed program should:

- Store each task as a dictionary with an integer `id`, a `title`, and a Boolean `completed` value
- Load all tasks from `tasks.json` using Python's built-in `json` module
- Save changes to `tasks.json` after a task is added or completed
- Create an empty task list when `tasks.json` does not exist


### 🛠️ Add and Complete Tasks

#### Description
Implement the task operations so a user can add a task, view the task list, and mark a task as complete. Keep the command-line menu running until the user chooses to quit.

#### Requirements
Completed program should:

- Add a new task with a unique integer ID and `completed` set to `False`
- Display each task with its ID, completion status, and title
- Mark the selected task as complete without changing its ID or title
- Show a clear message when the user enters an ID that does not exist


### 🛠️ Handle Errors and Write Tests

#### Description
Make the program reliable when its data file contains invalid JSON or when users enter invalid menu choices and task IDs. Then write unit tests using `unittest` without installing any external packages.

#### Requirements
Completed program should:

- Handle invalid JSON by showing an error message and continuing with an empty task list
- Reject non-numeric menu choices and task IDs without crashing
- Include at least three `unittest` test cases for task creation, completion, and an invalid task ID
- Run the tests with `python -m unittest`
