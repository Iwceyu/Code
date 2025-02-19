import os
import shutil
from datetime import datetime

# downloads = "~/Downloads"

def create_organization_folder(base_path):
    """
    :param base_path: Carpeta con archivos a organizar
    :return: Carpetas especificas para cada tipo de archivo
    """
    folders = {
        "imagenes": ['.jpg','.jpeg','.png','.gif','.bmp'],
        "documentos": ['.pdf','.doc','.docx','.txt'],
        "exel": ['.xlsx','.csv','.sav'],
        "audio": ['.mp3','.wav','.flac','.m4a'],
        "video": ['.mp4','.avi','.mkv','.mov'],
        "comprimidos": ['.zip','.rar','.7z'],
        "imagen_de_disco": ['.iso'],
        "otros": []
    }

    for folder in folders:
        folder_path = os.path.join(base_path,folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    return folders

def get_folder_for_extension(extension, folders_dict):
    """Determina la carpeta correcta para una extension dada"""
    for folder, extensions in folders_dict.items():
        if extension.lower() in extensions:
            return folder
    return 'otros'

def oragenize_files(directory):
    """Organiza los archivos en el directorio especificado"""
    try:
        # Crear registro de movimientos
        log = []

        # Obtener path absoluto
        directory = os.path.abspath(directory)

        # Crear carpetas de organizacion
        folders = create_organization_folder(directory)

        # Recorrer archivos en el directorio
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Ignorar carpetas y archivos ocultos
            if os.path.isfile(file_path) and not (filename.startswith('.') or filename.endswith('.py')):
                # Obtener extension
                extension = os.path.splitext(filename)[1]

                # Determinar carpeta destino
                dest_folder = get_folder_for_extension(extension, folders)
                destination = os.path.join(directory, dest_folder, filename)

                # Mover archivos
                try:
                    shutil.move(file_path, destination)
                    log.append(f"Movido: {filename} -> {dest_folder}/")
                except Exception as e:
                    log.append(f"Error al mover {filename}: {str(e)}")

        # Generar reporte
        if log:
            print("\n*** Reporte de Organizacion ***")
            print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Directorio: {directory}")
            print(f"\nMovimientos realizados:")
            for entry in log:
                print(f"- {entry}")
        else:
            print("No se encontraron archivos para organizar.")
    except Exception as e:
        print(f"Error durante la organizacion: {str(e)}")


if __name__ == '__main__':
    # Solicitar directorio a organizar
    directory = input("Ingrese la ruta del directorio a organizar (Enter para directorio actual): ")

    if not directory:
        directory = "."

    # Verificar que el directorio exista
    if not os.path.exists(directory):
        print("Error: El directorio especificado no existe.")
        exit(1)

    # Confirmar la accion
    print(f"Se organizaran los archivos en {os.path.abspath(directory)}")
    confirm = input("Desea continuar? (s/n)")

    if confirm.lower() == 's':
        oragenize_files(directory)
    else:
        print("Operacion cancelada")