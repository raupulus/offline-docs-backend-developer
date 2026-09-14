---
title: '"codecs" --- Codec registry and base classes'
source_url: https://docs.python.org/es/3
source_path: library/codecs.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1980
---

# "codecs" --- Codec registry and base classes

**Código fuente:** Lib/codecs.py

======================================================================

Este módulo define las clases base para los códecs estándar de Python
(codificadores y decodificadores) y proporciona acceso al registro
interno de códecs de Python, que administra el códec y el proceso de
búsqueda del manejo de errores. La mayoría de los códecs estándar son
*text encodings*, que codifican texto a bytes (y decodifican bytes a
texto), pero también se proporcionan códecs que codifican texto a
texto y bytes a bytes. Los códecs personalizados pueden codificar y
decodificar entre tipos arbitrarios, pero algunas características del
módulo están restringidas para usarse específicamente con *text
encodings* o con códecs que codifican a "bytes".

El módulo define las siguientes funciones para codificar y decodificar
con cualquier códec:

codecs.encode(obj, encoding='utf-8', errors='strict')

   Codifica *obj* utilizando el códec registrado para *encoding*.

   Se pueden dar *errors* para establecer el esquema de manejo de
   errores deseado. El manejador de errores predeterminado es
   "'estricto'", lo que significa que los errores de codificación
   provocan "ValueError" (o una subclase más específica del códec,
   como "UnicodeEncodeError"). Consulte Clases Base de Códec para
   obtener más información sobre el manejo de errores de códec.

codecs.decode(obj, encoding='utf-8', errors='strict')

   Decodifica *obj* utilizando el códec registrado para *encoding*.

   Se pueden dar *errors* para establecer el esquema de manejo de
   errores deseado. El manejador de errores predeterminado es
   "'estricto'", lo que significa que los errores de decodificación
   generan "ValueError" (o una subclase más específica de códec, como
   "UnicodeDecodeError"). Consulte Clases Base de Códec para obtener
   más información sobre el manejo de errores de códec.

codecs.charmap_build(string)

   Return a mapping suitable for encoding with a custom single-byte
   encoding. Given a "str" *string* of up to 256 characters
   representing a decoding table, returns either a compact internal
   mapping object "EncodingMap" or a "dictionary" mapping character
   ordinals to byte values. Raises a "TypeError" on invalid input.

Los detalles completos de cada códec también se pueden consultar
directamente:

codecs.lookup(encoding, /)

   Busca la información de códec en el registro de códec de Python y
   retorna un objeto "CodecInfo" como se define a continuación.

   Las codificaciones se buscan primero en la memoria caché del
   registro. Si no se encuentran, se explora la lista de funciones de
   búsqueda registradas. Si no se encuentran objetos "CodecInfo", se
   lanza un "LookupError". De lo contrario, el objeto "CodecInfo" se
   almacena en la memoria caché y se retorna a quien llama.

class codecs.CodecInfo(encode, decode, streamreader=None, streamwriter=None, incrementalencoder=None, incrementaldecoder=None, name=None)

   Detalles de códec al buscar el registro de códec. Los argumentos
   del constructor se almacenan en atributos del mismo nombre:

   name

      El nombre de la codificación.

   encode
   decode

      Las funciones de codificación y decodificación sin estado. Deben
      ser funciones o métodos que tengan la misma interfaz que los
      métodos "encode()" y "decode()" de instancias de *Codec* (ver
      Codec Interface). Se espera que las funciones o métodos
      funcionen en modo sin estado.

   incrementalencoder
   incrementaldecoder

      Clases de codificación y decodificación incremental o funciones
      de fábrica. Deben proporcionar la interfaz definida por las
      clases base "IncrementalEncoder" y "IncrementalDecoder",
      respectivamente. Los códecs incrementales pueden mantener el
      estado.

   streamwriter
   streamreader

      Las clases *stream*, tanto *writer* como *reader* o funciones de
      fábrica. Estos tienen que proporcionar la interfaz definida por
      las clases base "StreamWriter" y "StreamReader",
      respectivamente. Los códecs de flujo pueden mantener el estado.

Para simplificar el acceso a los diversos componentes de códec, el
módulo proporciona estas funciones adicionales que utilizan "lookup()"
para la búsqueda de códec:

codecs.getencoder(encoding)

   Busca el códec para la codificación dada y retorna su función de
   codificador.

   Lanza un "LookupError" en caso de que no se encuentre la
   codificación.

codecs.getdecoder(encoding)

   Busca el códec para la codificación dada y retorna su función de
   decodificador.

   Lanza un "LookupError" en caso de que no se encuentre la
   codificación.

codecs.getincrementalencoder(encoding)

   Busca el códec para la codificación dada y retorna su clase de
   codificador incremental o función de fábrica.

   Lanza un "LookupError" en caso de que no se encuentre la
   codificación o el códec no admita un codificador incremental.

codecs.getincrementaldecoder(encoding)

   Busca el códec para la codificación dada y retorna su clase de
   decodificador incremental o función de fábrica.

   Lanza un "LookupError" en caso de que no se encuentre la
   codificación o el códec no admita un decodificador incremental.

codecs.getreader(encoding)

   Busca el códec para la codificación dada y retorna su clase
   "StreamReader" o función de fábrica.

   Lanza un "LookupError" en caso de que no se encuentre la
   codificación.

codecs.getwriter(encoding)

   Busca el códec para la codificación dada y retorna su clase
   "StreamWriter" o función de fábrica.

   Lanza un "LookupError" en caso de que no se encuentre la
   codificación.

Los códecs personalizados se ponen a disposición registrando una
función de búsqueda de códecs adecuada:

codecs.register(search_function, /)

   Registra una función de búsqueda de códec. Se espera que las
   funciones de búsqueda tomen un argumento, que sea el nombre de
   codificación en minúsculas con guiones y espacios convertidos a
   guiones bajos, y que retorne un objeto "CodecInfo". En caso de que
   una función de búsqueda no pueda encontrar una codificación dada,
   debería retornar "None".

   Distinto en la versión 3.9: Guiones y espacios se convierten a
   guiones bajos.

codecs.unregister(search_function, /)

   Anula el registro de una función de búsqueda de códecs y elimina el
   caché del registro. Si la función de búsqueda no está registrada,
   no hace nada.

   Added in version 3.10.

Mientras que la función incorporada "open()" y el módulo asociado "io"
son el enfoque recomendado para trabajar con archivos de texto
codificados, este módulo proporciona funciones y clases de utilidad
adicionales que permiten el uso de una gama más amplia de códecs
cuando se trabaja con archivos binarios:

codecs.open(filename, mode='r', encoding=None, errors='strict', buffering=-1)

   Abre un archivo codificado utilizando el modo dado y retorna una
   instancia de "StreamReaderWriter", proporcionando
   codificación/decodificación transparente. El modo de archivo
   predeterminado es "'r'", que significa abrir el archivo en modo de
   lectura.

   Nota:

     Si el valor de *encoding* no es "None", entonces, los archivos
     codificados subyacentes siempre se abren en modo binario. No se
     realiza ninguna conversión automática de "'\n'" al leer y
     escribir. El argumento *mode* puede ser cualquier modo binario
     aceptable para la función integrada "open()"; la "'b'" se añade
     automáticamente.

   *encoding* especifica la codificación que se utilizará para el
   archivo. Se permite cualquier codificación que codifique y
   decodifique desde bytes, y los tipos de datos admitidos por los
   métodos de archivo dependen del códec utilizado.

   pueden proporcionarse *errors* para definir el manejo de errores.
   El valor predeterminado es "'estricto'", lo que hace que se genere
   un "ValueError" en caso de que ocurra un error de codificación.

   *buffering* tiene el mismo significado que para la función
   incorporada "open()". Su valor predeterminado es -1, lo que
   significa que se utilizará el tamaño predeterminado del búfer.

   Distinto en la versión 3.11: El modo "'U'" ha sido eliminado.

   Obsoleto desde la versión 3.14: "codecs.open()" has been superseded
   by "open()".

