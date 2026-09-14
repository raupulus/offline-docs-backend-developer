---
title: '"__main__" --- Top-level code environment'
source_url: https://docs.python.org/es/3
source_path: library/__main__.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1470
---

# "__main__" --- Top-level code environment

======================================================================

En Python, el nombre especial "__main__" es utilizado para dos
constructos importantes:

1. el nombre del entorno de máximo nivel del programa, que puede ser
   verificado usando la expresión "__name__=='__main__'"; y

2. el archivo "__main__.py" en paquetes de Python.

Ambos de estos mecanismos están relacionados con módulos de Python;
como los usuarios interactúan con ellos y como ellos interactúan entre
sí.  Están explicados en detalle más abajo.  Si estás empezando con
los módulos de Python, mira la sección tutorial Módulos para una
introducción.

## "__name__ == '__main__'"

Cuando un módulo o paquete de Python es importado, "__name__" es
asignado al nombre del módulo.  Normalmente, este es el nombre del
archivo de Python sin la extensión ".py":

   >>> import configparser
   >>> configparser.__name__
   'configparser'

Si el archivo es parte de un paquete, "__name__" también incluirá la
ruta del paquete padre:

   >>> from concurrent.futures import process
   >>> process.__name__
   'concurrent.futures.process'

Sin embargo, si el módulo es ejecutado en el entorno de código de
máximo nivel, su "__name__" se le asigna el valor del string
"'__main__'".

### ¿Qué es el "entorno de código de máximo nivel"?

"__main__" es el nombre del entorno en el cual se ejecuta el código de
máximo nivel. "Código de máximo nivel" es el primer módulo de Python
especificado por el usuario que empieza a ejecutarse. Es "de máximo
nivel" porque importa todos los demás módulos que necesita el
programa. A veces "código de máximo nivel" es llamado un *punto de
entrada* a la aplicación.

El entorno de código de máximo nivel puede ser:

* el ámbito de un intérprete interactivo:

     >>> __name__
     '__main__'

* el módulo de Python pasado al intérprete de Python como un argumento
  de archivo:

     $ python helloworld.py
     Hello, world!

* el módulo o paquete de Python pasado al interprete de Python con el
  argumento "-m":

     $ python -m tarfile
     usage: tarfile.py [-h] [-v] (...)

* Código de Python leído por el interprete desde input estándar:

     $ echo "import this" | python
     The Zen of Python, by Tim Peters

     Beautiful is better than ugly.
     Explicit is better than implicit.
     ...

* Código de Python pasado al intérprete Python con el argumento "-c":

     $ python -c "import this"
     The Zen of Python, by Tim Peters

     Beautiful is better than ugly.
     Explicit is better than implicit.
     ...

En cada una de estas situaciones, al "__name__" del módulo de máximo
nivel se le asigna el valor "'__main__'".

En consecuencia, un módulo puede descubrir si se está ejecutando o no
en el ámbito principal al verificar su propio "__name__", lo cual
permite un vocablo común para ejecutar código condicionalmente cuando
el módulo no es inicializado desde una declaración de importado:

   if __name__ == '__main__':
       # Execute when the module is not initialized from an import statement.
       ...

Ver también:

  Para una vista más detallada de como "__name__" es asignado en todas
  las situaciones, ver la sección tutorial Módulos.

### Uso idiomático

Algunos módulos contienen código que está pensado para uso de script
solamente, como para interpretar argumentos de línea de comando u
obtener datos de la entrada estándar.  Cuando un módulo como este
fuese importado desde un módulo distinto, por ejemplo para realizar
una prueba unitaria, el código del script se ejecutaría
involuntariamente.

Aquí es donde es útil usar el código de bloque "if
__name__=='__main__'". El código dentro desde bloque no se ejecutará a
menos que el módulo se ejecute en el entorno de máximo nivel.

