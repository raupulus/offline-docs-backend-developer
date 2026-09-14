---
title: '"compileall" --- Byte-compile Python libraries'
source_url: https://docs.python.org/es/3
source_path: library/compileall.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2030
---

# "compileall" --- Byte-compile Python libraries

**Código fuente:** Lib/compileall.py

======================================================================

Este módulo proporciona algunas funciones de utilidad para admitir la
instalación de bibliotecas Python. Estas funciones compilan archivos
fuente de Python en un árbol de directorios. Este módulo se puede usar
para crear los archivos de código de bytes almacenados en caché en el
momento de la instalación de la biblioteca, que los hace disponibles
para su uso incluso por usuarios que no tienen permiso de escritura en
los directorios de la biblioteca.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

## Uso de la línea de comandos

Este módulo puede funcionar como un *script* (usando  **python -m
compileall**) para compilar fuentes de Python.

directory ...
file ...

   Los argumentos posicionales son archivos para compilar o
   directorios que contienen archivos fuente, recorridos
   recursivamente. Si no se proporciona ningún argumento, se comporta
   como si la línea de comando fuera "-l *<directories from
   sys.path>*".

-l

   No se recurre en subdirectorios, solo compila archivos de código
   fuente contenidos en directorios nombrados o implícitos.

-f

   Forzar la reconstrucción incluso si las marcas de tiempo están
   actualizadas.

-q

   No imprimir la lista de archivos compilados. Si se pasa una vez,
   los mensajes de error se imprimirán. Si se pasa dos veces, ("-qq"),
   se suprime toda la salida.

-d destdir

   Directorio antepuesto a la ruta de cada archivo que está siendo
   compilado. Esto aparecerá en las devoluciones de tiempo de
   compilación, y también se compila en el archivo de código de bytes,
   donde se usará en las devoluciones de seguimiento y otros mensajes
   en casos donde el archivo fuente no existe al momento en que el
   archivo de código de bytes se ejecuta.

-s strip_prefix

   Remove the given prefix from paths recorded in the ".pyc" files.
   Paths are made relative to the prefix.

   This option can be used with "-p" but not with "-d".

-p prepend_prefix

   Prepend the given prefix to paths recorded in the ".pyc" files. Use
   "-p /" to make the paths absolute.

   This option can be used with "-s" but not with "-d".

-x regex

   regex se usa para buscar la ruta completa a cada archivo
   considerado para compilación, y si la regex produce una
   coincidencia, se omite el archivo.

-i list

   Leer el archivo "list" y cada línea que contiene la lista de
   archivos y directorios a compilar. Si "list" es "-", leer líneas
   desde "stdin".

-b

   Escribir los archivos de código de byte en las locaciones y nombres
   de herencia, que pueden sobreescribir los archivos de código de
   bytes creado para otra versión de Python. El comportamiento por
   defecto es escribir archivos en sus locaciones y nombres **PEP
   3147**, lo cual permite que archivos de código de byte de versiones
   múltiples de Python coexistan.

-r

   Controlar el nivel máximo de recurrencia para subdirectorios. Si
   esto está dado, la opción "-l" no se tendrá en cuenta. **python -m
   compileall <directory> -r 0** es equivalente a **python -m
   compileall <directory> -l**.

-j N

   Use *N* workers to compile the files within the given directory. If
   "0" is used, then the result of "os.process_cpu_count()" will be
   used.

--invalidation-mode [timestamp|checked-hash|unchecked-hash]

   Controlar cómo los archivos de código de byte generados se
   invalidan al momento de ejecución. El valor "timestamp" significa
   que se generarán los archivos ".pyc" con la marca de tiempo fuente
   y el tamaño insertados. Los valores "checked-hash" y "unchecked-
   hash" generan *pycs* basados en hash. Los *pycs* basados en hash
   del archivo insertan un hash de los contenidos del archivo fuente,
   en lugar de una marca de tiempo. Véase Invalidación del código de
   bytes en caché para mayor información sobre cómo Python valida
   archivos de cache de código de bytes. El valor por defecto es
   "timestamp"  si la variable de entorno "SOURCE_DATE_EPOCH" no está
   definida, y "checked-hash" si la variable de entorno
   "SOURCE_DATE_EPOCH" está definida.

-o level

   Compila con el nivel de optimización dado. Puede usarse varias
   veces para compilar varios niveles a la vez (por ejemplo,
   "compileall -o 1 -o 2").

-e dir

   Ignora los enlaces simbólicos que apuntan fuera del directorio
   dado.

--hardlink-dupes

   Si dos archivos ".pyc" con diferente nivel de optimización tienen
   el mismo contenido, use enlaces físicos para consolidar los
   archivos duplicados.

Distinto en la versión 3.2: Se agregaron las opciones "-i", "-b" y
"-h".

Distinto en la versión 3.5: Se agregaron las opciones "-j", "-r", and
"-qq". La opción "-q" se cambió a un valor multinivel. "-b" siempre
producirá un archivo de código de byte que termina en ".pyc", nunca
".pyo".

Distinto en la versión 3.7: Se agregó la opción "--invalidation-mode".

