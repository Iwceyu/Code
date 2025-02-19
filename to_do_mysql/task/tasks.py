import mysql.connector
from os import name, system, environ as en


CONFIG = {
        "user": en.get("MYSQL_USER"),
        "password": en.get("MYSQL_PASSWORD"),
        "host": "127.0.0.1",
        "database": "to_do_list"
    }


def clean_console():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def to_do_connect(sql_instruction:str, values:tuple[any, any]=None):
    try:
        with mysql.connector.connect(**CONFIG) as con:
            cursor = con.cursor()
            if values is not None:
                cursor.execute(sql_instruction, values)
                con.commit()
            else:
                cursor.execute(sql_instruction)
                tasks = cursor.fetchall()
                if tasks:
                    print(f"Tasks to do:")
                    for task in tasks:
                        print(f"\t{task[0]}. {task[1]}.")
                    return True
                else:
                    print("Empty to-do list.")
                    return False
    except Exception as e:
        print(e)

def to_do_add(task:str):
    sql = "INSERT INTO to_do(task,is_done) VALUES (%s,%s)"
    values = (task, "no")
    to_do_connect(sql, values)

def to_do_list():
    sql = "SELECT * FROM to_do WHERE is_done='no'"
    return to_do_connect(sql)

def to_do_done(task_id:int):
    sql = "UPDATE to_do SET is_done = %s WHERE id = %s"
    values = ("yes", task_id)
    to_do_connect(sql, values)
