---
title: '"bz2" --- Support for **bzip2** compression'
source_url: https://docs.python.org/es/3
source_path: library/bz2.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1880
---

# "bz2" --- Support for **bzip2** compression

**Código fuente:** Lib/bz2.py

======================================================================

Este módulo proporciona una interfaz completa para comprimir y
descomprimir datos utilizando el algoritmo de compresión bzip2.

The "bz2" module contains:

* La función "open()" y la clase "BZ2File" para leer y escribir
  archivos comprimidos.

* Las clases "BZ2Compressor" y "BZ2Decompressor" para la
  (de)compresión incremental.

* Las funciones "compress()" y "decompress()" para una (de)compresión
  en un solo paso.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

## (De)compresión de archivos

bz2.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)

   Abre un archivo comprimido con bzip2 en modo binario o texto,
   retorna un *objeto archivo*.

   Al igual que con el constructor para "BZ2File", el argumento
   *filename* puede ser un nombre de archivo real (un objeto "str" o
   "bytes"), o un objeto de archivo existente para leer o escribirle.

   El argumento *mode* puede ser cualquiera de "'r'", "'rb'", "'w'",
   "'wb'", "'x'", "'xb'", "'a'" o "'ab'" para modo binario, o "'rt'",
   "'wt'", "'xt'" , o "'a'" para el modo de texto. El valor
   predeterminado es "'rb'".

   El argumento *compresslevel* es un entero del 1 al 9, como para el
   constructor de "BZ2File".

   Para el modo binario, esta función es equivalente a "BZ2File"
   constructor: "BZ2File(filename, mode,
   compresslevel=compresslevel)". En este caso, no se deben
   proporcionar los argumentos *encoding*, *errors* y *newline* (nueva
   linea).

   Para el modo de texto, se crea un objeto "BZ2File", y se envuelve
   en una instancia "io.TextIOWrapper" con la codificación
   especificada, el comportamiento de manejo de errores y los
   final(es) de línea.

   Added in version 3.3.

   Distinto en la versión 3.4: El modo "'x'" (creación exclusiva) ha
   sido agregado.

   Distinto en la versión 3.6: Acepta un objeto similar a una ruta
   (*path-like object*).

