import os
import tarfile
import requests
from io import BytesIO

# URL del archivo tar.gz
url = "https://www.php.net/distributions/manual/php_manual_es.tar.gz"

# Directorio donde se descomprimirá el archivo
destination_dir = "./public"

# Crear el directorio si no existe
os.makedirs(destination_dir, exist_ok=True)

# Descargar el archivo tar.gz
print(f"Descargando el archivo desde: {url}")
response = requests.get(url)

# Descomprimir directamente desde la memoria
print(f"Descomprimiendo el archivo en: {destination_dir}")

with tarfile.open(fileobj=BytesIO(response.content), mode="r:gz") as tar:
    # Obtener el nombre de la única carpeta dentro del tar
    folder_name = tar.getnames()[0].split('/')[0]

    # Extraer todo el contenido de la carpeta dentro del directorio destino
    tar.extractall(path=destination_dir)

    # Renombrar la carpeta extraída a 'php'
    extracted_folder_path = os.path.join(destination_dir, folder_name)
    renamed_folder_path = os.path.join(destination_dir, 'php')

    # Renombrar la carpeta a 'php'
    os.rename(extracted_folder_path, renamed_folder_path)

print("Proceso completado. El contenido está en:", renamed_folder_path)
