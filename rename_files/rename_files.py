import os
from datetime import datetime

fecha_actual = datetime.now().strftime("%Y%m%d")

def rename_files(directory: str, old_text: str, new_text:str):
    """
    :param directory: Direccion del archivo
    :param old_text: Texto a reemplazar
    :param new_text: Texto que reemplaza
    :return: Cambia el nombre del archivo
    """
    for filename in os.listdir(directory):
        if old_text in filename:
            old_file = os.path.join(directory,filename)
            new_file = os.path.join(directory,filename.replace(old_text, new_text))
            os.rename(old_file,new_file)
            print(f"Archivo renombrado: {filename} -> {filename.replace(old_text, new_text)}")

rename_files("archivos", fecha_actual, "Nuevo")