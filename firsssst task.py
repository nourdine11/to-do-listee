# 1- add a task to the list
# 2- mark a test as completed
# 3- view tasks
# 4- quit
def add_task ():
    # get a task from user
    task=input(" Enter your task : ")
    # define task status
    task_info={"task": task,"completed": False}
    # add task to the list
    tasks.append(task_info)
    print("Task added to the list successfuly")
    print(tasks)
    
def   mark_task_completed():
    # get list of incomplete tasks
    task_incomplete=[]
    for task in tasks :
        if not task["completed"]:
            task_incomplete.append(task)
        print(task_incomplete)
        # verify the list is not empty
    if not task_incomplete:
        print("No task to mark as completed")
        return
    # show them to the user
    for i,task in enumerate(task_incomplete):
        print(f"{i+1}-{task['task']}")
        print("-"*15)

    # get the task from the user
    task_index=int(input("Please enter index of task to be completed"))
    if task_index<0 or task_index>len(tasks):
        print("Invalid index")
    # mark the task as completed
    task_incomplete[task_index-1]["completed"] = True
    print("Task marked as completed")
    #show message to the user
    print("Task marke as completed")
def view_tasks():
    if not tasks :
       print("There is no tasks to view")
       return
    for i,task in enumerate(tasks):
        status="✔️" if task["completed"] else "❌"

        print(f"{i+1}.{task['task']} {status}")
def quit():
    print("Thank you for using our program")

        


message="""1- add a task to the list
2- mark a test as completed
3- view tasks 
4- quit
"""
tasks =[]
while True :
        print(message)
        # get the choice from user
        try :
             your_choice=input("Please enter your choice : ")
        except ValueError:
            print("please enter a valid integer")
            continue
        if your_choice== "1" :
            # add a task to the list of tasks 
            add_task()
    
        elif your_choice=="2":
            # mark a test as completed
            mark_task_completed()
        elif your_choice=="3":
            # view all of tasks 
            view_tasks()
        elif your_choice=="4":
            quit()
            break
        else :
            print(" choice invalide !")