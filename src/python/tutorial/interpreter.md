---
title: 2. Usando el intérprete de Python
source_url: https://docs.python.org/es/3
source_path: tutorial/interpreter.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4960
---

# 2. Usando el intérprete de Python

## 2.1. Invocar el intérprete

The Python interpreter is usually installed as
"/usr/local/bin/python3.14" on those machines where it is available;
putting "/usr/local/bin" in your Unix shell's search path makes it
possible to start it by typing the command:

   python3.14

en el terminal [1]. Ya que la elección del directorio dónde vivirá el
intérprete es una opción del proceso de instalación, puede estar en
otros lugares; consulta a tu gurú de Python local o administrador de
sistemas. (Por ejemplo, "/usr/local/python" es una alternativa
popular).

On Windows machines where you have installed Python from the Microsoft
Store, the "python3.14" command will be available. If you have the
py.exe launcher installed, you can use the "py" command. See Python
install manager for other ways to launch Python.

Se puede salir del intérprete con estado de salida cero ingresando el
carácter de fin de archivo ("Control"-"D" en Unix, "Control"-"Z" en
Windows). Si eso no funciona, puedes salir del intérprete escribiendo
el comando: "quit()".

The interpreter's line-editing features include interactive editing,
history substitution and code completion on most systems. Perhaps the
quickest check to see whether command line editing is supported is
typing a word in on the Python prompt, then pressing Left arrow (or
"Control"-"b"). If the cursor moves, you have command line editing;
see Appendix Edición de entrada interactiva y sustitución de historial
for an introduction to the keys. If nothing appears to happen, or if a
sequence like "^[[D" or "^B" appears, command line editing isn't
available; you'll only be able to use backspace to remove characters
from the current line.

El intérprete funciona de manera similar al shell de Unix: cuando se
le llama con una entrada estándar conectada a un terminal, lee y
ejecuta comandos de manera interactiva; cuando se le llama con un
argumento de nombre de archivo o con un archivo como entrada estándar,
lee y ejecuta un *script* desde ese archivo.

Una segunda forma de iniciar el intérprete es "python -c comando [arg]
...", que ejecuta las sentencias en *comando*, similar a la opción de
shell "-c" . Como las sentencias de Python a menudo contienen espacios
u otros caracteres que son especiales para el shell, generalmente se
recomienda citar *comando* en su totalidad.

Algunos módulos de Python también son útiles como scripts. Estos
pueden invocarse utilizando "python -m módulo [arg] ...", que ejecuta
el archivo fuente para *módulo* como si se hubiera escrito el nombre
completo en la línea de comandos.

Cuando se usa un script, a veces es útil poder ejecutar el script y
luego ingresar al modo interactivo. Esto se puede hacer pasando la
"-i" antes del nombre del script.

Todas las opciones de la línea de comandos se describen en Línea de
comandos y entorno.

### 2.1.1. Paso de argumentos

Cuando son conocidos por el intérprete, el nombre del script y los
argumentos adicionales se convierten a una lista de cadenas de texto
asignada a la variable "argv" del módulo "sys". Puedes acceder a esta
lista haciendo "import sys". La longitud de la lista es al menos uno;
cuando no se utiliza ningún script o argumento, "sys.argv[0]" es una
cadena vacía. Cuando se pasa el nombre del script con "'-'" (lo que
significa la entrada estándar), "sys.argv[0]" vale "'-'". Cuando se
usa "-c" *comando*, "sys.argv[0]" vale "'-c'". Cuando se usa "-m"
*módulo*, "sys.argv[0]" contiene el valor del nombre completo del
módulo. Las opciones encontradas después de "-c" *comando* o "-m"
*módulo* no son consumidas por el procesador de opciones de Python
pero de todas formas se almacenan en "sys.argv" para ser manejadas por
el comando o módulo.

### 2.1.2. Modo interactivo

Cuando se leen los comandos desde un terminal, se dice que el
intérprete está en *modo interactivo*. En este modo, espera el
siguiente comando con el *prompt primario*, generalmente tres signos
de mayor que (">>>"); para las líneas de continuación, aparece el
*prompt secundario*, por defecto tres puntos ("..."). El intérprete
imprime un mensaje de bienvenida que indica su número de versión y un
aviso de copyright antes de imprimir el primer *prompt primario*:

   $ python3.14
   Python 3.14 (default, April 4 2024, 09:25:04)
   [GCC 10.2.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Las líneas de continuación son necesarias cuando se ingresa una
construcción multilínea. Como ejemplo, echa un vistazo a la sentencia
"if":

   >>> the_world_is_flat = True
   >>> if the_world_is_flat:
   ...     print("Be careful not to fall off!")
   ...
   Be careful not to fall off!

Para más información sobre el modo interactivo, ver Modo interactivo.

## 2.2. El intérprete y su entorno

### 2.2.1. Codificación del código fuente

De forma predeterminada, los archivos fuente de Python se tratan como
codificados en UTF-8. En esa codificación, los caracteres de la
mayoría de los idiomas del mundo se pueden usar simultáneamente en
literales, identificadores y comentarios, aunque la biblioteca
estándar solo usa caracteres ASCII para los identificadores, una
convención que debería seguir cualquier código que sea portable.Para
mostrar todos estos caracteres correctamente, tu editor debe reconocer
que el archivo es UTF-8, y debe usar una fuente que admita todos los
caracteres del archivo.

Para declarar una codificación que no sea la predeterminada, se debe
agregar una línea de comentario especial como la *primera* línea del
archivo. La sintaxis es la siguiente:

   # -*- coding: encoding -*-

donde *encoding* es uno de los "codecs" soportados por Python.

Por ejemplo, para declarar que se utilizará la codificación de
Windows-1252, la primera línea del archivo de código fuente debe ser:

   # -*- coding: cp1252 -*-

Una excepción a la regla de *primera línea* es cuando el código fuente
comienza con una linea UNIX "shebang". En ese caso, la declaración de
codificación debe agregarse como la segunda línea del archivo. Por
ejemplo:

   #!/usr/bin/env python3
   # -*- coding: cp1252 -*-

-[ Notas al pie ]-

[1] En Unix, el intérprete de Python 3.x no está instalado por defecto
    con el ejecutable llamado "python", por lo que no entra en
    conflicto con un ejecutable de Python 2.x instalado
    simultáneamente.
