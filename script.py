todo_list = []

while True:
  
  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")

  choice = input("Enter your choice: ")
  if choice == "1":
    print("Adding task")
    new_task = input()
    todo_list.append(new_task)
    print("The task has been succesfully added")
  elif choice == "2":
    print("Removing task")
    if len(todo_list) == 0:
      print("Your ToDo list is empty")
    else:
      index_to_remove = int(input("Enter the task number to remove: ")) - 1
      if 0 <= index_to_remove < len(todo_list):
        todo_list.pop(index_to_remove)
      else:
        print("Invalid task number")
  elif choice == "3":
    print("Quitting")
    break

  
