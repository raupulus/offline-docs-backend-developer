---
title: '"lzma" --- Compression using the LZMA algorithm'
source_url: https://docs.python.org/es/3
source_path: library/lzma.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3150
---

# "lzma" --- Compression using the LZMA algorithm

Added in version 3.3.

**Código fuente:**Lib/lzma.py

======================================================================

Este módulo provee clases y funciones de conveniencia para comprimir y
descomprimir datos utilizando el algoritmo de compresión LZMA. También
se incluye una interfaz de fichero soportando el ".xz" y formatos de
fichero ".lzma" heredados utilizados por la utilidad **xz**, así como
flujos comprimidos sin procesar.

La interfaz proporcionada por este módulo es muy similar a la del
módulo "bz2". Tenga en cuenta que "LZMAFile" y "bz2.BZ2File" son
seguros para subprocesos *not*, por lo que si necesita utilizar una
única instancia "LZMAFile" de varios subprocesos, es necesario
protegerla con un candado.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

exception lzma.LZMAError

   Esta excepción es generada cuando un error ocurre durante la
   compresión o descompresión, o mientras se inicializa el estado de
   compresor/descompresor.

## Leyendo y escribiendo ficheros comprimidos

lzma.open(filename, mode='rb', *, format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

   Abre un fichero comprimido LZMA in binario o modo texto, retornando
   un *file object*.

   El argumento *filename* puede ser un nombre de fichero real (dado
   como un objeto "str", "bytes" o *path-like*), en cuyo caso el
   fichero nombrado es abierto, o puede ser un objeto de fichero
   existente para leer o escribir.

   El argumento *mode* puede ser cualquiera de ""r"", ""rb"", ""w"",
   ""wb"", ""x"", ""xb"", ""a"" o ""a"" para modo binario, o ""rt"",
   ""wt"", ""xt"", o ""at"" para modo texto. Por defecto es ""rb"".

   Al abrir un fichero para lectura, los argumentos *format* y
   *filters* tienen el mismo significado que para "LZMADecompressor".
   En este caso, los argumentos *check* y *preset* no deberían ser
   utilizados.

   Al abrir un fichero para lectura, los argumentos *format*, *check*,
   *preset* y *filters* tienen el mismo significado que para
   "LZMACompressor".

   Para modo binario, esta función es equivalente al constructor
   "LZMAFile": "LZMAFile(filename, mode, ...)". En este caso, los
   argumentos *encoding*, *errors* y *newline* no deben ser proveídos.

   Para modo texto, un objeto "LZMAFile" es creado, y envuelto en una
   instancia "io.TextIOWrapper" con codificación específica,
   comportamiento de manejo de errores, y codificación(es) de línea.

   Distinto en la versión 3.4: Agregado soporte para los modos ""x"",
   ""xb"" y ""xt"".

   Distinto en la versión 3.6: Acepta un *path-like object*.

class lzma.LZMAFile(filename=None, mode='r', *, format=None, check=-1, preset=None, filters=None)

   Abre un fichero comprimido LZMA en modo binario.

   Un "LZMAFIle" puede envolver un ya abierto *file object*, u operar
   directamente en un fichero nombrado. El argumento *filename*
   especifica el objeto de fichero a envolver, o el nombre del fichero
   para abrir (como un "str", "bytes" o un objeto *path-like*). Al
   envolver un objeto de fichero existente, el fichero envuelto no
   será cerrado cuando el "LZMAFile" es cerrado.

   El argumento *mode* puede ser ""r"" para lectura (por defecto),
   ""w"" para sobreescritura, ""x"" para creación exclusiva, o ""a""
   para agregado, Estos pueden ser equivalentemente dados como ""rb"",
   ""wb"", ""xb"" y ""ab"" respectivamente.

   Si *filename* es un objeto de fichero (en lugar de un nombre de
   fichero actual), un modo de ""w"" no trunca el fichero, y en cambio
   es equivalente a ""a"".

   Al abrir un fichero para escritura, el fichero de entrada puede ser
   la concatenación para múltiples flujos comprimidos separados. Estos
   son transparentemente decodificados como un único flujo lógico.

   Al abrir un fichero para lectura, los argumentos *format* y
   *filters* tienen el mismo significado que para "LZMADecompressor".
   En este caso, los argumentos *check* y *preset* no deberían ser
   utilizados.

   Al abrir un fichero para lectura, los argumentos *format*, *check*,
   *preset* y *filters* tienen el mismo significado que para
   "LZMACompressor".

   "LZMAFile" soporta todos los miembros especificados por
   "io.BufferedIOBase", excepto por "detach()" y "truncate()". La
   iteración y la instrucción "with" son soportadas.

   The following method and attributes are also provided:

   peek(size=-1)

      Retorna datos almacenados en búfer sin avanzar la posición del
      fichero. Al menos un byte de datos será retornado, a menos que
      EOF es alcanzado. El número exacto de bytes retornado no está
      especificado (el argumento *size* es ignorado).

      Nota:

        Mientras que llamar "peek()" no cambia la posición de fichero
        del "LZMAFile", puede cambiar la posición del objeto de
        fichero subyacente (por ejemplo si el "LZMAFile" fue
        construido pasando un objeto de fichero por *filename*).

   mode

      "'rb'" for reading and "'wb'" for writing.

      Added in version 3.13.

   name

      The lzma file name.  Equivalent to the "name" attribute of the
      underlying *file object*.

      Added in version 3.13.

   Distinto en la versión 3.4: Agregado soporte para los modos ""x"" y
   ""xb"".

   Distinto en la versión 3.5: El método "read()" acepta ahora un
   argumento de "None".

   Distinto en la versión 3.6: Acepta un *path-like object*.

## Comprimiendo y descomprimiendo datos en memoria

class lzma.LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)

   Crea un objeto compresor, el cual puede ser utilizado para
   comprimir datos incrementalmente.

   Para una forma más conveniente de comprimir un único fragmento de
   datos, vea "compress()".

   The *format* argument specifies what container format should be
   used. Possible values are "FORMAT_XZ" (the default), "FORMAT_ALONE"
   and "FORMAT_RAW".

   The *check* argument specifies the type of integrity check to
   include in the compressed data. This check is used when
   decompressing, to ensure that the data has not been corrupted.
   Possible values are "CHECK_NONE", "CHECK_CRC32", "CHECK_CRC64" (the
   default for "FORMAT_XZ") and "CHECK_SHA256".

   Si el chequeo especificado no es soportado, un "LZMAError" es
   generado.

   Las configuraciones de compresión pueden ser especificadas como un
   nivel de compresión predefinido (con el argumento *preset*), o en
   detalle como una cadena de filtro personalizada (con el argumento
   *filters*).

   El argumento *preset* (si es proveído) debería ser un entero entre
   "0" y "9" (inclusive), opcionalmente OR con la constante
   "PRESET_EXTREME". Si no se proporciona *preset* ni *filters*, el
   comportamiento por defecto es utilizar "PRESET_DEFAULT" (nivel
   preestablecido "6"). Altos preestablecidos producen salidas más
   pequeñas, pero vuelve el proceso de compresión más lento.

   Nota:

     En adición a ser más CPU-intensivo, la compresión con
     preestablecidos más altos también requiere mucha más memoria (y
     produce salida que necesita más memoria a descomprimir). Con un
     preestablecido de "9" por ejemplo, la sobrecarga para un objeto
     "LZMACompressor" puede ser tan alto como 800MiB. Por esta razón,
     es generalmente mejor quedarse con el preestablecido por defecto.

   El argumento *filters* (si es proveído) debería ser un
   especificador de cadena de filtro. Vea Especificando cadenas de
   filtro personalizadas para detalles.

   compress(data)

      Comprime *data* (un objeto "bytes"), retornando un objeto
      "bytes" conteniendo información comprimida por al menos parte de
      la entrada. Algo de *data* puede ser almacenado internamente,
      para uso en llamadas posteriores a "compress()" y "flush()". La
      información retornada debería ser concatenada con la salida en
      cualquier llamada previa a "compress()".

   flush()

      Finiquita el proceso de compresión, retornando un objeto "bytes"
      conteniendo cualquier información almacenada en los búferes
      internos del compresor.

      El compresor no puede ser utilizado después de que este método
      es llamado.

