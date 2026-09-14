---
title: '"pyclbr" --- Python module browser support'
source_url: https://docs.python.org/es/3
source_path: library/pyclbr.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3570
---

# "pyclbr" --- Python module browser support

**Código fuente:** Lib/pyclbr.py

======================================================================

The "pyclbr" module provides limited information about the functions,
classes, and methods defined in a Python-coded module.  The
information is sufficient to implement a module browser.  The
information is extracted from the Python source code rather than by
importing the module, so this module is safe to use with untrusted
code. This restriction makes it impossible to use this module with
modules not implemented in Python, including all standard and optional
extension modules.

pyclbr.readmodule(module, path=None)

   Retorna un diccionario que asigna nombres de clase a nivel de
   módulo con descriptores de clase. Si es posible, se incluyen
   descriptores para las clases base importadas. El parámetro *module*
   es una cadena con el nombre del módulo que se va a leer; puede ser
   el nombre de un módulo dentro de un paquete. Si se indica, *path*
   es una secuencia de rutas de directorios antepuesto a "sys.path",
   que se utiliza para localizar el código fuente del módulo.

   Esta función es la interfaz original y sólo se mantiene por
   compatibilidad. Retorna una versión filtrada de lo siguiente.

pyclbr.readmodule_ex(module, path=None)

   Retorna un árbol basado en diccionarios que contiene un descriptor
   de función o clase para cada función y clase definida en el módulo
   con una instrucción "def" o "class". El diccionario retornado
   asigna nombres de clase y función a nivel de módulo con sus
   descriptores. Los objetos anidados se introducen en el diccionario
   hijo de su elemento padre. Al igual que con *readmodule*, *module*
   nombra el módulo que se va a leer y *path* se antepone a sys.path.
   Si el módulo que se lee es un paquete, el diccionario retornado
   tiene una clave "'__path__'" cuyo valor es una lista que contiene
   la ruta del paquete.

Added in version 3.7: Descriptores para definiciones anidadas. Se
accede a ellos a través del nuevo atributo *children*. Cada uno tiene
un nuevo atributo *parent*.

Los descriptores retornados por estas funciones son instancias de las
clases Function y Class. No se espera que los usuarios creen
instancias de estas clases.

## Objetos Function

class pyclbr.Function

   Class "Function" instances describe functions defined by def
   statements.  They have the following attributes:

   file

      Nombre del archivo en el cual la función está definida.

   module

      El nombre del módulo que define la función descrita.

   name

      El nombre de la función.

   lineno

      El número de línea el en archivo donde inicia la definición.

   parent

      For top-level functions, "None".  For nested functions, the
      parent.

      Added in version 3.7.

   children

      A "dictionary" mapping names to descriptors for nested functions
      and classes.

      Added in version 3.7.

   is_async

      "True" for functions that are defined with the "async" prefix,
      "False" otherwise.

      Added in version 3.10.

## Objetos Class

class pyclbr.Class

   Class "Class" instances describe classes defined by class
   statements.  They have the same attributes as "Functions" and two
   more.

   file

      Nombre del archivo en el que la clase está definida.

   module

      Nombre del módulo que define la clase descrita.

   name

      El nombre de la clase.

   lineno

      El número de línea el en archivo donde inicia la definición.

   parent

      For top-level classes, "None".  For nested classes, the parent.

      Added in version 3.7.

   children

      Un diccionario asignando nombres con descriptores para las
      clases y funciones anidadas.

      Added in version 3.7.

   super

      A list of "Class" objects which describe the immediate base
      classes of the class being described.  Classes which are named
      as superclasses but which are not discoverable by
      "readmodule_ex()" are listed as a string with the class name
      instead of as "Class" objects.

   methods

      A "dictionary" mapping method names to line numbers. This can be
      derived from the newer "children" dictionary, but remains for
      back-compatibility.
