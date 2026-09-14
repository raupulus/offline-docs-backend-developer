---
title: '"zlib" --- Compression compatible with **gzip**'
source_url: https://docs.python.org/es/3
source_path: library/zlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4720
---

# "zlib" --- Compression compatible with **gzip**

======================================================================

For applications that require data compression, the functions in this
module allow compression and decompression, using the zlib library.

This is an *optional module*. If it is missing from your copy of
CPython, look for documentation from your distributor (that is,
whoever provided Python to you). If you are the distributor, see
Requirements for optional modules.

zlib's functions have many options and often need to be used in a
particular order.  This documentation doesn't attempt to cover all of
the permutations; consult the zlib manual for authoritative
information.

Para leer y escribir archivos ".gz" consultar el módulo "gzip".

La excepción y las funciones disponibles en este módulo son:

exception zlib.error

   Excepción provocada en errores de compresión y descompresión.

zlib.adler32(data[, value])

   Calcula una suma de comprobación Adler-32 de *data*. (Una suma de
   comprobación Adler-32 es casi tan confiable como un CRC32, pero se
   puede calcular mucho más rápidamente). El resultado es un entero de
   32 bits sin signo. Si *value* está presente, se utiliza como el
   valor inicial de la suma de comprobación; de lo contrario, se
   utiliza un valor predeterminado de 1. Pasar *value* permite
   calcular una suma de comprobación en ejecución durante la
   concatenación de varias entradas. El algoritmo no es
   criptográficamente fuerte y no se debe utilizar para la
   autenticación o las firmas digitales. Puesto que está diseñado como
   un algoritmo de suma de comprobación, no es adecuado su uso como un
   algoritmo *hash* general.

   Distinto en la versión 3.0: El resultado es siempre sin signo.

zlib.compress(data, /, level=Z_DEFAULT_COMPRESSION, wbits=MAX_WBITS)

   Compresses the bytes in *data*, returning a bytes object containing
   compressed data. *level* is an integer from "0" to "9" or "-1"
   controlling the level of compression; See "Z_BEST_SPEED" ("1"),
   "Z_BEST_COMPRESSION" ("9"), "Z_NO_COMPRESSION" ("0"), and the
   default, "Z_DEFAULT_COMPRESSION" ("-1") for more information about
   these values.

   The *wbits* argument controls the size of the history buffer (or
   the "window size") used when compressing data, and whether a header
   and trailer is included in the output.  It can take several ranges
   of values, defaulting to "15" ("MAX_WBITS"):

   * +9 a +15: el logaritmo en base dos del tamaño de la ventana, que
     por lo tanto oscila entre 512 y 32768. Los valores más grandes
     producen una mejor compresión a expensas de un mayor uso de
     memoria. Como resultado se incluirá un encabezado y un avance
     específicos de zlib.

   * −9 a −15: utiliza el valor absoluto de *wbits* como el logaritmo
     del tamaño de la ventana, al tiempo que produce una secuencia de
     salida sin encabezado ni suma de verificación.

   * +25 a +31 = 16 + (9 a 15): utiliza los 4 bits bajos del valor
     como el logaritmo del tamaño de la ventana, mientras que incluye
     un encabezado básico **gzip** y suma de verificación en la
     salida.

   Lanza la excepción "error" si ocurre cualquier error.

   Distinto en la versión 3.6: *level* ahora se puede utilizar como
   parámetro de palabra clave.

   Distinto en la versión 3.11: El parámetro *wbits* está ahora
   disponible para establecer bits de la ventana y tipo de compresión.