class lzma.LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

   Crea un objeto descompresor, el cual puede ser utilizado para
   descomprimir datos incrementalmente.

   Para una forma más conveniente de descomprimir un flujo completo de
   compresión a la vez, vea "decompress()".

   El argumento *format* especifica el formato de contenedor que
   debería ser utilizado. El valor por defecto es "FORMAT_AUTO", el
   cual puede descomprimir los ficheros ".xz" y ".lzma". Otros
   posibles valores son "FORMAT_XZ", "FORMAT_ALONE", y "FORMAT_RAW".

   El argumento *memlimit* especifica un límite (en bytes) en la
   cantidad de memoria que el descompresor puede utilizar. Cuando este
   argumento es utilizado, la descompresión fallará con un "LZMAError"
   si no es posible descomprimir la entrada dentro del límite de
   memoria dado.

   El argumento *filters* especifica la cadena de filtro que fue
   utilizado para crear el flujo que se descomprime. El argumento es
   requerido si *format* es "FORMAT_RAW", pero no debería ser
   utilizado para otros formatos. Vea Especificando cadenas de filtro
   personalizadas para más información sobre cadenas de filtro.

   Nota:

     Esta clase no maneja transparentemente entradas que contienen
     múltiples flujos comprimidos, a diferencia de "decompress()" y
     "LZMAFile". Para descomprimir una entrada multi-flujo con
     "LZMADecompressor", debería crear un nuevo descompresor para cada
     flujo.

   decompress(data, max_length=-1)

      Descomprime *data* (un *bytes-like object*), retornando
      información sin comprimir como bytes. Alguna *data* puede ser
      almacenada internamente, para uso en llamadas posteriores a
      "decompress()". La información retornada debería ser concatenada
      con la salida de cualquier llamada anterior a "decompress()".

      Si *max_length* no es negativo, retorna al menos *max_length*
      bytes para descomprimir información, Si este límite es alcanzado
      y salidas adicionales pueden ser producidas, el atributo
      "needs_input" será establecido a "False". En este caso, la
      siguiente llamada a "decompress()" podría proveer *data* como
      ""b''" para obtener más de la salida.

      Si toda la información ingresada fue descomprimida y retornada
      (ya sea porque esto fue menos que *max_length* bytes, o porque
      *max_length* fue negativo), el atributo "needs_input" será
      establecido a "True".

      Intentar descomprimir la información después de que el fin del
      flujo es alcanzado genera un "EOFError". Cualquier información
      encontrada después del fin del flujo es ignorada y guardada en
      el atributo "unused_data".

      Distinto en la versión 3.5: Agregado el parámetro *max_length*.

   check

      El ID del chequeo de integridad utilizado por el flujo de
      entrada. Esto puede ser "CHECK_UNKNOWN" hasta que suficiente de
      la entrada ha sido decodificada para determinar qué chequeo de
      integridad utiliza.

   eof

      "True" si el marcador de fin-de-flujo ha sido alcanzado.

   unused_data

      Información encontrada después del fin del flujo comprimido.

      Antes de que el fin del flujo es alcanzado, este será ""b"".

   needs_input

      "False" si el método "decompress()" puede proveer más
      información descomprimida antes de requerir nueva entrada
      descomprimida.

      Added in version 3.5.