codecs.EncodedFile(file, data_encoding, file_encoding=None, errors='strict')

   Retorna una instancia de "StreamRecoder", una versión envuelta de
   *file* que proporciona transcodificación transparente. El archivo
   original se cierra cuando se cierra la versión empaquetada.

   Los datos escritos en el archivo empaquetado se decodifican de
   acuerdo con la *data_encoding* dada y luego se escriben en el
   archivo original como bytes usando *file_encoding*. Los bytes
   leídos del archivo original se decodifican según *file_encoding*, y
   el resultado se codifica utilizando *data_encoding*.

   Si no se proporciona *file_encoding*, el valor predeterminado es
   *data_encoding*.

   Pueden proporcionarse *errors* para definir el manejo de errores.
   Su valor predeterminado es "'estricto'", lo que hace que se genere
   "ValueError" en caso de que ocurra un error de codificación.

codecs.iterencode(iterator, encoding, errors='strict', **kwargs)

   Uses an incremental encoder to iteratively encode the input
   provided by *iterator*. *iterator* must yield "str" objects. This
   function is a *generator*. The *errors* argument (as well as any
   other keyword argument) is passed through to the incremental
   encoder.

   Esta función requiere que el códec acepte texto en objetos "str"
   para codificar. Por lo tanto, no admite codificadores de bytes a
   bytes, como "base64_codec".

codecs.iterdecode(iterator, encoding, errors='strict', **kwargs)

   Uses an incremental decoder to iteratively decode the input
   provided by *iterator*. *iterator* must yield "bytes" objects. This
   function is a *generator*. The *errors* argument (as well as any
   other keyword argument) is passed through to the incremental
   decoder.

   Esta función requiere que el códec acepte objetos "bytes" para
   decodificar. Por lo tanto, no admite codificadores de texto a texto
   como "rot_13", aunque "rot_13" puede usarse de manera equivalente
   con "iterencode()".

codecs.readbuffer_encode(buffer, errors=None, /)

   Return a "tuple" containing the raw bytes of *buffer*, a buffer-
   compatible object or "str" (encoded to UTF-8 before processing),
   and their length in bytes.

   The *errors* argument is ignored.

      >>> codecs.readbuffer_encode(b"Zito")
      (b'Zito', 4)

El módulo también proporciona las siguientes constantes que son útiles
para leer y escribir en archivos dependientes de la plataforma:

codecs.BOM
codecs.BOM_BE
codecs.BOM_LE
codecs.BOM_UTF8
codecs.BOM_UTF16
codecs.BOM_UTF16_BE
codecs.BOM_UTF16_LE
codecs.BOM_UTF32
codecs.BOM_UTF32_BE
codecs.BOM_UTF32_LE

   Estas constantes definen varias secuencias de bytes, que son marcas
   de orden de bytes Unicode (BOM) para varias codificaciones. Se
   utilizan en flujos de datos UTF-16 y UTF-32 para indicar el orden
   de bytes utilizado, y en UTF-8 como firma Unicode. "BOM_UTF16" es
   "BOM_UTF16_BE" o "BOM_UTF16_LE" dependiendo del orden de bytes
   nativo de la plataforma, "BOM" es un alias para "BOM_UTF16",
   "BOM_LE" para "BOM_UTF16_LE" y "BOM_BE" para "BOM_UTF16_BE". Los
   otros representan la lista de materiales en las codificaciones
   UTF-8 y UTF-32.

## Clases Base de Códec

The "codecs" module defines a set of base classes which define the
interfaces for working with codec objects, and can also be used as the
basis for custom codec implementations.

Cada códec tiene que definir cuatro interfaces para que pueda usarse
como códec en Python: codificador sin estado, decodificador sin
estado, lector de flujo y escritor de flujo. El lector de flujo y los
escritores suelen reutilizar el codificador/decodificador sin estado
para implementar los protocolos de archivo. Los autores de códecs
también necesitan definir cómo manejará los errores de codificación y
decodificación.

### Manejadores de errores

Para simplificar y estandarizar el manejo de errores, los códecs
pueden implementar diferentes esquemas de manejo de errores aceptando
el argumento de cadena *errors*:

>>> 'German ß, ♬'.encode(encoding='ascii', errors='backslashreplace')
b'German \\xdf, \\u266c'
>>> 'German ß, ♬'.encode(encoding='ascii', errors='xmlcharrefreplace')
b'German &#223;, &#9836;'

Los siguientes manejadores de errores se pueden emplear con todos los
códecs Python Codificaciones estándar:

+---------------------------+-------------------------------------------------+
| Valor                     | Significado                                     |
|===========================|=================================================|
| "'strict'"                | Lanza "UnicodeError" (o una subclase), este es  |
|                           | el valor predeterminado. Implementado en        |
## |                           | "strictly_errors()".                            |

| "'ignore'"                | Ignore los datos mal formados y continúe sin    |
|                           | previo aviso. Implementado en                   |
## |                           | "ignore_errors()".                              |

| "'replace'"               | Sustituir con un marcador de reemplazo. Al      |
|                           | codificar, emplear "?" (carácter ASCII). Al     |
|                           | decodificar, usar "�" (U+FFFD, el CARÁCTER DE   |
|                           | REEMPLAZO oficial). Implementado en             |
## |                           | "replace_errors()".                             |

| "'backslashreplace'"      | Reemplazar con secuencias de escape mediante    |
|                           | barra invertida. Al codificar, emplear la forma |
|                           | hexadecimal del punto de código Unicode con los |
|                           | formatos "\x*hh*" "\u*xxxx*" "\U*xxxxxxxx*". Al |
|                           | decodificar, usa la forma hexadecimal del valor |
|                           | del byte con el formato "\x*hh*". Implementado  |
## |                           | en "backslashreplace_errors()".                 |

