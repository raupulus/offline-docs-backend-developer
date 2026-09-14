---
title: '"trace" --- Trace or track Python statement execution'
source_url: https://docs.python.org/es/3
source_path: library/trace.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4280
---

# "trace" --- Trace or track Python statement execution

**Código fuente:** Lib/trace.py

======================================================================

The "trace" module allows you to trace program execution, generate
annotated statement coverage listings, print caller/callee
relationships and list functions executed during a program run.  It
can be used in another program or from the command line.

Ver también:

  Coverage.py
     Una herramienta popular de terceros de cobertura que proporciona
     salida HTML junto con funciones avanzadas como cobertura de
     sucursales.

## Uso de la línea de comandos

The "trace" module can be invoked from the command line.  It can be as
simple as

   python -m trace --count -C . somefile.py ...

Lo anterior ejecutará "somefile.py" y generará listados anotados de
todos los módulos de Python importados durante la ejecución en el
directorio actual.

--help

   Muestra uso y sale.

--version

   Muestra la versión del módulo y sale.

Added in version 3.8: Added "--module" option that allows running an
executable module.

### Opciones principales

At least one of the following options must be specified when invoking
"trace".  The "--listfuncs" option is mutually exclusive with the "--
trace" and "--count" options. When "--listfuncs" is provided, neither
"--count" nor "--trace" are accepted, and vice versa.

-c, --count

   Genera un conjunto de archivos de lista anotados al finalizar el
   programa que muestra cuántas veces se ejecutó cada instrucción. Vea
   también "--coverdir", "--file" y "--no-report" a continuación.

-t, --trace

   Muestra las líneas a medida que se ejecutan.

-l, --listfuncs

   Muestra las funciones ejecutadas al ejecutar el programa.

-r, --report

   Genera una lista anotada de una ejecución del programa anterior que
   utilizó la opción "--count" y "--file". Esto no ejecuta ningún
   código.

-T, --trackcalls

   Muestra las relaciones de llamada expuestas al ejecutar el
   programa.

### Modificadores

-f, --file=<file>

   Nombre de un archivo para acumular recuentos durante varias
   ejecuciones de seguimiento. Debe usarse con la opción "--count".

-C, --coverdir=<dir>

   Directorio donde van los archivos del informe. El informe de
   cobertura para "paquete.modulo" se escribe en el archivo
   "*directorio*/*paquete*/*modulo*.cobertura".

-m, --missing

   Al generar listados anotados, marque las líneas que no se
   ejecutaron con ">>>>>>".

-s, --summary

   Cuando use "--count" o "--report", escriba un breve resumen en
   stdout para cada archivo procesado.

-R, --no-report

   No genera listados anotados. Esto es útil si tiene la intención de
   realizar varias ejecuciones con "--count", y luego producir un solo
   conjunto de listados anotados al final.

-g, --timing

   Prefija cada línea con la hora desde que se inició el programa.
   Solo se usa durante el rastreo.

### Filtros

Estas opciones pueden repetirse varias veces.

--ignore-module=<mod>

   Ignora cada uno de los nombres de módulo dados y sus submódulos (si
   es un paquete). El argumento puede ser una lista de nombres
   separados por una coma.

--ignore-dir=<dir>

   Ignora todos los módulos y paquetes en el directorio y
   subdirectorios nombrados. El argumento puede ser una lista de
   directorios separados por "os.pathsep".

## Interfaz programática

class trace.Trace(count=1, trace=1, countfuncs=0, countcallers=0, ignoremods=(), ignoredirs=(), infile=None, outfile=None, timing=False)

   Crea un objeto para rastrear la ejecución de una sola declaración o
   expresión. Todos los parámetros son opcionales. *count* habilita el
   conteo de números de línea. *trace* habilita el seguimiento de
   ejecución de línea. *countfuncs* habilita la lista de las funciones
   llamadas durante la ejecución. *countcallers* habilita el
   seguimiento de la relación de llamadas. *ignoremods* es una lista
   de módulos o paquetes para ignorar. *ignoredirs* es una lista de
   directorios cuyos módulos o paquetes deben ignorarse. *infile* es
   el nombre del archivo desde el cual leer la información de conteo
   almacenada. *outfile* es el nombre del archivo en el que se escribe
   la información de conteo actualizada. *timing* permite mostrar una
   marca de tiempo relativa al momento en que se inició el
   seguimiento.

   run(cmd)

      Ejecuta el comando y recopile estadísticas de la ejecución con
      los parámetros de seguimiento actuales. *cmd* debe ser una
      cadena o un objeto de código, adecuado para pasar a "exec()".

   runctx(cmd, globals=None, locals=None)

      Ejecuta el comando y recopile estadísticas de la ejecución con
      los parámetros de seguimiento actuales, en los entornos globales
      y locales definidos. Si no está definido, *globals* y *locals*
      por defecto son diccionarios vacíos.

   runfunc(func, /, *args, **kwds)

      Llama a *func* con los argumentos dados bajo el control del
      objeto "Trace" con los parámetros de rastreo actuales.

   results()

      Retorna un objeto "CoverageResults" que contiene los resultados
      acumulativos de todas las llamadas anteriores a "run", "runctx"
      y "runfunc" para la instancia dada "Trace". No restablece los
      resultados de seguimiento acumulados.

class trace.CoverageResults

   Un contenedor para los resultados de la cobertura, creado por
   "Trace.results()". No debe ser creado directamente por el usuario.

   update(other)

      Fusiona datos de otro objeto "CoverageResults".

   write_results(show_missing=True, summary=False, coverdir=None, *, ignore_missing_files=False)

      Escribe los resultados de la cobertura. Configure *show_missing*
      para mostrar las líneas que no tuvieron coincidencias.
      Configurar *summary* para incluir en la salida el resumen de
      cobertura por módulo. *coverdir* especifica el directorio en el
      que se enviarán los archivos de resultado de cobertura. Si es
      "None", los resultados de cada archivo fuente se colocan en su
      directorio.

      If *ignore_missing_files* is "True", coverage counts for files
      that no longer exist are silently ignored. Otherwise, a missing
      file will raise a "FileNotFoundError".

      Distinto en la versión 3.13: Added *ignore_missing_files*
      parameter.

Un ejemplo simple que demuestra el uso de la interfaz programática:

   import sys
   import trace

   # create a Trace object, telling it what to ignore, and whether to
   # do tracing or line-counting or both.
   tracer = trace.Trace(
       ignoredirs=[sys.prefix, sys.exec_prefix],
       trace=0,
       count=1)

   # run the new command using the given tracer
   tracer.run('main()')

   # make a report, placing output in the current directory
   r = tracer.results()
   r.write_results(show_missing=True, coverdir=".")
