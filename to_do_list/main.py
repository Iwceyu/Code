import os
from os import system, name, environ


def clean_console():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def add_task(tasks: list) -> list:
    number_tasks: int = int(input("How many tasks do you want to add?: "))

    for n in range(number_tasks):
        task: str = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print(f"Task: '{task}' added!")

    return tasks


def list_tasks(tasks: list):
    print("Tasks:\n")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not done"
        print(f"{index + 1}. Task: {task['task']} - {status}")


def done_task(tasks: list) -> str:
    task_index = int(input("\nEnter the task to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        return "Task marked as done"
    else:
        return "Not a valid task number."


def task_func():
    is_on = True
    tasks = []

    while is_on:
        print(
            """
        ===== To-do List =====
        1. Add task
        2. List tasks
        3. Mark task as done
        4. Exit
        """
        )

        choice = int(input("Select an option: "))

        if choice == 1:
            clean_console()
            add_task(tasks)

        elif choice == 2:
            clean_console()
            list_tasks(tasks)

        elif choice == 3:
            clean_console()
            list_tasks(tasks)
            done_task(tasks)

        elif choice == 4:
            is_on = False
            print("Leaving to-do list!....")

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    task_func()
