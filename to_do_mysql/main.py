from task import tasks
from time import sleep

def to_do():
    salir = False
    tasks.clean_console()
    while not salir:
        print("\n===== To-Do List =====\n")
        print("Please chose an option:")
        print("1. Create a task")
        print("2. List task/s")
        print("3. Mark task as done")
        print("4. Exit\n")
        try:
            option = int(input("Chose an option: "))
            if option == 1:
                tasks.to_do_add(input("Task to add: "))
            elif option == 2:
                tasks.clean_console()
                tasks.to_do_list()
            elif option == 3:
                tasks.clean_console()
                any_list = tasks.to_do_list()
                if any_list:
                    id = int(input("Task id: "))
                    tasks.to_do_done(id)
                    print("Task being done.")
                    sleep(3)
                    tasks.clean_console()
            elif option == 4:
                salir = True
                print("Clossing to-do application...")
                sleep(3)
                tasks.clean_console()
        except ValueError:
            tasks.clean_console()
            print("Not a valid option.")

if __name__ == "__main__":
    to_do()