| "'surrogateescape'"       | En la decodificación, reemplace el byte con     |
|                           | código sustituto individual que va desde        |
|                           | "U+DC80" a "U+DCFF". Este código se volverá a   |
|                           | convertir en el mismo byte cuando se use el     |
|                           | manejador de errores "'sustituto de paisaje'"   |
|                           | al codificar los datos. (Ver **PEP 383** para   |
## |                           | más información).                               |

Los siguientes manejadores de errores solo son aplicables a
*codificaciones de texto*:

+---------------------------+-------------------------------------------------+
| Valor                     | Significado                                     |
|===========================|=================================================|
| "'xmlcharrefreplace'"     | Reemplazar con una referencia de carácter       |
|                           | numérico XML/HTML, que es una forma decimal del |
|                           | punto de código Unicode con formato "&#*num*;". |
## |                           | Implementado en "xmlcharrefreplace_errors()".   |

| "'namereplace'"           | Reemplazar con secuencias de escape "\N{...}",  |
|                           | lo que aparece entre llaves, es la propiedad    |
|                           | Nombre de la Base de datos de Caracteres        |
|                           | Unicode. Implementado en                        |
## |                           | "namereplace_errors()".                         |

Además, el siguiente manejador de errores es específico de los códecs
dados:

+---------------------+--------------------------+---------------------------------------------+
| Valor               | Códecs                   | Significado                                 |
|=====================|==========================|=============================================|
| "'surrogatepass'"   | utf-8, utf-16, utf-32,   | Permite la codificación y decodificación    |
|                     | utf-16-be, utf-16-le,    | del punto de código sustituto ("U+D800" -   |
|                     | utf-32-be, utf-32-le     | "U+DFFF") como punto de código normal. De   |
|                     |                          | lo contrario, estos códecs tratan la        |
|                     |                          | presencia de un punto de código sustituto   |
## |                     |                          | en "str" como un error.                     |

Added in version 3.1: Los manejadores de errores "'surrogateescape'" y
"'surrogatepass'".

Distinto en la versión 3.4: Los manejadores de errores
"'surrogatepass'" ahora funcionan con los códecs utf-16* y utf-32*.

Added in version 3.5: El manejador de errores "'namereplace'".

Distinto en la versión 3.5: El manejador de errores
"'backslashreplace'" ahora funciona con decodificación y traducción.

El conjunto de valores permitidos puede ampliarse registrando un nuevo
manejador de errores con nombre:

codecs.register_error(name, error_handler, /)

   Registre la función de manejo de errores *error_handler* bajo el
   nombre *name*. Se invocará el argumento *error_handler* durante la
   codificación y decodificación en caso de error, cuando *name* se
   especifica como el parámetro de errores.

   Para la codificación, se llamará a *error_handler* con una
   instancia "UnicodeEncodeError", que contiene información sobre la
   ubicación del error. El manejador de errores debe generar esta o
   una excepción diferente, o retornar una tupla con un reemplazo para
   la parte no codificable de la entrada y una posición donde la
   codificación debe continuar. El reemplazo puede ser "str" o
   "bytes". Si el reemplazo son bytes, el codificador simplemente los
   copiará en el búfer de salida. Si el reemplazo es una cadena de
   caracteres, el codificador codificará el reemplazo. La codificación
   continúa en la entrada original en la posición especificada. Los
   valores de posición negativos se tratarán como relativos al final
   de la cadena de entrada. Si la posición resultante está fuera del
   límite, se lanzará "IndexError".

   La decodificación y la traducción funcionan de manera similar,
   excepto que "UnicodeDecodeError" o "UnicodeTranslateError" se
   pasarán al manejador y el sustituto del manejador de errores se
   colocará directamente en la salida.

Los manejadores de errores registrados previamente (incluidos los
manejadores de error estándar) se pueden buscar por nombre:

codecs.lookup_error(name, /)

   Retorna el manejador de errores previamente registrado con el
   nombre *name*.

   Lanza un "LookupError" en caso de que no se pueda encontrar el
   controlador.

Los siguientes manejadores de errores estándar también están
disponibles como funciones de nivel de módulo:

codecs.strict_errors(exception)

   Implementa el manejo de errores "'strict'".

   Cada error de codificación o decodificación genera un
   "UnicodeError".

codecs.ignore_errors(exception)

   Implementa el manejo de errores "'ignore'".

   Los datos con formato incorrecto se ignoran; la codificación o
   decodificación continúa sin previo aviso.

codecs.replace_errors(exception)

   Implementa el manejo de errores "'replace'" .

   Sustituye "?" (carácter ASCII) por errores de codificación o "�"
   (U+FFFD, el CARÁCTER DE REEMPLAZO oficial) por errores de
   decodificación.

codecs.backslashreplace_errors(exception)

   Implementa el manejador de errores "'backslashreplace'".

   Los datos con formato incorrecto se reemplazan por una secuencia de
   escape con barra invertida. Al codificar, emplea la forma
   hexadecimal del punto de código Unicode con los formatos "\x*hh*"
   "\u*xxxx*" "\U*xxxxxxxx*". Al decodificar, usa la forma hexadecimal
   del valor del byte con el formato "\x*hh*".

   Distinto en la versión 3.5: Funciona con la decodificación y
   traducción.

codecs.xmlcharrefreplace_errors(exception)

   Implementa el manejador de errores "'xmlcharrefreplace'" (solo para
   codificar dentro de *text encoding*).

   El carácter no codificable se reemplaza por una referencia de
   carácter numérico XML/HTML adecuada, que es una forma decimal del
   punto de código Unicode con formato "&#*num*;" .

codecs.namereplace_errors(exception)

   Implementa el manejo de errores "'namereplace" (solo para codificar
   dentro de *text encoding*).

   El carácter no codificable se reemplaza por una secuencia de escape
   "\N{...}". El conjunto de caracteres que aparecen entre llaves es
   la propiedad Nombre de la Base de datos de Caracteres Unicode. Por
   ejemplo, la letra minúscula alemana "'ß'" se convertirá en la
   secuencia de bytes "\N{LATIN SMALL LETTER SHARP S}" .

   Added in version 3.5.

### Codificación y decodificación sin estado

La clase base "Codec" define estos métodos que también definen las
interfaces de función del codificador y decodificador sin estado:

class codecs.Codec

   encode(input, errors='strict')

      Codifica el objeto *input* y retorna una tupla (objeto de
      salida, longitud consumida). Por ejemplo *text encoding*
      convierte un objeto de cadena de caracteres en un objeto de
      bytes utilizando una codificación de juego de caracteres
      particular (por ejemplo,``cp1252`` o "iso-8859-1").

      El argumento *errors* define el manejo de errores a aplicar. El
      valor predeterminado es el manejo "estricto".

      Es posible que el método no almacene estado en la instancia
      "Codec". Use "StreamWriter" para códecs que deben mantener el
      estado para que la codificación sea eficiente.

      El codificador debe poder manejar la entrada de longitud cero y
      retornar un objeto vacío del tipo de objeto de salida en esta
      situación.

   decode(input, errors='strict')

      Decodifica el objeto *input* y retorna una tupla (objeto de
      salida, longitud consumida). Por ejemplo, para un *codificación
      de texto*, la decodificación convierte un objeto de bytes
      codificado usando una codificación de juego de caracteres
      particular en un objeto de cadena de caracteres.

      Para codificaciones de texto y códecs de bytes a bytes, *input*
      debe ser un objeto de bytes o uno que proporcione la interfaz de
      búfer de solo lectura, por ejemplo, objetos de búfer y archivos
      mapeados en memoria.

      El argumento *errors* define el manejo de errores a aplicar. El
      valor predeterminado es el manejo "estricto".

      Es posible que el método no almacene estado en la instancia de
      "Codec". Use "StreamReader" para códecs que deben mantener el
      estado para que la decodificación sea eficiente.

      El decodificador debe poder manejar la entrada de longitud cero
      y retornar un objeto vacío del tipo de objeto de salida en esta
      situación.

### Codificación y decodificación incrementales

Las clases "IncrementalEncoder" y "IncrementalDecoder" proporcionan la
interfaz básica para la codificación y decodificación incrementales.
La codificación/decodificación de la entrada no se realiza con una
llamada a la función de codificador/decodificador sin estado, sino con
varias llamadas al método "encode()"/"decode()" del codificador
incremental /decodificador. El codificador/decodificador incremental
realiza un seguimiento del proceso de codificación/decodificación
durante las llamadas a métodos.

La salida combinada de las llamadas al método "encode()"/"decode()" es
el mismo que si todas las entradas individuales se unieran en una, y
esta entrada se codificara/decodificara con codificador/decodificador
sin estado.

#### Objetos IncrementalEncoder

La clase "IncrementalEncoder" se usa para codificar una entrada en
varios pasos. Define los siguientes métodos que cada codificador
incremental debe definir para ser compatible con el registro de códec
Python.

class codecs.IncrementalEncoder(errors='strict')

   Constructor para una clase instancia de "IncrementalEncoder".

   Todos los codificadores incrementales deben proporcionar esta
   interfaz de constructor. Son libres de agregar argumentos de
   palabras clave adicionales, pero el registro de códecs de Python
   solo utiliza los definidos aquí.

   La clase "IncrementalEncoder" puede implementar diferentes esquemas
   de manejo de errores al proporcionar el argumento de palabra clave
   *errors*. Ver Manejadores de errores para posibles valores.

   El argumento *errors* se asignará a un atributo del mismo nombre.
   La asignación a este atributo hace posible cambiar entre diferentes
   estrategias de manejo de errores durante la vida útil del objeto
   "IncrementalEncoder".

   encode(object, final=False)

      Codifica *object* (teniendo en cuenta el estado actual del
      codificador) y retorna el objeto codificado resultante. Si esta
      es la última llamada a "encode()" *final* debe ser verdadero (el
      valor predeterminado es falso).

   reset()

      Restablece el codificador al estado inicial. La salida se
      descarta: llama a ".encode(object, final=True)", pasando un byte
      vacío o una cadena de texto si es necesario, para restablecer el
      codificador y obtener la salida.

   getstate()

      Retorna el estado actual del codificador que debe ser un número
      entero. La implementación debe asegurarse de que "0" sea el
      estado más común. (Los estados que son más complicados que los
      enteros se pueden convertir en un entero al
      empaquetar/serializar el estado y codificar los bytes de la
      cadena resultante en un entero).

   setstate(state)

      Establece el estado del codificador en *state*. *state* debe ser
      un estado de codificador retornado por "getstate()".

#### Objetos IncrementalDecoder

La clase "IncrementalDecoder" se usa para decodificar una entrada en
varios pasos. Define los siguientes métodos que cada decodificador
incremental debe definir para ser compatible con el registro de códec
Python.

class codecs.IncrementalDecoder(errors='strict')

   Constructor para una instancia de "IncrementalDecoder".

   Todos los decodificadores incrementales deben proporcionar esta
   interfaz de constructor. Son libres de agregar argumentos de
   palabras clave adicionales, pero el registro de códecs de Python
   solo utiliza los definidos aquí.

   La clase "IncrementalDecoder" puede implementar diferentes esquemas
   de manejo de errores al proporcionar el argumento de palabra clave
   *errors*. Ver Manejadores de errores para posibles valores.

   El argumento *errors* se asignará a un atributo del mismo nombre.
   La asignación a este atributo hace posible cambiar entre diferentes
   estrategias de manejo de errores durante la vida útil del objeto
   "IncrementalDecoder".

   decode(object, final=False)

      Decodifica *object* (teniendo en cuenta el estado actual del
      decodificador) y retorna el objeto decodificado resultante. Si
      esta es la última llamada a "decode()" *final* debe ser
      verdadero (el valor predeterminado es falso). Si *final* es
      verdadero, el decodificador debe decodificar la entrada por
      completo y debe vaciar todos los búferes. Si esto no es posible
      (por ejemplo, debido a secuencias de bytes incompletas al final
      de la entrada), debe iniciar el manejo de errores al igual que
      en el caso sin estado (lo que podría generar una excepción).

   reset()

      Restablece el decodificador al estado inicial.

   getstate()

      Retorna el estado actual del decodificador. Debe ser una tupla
      con dos elementos, el primero debe ser el búfer que contiene la
      entrada aún sin codificar. El segundo debe ser un número entero
      y puede ser información de estado adicional. (La implementación
      debe asegurarse de que "0" sea la información de estado
      adicional más común). Si esta información de estado adicional es
      "0", debe ser posible establecer el decodificador en el estado
      que no tiene entrada almacenada y "0" como información de estado
      adicional, de modo que alimentar la entrada previamente
      almacenada en el búfer al decodificador la retorna al estado
      anterior sin producir ninguna salida. (La información de estado
      adicional que es más complicada que los enteros se puede
      convertir en un entero al empaquetar/serializar la información y
      codificar los bytes de la cadena resultante en un entero).

   setstate(state)

      Establezca el estado del decodificador en *state*. *state* debe
      ser un estado de decodificador retornado por "getstate()".

### Codificación y decodificación de flujos

The "StreamWriter" and "StreamReader" classes provide generic working
interfaces which can be used to implement new encoding submodules very
easily. See "encodings.utf_8" for an example of how this is done.

#### Objetos StreamWriter

La clase "StreamWriter" es una subclase de "Codec" y define los
siguientes métodos que cada escritor del flujo debe definir para ser
compatible con el registro de códecs Python.

class codecs.StreamWriter(stream, errors='strict')

   Constructor para una instancia de "StreamWriter".

   Todos los escritores de flujos deben proporcionar esta interfaz de
   constructor. Son libres de agregar argumentos de palabras clave
   adicionales, pero el registro de códecs de Python solo utiliza los
   definidos aquí.

   El argumento *stream* debe ser un objeto tipo archivo abierto para
   escribir texto o datos binarios, según corresponda para el códec
   específico.

   La clase "StreamWriter" puede implementar diferentes esquemas de
   manejo de errores al proporcionar el argumento de palabra clave
   *errors*. Consulte Manejadores de errores para ver los manejadores
   de errores estándar que puede admitir el códec de flujo subyacente.

   El argumento *errors* se asignará a un atributo del mismo nombre.
   La asignación a este atributo hace posible cambiar entre diferentes
   estrategias de manejo de errores durante la vida útil del objeto
   "StreamWriter".

   write(object)

      Escribe el contenido del objeto codificado en el flujo.

   writelines(list)

      Escribe una lista concatenada de cadenas en el flujo
      (posiblemente reutilizando el método "write()"). No se admiten
      iterables infinitos o muy grandes. Los códecs estándar de bytes
      a bytes no admiten este método.

   reset()

      Restablece los búfers de códec utilizados para mantener el
      estado interno.

      Llamar a este método debería garantizar que los datos en la
      salida se pongan en un estado limpio que permita agregar datos
      nuevos sin tener que volver a escanear todo el flujo para
      recuperar el estado.

Además de los métodos anteriores, la clase "StreamWriter" también debe
heredar todos los demás métodos y atributos del flujo subyacente.

#### Objetos StreamReader

La clase "StreamReader" es una subclase de "Codec" y define los
siguientes métodos que cada lector de flujo debe definir para ser
compatible con el registro de códecs de Python.

class codecs.StreamReader(stream, errors='strict')

   Constructor para una instancia de "StreamReader".

   Todos los lectores de flujo deben proporcionar esta interfaz de
   constructor. Son libres de agregar argumentos de palabras clave
   adicionales, pero el registro de códecs de Python solo utiliza los
   definidos aquí.

   El argumento *stream* debe ser un objeto tipo archivo abierto para
   leer texto o datos binarios, según corresponda para el códec
   específico.

   La clase "StreamReader" puede implementar diferentes esquemas de
   manejo de errores al proporcionar el argumento de palabra clave
   *errors*. Consulte Manejadores de errores para ver los manejadores
   de errores estándar que puede admitir el códec de flujo subyacente.

   El argumento *errors* se asignará a un atributo del mismo nombre.
   La asignación a este atributo hace posible cambiar entre diferentes
   estrategias de manejo de errores durante la vida útil del objeto
   "StreamReader".

   El conjunto de valores permitidos para el argumento *errors* se
   puede ampliar con "register_error()".

   read(size=-1, chars=-1, firstline=False)

      Decodifica datos del flujo y retorna el objeto resultante.

      El argumento *chars* indica el número de puntos de código
      decodificados o bytes a retornar. El método "read()" nunca
      retornará más datos de los solicitados, pero podría retornar
      menos, si no hay suficientes disponibles.

      El argumento *size* indica el número máximo aproximado de bytes
      codificados o puntos de código para leer para la decodificación.
      El decodificador puede modificar esta configuración según
      corresponda. El valor predeterminado -1 indica leer y
      decodificar tanto como sea posible. Este parámetro está diseñado
      para evitar tener que decodificar archivos grandes en un solo
      paso.

      La bandera *firstline* indica que sería suficiente retornar solo
      la primera línea, si hay errores de decodificación en las líneas
      posteriores.

      El método debe usar una estrategia de lectura codiciosa, lo que
      significa que debe leer la mayor cantidad de datos permitidos
      dentro de la definición de la codificación y el tamaño dado, por
      ejemplo si las terminaciones de codificación opcionales o los
      marcadores de estado están disponibles en la transmisión,
      también deben leerse.

   readline(size=None, keepends=True)

      Lee una línea del flujo de entrada y retorna los datos
      decodificados.

      *size*, si se da, se pasa como argumento de tamaño al método
      "read()" del *stream*.

      Si *keepends* es falso, las terminaciones de línea se eliminarán
      de las líneas retornadas.

   readlines(sizehint=None, keepends=True)

      Lee todas las líneas disponibles en el flujo de entrada y las
      retorna como una lista de líneas.

      Los finales de línea se implementan utilizando el método
      "decode()" del códec y se incluyen en las entradas de la lista
      si *keepends* es verdadero.

      *sizehint*, si se proporciona, se pasa como argumento *size* al
      método "read()" del *stream*.

   reset()

      Restablece los búfers de códec utilizados para mantener el
      estado interno.

      Tenga en cuenta que ningún reposicionamiento de flujo debe
      suceder. Este método está destinado principalmente a poder
      recuperarse de errores de decodificación.

Además de los métodos anteriores, la clase "StreamReader" también debe
heredar todos los demás métodos y atributos del flujo subyacente.

#### Objetos StreamReaderWriter

La clase "StreamReaderWriter" es una clase de conveniencia que permite
envolver flujos que funcionan tanto en modo de lectura como de
escritura.

El diseño es tal que uno puede usar las funciones de fábrica
retornadas por la función "lookup()" para construir la instancia.

class codecs.StreamReaderWriter(stream, Reader, Writer, errors='strict')

   Crea una instancia de "StreamReaderWriter". *stream* debe ser un
   objeto similar a un archivo. *Reader* y *Writer* deben ser
   funciones o clases de fábrica que proporcionen la interfaz
   "StreamReader" y "StreamWriter" respectivamente. El manejo de
   errores se realiza de la misma manera que se define para los
   lectores y escritores de flujos.

Las instancias "StreamReaderWriter" definen las interfaces combinadas
de "StreamReader" y clases "StreamWriter". Heredan todos los demás
métodos y atributos del flujo subyacente.

#### Objetos StreamRecoder

La clase "StreamRecoder" traduce datos de una codificación a otra, lo
que a veces es útil cuando se trata de diferentes entornos de
codificación.

El diseño es tal que uno puede usar las funciones de fábrica
retornadas por la función "lookup()" para construir la instancia.

class codecs.StreamRecoder(stream, encode, decode, Reader, Writer, errors='strict')

   Creates a "StreamRecoder" instance which implements a two-way
   conversion: *encode* and *decode* work on the frontend — the data
   visible to code calling "read()" and "write()", while *Reader* and
   *Writer* work on the backend — the data in *stream*.

   Puede usar estos objetos para realizar transcodificaciones
   transparentes, por ejemplo, de Latin-1 a UTF-8 y viceversa.

   El argumento *stream* debe ser un objeto similar a un archivo.

   Los argumentos *encode* y *decode* deben cumplir con la interfaz de
   "Codec". *Reader* y *Writer* deben ser funciones o clases de
   fábrica que proporcionen objetos de la interfaz "StreamReader" y
   "StreamWriter" respectivamente.

   El manejo de errores se realiza de la misma manera que se define
   para los lectores y escritores de flujos.

las instancias "StreamRecoder" definen las interfaces combinadas de
las clases "StreamReader" y "StreamWriter". Heredan todos los demás
métodos y atributos del flujo subyacente.

## Codificaciones y Unicode

Las cadenas de caracteres se almacenan internamente como secuencias de
puntos de código en el rango "U+0000"--"U+10FFFF". (Consultar **PEP
393** para obtener más detalles sobre la implementación). Una vez
utilizado un objeto de cadena de caracteres fuera de la CPU y de la
memoria, la *endianness* y cómo se almacenan estas matrices como bytes
se convierte en un problema. Al igual que con otros códecs, la
serialización de una cadena en una secuencia de bytes se conoce como
codificación, y la recreación de la cadena a partir de los bytes se
conoce como decodificación. Hay múltiples códecs para la serialización
de texto, a los que se puede consultar colectivamente mediante *text
encodings*.

La codificación de texto más simple (llamada "'latin-1'" o
"'iso-8859-1'") asigna los puntos de código 0--255 a los bytes "0x0"
-- "0xff", lo que significa que un objeto de cadena de caracteres que
contiene puntos de código encima de "U+00FF" no se puede codificar con
este códec. Al hacerlo, lanzará un "UnicodeEncodeError" que se parece
a lo siguiente (aunque los detalles del mensaje de error pueden
diferir): "UnicodeEncodeError: 'latin-1' codec can't encode character
'\u1234' 'in position 3: ordinal not in range(256)".

Hay otro grupo de codificaciones (las llamadas codificaciones de mapa
de caracteres) que eligen un subconjunto diferente de todos los puntos
de código Unicode y cómo estos puntos de código se asignan a los bytes
"0x0" -- "0xff". Para ver cómo se hace esto, simplemente abra, por
ejemplo "encodings/cp1252.py" (que es una codificación que se usa
principalmente en Windows). Hay una cadena constante con 256
caracteres que le muestra qué carácter está asignado a qué valor de
byte.

All of these encodings can only encode 256 of the 1114112 code points
defined in Unicode. A simple and straightforward way that can store
each Unicode code point, is to store each code point as four
consecutive bytes. There are two possibilities: store the bytes in big
endian or in little endian order. These two encodings are called
"UTF-32-BE" and "UTF-32-LE" respectively. Their disadvantage is that
if, for example, you use "UTF-32-BE" on a little endian machine you
will always have to swap bytes on encoding and decoding. Python's
"UTF-16" and "UTF-32" codecs avoid this problem by using the
platform's native byte order when no BOM is present. Python follows
prevailing platform practice, so native-endian data round-trips
without redundant byte swapping, even though the Unicode Standard
defaults to big-endian when the byte order is unspecified. When these
bytes are read by a CPU with a different endianness, the bytes have to
be swapped. To be able to detect the endianness of a "UTF-16" or
"UTF-32" byte sequence, a BOM ("Byte Order Mark") is used. This is the
Unicode character "U+FEFF". This character can be prepended to every
"UTF-16" or "UTF-32" byte sequence. The byte swapped version of this
character ("0xFFFE") is an illegal character that may not appear in a
Unicode text. When the first character of a "UTF-16" or "UTF-32" byte
sequence is "U+FFFE", the bytes have to be swapped on decoding.

Unfortunately the character "U+FEFF" had a second purpose as a "ZERO
WIDTH NO-BREAK SPACE": a character that has no width and doesn't allow
a word to be split. It can e.g. be used to give hints to a ligature
algorithm. With Unicode 4.0 using "U+FEFF" as a "ZERO WIDTH NO-BREAK
SPACE" has been deprecated (with "U+2060" ("WORD JOINER") assuming
this role). Nevertheless Unicode software still must be able to handle
"U+FEFF" in both roles: as a BOM it's a device to determine the
storage layout of the encoded bytes, and vanishes once the byte
sequence has been decoded into a string; as a "ZERO WIDTH NO-BREAK
SPACE" it's a normal character that will be decoded like any other.

