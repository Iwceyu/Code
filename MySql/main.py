import mysql.connector

def eliminar_cliente():
    id_usuario = int(input("Ingresa el id del usuario a eliminar: "))
    sql = f"UPDATE cliente SET isActive=0 WHERE id={id_usuario}"
    try:
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print(e)

def agregar_cliente():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    membresia = int(input("Ingrese la membresia: "))
    sql = "INSERT INTO cliente(nombre,apellido,membresia) VALUES (%s,%s,%s)"
    val = (nombre, apellido, membresia)
    try:
        cursor.execute(sql, val)
        con.commit()
    except Exception as e:
        con.rollback()

def cargar_clientes():
    con.commit()
    cursor.execute("SELECT * FROM cliente WHERE isActive=1")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(f"Id: {usuario[0]}, Nobre: {usuario[1]} | Apellido: {usuario[2]} | Membresia: {usuario[3]}")

def modificar_cliente():
    id_usuario = int(input("Ingresa el id del usuario a modificar: "))
    nombre = input("Ingrese el nuevo nombre: ")
    apellido = input("Ingrese el nuevo apellido: ")
    membresia = int(input("Ingrese la nueva membresia: "))
    sql = f"UPDATE cliente SET nombre=\"{nombre}\", apellido=\"{apellido}\", membresia={membresia} WHERE id={id_usuario}"
    try:
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print(e)


print("Para conectar con la base de datos favor de ingresar los siguientes datos:")
usuario = input("Ingrese su nombre de usuario: ")
password = input("Porfavor ingrese su password: ")

CONFIG = {"user":usuario,
          "password":password,
          "host":"127.0.0.1",
          "database":"zona_fit"}
try:
    with mysql.connector.connect(**CONFIG) as con:
        cursor = con.cursor()
        salir = False
        while not salir:
            seleccion = int(input("""
Porfavor seleccione una opcion:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir
Eleccion: """))
            if seleccion == 1:
                cargar_clientes()
            elif seleccion == 2:
                agregar_cliente()
            elif seleccion == 3:
                modificar_cliente()
            elif seleccion == 4:
                eliminar_cliente()
            elif seleccion == 5:
                salir = True


except Exception as e:
    print(e)