class bz2.BZ2File(filename, mode='r', *, compresslevel=9)

   Abre un archivo comprimido con bzip2 en modo binario.

   Si *filename* es un objeto tipo "str" o "bytes", abre el archivo
   nombrado directamente. De lo contrario, *filename* debería ser un
   *file object*, que se utilizará para leer o escribir los datos
   comprimidos.

   El argumento *mode* puede ser "'r'" para lectura (predeterminado),
   "'w'" para sobrescribir, "'x'" para creación exclusiva o "'a'" para
   anexar. Estos se pueden dar de manera equivalente como "'rb'",
   "'wb'", "'xb'" y "'ab'" respectivamente.

   Si *filename* es un objeto de archivo (en lugar de un nombre de
   archivo real), el modo "'w'" no trunca el archivo, y es equivalente
   a "'a'".

   Si *mode* es "'w'" o "'a'", *compresslevel* puede ser un número
   entero entre "1" y "9" especificando el nivel de compresión: "1"
   produce la menor compresión y "9" (predeterminado) produce la mayor
   compresión.

   Si *mode* es "'r'", el archivo de entrada puede ser la
   concatenación de múltiples flujos (streams) comprimidos.

   "BZ2File" proporciona todos los miembros especificados por
   "io.BufferedIOBase", excepto "detach()" y "truncate()". La
   iteración y la instrucción "with" están soportadas.

   "BZ2File" also provides the following methods and attributes:

   peek([n])

      Retorna datos almacenados en el búfer sin avanzar la posición
      del archivo. Se retornará al menos un byte de datos (a menos que
      sea EOF). El número exacto de bytes retornados no está
      especificado.

      Nota:

        Al invocar "peek()" no cambia la posición del archivo de
        "BZ2File", puede cambiar la posición del objeto de archivo
        subyacente (por ejemplo, si "BZ2File" se construyó pasando un
        objeto de archivo a *filename*).

      Added in version 3.3.

   fileno()

      Return the file descriptor for the underlying file.

      Added in version 3.3.

   readable()

      Return whether the file was opened for reading.

      Added in version 3.3.

   seekable()

      Return whether the file supports seeking.

      Added in version 3.3.

   writable()

      Return whether the file was opened for writing.

      Added in version 3.3.

   read1(size=-1)

      Read up to *size* uncompressed bytes, while trying to avoid
      making multiple reads from the underlying stream. Reads up to a
      buffer's worth of data if size is negative.

      Returns "b''" if the file is at EOF.

      Added in version 3.3.

   readinto(b)

      Read bytes into *b*.

      Returns the number of bytes read (0 for EOF).

      Added in version 3.3.

   mode

      "'rb'" for reading and "'wb'" for writing.

      Added in version 3.13.

   name

      The bzip2 file name.  Equivalent to the "name" attribute of the
      underlying *file object*.

      Added in version 3.13.

   Distinto en la versión 3.1: Se agregó soporte para la declaración
   "with".

   Distinto en la versión 3.3: Se agregó soporte para *filename*
   siendo un objeto de archivo (*file object*) en lugar de un nombre
   de archivo real.Se agregó el modo "'a'" (agregar), junto con el
   soporte para leer archivos de flujo múltiple (multi-stream).

   Distinto en la versión 3.4: El modo "'x'" (creación exclusiva) ha
   sido agregado.

   Distinto en la versión 3.5: El método "read()" ahora acepta el
   argumento "None".

   Distinto en la versión 3.6: Acepta un objeto similar a una ruta
   (*path-like object*).

   Distinto en la versión 3.9: El parámetro *buffering* ha sido
   retirado. Desde Python 3.0 era ignorado y estaba obsoleto. Pasa un
   objeto archivo abierto para controlar cómo el archivo es abierto.El
   parámetro *compresslevel* se convirtió en un argumento sólo por
   palabra clave.

   Distinto en la versión 3.10: Esta clase es insegura en hilos frente
   a múltiples lectores o escritores, al igual que sus clases
   equivalentes en "gzip" y "lzma" siempre lo han sido.

## (De)compresión incremental

class bz2.BZ2Compressor(compresslevel=9)

   Crea un nuevo objeto compresor. Este objeto puede usarse para
   comprimir datos de forma incremental. Para comprimir en un solo
   paso, use la función "compress()" en su lugar.

   *compresslevel*, si se proporciona, debe ser un número entero entre
   "1" y "9". El valor predeterminado es "9".

   compress(data)

      Provee datos al objeto del compresor. Retorna un fragmento de
      datos comprimidos si es posible, o una cadena de bytes vacía de
      lo contrario.

      Cuando haya terminado de proporcionar datos al compresor, llame
      al método "flush()" para finalizar el proceso de compresión.

   flush()

      Termina el proceso de compresión. Retorna los datos comprimidos
      que quedan en los búferes internos.

      El objeto compresor no puede usarse después de que se haya
      llamado a este método.