Distinto en la versión 3.9: Se agregaron las opciones "-s", "-p", "-e"
y "--hardlink-dupes". Se elevó el límite de recursividad
predeterminado de 10 a "sys.getrecursionlimit()". Se agregó la
posibilidad de especificar la opción "-o" varias veces.

No hay opción de línea de comando para controlar el nivel de
optimización que usa la función "compile()" porque el intérprete de
Python en sí mismo ya proporciona la opción: **python -O -m
compileall**.

De manera similar, la función "compile()" respeta la configuración
"sys.pycache_prefix". El cache de código de byte generado sólo será
útil si "compile()" se ejecuta con el mismo "sys.pycache_prefix" (si
es que existe alguno) que se utilizará en el momento de ejecución.

## Funciones públicas

compileall.compile_dir(dir, maxlevels=sys.getrecursionlimit(), ddir=None, force=False, rx=None, quiet=0, legacy=False, optimize=-1, workers=1, invalidation_mode=None, *, stripdir=None, prependdir=None, limit_sl_dest=None, hardlink_dupes=False)

   Descender recursivamente el árbol de directorio invocado por *dir*,
   compilando todos los archivos ".py" que encuentra en el camino.
   Devolver un valor verdadero si todos los archivos se compilan
   exitosamente, y un valor falso en el caso contrario.

   El parámetro *maxlevels* se usar para limitar la profundidad de la
   recursión; toma como valor predeterminado
   "sys.getrecursionlimit()".

   Si *ddir* está dado, se antepone a la ruta de cada archivo que se
   compila para usar en los rastreos de tiempo de compilación, y
   también se compilar en el archivo código de byte, donde se usarán
   en trazas y otros mensajes en casos donde el archivo fuente no
   existe en el momento cuando el archivo de código de byte se
   ejecuta.

   Si *force* es verdadero, los módulos se re-compilan aun cuando las
   marcas de tiempo están actualizadas.

   Si se proporciona *rx*, se llama a su método "search" en la ruta
   completa a cada archivo considerado para compilación, y si retorna
   un valor verdadero, se omite el archivo. Esto se puede usar para
   excluir archivos que coincidan con una expresión regular, dada como
   un objeto re.Pattern.

   Si *quiet* es "False" o "0" (el valor predeterminado), los nombres
   de archivo y otra información se imprimen en salida estándar. Si se
   configura en "1", solo se imprimen los errores. Si se configura en
   "2", se suprime toda la salida.

   Si *legacy* es verdadero, los archivos de código de byte se
   escriben en sus locaciones y nombres de herencia, que pueden
   sobreescribir los archivos de código de byte creado por otra
   versión de Python. El comportamiento por defecto es escribir
   archivos en sus locaciones y nombres **PEP 3147**, lo cual permite
   que archivos de código de byte de múltiples versiones de Python
   coexistan.

   *optimize* especifica el nivel de optimización para el compilador.
   Se pasa a una función incorporada "compile()". Acepta también una
   secuencia de niveles de optimización que conducen a múltiples
   compilaciones de un archivo ".py" en una llamada.

   El argumento *workers* especifica cuántos workers se usan para
   compilar archivos en paralelo. El comportamiento por defecto es no
   usar múltiples workers. Si la plataforma no puede usar workers
   múltiples y el argumento *workers* está dado, la compilación
   secuencial se usará como *fallback*. Si *workers* es 0, el número
   de núcleos se usa en el sistema. Si *workers* es menor que "0", se
   genera un "ValueError".

   *invalidation_mode* debería ser un miembro de la enumeración
   "py_compile.PycInvalidationMode" y controla cómo se invalidan los
   pycs generados en el momento de ejecución.

   Los argumentos *stripdir*, *prependdir* y *limit_sl_dest*
   corresponden a las opciones "-s", "-p" y "-e" descritas
   anteriormente. Pueden especificarse como "str", o "os.PathLike".

   Si *hardlink_dupes* es verdadero y dos archivos ".pyc" con
   diferente nivel de optimización tienen el mismo contenido, use
   enlaces físicos para consolidar los archivos duplicados.

   Distinto en la versión 3.2: Se agregó el parámetro *legacy* y
   *optimize*.

   Distinto en la versión 3.5: Se agregó el parámetro *workers*.

   Distinto en la versión 3.5: El parámetro *quiet* se cambió a un
   valor multinivel.

   Distinto en la versión 3.5: El parámetro *legacy* solo escribe
   archivos ".pyc", no archivos ".pyo", no import cuál sea el valor de
   *optimize*.

   Distinto en la versión 3.6: Acepta un *path-like object*.

   Distinto en la versión 3.7: Se agregó el parámetro
   *invalidation_mode*.

   Distinto en la versión 3.7.2: The *invalidation_mode* parameter's
   default value is updated to "None".

   Distinto en la versión 3.8: Configurar *workers* a 0 ahora elige el
   número óptimo de núcleos.

   Distinto en la versión 3.9: Se agregaron los argumentos *stripdir*,
   *prependdir*, *limit_sl_dest* y *hardlink_dupes*. El valor
   predeterminado de *maxlevels* se cambió de "10" a
   "sys.getrecursionlimit()"

