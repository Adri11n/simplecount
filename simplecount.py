import os
import platform
import glob
from datetime import datetime
print("""
     _______. __  .___  ___. .______    __       _______         ______   ______    __    __  .__   __. .___________.
    /       ||  | |   \/   | |   _  \  |  |     |   ____|       /      | /  __  \  |  |  |  | |  \ |  | |           |
   |   (----`|  | |  \  /  | |  |_)  | |  |     |  |__         |  ,----'|  |  |  | |  |  |  | |   \|  | `---|  |----`
    \   \    |  | |  |\/|  | |   ___/  |  |     |   __|        |  |     |  |  |  | |  |  |  | |  . `  |     |  |     
.----)   |   |  | |  |  |  | |  |      |  `----.|  |____       |  `----.|  `--'  | |  `--'  | |  |\   |     |  |     
|_______/    |__| |__|  |__| | _|      |_______||_______|       \______| \______/   \______/  |__| \__|     |__|     

""")
while True:
    command = input("command >")
    command = list(command.split(" "))
    if "list" in command:
        for x in glob.glob('*.txt'):
            print(os.path.splitext(x)[0])
    elif "create" in command:
        if os.path.isfile(command[1] + ".txt"):
            print("your counter already exists")
        else:
            with open(command[1] + ".txt", "w") as database:
                database.write("0")
            if os.path.isfile("simplecount.log"):
                pass
            else:
                with open("simplecount.log", "w") as database:
                    database.write("")
            now = datetime.now()
            now = now.strftime(" | %H:%M:%S | %d/%m/%Y")
            with open("simplecount.log", "a") as database:
                database.writelines(f"\ncounter {command[1]} was created{now}")
    elif "delete" in command:
        if os.path.isfile(command[1] + ".txt"):
            os.remove(command[1] + ".txt")
            if os.path.isfile("simplecount.log"):
                pass
            else:
                with open("simplecount.log", "w") as database:
                    database.write("")
            now = datetime.now()
            now = now.strftime(" | %H:%M:%S | %d/%m/%Y")
            with open("simplecount.log", "a") as database:
                database.writelines(f"\nthe counter {command[1]} was deleted{now}")
        else:
            print("your counter doesnt exists")
    elif "cd" in command:
        if os.path.isfile(command[1] + ".txt"):
            pass
        else:
            print("that counter doesnt exist")
            continue
        while True:
            command1 = input(f"({command[1]}) command >")
            command1 = list(command1.split(" "))
            if "help" in command1:
                print("""usage : [<args> <value>]
    add : adds the value you entered + the value in the count.txt file
    remove : adds the value in the count.txt file - the value you entered
    show : shows the current value of the counter
    reset : resets the value of the counter to 0
    clear : clears the whole terminal output
    exit : exits the counter your currently in""")
            elif "add" in command1:
                if "." in command1[1]:
                    command1[1] = float(command1[1])
                else:
                    command1[1] = int(command1[1])
                if type(command1[1]) is int:
                    with open(command[1] + ".txt", "r+") as database:
                        count = database.read()
                        count = int(count)
                        count = count + (command1[1])
                        database.seek(0)
                        database.write(str(count))
                else:
                    with open(command[1] + ".txt", "r+") as database:
                        count = database.read()
                        count = float(count)
                        count = count + float(command1[1])
                        database.seek(0)
                        database.write(str(count))
                if os.path.isfile("simplecount.log"):
                    pass
                else:
                    with open("simplecount.log", "w") as database:
                        database.write("")
                now = datetime.now()
                now = now.strftime(" | %H:%M:%S | %d/%m/%Y")
                with open("simplecount.log", "a") as database:
                    database.writelines(f"\nvalue of {command[1]} was changed by + {command1[1]} and is now {count}{now}")
            elif "remove" in command1:
                if "." in command1[1]:
                    command1[1] = float(command1[1])
                else:
                    command1[1] = int(command1[1])
                if type(command1[1]) is int:
                    with open(command[1] + ".txt", "r+") as database:
                        count = database.read()
                        count = int(count)
                        count = count - int(command1[1])
                        database.seek(0)
                        database.write(str(count))
                else:
                    with open(command[1] + ".txt", "r+") as database:
                        count = database.read()
                        count = float(count)
                        count = count - float(command1[1])
                        database.seek(0)
                        database.write(str(count))
                if os.path.isfile("simplecount.log"):
                    pass
                else:
                    with open("simplecount.log", "w") as database:
                        database.write("")
                now = datetime.now()
                now = now.strftime(" | %H:%M:%S | %d/%m/%Y")
                with open("simplecount.log", "a") as database:
                    database.writelines(f"\nvalue of {command[1]} was changed by - {command1[1]} and is now {count}{now}")
            elif "show" in command1:
                with open(command[1] + ".txt", "r+") as database:
                    count = database.read()
                    print(count)
            elif "clear" in command1:
                if platform.system() == "Windows":
                    os.system("cls")
                else:
                    os.system("clear")
            elif "reset" in command1:
                with open(command[1] + ".txt", "w") as database:
                    database.seek(0)
                    database.write("0")
                if os.path.isfile("simplecount.log"):
                    pass
                else:
                    with open("simplecount.log", "w") as database:
                        database.write("")
                now = datetime.now()
                now = now.strftime(" | %H:%M:%S | %d/%m/%Y")
                with open("simplecount.log", "a") as database:
                    database.writelines(f"\nvalue of {command[1]} was reseted{now}")
            elif "exit" in command1:
                print("\nbye see you next time :)\n")
                break
            else:
                print("\nyour input was unvalid\n")
                print("""usage : [<args> <value>]
    add : adds the value you entered + the value in the count.txt file
    remove : adds the value in the count.txt file - the value you entered
    show : shows the current value of the counter
    reset : resets the value of the counter to 0
    clear : clears the whole terminal output
    exit :  exits the counter your currently in""")
    elif "clear" in command:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    elif "help" in command:
        print("""usage : [<args> <value>]
            create : creates your counter (!note for the counter name spaces arent supported)
            delete : deletes an counter specified by the counter name 
            list : show all counters
            cd : switch to an counter specified by the counter name
            clear : clears the whole terminal output
            exit : breaks up simple count""")
    elif "exit" in command:
        exit()
    else:
        print("\nyour input was unvalid\n")
        print("""usage : [<args> <value>]
            create : creates your counter (!note for the counter name spaces arent supported)
            delete : deletes an counter specified by the counter name 
            list : show all counters
            cd : switch to an counter specified by the counter name
            clear : clears the whole terminal output
            exit : breaks up simple count""")