class bz2.BZ2Decompressor

   Crea un nuevo objeto descompresor. Este objeto puede usarse para
   descomprimir datos de forma incremental. Para descomprimir en un
   solo paso, use la función "decompress()" en su lugar.

   Nota:

     Esta clase no maneja de forma transparente las entradas que
     contienen múltiples flujos comprimidos, a diferencia de
     "decompress()" y "BZ2File". Si necesitas descomprimir una entrada
     de flujo múltiple con "BZ2Decompressor", debe usar un nuevo
     descompresor para cada flujo (stream).

   decompress(data, max_length=-1)

      Descomprime *datos* (un *bytes-like object*), retornando datos
      sin comprimir como bytes. Algunos de los *datos* pueden
      almacenarse internamente para su uso en llamadas posteriores a
      "decompress()". Los datos retornados deben concatenarse con la
      salida de cualquier llamada anterior a "decompress()".

      Si *max_length* no es negativo, retorna como máximo *max_length*
      bytes de datos descomprimidos. Si se alcanza este límite y se
      pueden producir más resultados, el atributo "needs_input" se
      establecerá en "False". En este caso, la siguiente llamada a
      "decompress()" puede proporcionar *datos* como "b''" para
      obtener más de la salida.

      Si todos los datos de entrada se descomprimieron y retornaron
      (ya sea porque esto era menor que *max_length* bytes, o porque
      *max_length* era negativo), el atributo "needs_input" se
      establecerá en "True".

      Intentar descomprimir datos una vez que se alcanza el final del
      flujo genera un "EOFError". Cualquier información encontrada
      después del final del flujo se ignora y se guarda en el atributo
      "unused_data".

      Distinto en la versión 3.5: Añadido el parámetro *max_length*.

   eof

      "True" si se ha alcanzado el marcador de fin de flujo.

      Added in version 3.3.

   unused_data

      Datos encontrados después del final del flujo comprimido.

      Si se accede a este atributo antes de que se haya alcanzado el
      final del flujo, su valor será "b''".

   needs_input

      "False" si el método "decompress()" puede proporcionar más datos
      descomprimidos antes de requerir una nueva entrada sin
      comprimir.

      Added in version 3.5.

## (Des)comprimir en un solo paso

bz2.compress(data, compresslevel=9)

   Comprime *datos*, un *objetos tipo binarios*.

   *compresslevel*, si se proporciona, debe ser un número entero entre
   "1" y "9". El valor predeterminado es "9".

   Para compresión incremental, use "BZ2Compressor" en su lugar.

bz2.decompress(data)

   Descomprime *datos*, un *objetos tipo binarios*.

   Si *data* es la concatenación de múltiples flujos comprimidos,
   descomprime todos los flujos.

   Para la descompresión incremental, use "BZ2Decompressor" en su
   lugar.

   Distinto en la versión 3.3: Se agregó soporte para entradas de
   flujo múltiple.

## Ejemplos de uso

Below are some examples of typical usage of the "bz2" module.

Usando "compress()" y "decompress()" para demostrar una compresión de
ida y vuelta (*round-trip*):

>>> import bz2
>>> data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
>>> c = bz2.compress(data)
>>> len(data) / len(c)  # Data compression ratio
1.513595166163142
>>> d = bz2.decompress(c)
>>> data == d  # Check equality to original object after round-trip
True

Usando "BZ2Compressor" para compresión incremental:

>>> import bz2
>>> def gen_data(chunks=10, chunksize=1000):
...     """Yield incremental blocks of chunksize bytes."""
...     for _ in range(chunks):
...         yield b"z" * chunksize
...
>>> comp = bz2.BZ2Compressor()
>>> out = b""
>>> for chunk in gen_data():
...     # Provide data to the compressor object
...     out = out + comp.compress(chunk)
...
>>> # Finish the compression process.  Call this once you have
>>> # finished providing data to the compressor.
>>> out = out + comp.flush()

El ejemplo anterior utiliza un flujo de datos bastante "no aleatorio"
(un flujo de fragmentos "b"z""). Los datos aleatorios tienden a
comprimirse mal, mientras que los datos ordenados y repetitivos
generalmente producen un alto grado de compresión.

Escribiendo y leyendo un archivo comprimido con bzip2 en modo binario:

>>> import bz2
>>> data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
>>> with bz2.open("myfile.bz2", "wb") as f:
...     # Write compressed data to file
...     unused = f.write(data)
...
>>> with bz2.open("myfile.bz2", "rb") as f:
...     # Decompress data from file
...     content = f.read()
...
>>> content == data  # Check equality to original object after round-trip
True
