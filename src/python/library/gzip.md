---
title: '"gzip" --- Support for **gzip** files'
source_url: https://docs.python.org/es/3
source_path: library/gzip.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2780
---

# "gzip" --- Support for **gzip** files

**Código fuente:** Lib/gzip.py

======================================================================

Este módulo proporciona una interfaz simple para comprimir y
descomprimir archivos como lo harían los programas GNU **gzip** y
**gunzip**.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

La compresión de datos la proporciona el módulo "zlib".

The "gzip" module provides the "GzipFile" class, as well as the
"open()", "compress()" and "decompress()" convenience functions. The
"GzipFile" class reads and writes **gzip**-format files, automatically
compressing or decompressing the data so that it looks like an
ordinary *file object*.

Tenga en cuenta que los formatos de archivo adicionales que pueden ser
descomprimidos por los programas **gzip** y **gunzip**, como los
producidos por **compress** y **pack**, no son compatibles con este
módulo.

El módulo define los siguientes elementos:

gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)

   Abre un archivo comprimido gzip en modo binario o de texto,
   retornando un *file object*.

   El argumento *filename* puede ser un nombre de archivo real (un
   objeto "str" o "bytes"), o un objeto archivo existente para leer o
   escribir.

   El argumento *mode* puede ser cualquiera de "'r'", "'rb'", "'a'",
   "'ab'", "'w'", "'wb'", "'x'" or "'xb'" para el modo binario, o
   "'rt'", "'at'", "'wt'", or "'xt'" para el modo texto. El valor
   predeterminado es "'rb'".

   El argumento *compresslevel* es un número entero de 0 a 9, como
   para el constructor "GzipFile".

   Para el modo binario, esta función es equivalente al constructor
   "GzipFile": "GzipFile (filename, mode, compresslevel)". En este
   caso, no se deben proporcionar los argumentos *encoding*, *errors*
   y *newline*.

   Para el modo texto, se crea un objeto "GzipFile" y se envuelve en
   una instancia "io.TextIOWrapper" con la codificación especificada,
   comportamiento de manejo de errores y terminación(es) de línea.

   Distinto en la versión 3.3: Se agregó soporte para que *filename*
   sea un objeto de archivo, soporte para el modo de texto y los
   argumentos *encoding*, *errors* y *newline*.

   Distinto en la versión 3.4: Se agregó soporte para los modos "'x'",
   "'xb'" y "'xt'".

   Distinto en la versión 3.6: Acepta un *path-like object*.

exception gzip.BadGzipFile

   An exception raised for invalid gzip files.  It inherits from
   "OSError". "EOFError" and "zlib.error" can also be raised for
   invalid gzip files.

   Added in version 3.8.

class gzip.GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None)

   Constructor para la clase "GzipFile", que simula la mayoría de los
   métodos de *file object*, con la excepción del método "truncate()".
   Al menos uno de *fileobj* y *filename* debe recibir un valor no
   trivial.

   La nueva instancia de clase se basa en *fileobj*, que puede ser un
   archivo normal, un objeto "io.BytesIO", o cualquier otro objeto que
   simule un archivo. El valor predeterminado es "None", en cuyo caso
   se abre *filename* para proporcionar un objeto de archivo.

   Cuando *fileobj* no es "None", el argumento *filename* solo se usa
   para ser incluido en el encabezado del archivo **gzip**, que puede
   incluir el nombre de archivo original del archivo sin comprimir. De
   forma predeterminada, el nombre de archivo es de *fileobj*, si es
   discernible; de lo contrario, el valor predeterminado es la cadena
   vacía, y en este caso el nombre del archivo original no se incluye
   en el encabezado.

   El argumento *mode* puede ser cualquiera de "'r'", "'rb'", "'a'",
   "'ab'", "'w'", "'wb'", "'x'", or "'xb'", dependiendo de si el
   archivo se leerá o escribirá. El valor predeterminado es el modo de
   *fileobj* si es discernible; de lo contrario, el valor
   predeterminado es "'rb'". En futuras versiones de Python, no se
   utilizará el modo *fileobj*. Es mejor especificar siempre *mode*
   para escribir.

   Tenga en cuenta que el archivo siempre se abre en modo binario.
   Para abrir un archivo comprimido en modo de texto, utilice "open()"
   (o ajuste su "GzipFile" con un "io.TextIOWrapper").

   El argumento *compresslevel* es un entero de "0" a "9" que controla
   el nivel de compresión; "1" es más rápido y produce la menor
   compresión, y "9" es más lento y produce la mayor compresión. "0"
   no es una compresión. El valor predeterminado es "9".

   The optional *mtime* argument is the timestamp requested by gzip.
   The time is in Unix format, i.e., seconds since 00:00:00 UTC,
   January 1, 1970. If *mtime* is omitted or "None", the current time
   is used. Use *mtime* = 0 to generate a compressed stream that does
   not depend on creation time.

   See below for the "mtime" attribute that is set when decompressing.

   Calling a "GzipFile" object's "close()" method does not close
   *fileobj*, since you might wish to append more material after the
   compressed data.  This also allows you to pass an "io.BytesIO"
   object opened for writing as *fileobj*, and retrieve the resulting
   memory buffer using the "io.BytesIO" object's "getvalue()" method.

   "GzipFile" admite la interfaz "io.BufferedIOBase", incluida la
   iteración y la declaración "with". Solo el método "truncate()" no
   está implementado.

   "GzipFile" también proporciona el siguiente método y atributo:

   peek(n)

      Read *n* uncompressed bytes without advancing the file position.
      The number of bytes returned may be more or less than requested.

      Nota:

        Al llamar a "peek()" no cambia la posición del archivo
        "GzipFile", puede cambiar la posición del objeto de archivo
        subyacente (por ejemplo, si el "GzipFile" se construyó con el
        parámetro *fileobj*).

      Added in version 3.2.

   mode

      "'rb'" for reading and "'wb'" for writing.

      Distinto en la versión 3.13: In previous versions it was an
      integer "1" or "2".

   mtime

      When decompressing, this attribute is set to the last timestamp
      in the most recently read header.  It is an integer, holding the
      number of seconds since the Unix epoch (00:00:00 UTC, January 1,
      1970). The initial value before reading any headers is "None".

   name

      La ruta al archivo gzip en disco, como "str" o "bytes". Equivale
      a la salida de "os.fspath()" en la ruta de entrada original, sin
      ninguna otra normalización, resolución o expansión.

   Distinto en la versión 3.1: Se ha agregado soporte para la
   declaración "with", junto con el argumento del constructor *mtime*
   y el atributo "mtime".

   Distinto en la versión 3.2: Se agregó soporte para archivos con
   relleno de ceros y que no se pueden buscar.

   Distinto en la versión 3.3: El método "io.BufferedIOBase.read1()"
   ahora está implementado.

   Distinto en la versión 3.4: Se agregó soporte para los modos "'x'"
   y "'xb'".

   Distinto en la versión 3.5: Se ha añadido soporte para escribir
   objetos arbitrarios *bytes-like objects*. El método "read()" ahora
   acepta un argumento de "None".

   Distinto en la versión 3.6: Acepta un *path-like object*.

   Obsoleto desde la versión 3.9: Abriendo "GzipFile" para escribir
   sin especificar el argumento *mode* está obsoleto.

   Distinto en la versión 3.12: Elimine el atributo "filename",
   utilice en su lugar el atributo "name`".

