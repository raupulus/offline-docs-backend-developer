---
title: '"zipimport" --- Import modules from Zip archives'
source_url: https://docs.python.org/es/3
source_path: library/zipimport.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4710
---

# "zipimport" --- Import modules from Zip archives

**Código fuente:** Lib/zipimport.py

======================================================================

This module adds the ability to import Python modules ("*.py",
"*.pyc") and packages from ZIP-format archives. It is usually not
needed to use the "zipimport" module explicitly; it is automatically
used by the built-in "import" mechanism for "sys.path" items that are
paths to ZIP archives.

Típicamente "sys.path" es una lista de cadenas con nombres de
directorios. Este módulo también permite a un elemento de  "sys.path"
ser una cadena con la que se nombre a un archivo ZIP. El archivo ZIP
puede contener una estructura de subdirectorios para soportar la
importación de paquetes, y una ruta dentro del archivo puede ser
especificada para únicamente importar desde un subdirectorio. Por
ejemplo, la ruta  "example.zip/lib/" sólo importaría desde el
subdirectorio "lib/" dentro del archivo.

Cualquier archivo puede estar presente en el archivo ZIP, pero los
importadores solo son invocados para archivos ".py" y ".pyc". La
importación ZIP de módulos dinámicos (".pyd", ".so") no está
permitida. Cabe señalar que si un archivo ZIP contiene solamente
archivos ".py", Python no intentará modificar el archivo agregando los
correspondientes archivos ".pyc", esto quiere decir que si un archivo
ZIP no contiene archivos ".pyc" la importación puede ser algo lenta.

Distinto en la versión 3.13: ZIP64 is supported

Distinto en la versión 3.8: Anteriormente, los archivos ZIP con un
comentario de archivo no eran compatibles.

Ver también:

  PKZIP Nota de aplicación
     Documentación sobre el formato de archivo ZIP por Phil Katz, el
     creador del formato y algoritmos utilizados.

  **PEP 273** - Importar módulos de archivos Zip
     Escrito por James C. Ahlstrom, quien también proporcionó una
     implementación. Python 2.3 sigue la especificación en PEP 273,
     pero utiliza una implementación escrita por Just van Rossum que
     utiliza los ganchos importados descritos en PEP 302.

  "importlib" - La implementación de la maquinaria de importación
     El paquete proporciona los protocolos relevantes para que los
     implementen todos los importadores.

Este módulo define una excepción:

exception zipimport.ZipImportError

   Excepción lanzada por objetos zipimporter. Es una subclase de
   "ImportError", por lo que también puede ser capturada como
   "ImportError".

## Objetos zipimporter

"zipimporter" es la clase para importar archivos ZIP.

class zipimport.zipimporter(archivepath)

   Crea una nueva instancia zipimporter. *archivepath* debe ser una
   ruta a un archivo ZIP, o a una ruta específica dentro de un archivo
   ZIP. Por ejemplo, un *archivepath* de "foo/bar.zip/lib" buscará
   módulos en el directorio "lib" dentro del archivo ZIP "foo/bar.zip"
   (siempre que exista).

   "ZipImportError" es lanzada si *archivepath* no apunta a un archivo
   ZIP válido.

   Distinto en la versión 3.12: Los métodos "find_loader()" y
   "find_module()", deprecados en la versión 3.10, han sido
   eliminados.  Use en su lugar "find_spec()".

   create_module(spec)

      Implementación de "importlib.abc.Loader.create_module()" que
      retorna "None" para solicitar explícitamente la semántica
      predeterminada.

      Added in version 3.10.

   exec_module(module)

      Implementación de "importlib.abc.Loader.exec_module()".

      Added in version 3.10.

   find_spec(fullname, target=None)

      Una implementación de
      "importlib.abc.PathEntryFinder.find_spec()".

      Added in version 3.10.

   get_code(fullname)

      Retorna el objeto de código para el módulo especificado. Lanza
      "ZipImportError" si el módulo no se pudo importar.

   get_data(pathname)

      Retorna los datos asociados con *pathname*. Lanza "OSError" si
      el archivo no fue encontrado.

      Distinto en la versión 3.3: "IOError" used to be raised, it is
      now an alias of "OSError".

   get_filename(fullname)

      Retorna el valor que se le habría asignado a "__file__" si el
      módulo especificado fue importado. Lanza "ZipImportError" si el
      módulo no se pudo importar.

      Added in version 3.1.

   get_source(fullname)

      Retorna el código fuente para el módulo especificado. Lanza
      "ZipImportError" si el módulo no pudo ser encontrado, retorna
      "None" si el archivo contiene al módulo, pero no tiene fuente
      para ello.

   is_package(fullname)

      Retorna "True" si el módulo especificado por *fullname* es un
      paquete. Lanza "ZipImportError" si el módulo no pudo ser
      encontrado.

   load_module(fullname)

      Carga el módulo especificado por *fullname*. *fullname* debe ser
      el nombre completo de módulo (punteado). Retorna el módulo
      importado, o lanza "ZipImportError" si no fue encontrado.

      Deprecated since version 3.10, will be removed in version 3.15:
      Utilizar en su lugar "exec_module()".

   invalidate_caches()

      Limpia la caché interna de información sobre los archivos que se
      encuentran dentro del archivo ZIP.

      Added in version 3.10.

   archive

      El nombre de archivo del archivo ZIP asociado del importador,
      sin una posible sub-ruta.

   prefix

      La sub-ruta dentro del archivo ZIP donde se buscan los módulos.
      Esta es la cadena vacía para objetos zipimporter la cual apunta
      a la raíz del archivo ZIP.

   Los atributos "archive" y "prefix", cuando son combinados con una
   barra diagonal, son iguales al argumento original *archivepath*
   dado al constructor "zipimporter".

## Ejemplos

Here is an example that imports a module from a ZIP archive - note
that the "zipimport" module is not explicitly used.

   $ unzip -l example_archive.zip
   Archive:  example_archive.zip
     Length     Date   Time    Name
    --------    ----   ----    ----
        8467  01-01-00 12:30   example.py
    --------                   -------
        8467                   1 file

   >>> import sys
   >>> # Add the archive to the front of the module search path
   >>> sys.path.insert(0, 'example_archive.zip')
   >>> import example
   >>> example.__file__
   'example_archive.zip/example.py'
