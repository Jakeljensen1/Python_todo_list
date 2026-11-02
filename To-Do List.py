def to_do_list():
  tasks = ["Mow the lawn", "Grocery store run", "Walk the dog"]

  while True: # print the menu
    print("\n To-do Task Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose option (1-4): ").strip() #.strip() removes extra commas/white spaces

    if choice == "1":
      if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
          print(f"{i}. {task}")
      else:
        print("No tasks added yet")

    elif choice == "2":
      new_task = input("List new task: ").strip()
      tasks.append(new_task)
      print(f"'{new_task}' has been added")

    elif choice == "3":
      task_num = int(input("Task # to remove: "))
      if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' was removed")

      else:
        print(f"Task # '{task_num}' is invalid")

    elif choice == "4":
      print("Goodbye")
      break

    else:
      print("Invalid input, try again.")


to_do_list()

#Setting up the venv environment:
# sudo apt update
# sudo apt install python3-venv
# python3 -m venv .venv
# source .venv/bin/activate
# deactivate to leave env




    