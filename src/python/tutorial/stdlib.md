---
title: 10. Brief tour of the standard library
source_url: https://docs.python.org/es/3
source_path: tutorial/stdlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: tutorial
order: 4990
---

# 10. Brief tour of the standard library

## 10.1. Operating system interface

El módulo "os" proporciona docenas de funciones para interactuar con
el sistema operativo:

   >>> import os
   >>> os.getcwd()      # Return the current working directory
   'C:\\Python314'
   >>> os.chdir('/server/accesslogs')   # Change current working directory
   >>> os.system('mkdir today')   # Run the command mkdir in the system shell
   0

Asegúrate de utilizar el estilo "import os" en lugar de "from os
import *". Esto evitará que "os.open()" oculte la función integrada
"open()", que funciona de manera muy diferente.

Las funciones integradas "dir()" y "help()" son útiles como ayudas
interactivas para trabajar con módulos grandes como "os":

   >>> import os
   >>> dir(os)
   <returns a list of all module functions>
   >>> help(os)
   <returns an extensive manual page created from the module's docstrings>

Para las tareas diarias de administración de archivos y directorios,
el módulo "shutil" proporciona una interfaz en un nivel superior que
es más fácil de usar:

   >>> import shutil
   >>> shutil.copyfile('data.db', 'archive.db')
   'archive.db'
   >>> shutil.move('/build/executables', 'installdir')
   'installdir'

## 10.2. File wildcards

El módulo "glob" proporciona una función para hacer listas de archivos
a partir de búsquedas con comodines en directorios:

   >>> import glob
   >>> glob.glob('*.py')
   ['primes.py', 'random.py', 'quote.py']

## 10.3. Command-line arguments

Los programas frecuentemente necesitan procesar argumentos de linea de
comandos. Estos argumentos se almacenan en el atributo *argv* del
módulo "sys" como una lista.   Por ejemplo, consideremos el siguiente
archivo :file: 'demo.py':

   # File demo.py
   import sys
   print(sys.argv)

Este es el resultado de ejecutar "python demo.py one two three" en la
línea de comandos:

   ['demo.py', 'one', 'two', 'three']

El modulo "argparse" provee un mecanismo más sofisticado para procesar
argumentos recibidos vía línea de comandos. El siguiente *script*
extrae uno o más nombres de archivos y un número opcional de líneas
para mostrar:

   import argparse

   parser = argparse.ArgumentParser(
       prog='top',
       description='Show top lines from each file')
   parser.add_argument('filenames', nargs='+')
   parser.add_argument('-l', '--lines', type=int, default=10)
   args = parser.parse_args()
   print(args)

Cuando se ejecuta en la línea de comandos con "python top.py --lines=5
alpha.txt beta.txt", el *script* establece "args.lines" a "5" y
"args.filenames" a "['alpha.txt', 'beta.txt']".

## 10.4. Error output redirection and program termination

El módulo "sys" también tiene sus atributos para *stdin*, *stdout*, y
*stderr*.  Este último es útil para emitir mensajes de alerta y error
para que se vean incluso cuando se haya redirigido *stdout*:

   >>> sys.stderr.write('Warning, log file not found starting a new one\n')
   Warning, log file not found starting a new one

La forma más directa de terminar un programa es usar "sys.exit()".

## 10.5. String pattern matching

El módulo "re" provee herramientas de expresiones regulares para un
procesamiento avanzado de cadenas.  Para manipulación y coincidencias
complejas, las expresiones regulares ofrecen soluciones concisas y
optimizadas:

   >>> import re
   >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
   ['foot', 'fell', 'fastest']
   >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
   'cat in the hat'

Cuando sólo se necesitan funciones sencillas, se prefieren los métodos
de cadenas porque son más fáciles de leer y depurar:

   >>> 'tea for too'.replace('too', 'two')
   'tea for two'

## 10.6. Matemáticas

The "math" module gives access to the underlying C library functions
for floating-point math:

   >>> import math
   >>> math.cos(math.pi / 4)
   0.70710678118654757
   >>> math.log(1024, 2)
   10.0

El módulo "random" provee herramientas para realizar selecciones
aleatorias:

   >>> import random
   >>> random.choice(['apple', 'pear', 'banana'])
   'apple'
   >>> random.sample(range(100), 10)   # sampling without replacement
   [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
   >>> random.random()    # random float from the interval [0.0, 1.0)
   0.17970987693706186
   >>> random.randrange(6)    # random integer chosen from range(6)
   4

El módulo "statistics" calcula propiedades de estadística básica (la
media, mediana, varianza, etc) de datos numéricos:

   >>> import statistics
   >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
   >>> statistics.mean(data)
   1.6071428571428572
   >>> statistics.median(data)
   1.25
   >>> statistics.variance(data)
   1.3720238095238095

El proyecto SciPy <https://scipy.org> tiene muchos otros módulos para
cálculos numéricos.

## 10.7. Internet access

Hay varios módulos para acceder a Internet y procesar sus protocolos.
Dos de los más simples son "urllib.request" para traer data de URLs y
"smtplib" para enviar correos:

   >>> from urllib.request import urlopen
   >>> with urlopen('https://docs.python.org/3/') as response:
   ...     for line in response:
   ...         line = line.decode()             # Convert bytes to a str
   ...         if 'updated' in line:
   ...             print(line.rstrip())         # Remove trailing newline
   ...
         Last updated on Nov 11, 2025 (20:11 UTC).

   >>> import smtplib
   >>> server = smtplib.SMTP('localhost')
   >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
   ... """To: jcaesar@example.org
   ... From: soothsayer@example.org
   ...
   ... Beware the Ides of March.
   ... """)
   >>> server.quit()

