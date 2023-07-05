import sqlite3
import pandas as pd
import os
conn = sqlite3.connect("Tasks.db")
import platform
cur = conn.cursor()

while True:
    print("1. Show list")
    print("2. Add task")
    print("3. Remove task")
    print("4. Update task priority")
    print("5. Quit")

    match input("Enter option by number?:"):
        case "1":
            cur.execute("select * from task_list order by priority asc")

            if result := cur.fetchall():
                result.insert(0,("id","Task Name","priority"))
                print(tabulate(result,tablefmt="fancy_grid",headers="firstrow"))
                
            else:
                print("List is empty")

        case "2":
            task_name = input("Enter task name?:")
            try:
                task_priority = int(input("Enter task priority?"))
            except ValueError:
                print("You typed wrong value")
                continue

            if task_priority < 1:
                print("task priority should be >= 1")
                continue
            cur.execute("insert into task_list(name,priority) values(?,?)",(task_name,task_priority))
            conn.commit()
            print("Added the task in database")
        
        case "3":
            identity = input("which id do you want to remove task from?:")
            cur.execute("delete from task_list where id=?",(identity))
            conn.commit()
            print("Deleted task")
        
        case "4":
             try:
                task_priority = int(input("Enter new task priority?"))
             except ValueError:
                print("You typed wrong value")
                continue

             if task_priority < 1:
                print("task priority should be >= 1")
                continue
             cur.execute("update task_list set priority = ?",(task_priority))
             conn.commit()
             print("Added the task in database")
        
        case "5":
            conn.close()
            print("Well, it's nice seeing you")
            quit(0)
        case _:
            print("Error, you typed in wrong input")
    input("Press enter to go to main menu")

    if platform.system() == "Windows":
        os.system("cls")
    else:
        #This as i am running this on mac
        os.system("clear")