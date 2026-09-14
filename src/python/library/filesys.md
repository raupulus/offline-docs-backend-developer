---
title: Acceso a archivos y directorios
source_url: https://docs.python.org/es/3
source_path: library/filesys.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2630
---

# Acceso a archivos y directorios

Los módulos descritos en este capítulo tratan de archivos de disco y
directorios.  Por ejemplo, hay módulos para leer las propiedades de
los archivos, manipular rutas de acceso de forma portátil y crear
archivos temporales.  La lista completa de módulos en este capítulo
es:

* "pathlib" --- Rutas de sistemas orientada a objetos

  * Uso básico

  * Excepciones

  * Rutas puras

    * Propiedades generales

    * Operadores

    * Acceso a partes individuales

    * Métodos y propiedades

  * Rutas concretas

    * Análisis y generación de URI

    * Ampliando y resolviendo caminos

    * Consulta de tipo de archivo y estado

    * Lectura y escritura de archivos

    * Directorios de lectura

    * Creando archivos y directorios

    * Copying, moving and deleting

    * Permisos y propiedad

  * Lenguaje de patrones

  * Comparación con el módulo "glob"

  * Comparación con los módulos "os" y "os.path"

    * Herramientas correspondientes

  * Protocols

* "os.path" --- Common pathname manipulations

* "stat" --- Interpreting "stat()" results

* "filecmp" --- File and Directory Comparisons

  * La clase "dircmp"

* "tempfile" --- Generate temporary files and directories

  * Ejemplos

  * Funciones y variables deprecadas

* "glob" --- Unix style pathname pattern expansion

  * Examples

* "fnmatch" --- Unix filename pattern matching

* "linecache" --- Random access to text lines

* "shutil" --- High-level file operations

  * Operaciones de directorios y archivos

    * Operaciones de copia eficientes dependientes de la plataforma

    * ejemplo de *copytree*

    * ejemplo de rmtree

  * Operaciones de archivado

    * Ejemplo de archivado

    * Ejemplo de archivado con *base_dir*

  * Consulta el tamaño de la terminal de salida

Ver también:

  Módulo "os"
     Interfaces del sistema operativo, incluidas las funciones para
     trabajar con archivos en un nivel inferior al de Python *file
     objects*.

  Módulo "io"
     La biblioteca de I/O integrada de Python, incluidas las clases
     abstractas y algunas clases concretas, como la I/O de archivos.

  Función incorporada "open()"
     La forma estándar de abrir archivos para leer y escribir con
     Python.