(Nota que el segundo ejemplo necesita un servidor de correo corriendo
en la máquina local)

## 10.8. Dates and times

El módulo "datetime" ofrece clases para gestionar fechas y tiempos
tanto de manera simple como compleja.  Aunque soporta aritmética sobre
fechas y tiempos, la aplicación se centra en la extracción eficiente
de elementos para el formateo y la manipulación de los datos de
salida.  El módulo también admite objetos que tienen en cuenta la zona
horaria.

   >>> # dates are easily constructed and formatted
   >>> import datetime as dt
   >>> now = dt.date.today()
   >>> now
   datetime.date(2003, 12, 2)
   >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
   '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

   >>> # dates support calendar arithmetic
   >>> birthday = dt.date(1964, 7, 31)
   >>> age = now - birthday
   >>> age.days
   14368

## 10.9. Data compression

Los módulos admiten directamente los formatos más comunes de archivo y
compresión de datos, entre ellos : "zlib", "gzip", "bz2", "lzma",
"zipfile" y "tarfile".

   >>> import zlib
   >>> s = b'witch which has which witches wrist watch'
   >>> len(s)
   41
   >>> t = zlib.compress(s)
   >>> len(t)
   37
   >>> zlib.decompress(t)
   b'witch which has which witches wrist watch'
   >>> zlib.crc32(s)
   226805979

## 10.10. Performance measurement

Algunos usuarios de Python desarrollan un profundo interés en conocer
el rendimiento relativo de las diferentes soluciones al mismo
problema.  Python provee una herramienta de medición que responde
inmediatamente a esas preguntas.

Por ejemplo, puede ser tentador usar la característica de empaquetado
y desempaquetado de las tuplas en lugar de la solución tradicional
para intercambiar argumentos.  El módulo "timeit" muestra rápidamente
una ligera ventaja de rendimiento:

   >>> from timeit import Timer
   >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
   0.57535828626024577
   >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
   0.54962537085770791

En contraste con el fino nivel de medición del módulo "timeit", los
módulos "profile" y "pstats" proveen herramientas para identificar
secciones críticas de tiempo en bloques de código más grandes.

## 10.11. Quality control

Una forma para desarrollar software de alta calidad consiste en
escribir pruebas para cada función mientras se desarrolla y correr
esas pruebas frecuentemente durante el proceso de desarrollo.

El módulo "doctest" provee una herramienta para revisar un módulo y
validar las pruebas integradas en las cadenas de documentación (o
*docstring*) del programa.  La construcción de las pruebas es tan
sencillo como cortar y pegar una ejecución típica junto con sus
resultados en los docstrings.  Esto mejora la documentación al proveer
al usuario un ejemplo y permite que el módulo *doctest* se asegure que
el código permanece fiel a la documentación:

   def average(values):
       """Computes the arithmetic mean of a list of numbers.

       >>> print(average([20, 30, 70]))
       40.0
       """
       return sum(values) / len(values)

   import doctest
   doctest.testmod()   # automatically validate the embedded tests

El módulo "unittest" no es tan sencillo como el módulo "doctest", pero
permite mantener un conjunto más completo de pruebas en un archivo
independiente:

   import unittest

   class TestStatisticalFunctions(unittest.TestCase):

       def test_average(self):
           self.assertEqual(average([20, 30, 70]), 40.0)
           self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
           with self.assertRaises(ZeroDivisionError):
               average([])
           with self.assertRaises(TypeError):
               average(20, 30, 70)

   unittest.main()  # Calling from the command line invokes all tests

## 10.12. Batteries included

Python tiene una filosofía de "pilas incluidas".  Esto se ve mejor en
las capacidades robustas y sofisticadas de sus paquetes más grandes.
Por ejemplo:

* Los módulos "xmlrpc.client" y "xmlrpc.server" convierten la
  implementación de llamadas a procedimientos remotos en una tarea
  casi trivial.  A pesar de los nombres de los módulos, no se necesita
  ningún conocimiento o manejo directo de XML.

* The "email" package is a library for managing email messages,
  including MIME and other **RFC 5322**-based message documents.
  Unlike "smtplib" and "poplib" which actually send and receive
  messages, the email package has a complete toolset for building or
  decoding complex message structures (including attachments) and for
  implementing internet encoding and header protocols.

* El paquete "json" proporciona un sólido soporte para analizar este
  popular formato de intercambio de datos.  El módulo "csv" permite la
  lectura y escritura directa de archivos en formato de valor separado
  por comas, comúnmente compatible con bases de datos y hojas de
  cálculo.  El procesamiento XML es compatible con los paquetes
  "xml.etree.ElementTree", "xml.dom" y "xml.sax". Juntos, estos
  módulos y paquetes simplifican en gran medida el intercambio de
  datos entre aplicaciones de Python y otras herramientas.

* El módulo "sqlite3" es un wrapper de la biblioteca de bases de datos
  SQLite, proporciona una base de datos constante que se puede
  actualizar y a la que se puede acceder utilizando una sintaxis SQL
  ligeramente no estándar.

* La internacionalización es compatible con una serie de módulos,
  incluyendo "gettext", "locale", y el paquete "codecs".
