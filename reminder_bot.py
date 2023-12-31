# reminder bot

# dictionary to store tasks
tasks = {}

# function to add a new task
def add_task(task, time):
  tasks[time] = task

# function to view all tasks
def view_tasks():
  for time, task in tasks.items():
    print(f"{time}: {task}")

# function to delete a task
def delete_task(time):
  if time in tasks:
    del tasks[time]
  else:
    print("Task not found")

# main loop
while True:
  # prompt the user to enter a command
  command = input("Enter a command (add, view, delete, quit): ").lower()

  # add a new task
  if command == "add":
    task = input("Enter the task: ")
    time = input("Enter the time: ")
    add_task(task, time)

  # view all tasks
  elif command == "view":
    view_tasks()

  # delete a task
  elif command == "delete":
    time = input("Enter the time of the task to delete: ")
    delete_task(time)

  # quit the program
  elif command == "quit":
    break

  # if the command is not recognized
  else:
    print("Command not recognized")