gzip.compress(data, compresslevel=9, *, mtime=0)

   Compress the *data*, returning a "bytes" object containing the
   compressed data.  *compresslevel* and *mtime* have the same meaning
   as in the "GzipFile" constructor above, but *mtime* defaults to 0
   for reproducible output.

   Added in version 3.2.

   Distinto en la versión 3.8: Se agregó el parámetro *mtime* para una
   salida reproducible.

   Distinto en la versión 3.11: Speed is improved by compressing all
   data at once instead of in a streamed fashion. Calls with *mtime*
   set to "0" are delegated to "zlib.compress()" for better speed. In
   this situation the output may contain a gzip header "OS" byte value
   other than 255 "unknown" as supplied by the underlying zlib
   implementation.

   Distinto en la versión 3.13: The gzip header OS byte is guaranteed
   to be set to 255 when this function is used as was the case in 3.10
   and earlier.

   Distinto en la versión 3.14: The *mtime* parameter now defaults to
   0 for reproducible output. For the previous behaviour of using the
   current time, pass "None" to *mtime*.

gzip.decompress(data)

   Descomprime *data*, retornando un objeto "bytes" que contiene los
   datos sin comprimir. Esta función es capaz de descomprimir datos
   gzip de varios miembros (múltiples bloques gzip concatenados entre
   sí). Cuando se está seguro de que los datos contienen un solo
   miembro, la función "zlib.decompress()" es más rápida si se
   establece *wbits* a 31.

   Added in version 3.2.

   Distinto en la versión 3.11: La velocidad se mejora al descomprimir
   los miembros simultáneamente en memoria en lugar de hacerlo de
   manera continua.

## Ejemplos de uso

Ejemplos de como leer un archivo comprimido:

   import gzip
   with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
       file_content = f.read()

Ejemplos de como crear un archivo comprimido GZIP:

   import gzip
   content = b"Lots of content here"
   with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
       f.write(content)

Ejemplos de como GZIP comprime un archivo existente:

   import gzip
   import shutil
   with open('/home/joe/file.txt', 'rb') as f_in:
       with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
           shutil.copyfileobj(f_in, f_out)

Ejemplo de como GZIP comprime una cadena binaria:

   import gzip
   s_in = b"Lots of content here"
   s_out = gzip.compress(s_in)

Ver también:

  Módulo "zlib"
     El módulo básico de compresión de datos necesario para admitir el
     formato de archivo **gzip**.

  In case gzip (de)compression is a bottleneck, the python-isal
  package speeds up (de)compression with a mostly compatible API.

## Command-line interface

The "gzip" module provides a simple command line interface to compress
or decompress files.

Once executed the "gzip" module keeps the input file(s).

Distinto en la versión 3.8: Agrega una nueva interfaz de línea de
comandos con un uso. De forma predeterminada, cuando ejecutará la CLI,
el nivel de compresión predeterminado es 6.

### Command-line options

file

   Si no se especifica *file*, lee de "sys.stdin".

--fast

   Indica el método de compresión más rápido (menos compresión).

--best

   Indica el método de compresión más lento (mejor compresión).

-d, --decompress

   Descomprime el archivo dado.

-h, --help

   Muestra el mensaje de ayuda.
