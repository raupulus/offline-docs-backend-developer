---
title: '"fileinput" --- Iterate over lines from multiple input streams'
source_url: https://docs.python.org/es/3
source_path: library/fileinput.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2620
---

# "fileinput" --- Iterate over lines from multiple input streams

**Código fuente:** Lib/fileinput.py

======================================================================

Este módulo implementa una clase auxiliar y funciones para escribir
rápidamente un bucle sobre una entrada estándar o una lista de
archivos. Si solo quiere leer o escribir un archivo, vea "open()".

El uso común es:

   import fileinput
   for line in fileinput.input(encoding="utf-8"):
       process(line)

Esto itera sobre las líneas de todos los archivos enumerados en
"sys.argv[1:]", por defecto a "sys.stdin" si la lista está vacía. Si
un nombre de archivo es "'-'", también se reemplaza por "sys.stdin" y
los argumentos opcionales *mode* y *openhook* se ignoran. Para
especificar una lista alternativa de nombres de archivo, se pasa como
primer argumento a "input()". También se permite un único nombre de
archivo.

Todos los archivos se abren en modo texto de manera predeterminada,
pero puede anular esto especificando el parámetro *mode* en la llamada
a "input()" o "FileInput". Si se produce un error de E/S durante la
apertura o lectura de un archivo, se lanza "OSError".

Distinto en la versión 3.3: "IOError" solía ser lanzado; ahora es un
alias de "OSError".

Si "sys.stdin" se usa más de una vez, el segundo y siguientes usos no
retornarán líneas, excepto tal vez para uso interactivo, o si se ha
reiniciado explícitamente (por ejemplo, usando "sys.stdin.seek(0)").

Los archivos vacíos se abren e inmediatamente se cierran; la única vez
que su presencia en la lista de nombres de archivo es notable es
cuando el último archivo abierto está vacío.

Las líneas se retornan con cualquier nueva línea intacta, lo que
significa que la última línea en un archivo puede no tener una.

You can control how files are opened by providing an opening hook via
the *openhook* parameter to "fileinput.input()" or "FileInput()". The
hook must be a function that takes two arguments, *filename* and
*mode*, and returns an accordingly opened file-like object. If
*encoding* and/or *errors* are specified, they will be passed to the
hook as additional keyword arguments. This module provides a
"hook_compressed()" to support compressed files.

La siguiente función es la interfaz principal de este módulo:

fileinput.input(files=None, inplace=False, backup='', *, mode='r', openhook=None, encoding=None, errors=None)

   Crea una instancia de la clase "FileInput". La instancia se usará
   como estado global para las funciones de este módulo y también se
   volverá a usar durante la iteración. Los parámetros de esta función
   se pasarán al constructor de la clase "FileInput".

   La instancia "FileInput" se puede usar como gestor de contexto en
   la declaración "with". En este ejemplo, *input* se cierra después
   de salir de la instrucción "with", incluso si se produce una
   excepción:

      with fileinput.input(files=('spam.txt', 'eggs.txt'), encoding="utf-8") as f:
          for line in f:
              process(line)

   Distinto en la versión 3.2: Se puede usar como gestor de contexto.

   Distinto en la versión 3.8: Los parámetros de palabras clave *mode*
   y *openhook* ahora son solo palabras clave.

   Distinto en la versión 3.10: Los parámetros exclusivos de palabra
   clave *encoding* y *errors* son añadidos.

Las siguientes funciones utilizan el estado global creado por
"fileinput.input()"; si no hay estado activo, es lanzado
"RuntimeError".

fileinput.filename()

   Retorna el nombre del archivo que se está leyendo actualmente.
   Antes de leer la primera línea, retorna "None".

fileinput.fileno()

   Retorna el entero "file descriptor" para el archivo actual. Cuando
   no se abre ningún archivo (antes de la primera línea y entre
   archivos), retorna "-1".

fileinput.lineno()

   Retorna el número de línea acumulativa de la línea que se acaba de
   leer. Antes de que se haya leído la primera línea, retorna "0".
   Después de leer la última línea del último archivo, retorna el
   número de línea de esa línea.

fileinput.filelineno()

   Retorna el número de línea en el archivo actual. Antes de que se
   haya leído la primera línea, retorna "0". Después de leer la última
   línea del último archivo, retorna el número de línea de esa línea
   dentro del archivo.

fileinput.isfirstline()

   Retorna "True" si la línea que acaba de leer es la primera línea de
   su archivo; de lo contrario, retorna "False".

fileinput.isstdin()

   Retorna "True" si la última línea se leyó de "sys.stdin", de lo
   contrario, retorna "False".

