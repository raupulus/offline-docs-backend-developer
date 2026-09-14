---
title: 11. Brief tour of the standard library --- part II
source_url: https://docs.python.org/es/3
source_path: tutorial/stdlib2.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 5000
---

# 11. Brief tour of the standard library --- part II

Este segundo paseo cubre módulos más avanzados que facilitan
necesidades de programación complejas.  Estos módulos raramente se
usan en scripts cortos.

## 11.1. Output formatting

El módulo "reprlib" provee una versión de "repr()" ajustada para
mostrar contenedores grandes o profundamente anidados, en forma
abreviada:

   >>> import reprlib
   >>> reprlib.repr(set('supercalifragilisticexpialidocious'))
   "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

El módulo "pprint" ofrece un control más sofisticado de la forma en
que se imprimen tanto los objetos predefinidos como los objetos
definidos por el usuario, de manera que sean legibles por el
intérprete. Cuando el resultado ocupa más de una línea, el generador
de "impresiones lindas" agrega saltos de línea y sangrías para mostrar
la estructura de los datos más claramente:

   >>> import pprint
   >>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
   ...     'yellow'], 'blue']]]
   ...
   >>> pprint.pprint(t, width=30)
   [[[['black', 'cyan'],
      'white',
      ['green', 'red']],
     [['magenta', 'yellow'],
      'blue']]]

El módulo "textwrap" formatea párrafos de texto para que quepan dentro
de cierto ancho de pantalla:

   >>> import textwrap
   >>> doc = """The wrap() method is just like fill() except that it returns
   ... a list of strings instead of one big string with newlines to separate
   ... the wrapped lines."""
   ...
   >>> print(textwrap.fill(doc, width=40))
   The wrap() method is just like fill()
   except that it returns a list of strings
   instead of one big string with newlines
   to separate the wrapped lines.

El módulo "locale" accede a una base de datos de formatos específicos
a una cultura.  El atributo *grouping* de la función *format* permite
una forma directa de formatear números con separadores de grupo:

   >>> import locale
   >>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
   'English_United States.1252'
   >>> conv = locale.localeconv()          # get a mapping of conventions
   >>> x = 1234567.8
   >>> locale.format_string("%d", x, grouping=True)
   '1,234,567'
   >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
   ...                      conv['frac_digits'], x), grouping=True)
   '$1,234,567.80'

## 11.2. Plantillas

El módulo "string" incluye una clase versátil "Template" (plantilla)
con una sintaxis simplificada apta para ser editada por usuarios
finales.  Esto permite que los usuarios personalicen sus aplicaciones
sin necesidad de modificar la aplicación en sí.

El formato usa marcadores cuyos nombres se forman con "$" seguido de
identificadores Python válidos (caracteres alfanuméricos y guión de
subrayado). Si se los encierra entre llaves, pueden seguir más
caracteres alfanuméricos sin necesidad de dejar espacios en blanco.
"$$" genera un "$":

   >>> from string import Template
   >>> t = Template('${village}folk send $$10 to $cause.')
   >>> t.substitute(village='Nottingham', cause='the ditch fund')
   'Nottinghamfolk send $10 to the ditch fund.'

El método "substitute()" lanza "KeyError" cuando no se suministra
ningún valor para un marcador mediante un diccionario o argumento por
nombre.  Para algunas aplicaciones los datos suministrados por el
usuario puede ser incompletos, y el método "safe_substitute()" puede
ser más apropiado: deja los marcadores inalterados cuando falten
datos:

   >>> t = Template('Return the $item to $owner.')
   >>> d = dict(item='unladen swallow')
   >>> t.substitute(d)
   Traceback (most recent call last):
     ...
   KeyError: 'owner'
   >>> t.safe_substitute(d)
   'Return the unladen swallow to $owner.'

Las subclases de *Template* pueden especificar un delimitador propio.
Por ejemplo, una utilidad de renombrado por lotes para una galería de
fotos puede escoger usar signos de porcentaje para los marcadores
tales como la fecha actual, el número de secuencia de la imagen, o el
formato de archivo:

   >>> import time, os.path
   >>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
   >>> class BatchRename(Template):
   ...     delimiter = '%'
   ...
   >>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
   Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

   >>> t = BatchRename(fmt)
   >>> date = time.strftime('%d%b%y')
   >>> for i, filename in enumerate(photofiles):
   ...     base, ext = os.path.splitext(filename)
   ...     newname = t.substitute(d=date, n=i, f=ext)
   ...     print('{0} --> {1}'.format(filename, newname))

   img_1074.jpg --> Ashley_0.jpg
   img_1076.jpg --> Ashley_1.jpg
   img_1077.jpg --> Ashley_2.jpg