Hay otra codificación que puede codificar el rango completo de
caracteres Unicode: UTF-8. UTF-8 es una codificación de 8 bits, lo que
significa que no hay problemas con el orden de bytes en UTF-8. Cada
byte en una secuencia de bytes UTF-8 consta de dos partes: bits
marcadores (los bits más significativos) y bits de carga útil. Los
bits marcadores son una secuencia de cero a cuatro bits "1" seguidos
de un bit "0". Los caracteres Unicode se codifican de esta manera (con
x siendo bits de carga útil, que cuando se concatenan dan el carácter
Unicode):

+-------------------------------------+------------------------------------------------+
| Rango                               | Codificación                                   |
|=====================================|================================================|
## | "U-00000000" ... "U-0000007F"       | 0xxxxxxx                                       |

## | "U-00000080" ... "U-000007FF"       | 110xxxxx 10xxxxxx                              |

## | "U-00000800" ... "U-0000FFFF"       | 1110xxxx 10xxxxxx 10xxxxxx                     |

## | "U-00010000" ... "U-0010FFFF"       | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx            |

El bit menos significativo del carácter Unicode es el bit x más a la
derecha.

Como UTF-8 es una codificación de 8 bits, no se requiere una lista de
materiales y cualquier carácter "U+FEFF" en la cadena decodificada
(incluso si es el primer carácter) se trata como un "ESPACIO SIN
QUIEBRE DE ANCHO CERO" (*``ZERO WIDTH NO-BREAK SPACE``*).

