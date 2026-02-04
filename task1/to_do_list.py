# # data_design

# tasks = [
#     {"id" : 1, "title" : "task_name", "status" : "pending"},
#     {"id" : 2, "title" : "task_name", "status" : "pending"}
# ]


tasks = []

# Functin for ADD_TASK

def Add_task():
    
    task_id = len(tasks) + 1
    title = input("Enter task name : ")
    status = input("Enter the task status : ")
    task = {

        id : task_id,
        "title" : title,
        "status" : status

        }
    
    tasks.append(task)
    print("Task added susccesfully .")




# Function for View all Tasks

def view_tasks():
    print("-----------   List of all Tasks   -----------\n")

    if  not tasks:
        print("no tasks found.")
        return
    
    print("task_id \t title \t\t status")
    print("------------------------------------------------")

    for task in tasks:
            print(f"{task[id]} \t\t {task['title']} \t\t {task['status']}")



# Function for task Update

def update_task():
    for task in tasks:
        if task["title"] == "title":
           task["status"] = input("change status : ")

           print("task updated successfully ")
           return
    print("not found")




# Function for application menu

def menu():

    while True:

        print("1. add tasks : ")
        print("2. view tasks : ")
        print("3. update task : ")
        print("4. delete task : ")
        print("5. click 5 to exit : ")

        choice = int(input("Enter option : "))

        if choice == 1:
            Add_task()
        
        elif choice == 2:
            view_tasks()

        elif choice == 3:
            update_task()

        elif choice == 4:
            delete_task()

        elif choice == 5:
            print("program exited ")
            break

        else:
            print("invalid option")


menu()