Poner cuantas menos declaraciones posible en el bloque debajo de "if
__name__=='__main__'" puede mejorar la claridad y validez del código.
Mas a menudo, la función llamada "main" encapsula el comportamiento
principal del programa:

   # echo.py

   import shlex
   import sys

   def echo(phrase: str) -> None:
      """A dummy wrapper around print."""
      # for demonstration purposes, you can imagine that there is some
      # valuable and reusable logic inside this function
      print(phrase)

   def main() -> int:
       """Echo the input arguments to standard output"""
       phrase = shlex.join(sys.argv)
       echo(phrase)
       return 0

   if __name__ == '__main__':
       sys.exit(main())  # next section explains the use of sys.exit

Note que si el módulo no encapsulase el código dentro de la función
"main" pero en vez lo pusiese directo dentro del bloque  "if
__name__=='__main__'", la variable "phrase" sería global al módulo
entero.  Esto está propenso a generar errores ya que otras funciones
dentro del módulo pudiesen estar usando involuntariamente la variable
global en lugar de un nombre local.  Una función "main" resuelve este
problema.

Usar una función "main" tiene el beneficio añadido de que la función
"echo" está aislada y es importable en otros sitios. Cuando "echo.py"
es importado, las funciones "echo" y "main" serán definidas, pero
ninguna de ellas será llamada porque "__name!='__main__'".

### Consideraciones de empaquetado

Las funciones "main" se utilizan a menudo para crear líneas de comando
al especificarlas como puntos de entrada para scripts de terminal.
Cuando esto se hace, pip inserta la llamada de la función a un script
plantilla, donde el valor retornado de "main" se pasa a "sys.exit()".
Por ejemplo:

   sys.exit(main())

Dado que la llamada a "main" está dentro de "sys.exit()", la
expectativa es que tu función devolverá un valor aceptable como una
entrada a "sys.exit()"; típicamente, un int o "None" (que se retorna
implícitamente si tu función no tiene una declaración de retorno).

Al seguir pro-activamente esta convención nosotros mismo, nuestro
módulo tendrá el mismo comportamiento cuando se ejecuta directamente
(es decir, "python echo.py") que si luego lo empaquetamos como un
punto de entrada de script de terminal en un paquete instalable
mediante pip.

En particular, ten cuidado al devolver cadenas de texto con tu función
"main". "sys.exit()" interpretará un argumento de cadena de texto como
un mensaje de fallo, entonces tu programa tendrá un código de salida
de "1", indicando fallo, y la cadena de texto será escrita a
"sys.stderr".  El ejemplo "echo.py" de antes muestra como usar la
convención "sys.exit(main())".

Ver también:

  Python Packaging User Guide contiene una colección de tutoriales y
  referencias sobre como distribuir e instalar paquetes de Python con
  herramientas modernas.

## "__main__.py" en paquetes de Python

Si no estás familiarizado con paquetes de Python, ver la sección
Paquetes del tutorial.  Comúnmente, el archivo "__main__.py" es
utilizado para proveer una interfaz de línea de comando para un
paquete. Considera el siguiente paquete hipotético, "*bandclass*":

   bandclass
     ├── __init__.py
     ├── __main__.py
     └── student.py

"__main__.py" será ejecutado cuando el paquete sea invocado
directamente desde la línea de comandos usando el indicador "-m". Por
ejemplo:

   $ python -m bandclass

Este comando causará que "__main__.py" se ejecute. El como se use este
mecanismo dependerá de la naturaleza del paquete que estás
escribiendo, pero en este caso hipotético, puede tener sentido
permitir que el profesor busque estudiantes:

   # bandclass/__main__.py

   import sys
   from .student import search_students

   student_name = sys.argv[1] if len(sys.argv) >= 2 else ''
   print(f'Found student: {search_students(student_name)}')

Note que "from .student import search_students" es un ejemplo de una
importación relativa.  Este estilo de importación debe ser utilizado
cuando se hace referencia a módulos dentro de un paquete.  Para más
detalles, ver Referencias internas en paquetes en la sección Módulos
del tutorial.

### Uso idiomático