Sin información externa, es imposible determinar de manera fidedigna
qué codificación se utilizó para codificar una cadena de caracteres.
Cada codificación de mapa de caracteres puede decodificar cualquier
secuencia de bytes aleatoria. Sin embargo, eso no es posible con
UTF-8, ya que las secuencias de bytes UTF-8 tienen una estructura que
no permite secuencias de bytes arbitrarias. Para aumentar la
confiabilidad con la que se puede detectar una codificación UTF-8,
Microsoft inventó una variante de UTF-8 (que Python 2.5 llama
""utf-8-sig"") para su programa Bloc de notas: Antes de que cualquier
carácter Unicode sea escrito en un archivo, se escribe un BOM
codificado en UTF-8 (que se muestra como una secuencia de bytes:
"0xef", "0xbb", "0xbf"). Como es bastante improbable que cualquier
archivo codificado del mapa de caracteres comience con estos valores
de bytes (que, por ejemplo, se asignarían a

      LETRA LATINA PEQUEÑA I CON DIAERESIS
      SEÑALADO A LA DERECHA DE DOBLE ÁNGULO MARCA DE CITA
      SIGNO DE PREGUNTA INVERTIDO

en iso-8859-1), esto aumenta la probabilidad de que una codificación
"utf-8-sig" pueda adivinarse correctamente a partir de la secuencia de
bytes. Por lo tanto, aquí la lista de materiales no se utiliza para
poder determinar el orden de bytes utilizado para generar la secuencia
de bytes, sino como una firma que ayuda a adivinar la codificación. Al
codificar, el códec utf-8-sig escribirá "0xef", "0xbb", "0xbf" como
los primeros tres bytes del archivo. Al decodificar, "utf-8-sig"
omitirá esos tres bytes si aparecen como los primeros tres bytes en el
archivo. En UTF-8, se desaconseja el uso de la lista de materiales y,
en general, debe evitarse.