compileall.compile_file(fullname, ddir=None, force=False, rx=None, quiet=0, legacy=False, optimize=-1, invalidation_mode=None, *, stripdir=None, prependdir=None, limit_sl_dest=None, hardlink_dupes=False)

   Compilar el archivo con ruta *fullname*. Retorna un valor verdadero
   si el archivo se compila exitosamente, y uno falso en el caso
   contrario.

   Si *ddir* está dado, se antepone a la ruta del archivo que está
   siendo compilado para su uso en las trazas de tiempo de
   compilación, y también se compilar en el archivo de código de
   bytes, donde será utilizado en trazas y otros mensajes en casos
   donde el archivo fuente no existe en el momento en que el archivo
   de código de bytes es ejecutado.

   Si se proporciona *rx*, a su método "search" se le pasa el nombre
   de ruta completo al archivo que se está compilando, y si retorna un
   valor verdadero, el archivo no se compila y se retorna "True". Esto
   se puede usar para excluir archivos que coincidan con una expresión
   regular, dada como un objeto re.Pattern.

   Si *quiet* es "False" o "0" (el valor predeterminado), los nombres
   de archivo y otra información se imprimen en salida estándar. Si se
   configura en "1", solo se imprimen los errores. Si se configura en
   "2", se suprime toda la salida.

   Si *legacy* es verdadero, los archivos de código de byte se
   escriben en sus locaciones y nombres de herencia, que pueden
   sobreescribir los archivos de código de byte creado por otra
   versión de Python. El comportamiento por defecto es escribir
   archivos en sus locaciones y nombres **PEP 3147**, lo cual permite
   que archivos de código de byte de múltiples versiones de Python
   coexistan.

   *optimize* especifica el nivel de optimización para el compilador.
   Se pasa a una función incorporada "compile()". Acepta también una
   secuencia de niveles de optimización que conducen a múltiples
   compilaciones de un archivo ".py" en una llamada.

   *invalidation_mode* debería ser un miembro de la enumeración
   "py_compile.PycInvalidationMode" y controla cómo se invalidan los
   pycs generados en el momento de ejecución.

   Los argumentos *stripdir*, *prependdir* y *limit_sl_dest*
   corresponden a las opciones "-s", "-p" y "-e" descritas
   anteriormente. Pueden especificarse como "str", o "os.PathLike".

   Si *hardlink_dupes* es verdadero y dos archivos ".pyc" con
   diferente nivel de optimización tienen el mismo contenido, use
   enlaces físicos para consolidar los archivos duplicados.

   Added in version 3.2.

   Distinto en la versión 3.5: El parámetro *quiet* se cambió a un
   valor multinivel.

   Distinto en la versión 3.5: El parámetro *legacy* solo escribe
   archivos ".pyc", no archivos ".pyo", no import cuál sea el valor de
   *optimize*.

   Distinto en la versión 3.7: Se agregó el parámetro
   *invalidation_mode*.

   Distinto en la versión 3.7.2: The *invalidation_mode* parameter's
   default value is updated to "None".

   Distinto en la versión 3.9: Se agregaron los argumentos *stripdir*,
   *prependdir*, *limit_sl_dest* y *hardlink_dupes*.

compileall.compile_path(skip_curdir=True, maxlevels=0, force=False, quiet=0, legacy=False, optimize=-1, invalidation_mode=None)

   Compila en bytes todos los archivos ".py" a lo largo de "sys.path".
   Retorna un valor verdadero si todos los archivos se compilan
   exitosamente, y uno falso en el caso contrario.

   Si *skip_curdir* es verdadero (el valor predeterminado), el
   directorio actual no está incluido en la búsqueda. Todos los otros
   parámetros se pasan a la función "compile_dir()". Nótese que, al
   contrario de las otras funciones de compilación, "maxlevels" tomar
   "0" como valor predeterminado.

   Distinto en la versión 3.2: Se agregó el parámetro *legacy* y
   *optimize*.

   Distinto en la versión 3.5: El parámetro *quiet* se cambió a un
   valor multinivel.

   Distinto en la versión 3.5: El parámetro *legacy* solo escribe
   archivos ".pyc", no archivos ".pyo", no import cuál sea el valor de
   *optimize*.

   Distinto en la versión 3.7: Se agregó el parámetro
   *invalidation_mode*.

   Distinto en la versión 3.7.2: The *invalidation_mode* parameter's
   default value is updated to "None".

Para forzar la re-compilación del los archivos ".py" en el
subdirectorio "Lib/" y todos sus subdirectorios:

   import compileall

   compileall.compile_dir('Lib/', force=True)

   # Perform same compilation, excluding files in .svn directories.
   import re
   compileall.compile_dir('Lib/', rx=re.compile(r'[/\\][.]svn'), force=True)

   # pathlib.Path objects can also be used.
   import pathlib
   compileall.compile_dir(pathlib.Path('Lib/'), force=True)

Ver también:

  Módulo "py_compile"
     Compilación byte de un solo archivo fuente.