fileinput.nextfile()

   Cierra el archivo actual para que la próxima iteración lea la
   primera línea del siguiente archivo (si corresponde); las líneas no
   leídas del archivo no contarán para el recuento de líneas
   acumuladas. El nombre del archivo no se cambia hasta que se haya
   leído la primera línea del siguiente archivo. Antes de que se haya
   leído la primera línea, esta función no tiene efecto; no se puede
   usar para omitir el primer archivo. Después de leer la última línea
   del último archivo, esta función no tiene efecto.

fileinput.close()

   Cierra la secuencia.

La clase que implementa el comportamiento de secuencia proporcionado
por el módulo también está disponible para la subclasificación:

class fileinput.FileInput(files=None, inplace=False, backup='', *, mode='r', openhook=None, encoding=None, errors=None)

   La Clase "FileInput" es la implementación; sus métodos
   "filename()", "fileno()", "lineno()", "filelineno()",
   "isfirstline()", "isstdin()", "nextfile()" y "close()" corresponden
   a las funciones del mismo nombre en el módulo. Además es *iterable*
   y tiene un método "readline()" que retorna la siguiente línea de
   entrada. Se debe acceder a la secuencia en orden estrictamente
   secuencial; acceso aleatorio y "readline()" no se pueden mezclar.

   Con *mode* puede especificar qué modo de archivo se pasará a
   "open()". Debe ser uno de "'r'" y "'rb'".

   El *openhook*, cuando se proporciona, debe ser una función que tome
   dos argumentos, *filename* y *mode*, y retorne un objeto similar a
   un archivo abierto en consecuencia. No puede usar *inplace* y
   *openhook* juntos.

   Puedes especificar *encoding* y *errors* que son pasados a "open()"
   o *openhook*.

   Una instancia "FileInput" se puede usar como gestor de contexto en
   la instrucción "with". En este ejemplo, *input* se cierra después
   de salir de la palabra "with", incluso si se produce una excepción:

      with FileInput(files=('spam.txt', 'eggs.txt')) as input:
          process(input)

   Distinto en la versión 3.2: Se puede usar como gestor de contexto.

   Distinto en la versión 3.8: El parámetro de palabra clave *mode* y
   *openhook* ahora son solo palabras clave.

   Distinto en la versión 3.10: Los parámetros exclusivos de palabra
   clave *encoding* y *errors* son añadidos.

   Distinto en la versión 3.11: Los modos "'rU'" y "'U'" y el método
   "__getitem__()" han sido eliminados.

**Filtrado al instante opcional:** si el argumento de la palabra clave
"inplace=True" se pasa a "fileinput.input()" o al constructor
"FileInput", el archivo se mueve a una copia de seguridad y la salida
estándar es dirigida al archivo de entrada (si ya existe un archivo
con el mismo nombre que el archivo de copia de seguridad, se
reemplazará en silencio). Esto hace posible escribir un filtro que
reescribe su archivo de entrada en su lugar. Si se proporciona el
parámetro *backup* (generalmente como "backup='.<some extension>'"),
este especifica la extensión para el archivo de respaldo y el archivo
de respaldo permanece; de forma predeterminada, la extensión es
"'.bak'" y se elimina cuando se cierra el archivo de salida. El
filtrado en el lugar se desactiva cuando se lee la entrada estándar.

Este módulo proporciona los dos enlaces de apertura siguientes:

fileinput.hook_compressed(filename, mode, *, encoding=None, errors=None)

   Abre de forma transparente archivos comprimidos con *gzip* y
   *bzip2* (reconocidos por las extensiones "'.gz'" and "'.bz2'")
   utilizando los módulos "gzip" y "bz2". Si la extensión del nombre
   de archivo no es "'.gz'" or "'.bz2'", el archivo se abre
   normalmente (es decir, usando "open()" sin descompresión).

   Los valores *encoding* y *errors* se pasan a "io.TextIOWrapper"
   para archivos comprimidos y para abrir archivos normales.

   Ejemplo de uso: "fi =
   fileinput.FileInput(openhook=fileinput.hook_compressed,
   encoding="utf-8")"

   Distinto en la versión 3.10: Los parámetros exclusivos de palabra
   clave *encoding* y *errors* son añadidos.

fileinput.hook_encoded(encoding, errors=None)

   Retorna un enlace que abre cada archivo con "open()", usando el
   *encoding* y *errors* dados para leer el archivo.

   Ejemplo de uso: "fi =
   fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8",
   "surrogateescape"))"

   Distinto en la versión 3.6: Se agregó el parámetro opcional
   *errors*.

   Obsoleto desde la versión 3.10: Esta función está en desuso ya que
   "fileinput.input()" y "FileInput" ahora tienen los parámetros
   *encoding* y *errors*.