Los contenidos de "__main__.py" no están típicamente acotados dentro
de bloques "if __name__=='__main__'".  En cambio, esos archivos se
mantienen cortos e importan funciones para ejecutar desde otros
módulos.  A esos otros módulos se les puede fácilmente realizar
pruebas unitarias y son apropiadamente re-utilizables.

Si se usa, un bloque "if __name__=='__main__'" seguirá funcionando
como se espera para un archivo "__main__.py" dentro de un paquete,
porque su atributo "__name__" incluirá la ruta del paquete si es
importado:

   >>> import asyncio.__main__
   >>> asyncio.__main__.__name__
   'asyncio.__main__'

This won't work for "__main__.py" files in the root directory of a
".zip" file though.  Hence, for consistency, a minimal "__main__.py"
without a "__name__" check is preferred.

Ver también:

  En "venv" puedes conseguir un ejemplo de un paquete con un
  "__main__.py" minimalista en la librería estándar. No contiene un
  bloque "if __name__=='__main__'". Lo puedes invocar con "python -m
  venv [directorio]".

  Ver "runpy" para más detalles sobre el indicador "-m" para el
  interprete ejecutable.

  Ver "zipapp" para más información sobre como ejecutar aplicaciones
  empaquetadas como archivos *.zip*. En este caso Python busca un
  archivo "__main__.py" en el directorio raíz del archivo comprimido.

## "import __main__"

Independientemente de con cual módulo se ha iniciado un programa de
Python, otros módulos que están siendo ejecutados dentro del mismo
programa pueden importar el ámbito del entorno de máximo nivel
(*namespace*) al importar el módulo "__main__".  Esto no importa un
archivo "__main__.py" pero en su lugar cualquier módulo que recibió el
nombre especial "'__main__'".

Acá hay un módulo ejemplo que consume el nombre de espacio "__main__":

   # namely.py

   import __main__

   def did_user_define_their_name():
       return 'my_name' in dir(__main__)

   def print_user_name():
       if not did_user_define_their_name():
           raise ValueError('Define the variable `my_name`!')

       print(__main__.my_name)

Ejemplo del uso de este módulo puede ser:

   # start.py

   import sys

   from namely import print_user_name

   # my_name = "Dinsdale"

   def main():
       try:
           print_user_name()
       except ValueError as ve:
           return str(ve)

   if __name__ == "__main__":
       sys.exit(main())

Si ahora iniciamos nuestro programa el resultado sería así:

   $ python start.py
   Define the variable `my_name`!

El código de salida del programa sería 1, indicando un error. Des-
comentando la línea con "my_name = "Dinsdale"" arregla el programa y
ahora sale con un código de estado 0, indicando éxito:

   $ python start.py
   Dinsdale

Note que importar "__main__" no causa ningún problema de
involuntariamente ejecutar código de máximo nivel que ha sido pensado
para uso por scripts que es puesto en el bloque "if
__name__=="__main__"" del módulo "start". ¿Por qué funciona esto?

Python inserta un módulo "__main__" vacío en "sys.modules" al inicio
del intérprete, y lo puebla ejecutando código de máximo nivel. En
nuestro ejemplo este es el módulo "start" que corre línea a línea e
importa "namely". A su vez, "namely" importa "__main__" (que es en
verdad "start"). ¡Es un ciclo de importado! Afortunadamente, como el
módulo parcialmente poblado "__main__" está presente en "sys.modules",
Python pasa eso a "namely". Ver Special considerations for __main__ en
la referencia del sistema para información detallada de como funciona.

El REPL Python es otro ejemplo de un "entorno de máximo nivel", por lo
tanto, cualquier cosa definida en el REPL se hace parte del ámbito
"__main__":

   >>> import namely
   >>> namely.did_user_define_their_name()
   False
   >>> namely.print_user_name()
   Traceback (most recent call last):
   ...
   ValueError: Define the variable `my_name`!
   >>> my_name = 'Jabberwocky'
   >>> namely.did_user_define_their_name()
   True
   >>> namely.print_user_name()
   Jabberwocky

El ámbito "__main__" es utilizado en la implementación de "pdb" y
"rlcompleter".