zlib.compressobj(level=Z_DEFAULT_COMPRESSION, method=DEFLATED, wbits=MAX_WBITS, memLevel=DEF_MEM_LEVEL, strategy=Z_DEFAULT_STRATEGY[, zdict])

   Retorna un objeto de compresión, para ser usado para comprimir
   flujos de datos que no caben en la memoria de una vez.

   *level* is the compression level -- an integer from "0" to "9" or
   "-1". See "Z_BEST_SPEED" ("1"), "Z_BEST_COMPRESSION" ("9"),
   "Z_NO_COMPRESSION" ("0"), and the default, "Z_DEFAULT_COMPRESSION"
   ("-1") for more information about these values.

   *method* es el algoritmo de compresión. Actualmente, el único valor
   admitido es "DEFLATED".

   El parámetro *wbits* controla el tamaño del búfer histórico (o el
   "tamaño de ventana") y qué formato de encabezado y cola será usado.
   Tiene el mismo significado que el descrito para decompress().

   El argumento *memLevel* controla la cantidad de memoria utilizada
   para el estado de compresión interna. Los valores posibles varían
   de "1" a "9". Los valores más altos usan más memoria, pero son más
   rápidos y producen una salida más pequeña.

   *strategy* is used to tune the compression algorithm. Possible
   values are "Z_DEFAULT_STRATEGY", "Z_FILTERED", "Z_HUFFMAN_ONLY",
   "Z_RLE" and "Z_FIXED".

   *zdict* es un diccionario de compresión predefinido. Este es una
   secuencia de bytes (como un objeto "bytes") que contiene
   subsecuencias que se espera que ocurran con frecuencia en los datos
   que se van a comprimir. Las subsecuencias que se espera que sean
   más comunes deben aparecer al final del diccionario.

   Distinto en la versión 3.3: Se agregó el parámetro *zdict* y el
   soporte de argumentos de palabras clave.

zlib.crc32(data[, value])

   Calcula un suma de comprobación CRC (comprobación de redundancia
   cíclica, por sus siglas en inglés *Cyclic Redundancy Check*) de
   *datos*. El resultado es un entero de 32 bits sin signo. Si *value*
   está presente, se usa como el valor inicial de la suma de
   verificación; de lo contrario, se usa el valor predeterminado 0.
   Pasar *value* permite calcular una suma de verificación en
   ejecución sobre la concatenación de varias entradas. El algoritmo
   no es criptográficamente fuerte y no debe usarse para autenticación
   o firmas digitales. Dado que está diseñado para usarse como un
   algoritmo de suma de verificación, no es adecuado su uso como
   algoritmo *hash* general.

   Distinto en la versión 3.0: El resultado es siempre sin signo.

zlib.decompress(data, /, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE)

   Descomprime los bytes en *data*, retornando un objeto de bytes que
   contiene los datos sin comprimir. El parámetro *wbits* depende del
   formato de *data*, y se trata más adelante. Si se da *bufsize*, se
   usa como el tamaño inicial del búfer de salida. Provoca la
   excepción "error" si se produce algún error.

   El parámetro *wbits* controla el tamaño del búfer histórico (o el
   "tamaño de ventana") y qué formato de encabezado y cola se espera.
   Es similar al parámetro para "compressobj()", pero acepta más
   rangos de valores:

   * +8 a +15: el logaritmo en base dos del tamaño del búfer. La
     entrada debe incluir encabezado y cola zlib.

   * 0: determina automáticamente el tamaño del búfer desde el
     encabezado zlib. Solo se admite desde zlib 1.2.3.5.

   * -8 to -15: utiliza el valor absoluto de *wbits* como el logaritmo
     del tamaño del búfer. La entrada debe ser una transmisión sin
     formato, sin encabezado ni cola.

   * +24 a +31 = 16 + (8 a 15): utiliza los 4 bits de bajo orden del
     valor como el logaritmo del tamaño del búfer. La entrada debe
     incluir encabezado y cola gzip.

   * +40 a +47 = 32 + (8 a 15): utiliza los 4 bits de bajo orden del
     valor como el logaritmo del tamaño del búfer y acepta
     automáticamente el formato zlib o gzip.

   Al descomprimir una secuencia, el tamaño del búfer no debe ser
   menor al tamaño utilizado originalmente para comprimir la
   secuencia; el uso de un valor demasiado pequeño puede generar una
   excepción "error". El valor predeterminado *wbits* corresponde al
   tamaño más grande de búfer y requiere que se incluya encabezado y
   cola zlib.

   *bufsize* es el tamaño inicial del búfer utilizado para contener
   datos descomprimidos. Si se requiere más espacio, el tamaño del
   búfer aumentará según sea necesario, por lo que no hay que tomar
   este valor como exactamente correcto; al ajustarlo solo se
   guardarán algunas llamadas en "malloc()".

   Distinto en la versión 3.6: *wbits* y *bufsize* se pueden usar como
   argumentos de palabra clave.