## Codificaciones estándar

Python comes with a number of codecs built-in, either implemented as C
functions or with dictionaries as mapping tables. The following table
lists the codecs by name, together with a few common aliases, and the
languages for which the encoding is likely used. Neither the list of
aliases nor the list of languages is meant to be exhaustive. Notice
that spelling alternatives that only differ in case or use a hyphen
instead of an underscore are also valid aliases because they are
equivalent when normalized by "normalize_encoding()". For example,
"'utf-8'" is a valid alias for the "'utf_8'" codec.

Nota:

  The below table lists the most common aliases, for a complete list
  refer to the source aliases.py file.

On Windows, "cpXXX" codecs are available for all code pages. But only
codecs listed in the following table are guarantead to exist on other
platforms.

Algunas codificaciones comunes pueden omitir la maquinaria de búsqueda
de códecs para mejorar el rendimiento. CPython solo reconoce estas
oportunidades de optimización para un conjunto limitado de alias (sin
distinción entre mayúsculas y minúsculas): utf-8, utf8, latin-1,
latin1, iso-8859-1, iso8859-1, mbcs (solo Windows), ascii, us-ascii,
utf-16, utf16, utf-32, utf32, y lo mismo usando guiones bajos en lugar
de guiones. El uso de alias alternativos para estas codificaciones
puede resultar en una ejecución más lenta.

Distinto en la versión 3.6: Oportunidad de optimización reconocida
para us-ascii.

Muchos de los juegos de caracteres admiten los mismos idiomas. Varían
en caracteres individuales (por ejemplo, si el SIGNO EURO es
compatible o no), y en la asignación de caracteres para codificar
posiciones. Para los idiomas europeos en particular, generalmente
existen las siguientes variantes:

* un conjunto de códigos ISO 8859

* una página de códigos de Microsoft Windows, que generalmente se
  deriva de un conjunto de códigos 8859, pero reemplaza los caracteres
  de control con caracteres gráficos adicionales

* una página de códigos EBCDIC de IBM

* una página de códigos de IBM PC, que es compatible con ASCII

+-------------------+----------------------------------+----------------------------------+
| Códec             | Aliases                          | Lenguajes                        |
|===================|==================================|==================================|
## | ascii             | 646, us-ascii                    | Inglés                           |

## | big5              | big5-tw, csbig5                  | Chino Tradicional                |

## | big5hkscs         | big5-hkscs, hkscs                | Chino Tradicional                |

## | cp037             | IBM037, IBM039                   | Inglés                           |

## | cp273             | 273, IBM273, csIBM273            | Alemán  Added in version 3.4.    |

## | cp424             | EBCDIC-CP-HE, IBM424             | Hebreo                           |

## | cp437             | 437, IBM437                      | Inglés                           |

| cp500             | EBCDIC-CP-BE, EBCDIC-CP-CH,      | Europa Occidental                |
## |                   | IBM500                           |                                  |

## | cp720             |                                  | Árabe                            |

## | cp737             |                                  | Griego                           |

## | cp775             | IBM775                           | Lenguajes bálticos               |

## | cp850             | 850, IBM850                      | Europa Occidental                |

## | cp852             | 852, IBM852                      | Europa central y del este        |

| cp855             | 855, IBM855                      | Belarusian, Bulgarian,           |
## |                   |                                  | Macedonian, Russian, Serbian     |

## | cp856             |                                  | Hebreo                           |

## | cp857             | 857, IBM857                      | Turco                            |

## | cp858             | 858, IBM00858                    | Europa Occidental                |

## | cp860             | 860, IBM860                      | Portugués                        |

## | cp861             | 861, CP-IS, IBM861               | Islandés                         |

## | cp862             | 862, IBM862                      | Hebreo                           |

## | cp863             | 863, IBM863                      | Canadiense                       |

## | cp864             | IBM864                           | Árabe                            |

## | cp865             | 865, IBM865                      | Danés, Noruego                   |

## | cp866             | 866, IBM866                      | Ruso                             |

## | cp869             | 869, CP-GR, IBM869               | Griego                           |

## | cp874             |                                  | Tailandés                        |

## | cp875             |                                  | Griego                           |

| cp932             | 932, ms932, mskanji, ms-kanji,   | Japonés                          |
## |                   | windows-31j                      |                                  |

## | cp949             | 949, ms949, uhc                  | Coreano                          |

## | cp950             | 950, ms950                       | Chino Tradicional                |

## | cp1006            |                                  | Urdu                             |

## | cp1026            | ibm1026                          | Turco                            |

## | cp1125            | 1125, ibm1125, cp866u, ruscii    | Ucraniano  Added in version 3.4. |

## | cp1140            | IBM01140                         | Europa Occidental                |

## | cp1250            | windows-1250                     | Europa central y del este        |

| cp1251            | windows-1251                     | Belarusian, Bulgarian,           |
## |                   |                                  | Macedonian, Russian, Serbian     |

## | cp1252            | windows-1252                     | Europa Occidental                |

## | cp1253            | windows-1253                     | Griego                           |

## | cp1254            | windows-1254                     | Turco                            |

## | cp1255            | windows-1255                     | Hebreo                           |

## | cp1256            | windows-1256                     | Árabe                            |

## | cp1257            | windows-1257                     | Lenguajes bálticos               |

## | cp1258            | windows-1258                     | Vietnamita                       |

## | euc_jp            | eucjp, ujis, u-jis               | Japonés                          |

## | euc_jis_2004      | jisx0213, eucjis2004             | Japonés                          |

## | euc_jisx0213      | eucjisx0213                      | Japonés                          |

| euc_kr            | euckr, korean, ksc5601,          | Coreano                          |
|                   | ks_c-5601, ks_c-5601-1987,       |                                  |
## |                   | ksx1001, ks_x-1001               |                                  |

| gb2312            | chinese, csiso58gb231280, euc-   | Chino simplificado               |
|                   | cn, euccn, eucgb2312-cn,         |                                  |
|                   | gb2312-1980, gb2312-80, iso-     |                                  |
## |                   | ir-58                            |                                  |

## | gbk               | 936, cp936, ms936                | Chino Unificado                  |

## | gb18030           | gb18030-2000                     | Chino Unificado                  |

## | hz                | hzgb, hz-gb, hz-gb-2312          | Chino simplificado               |

| iso2022_jp        | csiso2022jp, iso2022jp,          | Japonés                          |
## |                   | iso-2022-jp                      |                                  |

## | iso2022_jp_1      | iso2022jp-1, iso-2022-jp-1       | Japonés                          |

| iso2022_jp_2      | iso2022jp-2, iso-2022-jp-2       | Japonés, Coreano, Chino          |
|                   |                                  | simplificado, Europa occidental, |
## |                   |                                  | Griego                           |

## | iso2022_jp_2004   | iso2022jp-2004, iso-2022-jp-2004 | Japonés                          |

## | iso2022_jp_3      | iso2022jp-3, iso-2022-jp-3       | Japonés                          |

## | iso2022_jp_ext    | iso2022jp-ext, iso-2022-jp-ext   | Japonés                          |

| iso2022_kr        | csiso2022kr, iso2022kr,          | Coreano                          |
## |                   | iso-2022-kr                      |                                  |