Las plantillas también pueden ser usadas para separar la lógica del
programa de los detalles de múltiples formatos de salida.  Esto
permite sustituir plantillas específicas para archivos XML, reportes
en texto plano, y reportes web en HTML.

## 11.3. Working with binary data record layouts

El módulo "struct" provee las funciones "pack()" y "unpack()" para
trabajar con formatos de registros binarios de longitud variable.  El
siguiente ejemplo muestra cómo recorrer la información de encabezado
en un archivo ZIP sin usar el módulo "zipfile".  Los códigos ""H"" e
""I"" representan números sin signo de dos y cuatro bytes
respectivamente.  El ""<"" indica que son de tamaño estándar y los
bytes tienen ordenamiento *little-endian*:

   import struct

   with open('myfile.zip', 'rb') as f:
       data = f.read()

   start = 0
   for i in range(3):                      # show the first 3 file headers
       start += 14
       fields = struct.unpack('<IIIHH', data[start:start+16])
       crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

       start += 16
       filename = data[start:start+filenamesize]
       start += filenamesize
       extra = data[start:start+extra_size]
       print(filename, hex(crc32), comp_size, uncomp_size)

       start += extra_size + comp_size     # skip to the next header

## 11.4. Multi-hilos

La técnica de multi-hilos (o *multi-threading*) permite desacoplar
tareas que no tienen dependencia secuencial.  Los hilos se pueden usar
para mejorar el grado de reacción de las aplicaciones que aceptan
entradas del usuario mientras otras tareas se ejecutan en segundo
plano.  Un caso de uso relacionado es ejecutar E/S en paralelo con
cálculos en otro hilo.

El código siguiente muestra cómo el módulo de alto nivel "threading"
puede ejecutar tareas en segundo plano mientras el programa principal
continúa su ejecución:

   import threading, zipfile

   class AsyncZip(threading.Thread):
       def __init__(self, infile, outfile):
           super().__init__()
           self.infile = infile
           self.outfile = outfile

       def run(self):
           with zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED) as f:
               f.write(self.infile)
           print('Finished background zip of:', self.infile)

   background = AsyncZip('mydata.txt', 'myarchive.zip')
   background.start()
   print('The main program continues to run in foreground.')

   background.join()    # Wait for the background task to finish
   print('Main program waited until background was done.')

El desafío principal de las aplicaciones multi-hilo es la coordinación
entre los hilos que comparten datos u otros recursos.  A ese fin, el
módulo *threading* provee una serie de primitivas de sincronización
que incluyen bloqueos, eventos, variables de condición, y semáforos.

Aún cuando esas herramientas son poderosas, pequeños errores de diseño
pueden resultar en problemas difíciles de reproducir.  La forma
preferida de coordinar tareas es concentrar todos los accesos a un
recurso en un único hilo y después usar el módulo "queue" para
alimentar dicho hilo con pedidos desde otros hilos.  Las aplicaciones
que usan objetos "Queue" para comunicación y coordinación entre hilos
son más fáciles de diseñar, más legibles, y más confiables.

## 11.5. Registrando

El módulo "logging" ofrece un sistema de registros (*logs*) completo y
flexible.  En su forma más simple, los mensajes de registro se envían
a un archivo o a "sys.stderr":

   import logging
   logging.debug('Debugging information')
   logging.info('Informational message')
   logging.warning('Warning:config file %s not found', 'server.conf')
   logging.error('Error occurred')
   logging.critical('Critical error -- shutting down')

Ésta es la salida obtenida:

   WARNING:root:Warning:config file server.conf not found
   ERROR:root:Error occurred
   CRITICAL:root:Critical error -- shutting down

De forma predeterminada, los mensajes de depuración e informativos se
suprimen, y la salida se envía al error estándar.  Otras opciones de
salida incluyen mensajes de enrutamiento a través de correo
electrónico, datagramas, sockets, o un servidor HTTP.  Nuevos filtros
pueden seleccionar diferentes rutas basadas en la prioridad del
mensaje: "DEBUG", "INFO", "WARNING", "ERROR", y "CRITICAL"
(Depuración, Informativo, Atención, Error y Crítico respectivamente)

El sistema de registro puede configurarse directamente desde Python o
puede cargarse la configuración desde un archivo modificable por el
usuario para personalizar el registro sin alterar la aplicación.

## 11.6. Weak references

Python realiza administración de memoria automática (cuenta de
referencias para la mayoría de los objetos, y *garbage collection*
para eliminar ciclos).  La memoria se libera poco después de que la
última referencia a la misma haya sido eliminada.