zlib.decompressobj(wbits=MAX_WBITS[, zdict])

   Retorna un objeto de descompresión, que se utilizará para
   descomprimir flujos de datos que no caben en la memoria de una vez.

   El parámetro *wbits* controla el tamaño del búfer histórico (o el
   "tamaño de ventana") y qué formato de encabezado y cola se espera.
   Tiene el mismo significado que described for decompress().

   El parámetro *zdict* especifica un diccionario de compresión
   predefinido. Si se proporciona, este debe ser el mismo diccionario
   utilizado por el compresor que produjo los datos que se van a
   descomprimir.

   Nota:

     Si *zdict* es un objeto mutable (como "bytearray"), no se debe
     modificar su contenido entre la llamada "decompressobj()" y la
     primera llamada al método descompresor "decompress()".

   Distinto en la versión 3.3: Se agregó el parámetro *zdict*.

Los objetos de compresión admiten los siguientes métodos:

Compress.compress(data)

   Comprime *data*, y retorna al menos algunos de los datos
   comprimidos como un objeto de bytes. Estos datos deben concatenarse
   a la salida producida por cualquier llamada anterior al método
   "compress()". Algunas entradas pueden mantenerse en un búfer
   interno para su posterior procesamiento.

Compress.flush([mode])

   All pending input is processed, and a bytes object containing the
   remaining compressed output is returned.  *mode* can be selected
   from the constants "Z_NO_FLUSH", "Z_PARTIAL_FLUSH", "Z_SYNC_FLUSH",
   "Z_FULL_FLUSH", "Z_BLOCK", or "Z_FINISH", defaulting to "Z_FINISH".
   Except "Z_FINISH", all constants allow compressing further
   bytestrings of data, while "Z_FINISH" finishes the compressed
   stream and prevents compressing any more data.  After calling
   "flush()" with *mode* set to "Z_FINISH", the "compress()" method
   cannot be called again; the only realistic action is to delete the
   object.

Compress.copy()

   Retorna una copia del objeto compresor. Esto se puede utilizar para
   comprimir eficientemente un conjunto de datos que comparten un
   prefijo inicial común.

Distinto en la versión 3.8: Añadido "copy.copy()" y "copy.deepcopy()"
para el soporte de objetos de compresión.

Los objetos de descompresión admiten los siguientes métodos y
atributos:

Decompress.unused_data

   Un objeto de bytes que contiene todos los bytes restantes después
   de los datos comprimidos. Es decir, esto permanece "b """ hasta que
   esté disponible el último byte que contiene datos de compresión. Si
   la cadena de bytes completa resultó contener datos comprimidos, es
   "b""", un objeto de bytes vacío.

Decompress.unconsumed_tail

   Un objeto de bytes que contiene datos no procesados por la última
   llamada al método "descompress()" , debido a un desbordamiento del
   límite del búfer de datos descomprimidos. Estos datos aún no han
   sido procesados por la biblioteca zlib, por lo que debe enviarlos
   (potencialmente concatenando los datos nuevamente) mediante una
   llamada al método "descompress()" para obtener la salida correcta.

Decompress.eof

   Un valor booleano que indica si se ha alcanzado el final del flujo
   de datos comprimido.

   Esto hace posible distinguir entre un flujo comprimido
   correctamente y uno incompleto o truncado.

   Added in version 3.3.

Decompress.decompress(data, max_length=0)

   Descomprime *data*, retornando un objeto de bytes que contiene al
   menos parte de los datos descomprimidos en *string*. Estos datos
   deben concatenarse con la salida producida por cualquier llamada
   anterior al método "decompress()". Algunos de los datos de entrada
   pueden conservarse en búfer internos para su posterior
   procesamiento.

   Si el parámetro opcional *max_length* no es cero, el valor de
   retorno no será más largo que *max_length*. Esto puede significar
   que no toda la entrada comprimida puede procesarse; y los datos no
   consumidos se almacenarán en el atributo "unconsumed_tail". Esta
   cadena de bytes debe pasarse a una llamada posterior a
   "decompress()" si la descompresión ha de continuar. Si *max_length*
   es cero, toda la entrada se descomprime y "unconsumed_tail" queda
   vacío.

   Distinto en la versión 3.6: *max_length* puede ser utilizado como
   argumento de palabras clave.

Decompress.flush([length])

   Se procesan todas las entradas pendientes y se retorna un objeto de
   bytes que contiene el resto de los datos que se descomprimirán.
   Después de llamar a "flush()", no se puede volver a llamar al
   método "decompress()". La única acción posible es eliminar el
   objeto.

   El parámetro opcional *length* establece el tamaño inicial del
   búfer de salida.

