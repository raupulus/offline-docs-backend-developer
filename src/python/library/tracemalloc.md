---
title: '"tracemalloc" --- Trace memory allocations'
source_url: https://docs.python.org/es/3
source_path: library/tracemalloc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4300
---

# "tracemalloc" --- Trace memory allocations

Added in version 3.4.

**Código fuente:** Lib/tracemalloc.py

======================================================================

El módulo tracemalloc es una herramienta de depuración para rastrear
los espacios de memoria asignados por Python. Este proporciona la
siguiente información:

* El rastreo al lugar de origen del objeto asignado

* Las estadísticas en los espacios de memoria asignados por nombre de
  archivo y por número de línea: tamaño total, número y tamaño
  promedio de los espacios de memoria asignados

* Calcula las diferencias entre dos informes instantáneos para
  detectar alguna filtración en la memoria

Para rastrear la mayoría de los espacios de memoria asignados por
Python; el módulo debe empezar tan pronto como sea posible
configurando la variable del entorno "PYTHONTRACEMALLOC" a "1", o
usando la opción del comando de línea "-X" "tracemalloc". La función
"tracemalloc.start()" puede ser llamada en tiempo de ejecución para
empezar a rastrear las asignaciones de memoria de Python.

Por defecto, el rastreo de un espacio de memoria asignado solo guarda
el cuadro mas reciente (1 cuadro). Para guardar 25 cuadros desde el
"PYTHONTRACEMALLOC`comienzo, configura la variable del entorno a
``25`", o usa "-X" "tracemalloc=25" en la opción de línea de comando.

## Ejemplos

### Mostrar los 10 principales

Mostrar los 10 archivos asignando la mayor cantidad de memoria:

   import tracemalloc

   tracemalloc.start()

   # ... run your application ...

   snapshot = tracemalloc.take_snapshot()
   top_stats = snapshot.statistics('lineno')

   print("[ Top 10 ]")
   for stat in top_stats[:10]:
       print(stat)

Ejemplo de la salida del conjunto de pruebas de Python:

   [ Top 10 ]
   <frozen importlib._bootstrap>:716: size=4855 KiB, count=39328, average=126 B
   <frozen importlib._bootstrap>:284: size=521 KiB, count=3199, average=167 B
   /usr/lib/python3.4/collections/__init__.py:368: size=244 KiB, count=2315, average=108 B
   /usr/lib/python3.4/unittest/case.py:381: size=185 KiB, count=779, average=243 B
   /usr/lib/python3.4/unittest/case.py:402: size=154 KiB, count=378, average=416 B
   /usr/lib/python3.4/abc.py:133: size=88.7 KiB, count=347, average=262 B
   <frozen importlib._bootstrap>:1446: size=70.4 KiB, count=911, average=79 B
   <frozen importlib._bootstrap>:1454: size=52.0 KiB, count=25, average=2131 B
   <string>:5: size=49.7 KiB, count=148, average=344 B
   /usr/lib/python3.4/sysconfig.py:411: size=48.0 KiB, count=1, average=48.0 KiB

Se puede ver que Python ha cargado "4855 KiB" de data (código de bytes
y constantes) desde los módulos y que el modulo "collections" asigno
"24KiB" para crear tipos "namedtuple".

Mira "Snapshot.statistics()" para más opciones.

### Calcula las diferencias

Toma dos capturas instantáneas y muestra las diferencias:

   import tracemalloc
   tracemalloc.start()
   # ... start your application ...

   snapshot1 = tracemalloc.take_snapshot()
   # ... call the function leaking memory ...
   snapshot2 = tracemalloc.take_snapshot()

   top_stats = snapshot2.compare_to(snapshot1, 'lineno')

   print("[ Top 10 differences ]")
   for stat in top_stats[:10]:
       print(stat)

Ejemplo de la salida antes y después de probar el conjunto de pruebas
de Python:

   [ Top 10 differences ]
   <frozen importlib._bootstrap>:716: size=8173 KiB (+4428 KiB), count=71332 (+39369), average=117 B
   /usr/lib/python3.4/linecache.py:127: size=940 KiB (+940 KiB), count=8106 (+8106), average=119 B
   /usr/lib/python3.4/unittest/case.py:571: size=298 KiB (+298 KiB), count=589 (+589), average=519 B
   <frozen importlib._bootstrap>:284: size=1005 KiB (+166 KiB), count=7423 (+1526), average=139 B
   /usr/lib/python3.4/mimetypes.py:217: size=112 KiB (+112 KiB), count=1334 (+1334), average=86 B
   /usr/lib/python3.4/http/server.py:848: size=96.0 KiB (+96.0 KiB), count=1 (+1), average=96.0 KiB
   /usr/lib/python3.4/inspect.py:1465: size=83.5 KiB (+83.5 KiB), count=109 (+109), average=784 B
   /usr/lib/python3.4/unittest/mock.py:491: size=77.7 KiB (+77.7 KiB), count=143 (+143), average=557 B
   /usr/lib/python3.4/urllib/parse.py:476: size=71.8 KiB (+71.8 KiB), count=969 (+969), average=76 B
   /usr/lib/python3.4/contextlib.py:38: size=67.2 KiB (+67.2 KiB), count=126 (+126), average=546 B

Se puede ver que Python cargó "8173 KiB" de información del modulo
(código de bytes y constantes), y que eso es "4428KiB" más de lo que
ha sido cargado antes de los test, cuando la anterior captura de
pantalla fue tomada. De manera similar, el modulo "linecache" ha
almacenado en caché "940 KiB" del código fuente de Python para
formatear los seguimientos, todo desde la captura instantánea.

Si el sistema tiene poca memoria libre, los informes instantáneos
pueden ser escritos en el disco usando el método "Snapshot.dump()"
para analizar el informe instantáneo offline. Después usa el método
"Snapshot.load()" para actualizar el informe.

### Consigue el seguimiento del bloque de memoria

Código para configurar el seguimiento del bloque de memoria más
grande:

   import tracemalloc

   # Store 25 frames
   tracemalloc.start(25)

   # ... run your application ...

   snapshot = tracemalloc.take_snapshot()
   top_stats = snapshot.statistics('traceback')

   # pick the biggest memory block
   stat = top_stats[0]
   print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
   for line in stat.traceback.format():
       print(line)

Ejemplo de la salida del conjunto de pruebas de Python (rastreo
limitado a 25 cuadros):

   903 memory blocks: 870.1 KiB
     File "<frozen importlib._bootstrap>", line 716
     File "<frozen importlib._bootstrap>", line 1036
     File "<frozen importlib._bootstrap>", line 934
     File "<frozen importlib._bootstrap>", line 1068
     File "<frozen importlib._bootstrap>", line 619
     File "<frozen importlib._bootstrap>", line 1581
     File "<frozen importlib._bootstrap>", line 1614
     File "/usr/lib/python3.4/doctest.py", line 101
       import pdb
     File "<frozen importlib._bootstrap>", line 284
     File "<frozen importlib._bootstrap>", line 938
     File "<frozen importlib._bootstrap>", line 1068
     File "<frozen importlib._bootstrap>", line 619
     File "<frozen importlib._bootstrap>", line 1581
     File "<frozen importlib._bootstrap>", line 1614
     File "/usr/lib/python3.4/test/support/__init__.py", line 1728
       import doctest
     File "/usr/lib/python3.4/test/test_pickletools.py", line 21
       support.run_doctest(pickletools)
     File "/usr/lib/python3.4/test/regrtest.py", line 1276
       test_runner()
     File "/usr/lib/python3.4/test/regrtest.py", line 976
       display_failure=not verbose)
     File "/usr/lib/python3.4/test/regrtest.py", line 761
       match_tests=ns.match_tests)
     File "/usr/lib/python3.4/test/regrtest.py", line 1563
       main()
     File "/usr/lib/python3.4/test/__main__.py", line 3
       regrtest.main_in_temp_cwd()
     File "/usr/lib/python3.4/runpy.py", line 73
       exec(code, run_globals)
     File "/usr/lib/python3.4/runpy.py", line 160
       "__main__", fname, loader, pkg_name)

Se puede ver que la mayor parte de la memoria fue asignada en el
módulo "importlib" para cargar datos (códigos de bytes y constantes)
desde módulos "870.1 KiB". El rastreo esta donde el módulo "importlib"
cargó datos más recientemente: en la linea "import pdb" el módulo
"doctest". El rastreo puede cambiar si se carga un nuevo módulo.

### "Los 10 más bonitos"

Codifica para configurar las 10 líneas que asignan gran parte de la
memoria con una salida "bonita", ignorando los archivos "<frozen
importlib._bootstrap>" y "<unkownn>":

   import linecache
   import os
   import tracemalloc

   def display_top(snapshot, key_type='lineno', limit=10):
       snapshot = snapshot.filter_traces((
           tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
           tracemalloc.Filter(False, "<unknown>"),
       ))
       top_stats = snapshot.statistics(key_type)

       print("Top %s lines" % limit)
       for index, stat in enumerate(top_stats[:limit], 1):
           frame = stat.traceback[0]
           print("#%s: %s:%s: %.1f KiB"
                 % (index, frame.filename, frame.lineno, stat.size / 1024))
           line = linecache.getline(frame.filename, frame.lineno).strip()
           if line:
               print('    %s' % line)

       other = top_stats[limit:]
       if other:
           size = sum(stat.size for stat in other)
           print("%s other: %.1f KiB" % (len(other), size / 1024))
       total = sum(stat.size for stat in top_stats)
       print("Total allocated size: %.1f KiB" % (total / 1024))

   tracemalloc.start()

   # ... run your application ...

   snapshot = tracemalloc.take_snapshot()
   display_top(snapshot)

Ejemplo de la salida del conjunto de pruebas de Python:

   Top 10 lines
   #1: Lib/base64.py:414: 419.8 KiB
       _b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]
   #2: Lib/base64.py:306: 419.8 KiB
       _a85chars2 = [(a + b) for a in _a85chars for b in _a85chars]
   #3: collections/__init__.py:368: 293.6 KiB
       exec(class_definition, namespace)
   #4: Lib/abc.py:133: 115.2 KiB
       cls = super().__new__(mcls, name, bases, namespace)
   #5: unittest/case.py:574: 103.1 KiB
       testMethod()
   #6: Lib/linecache.py:127: 95.4 KiB
       lines = fp.readlines()
   #7: urllib/parse.py:476: 71.8 KiB
       for a in _hexdig for b in _hexdig}
   #8: <string>:5: 62.0 KiB
   #9: Lib/_weakrefset.py:37: 60.0 KiB
       self.data = set()
   #10: Lib/base64.py:142: 59.8 KiB
       _b32tab2 = [a + b for a in _b32tab for b in _b32tab]
   6220 other: 3602.8 KiB
   Total allocated size: 5303.1 KiB

Mira "Snapshot.statistics()" para más opciones.

#### Graba los tamaños actual y máximo de todos los bloques de memoria rastreados

El siguiente código calcula dos sumas como "0 + 1 + 2 + ..." de forma
ineficiente, creando una lista con estos números. Esta lista consume
mucha memoria de forma temporal. Podemos usar "get_traced_memory()" y
"reset_peak()" para observar el pequeño uso de memoria después de que
la suma es calculada, así como también el uso máximo de memoria
durante el cálculo:

   import tracemalloc

   tracemalloc.start()

   # Example code: compute a sum with a large temporary list
   large_sum = sum(list(range(100000)))

   first_size, first_peak = tracemalloc.get_traced_memory()

   tracemalloc.reset_peak()

   # Example code: compute a sum with a small temporary list
   small_sum = sum(list(range(1000)))

   second_size, second_peak = tracemalloc.get_traced_memory()

   print(f"{first_size=}, {first_peak=}")
   print(f"{second_size=}, {second_peak=}")

Salida:

   first_size=664, first_peak=3592984
   second_size=804, second_peak=29704

El uso de "reset_peak()" asegura que podemos registrar precisamente el
uso máximo de memoria durante el cálculo de "small_sum", incluso si es
mucho menor al máximo total desde la llamada a "start()". Sin la
llamada a "reset_peak()", "second_peak" seguiría siendo el uso máximo
de memoria del cálculo de "large_sum" (es decir, igual a
"first_peak"). En este caso ambos máximos son mucho mayores al uso
final de memoria, lo que sugiere que podemos optimizar (removiendo la
llamada innecesaria a "list", y escribiendo "sum(range(...))").

## API

### Funciones

tracemalloc.clear_traces()

   Limpia los rastros de los bloques de memoria asignados por Python.

   Mira también la función "stop()".

tracemalloc.get_object_traceback(obj)

   Get the traceback where the Python object *obj* was allocated.
   Return a "Traceback" instance, or "None" if the "tracemalloc"
   module is not tracing memory allocations or did not trace the
   allocation of the object.

   Mira también las funciones "gc.get_referrers()" y
   "sys.getsizeof()".

tracemalloc.get_traceback_limit()

   Obtiene el número máximo de cuadros guardados en el seguimiento de
   un rastro.

   The "tracemalloc" module must be tracing memory allocations to get
   the limit, otherwise an exception is raised.

   El limite es establecido por la función "start()".

tracemalloc.get_traced_memory()

   Get the current size and peak size of memory blocks traced by the
   "tracemalloc" module as a tuple: "(current: int, peak: int)".

tracemalloc.reset_peak()

   Set the peak size of memory blocks traced by the "tracemalloc"
   module to the current size.

   Do nothing if the "tracemalloc" module is not tracing memory
   allocations.

   Esta función sólo modifica el valor guardado para el uso máximo de
   memoria, y no modifica o borra ningún rastreo, no como
   "clear_traces()". Capturas tomadas con "take_snapshot()" antes de
   una llamada a "reset_peak()" pueden ser comparadas
   significativamente con capturas hechas después de la llamada.

   Mira también la función "get_traced_memory()".

   Added in version 3.9.

tracemalloc.get_tracemalloc_memory()

   Get the memory usage in bytes of the "tracemalloc" module used to
   store traces of memory blocks. Return an "int".

tracemalloc.is_tracing()

   "True" if the "tracemalloc" module is tracing Python memory
   allocations, "False" otherwise.

   También mira las funciones "start()" y "stop()".

tracemalloc.start(nframe: int = 1)

   Empieza a rastrear las asignaciones de memoria de Python: instala
   *hooks* en las asignaciones de memoria de Python. Los rastreos
   coleccionados van a estar limitados a *nframe*. Por defecto, un
   rastro de un bloque de memoria solo guarda el cuadro mas reciente:
   el limite es "1". *nframe* debe ser mayor o igual a *1*.

   El número original de cuadros totales que componen el seguimiento
   observando el atributo "Traceback.total_nframe".

   Guardar mas de "1" cuadro es solo útil para calcular estadísticas
   agrupadas por seguimiento o para calcular estadísticas acumulativa:
   mira las funciones "Snapshot.compare_to()" y
   "Snapshot.statistics()".

   Storing more frames increases the memory and CPU overhead of the
   "tracemalloc" module. Use the "get_tracemalloc_memory()" function
   to measure how much memory is used by the "tracemalloc" module.

   La variable del entorno "PYTHONTRACEMALLOC"
   ("PYTHONTRACEMALLOC=NFRAME") y la opción de comando de linea "-X"
   "tracemalloc=NFRAME" se puede usar para empezar a rastrear desde el
   inicio.

   También mira las funciones "stop()", "is_tracing()" y
   "get_traceback_limit()".

tracemalloc.stop()

   Detiene el rastreo de las asignaciones de memoria de Python:
   desinstala los *hooks*. También limpia todos los rastros de memoria
   recolectados acerca de los bloques de memoria asignados por Python.

   Llama a la función "take_snapshot()" para tomar una captura
   instantánea de los rastreos, antes de limpiarlos.

   También mira las funciones "start()", "is_tracing()" y
   "clear_traces()".

tracemalloc.take_snapshot()

   Toma una captura instantánea de los bloques de memoria asignados
   por Python. Retorna una nueva instancia de la clase "Snapshot".

   The snapshot does not include memory blocks allocated before the
   "tracemalloc" module started to trace memory allocations.

   Los seguimientos de los rastros son limitados por la función
   "get_traceback_limit()". Usa el parámetro *nframe* de la función
   "start()" para guardar mas cuadros.

   The "tracemalloc" module must be tracing memory allocations to take
   a snapshot, see the "start()" function.

   También mira la función "get_object_traceback()".

### Filtro de dominio

class tracemalloc.DomainFilter(inclusive: bool, domain: int)

   Filtra los rastros de los bloques de memoria por su espacio de
   dirección (dominio).

   Added in version 3.6.

   inclusive

      Si *inclusive* es "True" (incluye), relaciona los bloques de
      memoria asignados en el espacio de dirección "domain".

      Si *inclusive* es "False" (excluye), relaciona los bloques de
      memoria no asignados en el espacio de dirección "domain".

   domain

      Espacio de dirección de un bloque de memoria ("int"). Propiedad
      solo-lectura.

### Filtro

class tracemalloc.Filter(inclusive: bool, filename_pattern: str, lineno: int = None, all_frames: bool = False, domain: int = None)

   Filtra los rastros de los bloques de memoria.

   También mira la función "fnmatch.fnmatch()" para la sintaxis de
   *filename_pattern*. La extensión "'.pyc'" es remplazada por
   "'.py'".

   Ejemplos:

   * "Filter(True, subprocess.__file__)" solo incluye los rastros de
     el módulo "subprocess"

   * "Filter(False, tracemalloc.__file__)" excludes traces of the
     "tracemalloc" module

   * "Filter(False, "<unknown>")" excluye los seguimientos vacíos

   Distinto en la versión 3.5: La extensión "'.pyo'" ya no se remplaza
   con "'.py'".

   Distinto en la versión 3.6: Agregado el atributo "domain" .

   domain

      El espacio de dirección de un bloque de memoria ("int" o
      "None").

      tracemalloc usa el dominio "0" para rastrear las asignaciones de
      memoria hechas por Python. Las extensiones C pueden usar otros
      dominios para rastrear otros recursos.

   inclusive

      Si *inclusive* es "True" (incluye), solo relaciona los bloques
      de memoria asignados en un archivo con el nombre coincidiendo
      con el atributo "filename_pattern" en el número de línea del
      atributo "lineno".

      Si *inclusive* es "False" (excluye), ignora los bloques de
      memoria asignados en un archivo con el nombre coincidiendo con
      el atributo "filename_pattern" en el número de línea del
      atributo "lineno".

   lineno

      El número de linea ("int") del filtro. Si *lineno* es "None", el
      filtro se relaciona con cualquier número de linea.

   filename_pattern

      El patrón del nombre de archivo del filtro ("str"). Propiedad
      solo-lectura.

   all_frames

      Si *all_frames* es "True", todos los cuadros de los rastreos son
      chequeados. Si *all_frames* es "False", solo el cuadro mas
      reciente es chequeado.

      El atributo no tiene efecto si el limite de rastreo es "1".
      Mira la función "get_traceback_limit()" y el atributo
      "Snapshot.traceback_limit".

### Cuadro

class tracemalloc.Frame

   Cuadro de un rastreo.

   La clase "Traceback" es una secuencia de las instancias de la clase
   "Frame".

   filename

      Nombre de archivo ("str").

   lineno

      Número de línea ("int").

### Captura instantánea

class tracemalloc.Snapshot

   Captura instantánea de los rastros de los bloques de memoria
   asignados por Python.

   La función "take_snapshot()" crea una instancia de captura
   instantánea.

   compare_to(old_snapshot: Snapshot, key_type: str, cumulative: bool = False)

      Calcula las diferencias con una vieja captura instantánea.
      Obtiene las estadísticas en una lista ordenada de instancias de
      la clase "StatisticDiff" agrupadas por *key_type*.

      Mira el método "Snapshot.statistics()" para los parámetros
      *key_type* y *cumulative*.

      El resultado esta guardado desde el más grande al más pequeño
      por los valores absolutos de "StatisticDiff.size_diff()",
      "StatisticDiff.size()", el valor absoluto de
      "StatisticDiff.count_diff()", "Statistic.count()" y después por
      el atributo "StatisticDiff.traceback()".

   dump(filename)

      Escribe la captura instantánea en un archivo.

      Usa el método "load()" para recargar la captura instantánea.

   filter_traces(filters)

      Crea una nueva instancia de clase "Snapshot" con una secuencia
      de "traces" filtrados, *filters* es una lista de las instancias
      de "DomainFilter" y "Filter".  Si *filters* es una lista vacía,
      retorna una nueva instancia de clase "Snapshot" con una copia de
      los rastreos.

      Los filtros "todo incluido" se aplican de a uno, si los filtros
      no incluidos coinciden. Si al menos un filtro exclusivo
      coincide, se ignora un rastro.

      Distinto en la versión 3.6: Las instancias de clase
      "DomainFilter" ahora también son aceptadas en *filters*.

   classmethod load(filename)

      Carga la captura instantánea desde un archivo.

      También mira el método "dump()".

   statistics(key_type: str, cumulative: bool = False)

      Obtiene estadísticas como una lista ordenada, de instancias de
      "Statistic" agrupadas por *key_type*:

      +-----------------------+--------------------------+
      | key_type              | descripción              |
      |=======================|==========================|
      | "'filename'"          | nombre del archivo       |
      +-----------------------+--------------------------+
      | "'lineno'"            | nombre del archivo y     |
      |                       | número de línea          |
      +-----------------------+--------------------------+
      | "'traceback'"         | seguimiento              |
      +-----------------------+--------------------------+

      If *cumulative* is "True", cumulate size and count of memory
      blocks of all frames of the traceback of a trace, not only the
      most recent frame. The cumulative mode can only be used with
      *key_type* equal to "'filename'" and "'lineno'".

      El resultado se organiza desde el más grande hasta el más
      pequeño por el atributo "Statistic.size", "Statistic.count" y
      después por "Statistic.traceback".

   traceback_limit

      El número máximo de cuadros organizados en el rastreo del
      atributo "traces": resulta de la función "get_traceback_limit"
      cuando la captura instantánea fue tomada.

   traces

      Rastros de todos los bloques de memoria asignados por Python:
      secuencia de instancias de "Trace".

      La secuencia tiene un orden que no esta definido. Usa el método
      "Snapshot.statistics()" para obtener una lista ordenada de
      estadísticas.

### Estadística

class tracemalloc.Statistic

   Estadística de las asignaciones de memoria.

   "Snapshot.statistics()" retorna una lista de instancias de la clase
   "Statistic".

   También mira la clase "StatisticDiff".

   count

      Número de bloques de memoria ("int").

   size

      El tamaño total de los bloques de memoria en bytes ("int").

   traceback

      Rastrea donde un bloque de memoria fue asignado, la instancia de
      la clase "Traceback".

### StatisticDiff

class tracemalloc.StatisticDiff

   La diferencia de estadística en las asignaciones de memoria entre
   una vieja y una nueva instancia de clase "Snapshot".

   "Snapshot.compare_to()" retorna una lista de instancias de la clase
   "StatisticDiff". Mira también la clase "Statistic".

   count

      El número de bloques de memoria en la nueva captura de pantalla
      ("int"): "0" si los bloques de memoria han sido liberados en la
      nueva captura instantánea.

   count_diff

      La diferencia de los números de los bloques de memoria entre las
      capturas viejas y nuevas ("int"): "0" si el bloque de memoria ha
      sido asignado en la nueva captura instantánea.

   size

      El tamaño total de los bloques de memoria en bytes en la nueva
      captura instantánea ("int"): "0" si el bloque de memoria ha sido
      liberado en la nueva captura instantánea.

   size_diff

      La diferencia de el tamaño total de un bloque de memoria en
      bytes entre las capturas instantáneas viejas y nuevas ("int"):
      "0" si el bloque de memoria ha sido asignado en la nueva captura
      instantánea.

   traceback

      Rastrea donde los bloques de memoria han sido asignados,
      instancia de la clase "Traceback".

### Rastro

class tracemalloc.Trace

   Rastro de un bloque de memoria.

   El atributo "Snapshot.traces" es una secuencia de las instancias de
   la clase "Trace".

   Distinto en la versión 3.6: Agregado el atributo "domain" .

   domain

      Espacio de dirección de un bloque de memoria ("int"). Propiedad
      solo-lectura.

      tracemalloc usa el dominio "0" para rastrear las asignaciones de
      memoria hechas por Python. Las extensiones C pueden usar otros
      dominios para rastrear otros recursos.

   size

      Tamaño de un bloque de memoria en bytes ("int").

   traceback

      Rastrea donde un bloque de memoria fue asignado, la instancia de
      la clase "Traceback".

### Seguimiento

class tracemalloc.Traceback

   La secuencia de las instancias de la clase "Frame" organizadas
   desde el cuadro mas antiguo al más reciente.

   Un seguimiento contiene por lo menos "1" cuadro. Si el módulo
   "tracemalloc" falla al traer un cuadro, se usa el nombre del
   archivo ""<unknown>"" en el número de linea "0".

   When a snapshot is taken, tracebacks of traces are limited to
   "get_traceback_limit()" frames. See the "take_snapshot()" function.
   The original number of frames of the traceback is stored in the
   "Traceback.total_nframe" attribute. That allows one to know if a
   traceback has been truncated by the traceback limit.

   The "Trace.traceback" attribute is a "Traceback" instance.

   Distinto en la versión 3.7: Los cuadros están organizados desde el
   mas antiguo hasta el más reciente, en vez de el más reciente al más
   antiguo.

   total_nframe

      Número total de cuadros que componen el seguimiento antes de ser
      truncado. Este atributo puede ser "None" si no hay información
      disponible.

   Distinto en la versión 3.9: El atributo "Traceback.total_nframe"
   fue añadido.

   format(limit=None, most_recent_first=False)

      Formatea el seguimiento como una lista de líneas. Usa el módulo
      "linecache" para recuperar líneas del código fuente. Si se
      configura el límite, formatea los cuadros más recientes de los
      límites, si límite es positivo. De otra manera, formatea los
      cuadros más antiguos de "abs(limit)". Si *most_recent_first* es
      "True", se invierte el orden de los cuadros formateados,
      devolviendo el cuadro más reciente en lugar del último.

      Similar a la función "traceback.format_tb()", excepto por el
      método "format()" que no incluye nuevas líneas.

      Ejemplo:

         print("Traceback (most recent call first):")
         for line in traceback:
             print(line)

      Salida:

         Traceback (most recent call first):
           File "test.py", line 9
             obj = Object()
           File "test.py", line 12
             tb = tracemalloc.get_object_traceback(f())
