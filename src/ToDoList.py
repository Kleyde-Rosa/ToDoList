import json
import datetime

filename = '../resources/tasks.json'


def addTask():
    now = datetime.datetime.now()
    print("============================= Adding Task=============================================")
    task_name = input("Enter task name: : ")
    date =str(now.strftime("%d/%m/%Y"))
    hour = str(now.strftime('%H:%M'))
    week = str(now.strftime('%A'))
    status = False

    task = {"task_name" : task_name, "date" : date, "hour" : hour, "week" : week, "status" : status}

    try:
        with open(filename, 'r') as f:
            content = json.load(f)

    except FileNotFoundError:
        content = []

    content.append(task)

    with open(filename, 'w') as f:
        json.dump(content, f, indent=4)



def finish():
    print("=============================== Mark As Completed ===================================================")
    task_name = input("Enter task name: ")
    now = datetime.datetime.now()

    with open(filename, 'r') as f:
        content = json.load(f)

    for task in content:
        if task['task_name'] == task_name:
            task['status'] = True
            task['hour'] = now.strftime('%H:%M')
            task['date'] = now.strftime('%m/%d/%Y')
            task['week'] = now.strftime('%A')

    with open(filename, 'w') as f:
        json.dump(content, f, indent=4 )




def completed():
    print("================================ Completed Tasks ===================================================")
    with open(filename, 'r') as f:
        content = json.load(f)

    for task in content:
        if task["status"] == True:
            print(f"Task Name: {task['task_name'].title()}")
            print(f"Date: {task['date']}")
            print(f"Time: {task['hour']}H {task['week']}")
            print()

def uncompleted():
    print("================================ Uncompleted Tasks ==================================================")
    with open(filename, 'r')  as f:
        content = json.load(f)

    for task in content:
        if task["status"] == False:
            print(f"Task Name: {task['task_name'].title()}")
            print(f"Date: {task['date']}")
            print(f"Time: {task['hour']}H {task['week']}")
            print()






def main():
    while True:
        print("================================        Main        =================================================")
        print("1 Add Task")
        print("2 Mark as completed")
        print("3 List completed tasks")
        print("4 List uncompleted task")
        print("Enter 'q' to quit!")

        option = input().lower()

        if (option == "1"):
            addTask()
        elif(option == "2"):
            finish()
        elif(option == "3"):
            completed()
        elif(option == "4"):
            uncompleted()
        else:
            if option == 'q':
                break
main()