Decompress.copy()

   Retorna una copia del objeto de descompresión. Puede usarlo para
   guardar el estado de la descompresión actual, de modo que pueda
   regresar rápidamente a esta ubicación más tarde.

Distinto en la versión 3.8: Añadido "copy.copy()" y "copy.deepcopy()"
para el soporte de objetos de compresión.

The following constants are available to configure compression and
decompression behavior:

zlib.DEFLATED

   The deflate compression method.

zlib.MAX_WBITS

   The maximum window size, expressed as a power of 2. For example, if
   "MAX_WBITS" is "15" it results in a window size of "32 KiB".

zlib.DEF_MEM_LEVEL

   The default memory level for compression objects.

zlib.DEF_BUF_SIZE

   The default buffer size for decompression operations.

zlib.Z_NO_COMPRESSION

   Compression level "0"; no compression.

   Added in version 3.6.

zlib.Z_BEST_SPEED

   Compression level "1"; fastest and produces the least compression.

zlib.Z_BEST_COMPRESSION

   Compression level "9"; slowest and produces the most compression.

zlib.Z_DEFAULT_COMPRESSION

   Default compression level ("-1"); a compromise between speed and
   compression. Currently equivalent to compression level "6".

zlib.Z_DEFAULT_STRATEGY

   Default compression strategy, for normal data.

zlib.Z_FILTERED

   Compression strategy for data produced by a filter (or predictor).

zlib.Z_HUFFMAN_ONLY

   Compression strategy that forces Huffman coding only.

zlib.Z_RLE

   Compression strategy that limits match distances to one (run-length
   encoding).

   This constant is only available if Python was compiled with zlib
   1.2.0.1 or greater.

   Added in version 3.6.

zlib.Z_FIXED

   Compression strategy that prevents the use of dynamic Huffman
   codes.

   This constant is only available if Python was compiled with zlib
   1.2.2.2 or greater.

   Added in version 3.6.

zlib.Z_NO_FLUSH

   Flush mode "0". No special flushing behavior.

   Added in version 3.6.

zlib.Z_PARTIAL_FLUSH

   Flush mode "1". Flush as much output as possible.

zlib.Z_SYNC_FLUSH

   Flush mode "2". All output is flushed and the output is aligned to
   a byte boundary.

zlib.Z_FULL_FLUSH

   Flush mode "3". All output is flushed and the compression state is
   reset.

zlib.Z_FINISH

   Flush mode "4". All pending input is processed, no more input is
   expected.

zlib.Z_BLOCK

   Flush mode "5". A deflate block is completed and emitted.

   This constant is only available if Python was compiled with zlib
   1.2.2.2 or greater.

   Added in version 3.6.

zlib.Z_TREES

   Flush mode "6", for inflate operations. Instructs inflate to return
   when it gets to the next deflate block boundary.

   This constant is only available if Python was compiled with zlib
   1.2.3.4 or greater.

   Added in version 3.6.

La información sobre la versión de la biblioteca zlib en uso está
disponible a través de las siguientes constantes:

zlib.ZLIB_VERSION

   Versión de la biblioteca zlib utilizada al compilar el módulo.
   Puede ser diferente de la biblioteca zlib utilizada actualmente por
   el sistema, que puede ver en "ZLIB_RUNTIME_VERSION".

zlib.ZLIB_RUNTIME_VERSION

   Cadena que contiene la versión de la biblioteca zlib utilizada
   actualmente por el intérprete.

   Added in version 3.3.

zlib.ZLIBNG_VERSION

   The version string of the zlib-ng library that was used for
   building the module if zlib-ng was used. When present, the
   "ZLIB_VERSION" and "ZLIB_RUNTIME_VERSION" constants reflect the
   version of the zlib API provided by zlib-ng.

   If zlib-ng was not used to build the module, this constant will be
   absent.

   Added in version 3.14.

Ver también:

  Módulo "gzip"
     Lectura y escritura de los archivos en formato **gzip**.

  https://www.zlib.net
     Página oficial de la biblioteca zlib.

  https://www.zlib.net/manual.html
     El manual de zlib explica la semántica y el uso de las numerosas
     funciones de la biblioteca.

  In case gzip (de)compression is a bottleneck, the python-isal
  package speeds up (de)compression with a mostly compatible API.
