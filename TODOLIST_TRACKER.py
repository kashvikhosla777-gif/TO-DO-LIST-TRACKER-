# To-Do List Manager Project 
tasks = []   # format: task , status , due , category , priority
def add_task():
    task = input("Enter new task: ")
    due = input("Enter due date (DD-MM-YYYY): ")
    category = input("Enter category (work/personal/school/etc.): ")
    priority = input("Enter priority (high/medium/low): ")
    record = task + " , not done , " + due + " , " + category + " , " + priority
    tasks.append(record)
    print("Task added.")
def view_tasks():
    if len(tasks)==0:
        print("No tasks yet.")
    else:
        print("Your Tasks:")
        i=0
        while i < len(tasks):
            print(str(i + 1) + ") " + tasks[i])
            i=i + 1
def mark_complete():
    view_tasks()
    if len(tasks)>0:
        num=input("Enter task number to mark completed: ")
        num=int(num)
        if num>=1 and num<=len(tasks):
            parts=tasks[num - 1].split("  ")
            task=parts[0]
            due=parts[2]
            category=parts[3]
            priority=parts[4]
            tasks[num - 1]=task + "  done  " + due + "  " + category + "  " + priority
            print("Task marked completed")
        else:
            print("Invalid number")
def edit_task():
    view_tasks()
    if len(tasks)>0:
        num=input("Enter task number to edit: ")
        num=int(num)
        if num>=1 and num<=len(tasks):
            new_task=input("Enter new task: ")
            new_due=input("Enter new due date (DD-MM-YYYY: ")
            new_category=input("Enter new category: ")
            new_priority=input("Enter new priority: ")
            parts=tasks[num - 1].split(" , ")
            status=parts[1]
            tasks[num - 1] = new_task + " , " + status + " , " + new_due + " , " + new_category + " . " + new_priority
            print("Task updated")
        else:
            print("Invalid number")
def delete_task():
    view_tasks()
    if len(tasks)>0:
        num=input("Enter task number to delete: ")
        num=int(num)
        if num>=1 and num<=len(tasks):
            tasks.pop(num - 1)
            print("Task deleted")
        else:
            print("Invalid number")
def check_reminders():
    print("Tasks Due Today or Overdue:")
    today=input("Enter today's date (DD-MM-YYYY)): ")
    found=False
    i=0
    while i<len(tasks):
        parts=tasks[i].split(" / ")
        due=parts[2]
        status=parts[1]
        if  due<=today and status=="not done":
            print(str(i + 1) + ") " + tasks[i])
            found =True
        i = i + 1
    if found==False:
        print("No due tasks.")
def task_count():
    total=len(tasks)
    done=0
    pending =0
    i = 0
    while i < len(tasks):
        parts=tasks[i].split(" / ")
        if parts[1]=="done":
            done = done + 1
        else:
            pending = pending + 1
        i = i + 1
    print("Total tasks:", total)
    print("Completed tasks:", done)
    print("Pending tasks:", pending)
def save_tasks():
    f = open("tasks.txt", "w")
    i = 0
    while i < len(tasks):
        f.write(tasks[i])
        i = i + 1
    f.close()
    print("Tasks saved.")
run="yes"
while run== "yes":
    print()
    print("TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Check Reminders")
    print("7. Task Count Summary")
    print("8. Save & Exit")
 
    choice = input("Your choice: ")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        edit_task()
    elif choice=="4":
        delete_task()
    elif choice=="5":
        mark_complete()
    elif choice=="6":
        check_reminders()
    elif choice=="7":
        task_count()
    elif choice=="8":
        save_tasks()
        run="no"
    else:
        print("Wrong choice.")