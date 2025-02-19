import pandas
from datetime import datetime as dt
from docxtpl import DocxTemplate

nombre = "David Elias Alvarez"
telefono = "(123) 456-789"
correo = "david@correo.com"
fecha = dt.today().strftime("%d/%m/%Y")

CONSTANTES = {
    "nombre": nombre,
    "telefono":telefono,
    "correo":correo,
    "fecha":fecha
}

doc = DocxTemplate("plantilla.docx")
df = pandas.read_excel("alumnos.xlsx")

for indice, fila in df.iterrows():
    contenido = {
        "nombre_alumno":fila["Nombre Alumno"],
        "nota_mat":fila["Mat"],
        "nota_fis":fila["Fis"],
        "nota_qui":fila["Qui"]
    }
    # Agregamos el diccionario con las constantes personales
    contenido.update(CONSTANTES)
    doc.render(contenido)
    doc.save(f"Notas de {fila['Nombre Alumno']}.docx")
