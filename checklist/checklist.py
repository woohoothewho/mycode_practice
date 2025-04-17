from rich import print

def print_tasks(tasks):

    print()
    print("Today's To Do list:")
    print("------------------")
    if len(tasks) < 1:
        print()
        print("empty")
        print()
    else:
        for i, task in enumerate(tasks, start=1):
            if task["completed"]:
                print(f"[strike]{i}.{task['task name']}[/strike]")
            else:
                print(f"{i}.{task['task name']}")

    print("------------------")
    print()
    print("Add - 1 | Remove - 2 | Check - 3 | Un-Check - 4 | (q to quit)")
    print()

tasks = []

def main():

    print_tasks(tasks)

    while True:

        choice = input("Choice (1-4): ")

        if choice == "1":   # ADD TASK
            task = input("What's your task for today?: ")
            task = {"task name": task,
                    "completed": False}
            tasks.append(task)
            print_tasks(tasks)


        elif choice == "2":   # REMOVE TASK
            if len(tasks) < 1:
                print()
                print("You have no tasks to remove")
                print()
                continue
            else:
                num = len(tasks)

            task = input(f"Which task you want to remove? (1-{num}): ")
            try:
                task = int(task) - 1
                del tasks[task]
                print_tasks(tasks)

            except ValueError:
                print("Invalid input (select by number)")
            except IndexError:
                print(f"Please enter a number between 1 and {len(tasks)}")

        elif choice == "3":   # CHECK TASK
            if len(tasks) < 1:
                print()
                print("You have no tasks to check")
                print()
                continue
            else:
                num = len(tasks)
            
            task = input(f"Which task to check? (1-{num}): ")
            try:
                task_index = int(task) - 1
                tasks[task_index]["completed"] = True
                print_tasks(tasks)

            except ValueError:
                print("Invalid input (select by number)")
            except IndexError:
                print(f"Please enter a number between 1 and {len(tasks)}")

        elif choice == "4":   # UN-CHECK TASK
            if len(tasks) < 1:
                print()
                print("You have no tasks to check")
                print()
                continue
            else:
                num = len(tasks)
            
            task = input(f"Which task to un-check? (1-{num}): ")
            try:
                task_index = int(task) - 1
                tasks[task_index]["completed"] = False
                print_tasks(tasks)

            except ValueError:
                print("Invalid input (select by number)")
            except IndexError:
                print(f"Please enter a number between 1 and {len(tasks)}")
                
        elif choice.lower() == "q":
            print()
            print("Goodbye!")
            print()
            break
        else:
            print("Please pick one option (1-4)")



if __name__ == '__main__':
    main()