| latin_1           | iso-8859-1, iso8859-1, 8859,     | Europa Occidental                |
## |                   | cp819, latin, latin1, L1         |                                  |

## | iso8859_2         | iso-8859-2, latin2, L2           | Europa central y del este        |

## | iso8859_3         | iso-8859-3, latin3, L3           | Esperanto, Maltés                |

## | iso8859_4         | iso-8859-4, latin4, L4           | Northern Europe                  |

| iso8859_5         | iso-8859-5, cyrillic             | Belarusian, Bulgarian,           |
## |                   |                                  | Macedonian, Russian, Serbian     |

## | iso8859_6         | iso-8859-6, arabic               | Árabe                            |

## | iso8859_7         | iso-8859-7, greek, greek8        | Griego                           |

## | iso8859_8         | iso-8859-8, hebrew               | Hebreo                           |

## | iso8859_9         | iso-8859-9, latin5, L5           | Turco                            |

## | iso8859_10        | iso-8859-10, latin6, L6          | Lenguajes nórdicos               |

## | iso8859_11        | iso-8859-11, thai                | Lenguajes tailandeses            |

## | iso8859_13        | iso-8859-13, latin7, L7          | Lenguajes bálticos               |

## | iso8859_14        | iso-8859-14, latin8, L8          | Lenguajes Celtas                 |

## | iso8859_15        | iso-8859-15, latin9, L9          | Europa Occidental                |

## | iso8859_16        | iso-8859-16, latin10, L10        | Europa sudoriental               |

## | johab             | cp1361, ms1361                   | Coreano                          |

## | koi8_r            |                                  | Ruso                             |

## | koi8_t            |                                  | Tayiko  Added in version 3.5.    |

## | koi8_u            |                                  | Ucraniano                        |

## | kz1048            | kz_1048, strk1048_2002, rk1048   | Kazajo  Added in version 3.5.    |

| mac_cyrillic      | maccyrillic                      | Belarusian, Bulgarian,           |
## |                   |                                  | Macedonian, Russian, Serbian     |

## | mac_greek         | macgreek                         | Griego                           |

## | mac_iceland       | maciceland                       | Islandés                         |

| mac_latin2        | maclatin2, maccentraleurope,     | Europa central y del este        |
## |                   | mac_centeuro                     |                                  |

## | mac_roman         | macroman, macintosh              | Europa Occidental                |

## | mac_turkish       | macturkish                       | Turco                            |

| ptcp154           | csptcp154, pt154, cp154,         | Kazajo                           |
## |                   | cyrillic-asian                   |                                  |

| shift_jis         | csshiftjis, shiftjis, sjis,      | Japonés                          |
## |                   | s_jis                            |                                  |

| shift_jis_2004    | shiftjis2004, sjis_2004,         | Japonés                          |
## |                   | sjis2004                         |                                  |

| shift_jisx0213    | shiftjisx0213, sjisx0213,        | Japonés                          |
## |                   | s_jisx0213                       |                                  |

## | utf_32            | U32, utf32                       | todos los lenguajes              |

## | utf_32_be         | UTF-32BE                         | todos los lenguajes              |

## | utf_32_le         | UTF-32LE                         | todos los lenguajes              |

## | utf_16            | U16, utf16                       | todos los lenguajes              |

## | utf_16_be         | UTF-16BE                         | todos los lenguajes              |

## | utf_16_le         | UTF-16LE                         | todos los lenguajes              |

## | utf_7             | U7, unicode-1-1-utf-7            | todos los lenguajes              |

## | utf_8             | U8, UTF, utf8, cp65001           | todos los lenguajes              |

## | utf_8_sig         |                                  | todos los lenguajes              |

Distinto en la versión 3.4: Los codificadores utf-16* y utf-32* ya no
permiten codificar puntos de código sustitutos ("U+D800" -- "U+DFFF").
Los decodificadores utf-32* ya no decodifican secuencias de bytes que
corresponden a puntos de código sustituto.

Distinto en la versión 3.8: "cp65001" ahora es un alias de "utf_8".

Distinto en la versión 3.14: On Windows, "cpXXX" codecs are now
available for all code pages.

## Codificaciones específicas de Python

Varios códecs predefinidos son específicos de Python, por lo que sus
nombres de códec no tienen significado fuera de Python. Estos se
enumeran en las tablas a continuación según los tipos de entrada y
salida esperados (tenga en cuenta que si bien las codificaciones de
texto son el caso de uso más común para los códecs, la infraestructura
de códecs subyacente admite transformaciones de datos arbitrarias en
lugar de solo codificaciones de texto). Para los códecs asimétricos,
el significado indicado describe la dirección de codificación.

### Codificaciones de texto

Los siguientes códecs proporcionan codificación de "str" a "bytes" y
decodificación de *bytes-like object* a "str", similar a las
codificaciones de texto Unicode.

+----------------------+-----------+-----------------------------+
| Códec                | Aliases   | Significado                 |
|======================|===========|=============================|
| idna                 |           | Implementar **RFC 3490**,   |
|                      |           | ver también                 |
|                      |           | "encodings.idna". Solo se   |
## |                      |           | admite "errors='strict'".   |

| mbcs                 | ansi,     | Solo Windows: codifique el  |
|                      | dbcs      | operando de acuerdo con la  |
|                      |           | página de códigos ANSI      |
## |                      |           | (CP_ACP).                   |

| oem                  |           | Solo Windows: codifique el  |
|                      |           | operando de acuerdo con la  |
|                      |           | página de códigos OEM       |
|                      |           | (CP_OEMCP).  Added in       |
## |                      |           | version 3.6.                |

## | palmos               |           | Codificación de PalmOS 3.5. |

| punycode             |           | Implementar **RFC 3492**.   |
|                      |           | Los códecs con estado no    |
|                      |           | son compatibles.            |
|                      |           | Advertencia:   The decoding |
|                      |           | and encoding algorithms     |
|                      |           | scale poorly, so limit the  |
## |                      |           | length of untrusted input.  |

| raw_unicode_escape   |           | Codificación Latin-1 con    |
|                      |           | "\u*XXXX*" y "\U*XXXXXXXX*" |
|                      |           | para otros puntos de        |
|                      |           | código. Las barras          |
|                      |           | invertidas existentes no se |
|                      |           | escapan de ninguna manera.  |
|                      |           | Se usa en el protocolo      |
## |                      |           | Python *pickle*.            |

| indefinido           |           | This Codec should only be   |
|                      |           | used for testing purposes.  |
|                      |           | Lanza una excepción para    |
|                      |           | todas las conversiones,     |
|                      |           | incluso cadenas vacías. El  |
|                      |           | manejador de errores se     |
## |                      |           | ignora.                     |

| unicode_escape       |           | Codificación adecuada como  |
|                      |           | contenido de un literal     |
|                      |           | Unicode en código fuente    |
|                      |           | Python codificado en ASCII, |
|                      |           | excepto que no se escapan   |
|                      |           | las comillas. Decodificar   |
|                      |           | desde el código fuente      |
|                      |           | Latin-1. Tenga en cuenta    |
|                      |           | que el código fuente de     |
|                      |           | Python realmente usa UTF-8  |
## |                      |           | por defecto.                |

Distinto en la versión 3.8: Se elimina el códec "unicode_internal".

### Transformaciones Binarias

Los siguientes códecs proporcionan transformaciones binarias: mapeos
de *bytes-like object* a "bytes". No son compatibles con
"bytes.decode()" (que solo produce "str" de salida).

+------------------------+--------------------+--------------------------------+--------------------------------+
| Códec                  | Aliases            | Significado                    | Codificador / decodificador    |
|========================|====================|================================|================================|
| base64_codec [1]       | base64, base_64    | Convierta el operando a MIME   | "base64.encodebytes()" /       |
|                        |                    | base64 multilínea (el          | "base64.decodebytes()"         |
|                        |                    | resultado siempre incluye un   |                                |
|                        |                    | "'\n'" final).  Distinto en la |                                |
|                        |                    | versión 3.4: acepta cualquier  |                                |
|                        |                    | *bytes-like object* como       |                                |
|                        |                    | entrada para codificar y       |                                |
## |                        |                    | decodificar                    |                                |

