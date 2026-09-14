---
title: Modo de desarrollo de Python
source_url: https://docs.python.org/es/3
source_path: library/devmode.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2310
---

# Modo de desarrollo de Python

Added in version 3.7.

El modo de desarrollo de Python introduce comprobaciones adicionales
en tiempo de ejecución que son muy costosas para ser activadas por
defecto. No debería ser más verboso que el predeterminado si el código
es correcto; sólo se emiten nuevas advertencias cuando se detecta un
problema.

Puede activarse mediante la opción de línea de comandos "-X dev" o
estableciendo la variable de entorno "PYTHONDEVMODE" en "1".

Consulte también Compilación de depuración de Python.

## Efectos del modo de desarrollo de Python

Activar el modo de desarrollo de Python es similar al siguiente
comando, pero con efectos adicionales que se describen a continuación:

   PYTHONMALLOC=debug PYTHONASYNCIODEBUG=1 python -W default -X faulthandler

Efectos del modo de desarrollo de Python:

* Añadir "default" filtro de avisos.Se muestran las siguientes
  advertencias:

  * "DeprecationWarning"

  * "ImportWarning"

  * "PendingDeprecationWarning"

  * "ResourceWarning"

  Normalmente, los advertencias son filtradas por defecto warning
  filters.

  Se comporta como si se utilizara la opción de línea de comandos "-W
  default".

  Utilice la opción de línea de comandos "-W error" o establezca la
  variable de entorno "PYTHONWARNINGS" en "error" para tratar las
  advertencias como errores.

* Instalar hooks(enganches) de depuración en los asignadores de
  memoria para comprobar:

  * Desbordamiento del búfer

  * Sobrecarga del búfer

  * Violación de la API del asignador de memoria

  * Uso inseguro del GIL

  Ver la función en C "PyMem_SetupDebugHooks()".

  Se comporta como si la variable de entorno "PYTHONMALLOC" estuviera
  establecida en "debug".

  Para activar el modo de desarrollo de Python sin instalar ganchos de
  depuración en los asignadores de memoria, establezca la variable de
  entorno "PYTHONMALLOC" a "default".

* Llama a "faulthandler.enable()" al inicio de Python para instalar
  los handlers(manejadores) de las señales "SIGSEGV", "SIGFPE",
  "SIGABRT", "SIGBUS" y "SIGILL" para volcar la traza de Python en
  caso de fallo.

  Se comporta como si se utilizara la opción de línea de comandos "-X
  faulthandler" o si la variable de entorno "PYTHONFAULTHANDLER" se
  establece en "1".

* Habilitar asyncio debug mode. Por ejemplo, "asyncio" comprueba las
  corutinas que no fueron esperadas y las registra.

  Se comporta como si la variable de entorno "PYTHONASYNCIODEBUG"
  estuviera establecida en "1".

* Comprueba los argumentos *encoding* y *errors* para las operaciones
  de codificación y decodificación de cadenas. Ejemplos: "open()",
  "str.encode()" y "bytes.decode()".

  Por defecto, para un mejor rendimiento, el argumento *errors* sólo
  se comprueba en el primer error de codificación/decodificación y el
  argumento *encoding* a veces se ignora para las cadenas vacías.

* El destructor de "io.IOBase" registra las excepciones "close()".

* Establece el atributo "dev_mode" de "sys.flags" a "True".

El Modo de Desarrollo de Python no habilita el módulo "tracemalloc"
por defecto, porque el costo de la sobrecarga (para el rendimiento y
la memoria) sería demasiado grande. Activar el módulo "tracemalloc"
proporciona información adicional sobre el origen de algunos errores.
Por ejemplo, "ResourceWarning" registra la traza donde se asignó el
recurso, y un error de desbordamiento de búfer registra la traza donde
se asignó el bloque de memoria.

El modo de desarrollo de Python no impide que la opción de línea de
comandos "-O" elimine las declaraciones "assert" ni que establezca
"__debug__" a "False".

El modo de desarrollo de Python solo se puede habilitar en el inicio
de Python. Su valor se puede leer en "sys.flags.dev_mode".

Distinto en la versión 3.8: El destructor de "io.IOBase" ahora
registra las excepciones "close()".

Distinto en la versión 3.9: Los argumentos *enconding* y *errors* se
comprueban ahora para las operaciones de codificación y
descodificación de cadenas.

## Ejemplo de ResourceWarning

Ejemplo de un script que cuenta el número de líneas del archivo de
texto especificado en la línea de comandos:

   import sys

   def main():
       fp = open(sys.argv[1])
       nlines = len(fp.readlines())
       print(nlines)
       # The file is closed implicitly

   if __name__ == "__main__":
       main()

El script no cierra el archivo explícitamente. Por defecto, Python no
emite ninguna advertencia. Ejemplo usando README.txt, que tiene 269
líneas:

   $ python script.py README.txt
   269

Al activar el modo de desarrollo de Python aparece una advertencia
"ResourceWarning":

   $ python -X dev script.py README.txt
   269
   script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
     main()
   ResourceWarning: Enable tracemalloc to get the object allocation traceback

Además, al activar "tracemalloc" se muestra la línea en la que se
abrió el archivo:

   $ python -X dev -X tracemalloc=5 script.py README.rst
   269
   script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
     main()
   Object allocated at (most recent call last):
     File "script.py", lineno 10
       main()
     File "script.py", lineno 4
       fp = open(sys.argv[1])

La solución es cerrar explícitamente el archivo. Ejemplo utilizando un
gestor de contexto:

   def main():
       # Close the file explicitly when exiting the with block
       with open(sys.argv[1]) as fp:
           nlines = len(fp.readlines())
       print(nlines)

No cerrar un recurso explícitamente puede dejar un recurso abierto
durante mucho más tiempo del estimado; puede causar graves problemas
al salir de Python. Es malo en CPython, pero es aún peor en PyPy.
Cerrar los recursos explícitamente hace que una aplicación sea más
detallista y más fiable.

## Ejemplo de error de descriptor de archivo incorrecto

Script que muestra la primera línea de sí mismo:

   import os

   def main():
       fp = open(__file__)
       firstline = fp.readline()
       print(firstline.rstrip())
       os.close(fp.fileno())
       # The file is closed implicitly

   main()

Por defecto, Python no emite ninguna advertencia:

   $ python script.py
   import os

El modo de desarrollo de Python muestra un "ResourceWarning" y
registra un error "Bad file descriptor" cuando termina el objeto
archivo:

   $ python -X dev script.py
   import os
   script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
     main()
   ResourceWarning: Enable tracemalloc to get the object allocation traceback
   Exception ignored in: <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
   Traceback (most recent call last):
     File "script.py", line 10, in <module>
       main()
   OSError: [Errno 9] Bad file descriptor

"os.close(fp.fileno())" cierra el descriptor de archivo. Cuando el
finalizador de objetos de archivo intenta cerrar el descriptor de
archivo de nuevo, falla con el error "Bad file descriptor". Un
descriptor de archivo debe cerrarse sólo una vez. En el peor de los
casos, cerrarlo dos veces puede provocar un fallo (ver bpo-18748 para
un ejemplo).

La solución es eliminar la línea "os.close(fp.fileno())", o abrir el
archivo con "closefd=False".