Este enfoque funciona bien para la mayoría de las aplicaciones pero de
vez en cuando existe la necesidad de controlar objetos sólo mientras
estén siendo utilizados por otra cosa. Desafortunadamente, el sólo
hecho de controlarlos crea una referencia que los convierte en
permanentes. El módulo "weakref" provee herramientas para controlar
objetos sin crear una referencia. Cuando el objeto no se necesita mas,
es removido automáticamente de una tabla de referencias débiles y se
dispara una *callback* para objetos *weakref*. Comúnmente las
aplicaciones incluyen cacheo de objetos que son costosos de crear:

   >>> import weakref, gc
   >>> class A:
   ...     def __init__(self, value):
   ...         self.value = value
   ...     def __repr__(self):
   ...         return str(self.value)
   ...
   >>> a = A(10)                   # create a reference
   >>> d = weakref.WeakValueDictionary()
   >>> d['primary'] = a            # does not create a reference
   >>> d['primary']                # fetch the object if it is still alive
   10
   >>> del a                       # remove the one reference
   >>> gc.collect()                # run garbage collection right away
   0
   >>> d['primary']                # entry was automatically removed
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       d['primary']                # entry was automatically removed
     File "C:/python314/lib/weakref.py", line 46, in __getitem__
       o = self.data[key]()
   KeyError: 'primary'

## 11.7. Tools for working with lists

Muchas necesidades de estructuras de datos pueden ser satisfechas con
el tipo integrado lista.  Sin embargo, a veces se hacen necesarias
implementaciones alternativas con rendimientos distintos.

The "array" module provides an "array" object that is like a list that
stores only homogeneous data and stores it more compactly.  The
following example shows an array of numbers stored as two byte
unsigned binary numbers (typecode ""H"") rather than the usual 16
bytes per entry for regular lists of Python int objects:

   >>> from array import array
   >>> a = array('H', [4000, 10, 700, 22222])
   >>> sum(a)
   26932
   >>> a[1:3]
   array('H', [10, 700])

The "collections" module provides a "deque" object that is like a list
with faster appends and pops from the left side but slower lookups in
the middle. These objects are well suited for implementing queues and
breadth first tree searches:

   >>> from collections import deque
   >>> d = deque(["task1", "task2", "task3"])
   >>> d.append("task4")
   >>> print("Handling", d.popleft())
   Handling task1

   unsearched = deque([starting_node])
   def breadth_first_search(unsearched):
       node = unsearched.popleft()
       for m in gen_moves(node):
           if is_goal(m):
               return m
           unsearched.append(m)

Además de las implementaciones alternativas de listas, la biblioteca
ofrece otras herramientas como el módulo "bisect" con funciones para
manipular listas ordenadas:

   >>> import bisect
   >>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
   >>> bisect.insort(scores, (300, 'ruby'))
   >>> scores
   [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

El módulo "heapq" provee funciones para implementar pilas (*heaps*)
basados en listas comunes.  El menor valor ingresado se mantiene en la
posición cero. Esto es útil para aplicaciones que acceden a menudo al
elemento más chico pero no quieren hacer un orden completo de la
lista:

   >>> from heapq import heapify, heappop, heappush
   >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   >>> heapify(data)                      # rearrange the list into heap order
   >>> heappush(data, -5)                 # add a new entry
   >>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
   [-5, 0, 1]

## 11.8. Decimal floating-point arithmetic

The "decimal" module offers a "Decimal" datatype for decimal floating-
point arithmetic.  Compared to the built-in "float" implementation of
binary floating point, the class is especially helpful for

* aplicaciones financieras y otros usos que requieren representación
  decimal exacta,

* control sobre la precisión,

* control sobre el redondeo para cumplir requisitos legales,

* seguimiento de dígitos decimales significativos, o

* aplicaciones donde el usuario espera que los resultados coincidan
  con cálculos hecho a mano.

Por ejemplo, calcular un impuesto del 5% de una tarifa telefónica de
70 centavos da resultados distintos con punto flotante decimal y punto
flotante binario. La diferencia se vuelve significativa si los
resultados se redondean al centavo más próximo:

   >>> from decimal import *
   >>> round(Decimal('0.70') * Decimal('1.05'), 2)
   Decimal('0.74')
   >>> round(.70 * 1.05, 2)
   0.73

El resultado con "Decimal" conserva un cero al final, calculando
automáticamente cuatro cifras significativas a partir de los
multiplicandos con dos cifras significativas.  Decimal reproduce la
matemática como se la hace a mano, y evita problemas que pueden surgir
cuando el punto flotante binario no puede representar exactamente
cantidades decimales.

La representación exacta permite a la clase "Decimal" hacer cálculos
de modulo y pruebas de igualdad que son inadecuadas para punto
flotante binario:

   >>> Decimal('1.00') % Decimal('.10')
   Decimal('0.00')
   >>> 1.00 % 0.10
   0.09999999999999995

   >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
   True
   >>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
   False

El módulo "decimal" provee aritmética con tanta precisión como haga
falta:

   >>> getcontext().prec = 36
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857')