| bz2_codec              | bz2                | Comprime el operando usando    | "bz2.compress()" /             |
## |                        |                    | bz2.                           | "bz2.decompress()"             |

| hex_codec              | hex                | Convierte el operando en       | "binascii.b2a_hex()" /         |
|                        |                    | representación hexadecimal,    | "binascii.a2b_hex()"           |
## |                        |                    | con dos dígitos por byte.      |                                |

| quopri_codec           | quopri,            | Convierte el operando a MIME   | "quopri.encode()" con          |
|                        | quotedprintable,   | citado imprimible.             | "quotetabs=True" /             |
## |                        | quoted_printable   |                                | "quopri.decode()"              |

| uu_codec               | uu                 | Convierte el operando usando   |                                |
## |                        |                    | uuencode.                      |                                |

| zlib_codec             | zip, zlib          | Comprime el operando usando    | "zlib.compress()" /            |
## |                        |                    | gzip.                          | "zlib.decompress()"            |

[1] Además de *objetos similares a bytes*, "'base64_codec'" también
    acepta instancias solo ASCII de "str" para decodificación

Added in version 3.2: Restauración de las transformaciones binarias.

Distinto en la versión 3.4: Restauración de los alias para las
transformaciones binarias.

### Standalone Codec Functions

The following functions provide encoding and decoding functionality
similar to codecs, but are not available as named codecs through
"codecs.encode()" or "codecs.decode()". They are used internally (for
example, by "pickle") and behave similarly to the "string_escape"
codec that was removed in Python 3.

codecs.escape_encode(input, errors=None)

   Encode *input* using escape sequences. Similar to how "repr()" on
   bytes produces escaped byte values.

   *input* must be a "bytes" object.

   Returns a tuple "(output, length)" where *output* is a "bytes"
   object and *length* is the number of bytes consumed.

codecs.escape_decode(input, errors=None)

   Decode *input* from escape sequences back to the original bytes.

   *input* must be a *bytes-like object*.

   Returns a tuple "(output, length)" where *output* is a "bytes"
   object and *length* is the number of bytes consumed.

### Transformaciones de texto

El siguiente códec proporciona una transformación de texto: un mapeo
de "str" a "str". No es compatible con "str.encode()" (que solo
produce "bytes" de salida).

+----------------------+-----------+-----------------------------+
| Códec                | Aliases   | Significado                 |
|======================|===========|=============================|
| rot_13               | rot13     | Retorna el cifrado César    |
|                      |           | (*Caesar-cypher*) del       |
## |                      |           | operando.                   |

Added in version 3.2: Restauración de la transformación de texto
"rot_13".

Distinto en la versión 3.4: Restauración del alias "rot13".

## "encodings" --- Encodings package

This module implements the following functions:

encodings.normalize_encoding(encoding)

   Normalize encoding name *encoding*.

   Normalization works as follows: all non-alphanumeric characters
   except the dot used for Python package names are collapsed and
   replaced with a single underscore, leading and trailing underscores
   are removed. For example, "'  -;#'" becomes "'_'".

   Note that *encoding* should be ASCII only.

Nota:

  The following functions should not be used directly, except for
  testing purposes; "codecs.lookup()" should be used instead.

encodings.search_function(encoding)

   Search for the codec module corresponding to the given encoding
   name *encoding*.

   This function first normalizes the *encoding* using
   "normalize_encoding()", then looks for a corresponding alias. It
   attempts to import a codec module from the encodings package using
   either the alias or the normalized name. If the module is found and
   defines a valid "getregentry()" function that returns a
   "codecs.CodecInfo" object, the codec is cached and returned.

   If the codec module defines a "getaliases()" function any returned
   aliases are registered for future use.

encodings.win32_code_page_search_function(encoding)

   Search for a Windows code page encoding *encoding* of the form
   "cpXXXX".

   If the code page is valid and supported, return a
   "codecs.CodecInfo" object for it.

   Availability: Windows.

   Added in version 3.14.

This module implements the following exception:

exception encodings.CodecRegistryError

   Raised when a codec is invalid or incompatible.

## "encodings.idna" --- Internationalized Domain Names in Applications

Este módulo implementa **RFC 3490** (nombres de dominio
internacionalizados en aplicaciones) y **RFC 3492** (*Nameprep*: un
perfil de *Stringprep* para nombres de dominio internacionalizados
(IDN)). Se basa en la codificación "punycode" y "stringprep".

If you need the IDNA 2008 standard from **RFC 5891** and **RFC 5895**,
use the third-party idna module.

Estas RFC juntas definen un protocolo para admitir caracteres no ASCII
en los nombres de dominio. Un nombre de dominio que contiene
caracteres no ASCII (como "www.Alliancefrançaise.nu") se convierte en
una codificación compatible con ASCII (ACE, como "www.xn
--alliancefranaise-npb.nu"). La forma ACE del nombre de dominio se
utiliza en todos los lugares donde el protocolo no permite caracteres
arbitrarios, como consultas DNS, campos HTTP *Host*, etc. Esta
conversión se lleva a cabo en la aplicación; si es posible invisible
para el usuario: la aplicación debe convertir de forma transparente
las etiquetas de dominio Unicode a IDNA en el cable, y volver a
convertir las etiquetas ACE a Unicode antes de presentarlas al
usuario.

Python admite esta conversión de varias maneras: el códec "idna"
realiza la conversión entre Unicode y ACE, separando una cadena de
entrada en etiquetas basadas en los caracteres separadores definidos
en la sección 3.1 de RFC 3490 **RFC 3490 Section 3.1** y convertir
cada etiqueta a ACE según sea necesario, y por el contrario, separar
una cadena de bytes de entrada en etiquetas basadas en el separador
"." y convertir cualquier etiqueta ACE encontrada en unicode. Además,
el módulo "socket" convierte de forma transparente los nombres de host
Unicode a ACE, por lo que las aplicaciones no necesitan preocuparse
por convertir los nombres de host ellos mismos cuando los pasan al
módulo de socket. Además de eso, los módulos que tienen nombres de
host como parámetros de función, como "http.client" y "ftplib",
aceptan nombres de host Unicode ("http.client" y luego también envían
un mensaje transparente IDNA *hostname* en el campo *Host* si envía
ese campo).

Al recibir nombres de host desde el cable (como en la búsqueda inversa
de nombres), no se realiza una conversión automática a Unicode: las
aplicaciones que deseen presentar dichos nombres de host al usuario
deben decodificarlos en Unicode.

The module "encodings.idna" also implements the nameprep procedure,
which performs certain normalizations on host names, to achieve case-
insensitivity of international domain names, and to unify similar
characters. The nameprep functions can be used directly if desired.

encodings.idna.nameprep(label)

   Retorna la versión pasada por *nameprep* (o versión *nameprepped*)
   de *label*. La implementación actualmente asume cadenas de
   caracteres de consulta, por lo que "AllowUnassigned" es verdadero.

encodings.idna.ToASCII(label)

   Convierte una etiqueta a ASCII, como se especifica en **RFC 3490**.
   Se supone que "UseSTD3ASCIIRules" es falso.

encodings.idna.ToUnicode(label)

   Convierte una etiqueta a Unicode, como se especifica en **RFC
   3490**.

## "encodings.mbcs" --- Windows ANSI codepage

Este módulo implementa la página de códigos ANSI (CP_ACP).

Availability: Windows.

Distinto en la versión 3.2: Antes de 3.2, se ignoraba el argumento
*errors*; "'replace'" siempre se usó para codificar e "'ignore'" para
decodificar.

Distinto en la versión 3.3: Admite cualquier manejador de errores.

## "encodings.utf_8_sig" --- UTF-8 codec with BOM signature

Este módulo implementa una variante del códec UTF-8. Al codificar, una
lista de materiales codificada en UTF-8 se antepondrá a los bytes
codificados en UTF-8. Para el codificador con estado esto solo se hace
una vez (en la primera escritura en el flujo de bytes). En la
decodificación, se omitirá una lista de materiales opcional codificada
en UTF-8 al comienzo de los datos.
