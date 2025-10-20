

tasks = ["Study", "Exercise", "Singing", "Reading"]
print("Here are your tasks", tasks)
task_completed = []
complete = input("enter task you have completed : ")

if complete in tasks :
    task_completed.append(complete)
    print(task_completed)
    tasks.remove(complete)
    print(tasks)
else:
    print("enter valid task")
    exit()
   
    
add = input("enter task you want to add : ")
tasks.append(add)
print(tasks)

remove1 = input("enter task you want to remove or enter exit : ")
if remove1 == "exit":
    exit()
tasks.remove(remove1)
print(tasks)
