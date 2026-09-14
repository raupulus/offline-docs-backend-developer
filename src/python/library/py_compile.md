---
title: '"py_compile" --- Compile Python source files'
source_url: https://docs.python.org/es/3
source_path: library/py_compile.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3560
---

# "py_compile" --- Compile Python source files

**Código fuente** Lib/py_compile.py

======================================================================

The "py_compile" module provides a function to generate a byte-code
file from a source file, and another function used when the module
source file is invoked as a script.

Aunque no es necesario seguidamente, esta función puede ser útil
cuando se instalan módulos para uso compartido, especialmente si
algunos de los usuarios pueden no tener permisos para escribir el
archivo caché de bytes en el directorio conteniendo el código fuente.

exception py_compile.PyCompileError

   Cuando un error ocurre mientras se intenta compilar el archivo, se
   lanza una excepción.

py_compile.compile(file, cfile=None, dfile=None, doraise=False, optimize=-1, invalidation_mode=PycInvalidationMode.TIMESTAMP, quiet=0)

   Compile a source file to byte-code and write out the byte-code
   cache file. The source code is loaded from the file named *file*.
   The byte-code is written to *cfile*, which defaults to the **PEP
   3147**/**PEP 488** path, ending in ".pyc". For example, if *file*
   is "/foo/bar/baz.py" *cfile* will default to
   "/foo/bar/__pycache__/baz.cpython-32.pyc" for Python 3.2.  If
   *dfile* is specified, it is used instead of *file* as the name of
   the source file from which source lines are obtained for display in
   exception tracebacks. If *doraise* is true, a "PyCompileError" is
   raised when an error is encountered while compiling *file*. If
   *doraise* is false (the default), an error string is written to
   "sys.stderr", but no exception is raised.  This function returns
   the path to byte-compiled file, i.e. whatever *cfile* value was
   used.

   Los argumentos *doraise* y *quiet* determinan cómo los errores son
   gestionados mientras se compila el archivo. Si *quiet* es 0 o 1, y
   *doraise* es falso, la conducta por defecto es habilitada: un error
   cadena de caracteres es escrito a "sys.stderr", y la función
   retorna "None" en vez de una ruta. Si *doraise* es verdadero, se
   lanzará un "PyCompileError". Sin embargo si *quiet* es 2, ningún
   mensaje es escrito y *doraise* no tiene efecto.

   Si la ruta que *cfile* se convierte (sea especificada
   explícitamente o computada) es un enlace simbólico o archivo no
   regular, se lanzará "FileExistsError". Esto es para actuar como una
   advertencia que la importación convertirá esas rutas en archivos
   regulares si ésta tiene permitido escribir archivos compilados en
   bytes a esas rutas. Este es un efecto secundario de importar usando
   el renombramiento de archivos para colocar el archivo de bytes
   compilado final en el lugar para prevenir problemas de escritura en
   archivos simultáneos.

   *optimize* controla el nivel de optimización y si es pasado a la
   función construida "compile()".  El predeterminado de "-1"
   selecciona el nivel de optimización del intérprete actual.

   *invalidation_mode* debería ser un miembro del enum
   "PycInvalidationMode" y controla cómo el caché de código de bytes
   generado es invalidado en el tiempo de ejecución.  El
   predeterminado es "PycInvalidationMode.CHECKED_HASH" si la variable
   de entorno "SOURCE_DATE_EPOCH" está establecida, de otra manera el
   predeterminado es "PycInvalidationMode.TIMESTAMP".

   Distinto en la versión 3.2: Cambiado el valor por defecto de
   *cfile* para que cumpla **PEP 3147**. El por defecto anterior era
   *file* + "'c'" ("'o'" si la optimización estaba habilitada).
   También agregado el parámetro *optimize*.

   Distinto en la versión 3.4: Se cambió el código para usar
   "importlib" para la escritura del archivo almacenado de código de
   bytes. Esto significa que la semántica de la creación/escritura del
   archivo ahora coincide con lo que "importlib" hace, por ejemplo
   permisos, semántica de escribir-y-mover, etc. Además se agregó la
   consideración de que "FileExistsError" es lanzado si *cfile* es un
   enlace simbólico o un archivo no regular.

   Distinto en la versión 3.7: El parámetro *invalidation_mode* fue
   agregado como se especificó en **PEP 552**. Si la variable de
   entorno "SOURCE_DATE_EPOCH" se establece, *invalidation_mode* será
   forzada a "PycInvalidationMode.CHECKED_HASH".

   Distinto en la versión 3.7.2: La variable de entorno
   "SOURCE_DATE_EPOCH" ya no sobreescribe el valor del argumento
   *invalidation_mode*, y en vez de eso determina su valor por
   defecto.

   Distinto en la versión 3.8: El parámetro *quiet* fue agregado.

class py_compile.PycInvalidationMode

   An enumeration of possible methods the interpreter can use to
   determine whether a bytecode file is up to date with a source file.
   The ".pyc" file indicates the desired invalidation mode in its
   header. See Invalidación del código de bytes en caché for more
   information on how Python invalidates ".pyc" files at runtime.

   Added in version 3.7.

   TIMESTAMP

      El archivo ".pyc" incluye una marca de tiempo y tamaño del
      archivo fuente, el cual Python comparará contra los metadatos
      del archivo fuente durante el tiempo de ejecución para
      determinar si el archivo ".pyc" necesita ser regenerado.

   CHECKED_HASH

      El archivo ".pyc" incluye un hash del contenido del archivo
      fuente, el cual Python comparará contra la fuente durante el
      tiempo de ejecución para determinar si el archivo ".pyc"
      necesita ser regenerado.

   UNCHECKED_HASH

      Como "CHECKED_HASH", el archivo ".pyc" incluye un has del
      contenido del archivo fuente. Sin embargo, Python asumirá
      durante el tiempo de ejecución que el archivo ".pyc" está
      actualizado y no validará el ".pyc" contra el archivo fuente en
      lo absoluto.

      Esta opción es útil cuando los ".pucs" se mantienen actualizados
      al día por algún sistema externo a Python como un sistema de
      compilación.

## Interfaz de línea de comandos

Este módulo puede invocarse como un script para compilar varios
archivos fuente. Los archivos nombrados en *filenames* se compilan y
el código de bytes resultante se almacena en caché de la manera
normal. Este programa no busca en una estructura de directorio para
localizar archivos fuente; solo compila archivos nombrados
explícitamente. El estado de salida es distinto de cero si uno de los
archivos no se pudo compilar.

<file> ... <fileN>
-

   Los argumentos posicionales son archivos para compilar. Si "-" es
   el único parámetro, la lista de archivos se toma de la entrada
   estándar.

-q, --quiet

   Suprime la salida de errores.

Distinto en la versión 3.2: Agregado soporte para "-".

Distinto en la versión 3.10: Agregado soporte para "-q".

Ver también:

  Módulo "compileall"
     Utilidades para compilar todos los archivos fuente Python en el
     árbol del directorio.
