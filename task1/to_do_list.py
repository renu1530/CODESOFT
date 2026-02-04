# to do list application

tasks = []

# Function for TASK ADD

def task_add():

  print("----  ADD TASKS   ----")

  task_id = len(tasks) + 1
  task_title = input("Enter the task name : ")
  task_status = input("Add the status of task : ")

  task = {
      "id" : task_id,
      "title" : task_title,
      "status" : task_status
  }
  tasks.append(task)
  print('task added successfully')



# Function for TASK View

def task_view():
  print("----  VIEW TASKS   ----")

  print("Task ID \t\t Task Name \t\t Status")
  for task in tasks:
    print(f"{task['id']} \t\t\t {task['title']} \t\t\t {task['status']}")


  if len(tasks) == 0:
    print("No tasks found")

  else:
    print("No task found")




# Function for TASK Update

def task_update():
  print("----  UPDATE TASKS   ----")
  task_id = int(input("Enter the task id : "))
  for task in tasks:
    if task['id'] == task_id:
      task['title'] = input("Enter the updated task name : ")
      task['status'] = input("Enter the updated status Complete/Pending: ")

      print("task updated successfully")
      break

    else:
      print("Task not found")



# Function for task Delete

def task_delete():
  print("----  DELETE TASKS   ----")
  task_id = int(input("Enter the task id : "))
  for task in tasks:
    if task['id'] == task_id:
      tasks.remove(task)
      print("task deleted successfully")
      break

    else:
      print("Task not found")


# Function for Application menu

def menu():
  while True:
    print("-------- TO - DO - LIST - MENU  -------- ")

    print('1. Add new task. ')
    print('2. View all tasks. ')
    print('3. Update tasks. ')
    print('4. Delete tasks. ')
    print('5. Click 5 for exit. ')

    choice = int(input("Enter the choice : "))

    if choice == 1:
      task_add()

    elif choice == 2:
      task_view()

    elif choice == 3:
      task_update()

    elif choice == 4:
      task_delete()

    elif choice == 5:
      print('program exited ')
      break

    else:
      print("Invalid option")

menu()