lzma.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)

   Comprime *data* (un objeto "bytes"), retornando la información
   comprimida como un objeto "bytes".

   Vea "LZMACompressor" arriba para una descripción de los argumentos
   *format*, *check*, *preset* y *filters*.

lzma.decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

   Descomprime *data* (un objeto "bytes"), retornando la información
   descomprimida como un objeto "bytes".

   Si *data* es la concatenación de múltiples flujos comprimidos
   distintos, descomprime todos esos flujos, y retorna la
   concatenación de los resultados.

   Vea "LZMADecompressor" arriba para una descripción de los
   argumentos *format*, *memlimit* y *filters*.

## Misceláneas

lzma.is_check_supported(check)

   Retorna "True" si el chequeo de integridad dado es soportado en
   este sistema.

   "CHECK_NONE" y "CHECK_CRC32" son soportados siempre. "CHECK_CRC64"
   y "CHECK_SHA256" pueden no estar disponibles si está utilizando una
   versión de **liblzma** que fue compilada con un conjunto de
   funciones limitado.

## Especificando cadenas de filtro personalizadas

Un especificador de cadena de filtro es una secuencia de diccionarios,
donde cada diccionario contiene el ID y opciones para un único filtro.
Cada diccionario debe contener la llave ""id"", y puede contener
llaves adicionales para especificar opciones filtro-dependientes. Los
ID de filtro válidos son como sigue:

* Filtro de compresión:

  * "FILTER_LZMA1" (para uso con "FORMAT_ALONE")

  * "FILTER_LZMA2" (para uso con "FORMAT_XZ" y "bytesFORMAT_RAW")

* Filtro delta:

  * "FILTER_DELTA"

* Filtros *Branch-Call-Jump (BCJ)*:

  * "FILTER_X86"

  * "FILTER_IA64"

  * "FILTER_ARM"

  * "FILTER_ARMTHUMB"

  * "FILTER_POWERPC"

  * "FILTER_SPARC"

Una cadena de filtro puede consistir de hasta 4 filtros, y no puede
estar vacía. El último filtro en la cadena debe ser un filtro de
compresión, y cualquier otro filtro debe ser un filtro delta o BCJ.

Los filtros de compresión soportan las siguientes opciones
(especificadas como entradas adicionales:

* "preset": Un ajuste de compresión a utilizar como una fuente de
  valores por defecto para opciones que no están especificadas
  explícitamente.

* "dict_size": Tamaño del diccionario en bytes. Esto debería estar
  entre 4 kiB y 1.5 GiB (inclusive).

* "lc" Número de bits de contexto literal.

* "lp": Número de bits de posición literal. La suma "lc + lp" debe ser
  al menos 4.

* "pb": Número de bits de posición; debe ser al menos 4.

* "mode": "MODE_FAST" o "MODE_NORMAL".

* "nice_len": Lo que debería ser considerado una "buena longitud" para
  una coincidencia. Esto debería ser 273 o menos.

* "mf": Qué buscador de coincidencias utilizar -- "MF_HC3", "MF_HC4".
  "MF_BT2", "MF_BT3", o "MF_BT4".

* "depth": Profundidad de búsqueda máxima utilizada por el buscador de
  coincidencias. 0 (por defecto) significa seleccionar automáticamente
  basado en otras opciones de filtro.

El filtro delta almacena las diferencias entre bytes, produciendo más
entrada repetitiva para el compresor en ciertas circunstancias.
Soporta una opción, "dist". Esto indica la distancia entre bytes a ser
sustraída. Por defecto es 1, por ejemplo toma las diferencias entre
bytes adyacentes.

Los filtros BCJ están destinados a ser aplicados a código máquina.
Convierten ramas, llamadas y saltos relativos en el código para
utilizar el direccionamiento absoluto, con el objetivo de incrementar
la redundancia que puede ser explotada por el compresor. Estos filtros
soportan una opción, "start_offset". Esto especifica la dirección que
debería ser mapeada al comienzo de la entrada de información. Por
defecto es 0.

## Constants

The following module-level constants are provided for use as the
*format*, *check*, *preset* and *filters* arguments of the classes and
functions above.

Container formats:

lzma.FORMAT_XZ

   The ".xz" container format.

lzma.FORMAT_ALONE

   The legacy ".lzma" container format.  This format is more limited
   than ".xz" -- it does not support integrity checks or multiple
   filters.

lzma.FORMAT_RAW

   A raw data stream, not using any container format.  This format
   specifier does not support integrity checks, and requires that you
   always specify a custom filter chain (for both compression and
   decompression).  Additionally, data compressed in this manner
   cannot be decompressed using "FORMAT_AUTO".

lzma.FORMAT_AUTO

   Used for decompression only.  The container format is detected
   automatically, so that both ".xz" and ".lzma" files can be
   decompressed.

Integrity checks:

lzma.CHECK_NONE

   No integrity check.  This is the default (and the only acceptable
   value) for "FORMAT_ALONE" and "FORMAT_RAW".

lzma.CHECK_CRC32

   A 32-bit Cyclic Redundancy Check.

lzma.CHECK_CRC64

   A 64-bit Cyclic Redundancy Check.  This is the default for
   "FORMAT_XZ".

lzma.CHECK_SHA256

   A 256-bit Secure Hash Algorithm.

lzma.CHECK_UNKNOWN

   The integrity check used by a stream could not yet be determined.
   This may be the value of the "LZMADecompressor.check" attribute
   until enough of the input has been decoded.

lzma.CHECK_ID_MAX

   The largest supported integrity-check ID.

Compression presets:

lzma.PRESET_DEFAULT

   The default compression preset, equivalent to preset level "6".

lzma.PRESET_EXTREME

   A flag that may be bitwise OR-ed with a preset level ("0" to "9")
   to select a slower but more thorough variant of that preset.

Filter IDs and options:

lzma.FILTER_LZMA1
lzma.FILTER_LZMA2

   The LZMA1 and LZMA2 compression filters.  "FILTER_LZMA1" is for use
   with "FORMAT_ALONE", while "FILTER_LZMA2" is for use with
   "FORMAT_XZ" and "FORMAT_RAW".

lzma.FILTER_DELTA

   The delta filter.

lzma.MODE_FAST
lzma.MODE_NORMAL

   Compression modes that may be used as the "mode" option of a filter
   specifier (see Especificando cadenas de filtro personalizadas).

lzma.MF_HC3
lzma.MF_HC4
lzma.MF_BT2
lzma.MF_BT3
lzma.MF_BT4

   Match finders that may be used as the "mf" option of a filter
   specifier (see Especificando cadenas de filtro personalizadas).

## Ejemplos

Leyendo un fichero comprimido:

   import lzma
   with lzma.open("file.xz") as f:
       file_content = f.read()

Creando un fichero comprimido:

   import lzma
   data = b"Insert Data Here"
   with lzma.open("file.xz", "w") as f:
       f.write(data)

Comprimiendo información en memoria:

   import lzma
   data_in = b"Insert Data Here"
   data_out = lzma.compress(data_in)

Compresión incremental:

   import lzma
   lzc = lzma.LZMACompressor()
   out1 = lzc.compress(b"Some data\n")
   out2 = lzc.compress(b"Another piece of data\n")
   out3 = lzc.compress(b"Even more data\n")
   out4 = lzc.flush()
   # Concatenate all the partial results:
   result = b"".join([out1, out2, out3, out4])

Escribiendo información comprimida en fichero ya abierto:

   import lzma
   with open("file.xz", "wb") as f:
       f.write(b"This data will not be compressed\n")
       with lzma.open(f, "w") as lzf:
           lzf.write(b"This *will* be compressed\n")
       f.write(b"Not compressed\n")

Creando un fichero comprimido utilizando una cadena de filtro
personalizada:

   import lzma
   my_filters = [
       {"id": lzma.FILTER_DELTA, "dist": 5},
       {"id": lzma.FILTER_LZMA2, "preset": 7 | lzma.PRESET_EXTREME},
   ]
   with lzma.open("file.xz", "w", filters=my_filters) as f:
       f.write(b"blah blah blah")
