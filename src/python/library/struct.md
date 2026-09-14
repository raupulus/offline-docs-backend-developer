---
title: '"struct" --- Interpret bytes as packed binary data'
source_url: https://docs.python.org/es/3
source_path: library/struct.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3950
---

# "struct" --- Interpret bytes as packed binary data

**Código fuente:** Lib/struct.py

======================================================================

Este módulo convierte entre valores de Python y estructuras de C
representadas como objetos de Python "bytes". Las cadenas de formato
compacto describen las conversiones previstas hacia/desde valores de
Python. Las funciones y objetos del módulo se pueden utilizar para dos
aplicaciones en gran medida distintas, el intercambio de datos con
fuentes externas (archivos o conexiones de red) o la transferencia de
datos entre la aplicación de Python y la capa de C.

Nota:

  Cuando no se proporciona ningún carácter de prefijo, el modo nativo
  es el predeterminado. Empaqueta o desempaqueta datos según la
  plataforma y el compilador en el que se creó el intérprete de
  Python. El resultado de empaquetar una estructura C determinada
  incluye bytes de relleno que mantienen la alineación adecuada para
  los tipos C involucrados; asimismo, se tiene en cuenta la alineación
  al desempaquetar. Por el contrario, cuando se comunican datos entre
  fuentes externas, el programador es responsable de definir el orden
  de bytes y el relleno entre elementos. Ver Orden de bytes, tamaño y
  alineación para más detalles.

Several "struct" functions (and methods of "Struct") take a *buffer*
argument.  This refers to objects that implement the Protocolo búfer
and provide either a readable or read-writable buffer.  The most
common types used for that purpose are "bytes" and "bytearray", but
many other types that can be viewed as an array of bytes implement the
buffer protocol, so that they can be read/filled without additional
copying from a "bytes" object.

## Funciones y excepciones

El módulo define la siguiente excepción y funciones:

exception struct.error

   Excepción lanzada en varias ocasiones; el argumento es una *string*
   que describe lo que está mal.

struct.pack(format, v1, v2, ...)

   Retorna un objeto bytes que contiene los valores *v1*, *v2*, ...
   empaquetado de acuerdo con la cadena de formato *format*.  Los
   argumentos deben coincidir exactamente con los valores requeridos
   por el formato.

struct.pack_into(format, buffer, offset, v1, v2, ...)

   Pack the values *v1*, *v2*, ... according to the format string
   *format* and write the packed bytes into the writable buffer
   *buffer* starting at position *offset*.  Note that *offset* is a
   required argument. A negative *offset* counts from the end of
   *buffer*.

struct.unpack(format, buffer)

   Desempaqueta del búfer *buffer* (normalmente empaquetado por
   "pack(format, ...)") según la cadena de formato *format*.  El
   resultado es una tupla incluso si contiene un solo elemento.  El
   tamaño del búfer en bytes debe coincidir con el tamaño requerido
   por el formato, como se refleja en "calcsize()".

struct.unpack_from(format, /, buffer, offset=0)

   Unpack from *buffer* starting at position *offset*, according to
   the format string *format*.  The result is a tuple even if it
   contains exactly one item.  The buffer's size in bytes, starting at
   position *offset*, must be at least the size required by the
   format, as reflected by "calcsize()". A negative *offset* counts
   from the end of *buffer*.

struct.iter_unpack(format, buffer)

   Desempaqueta de manera iterativa desde el búfer *buffer* según la
   cadena de formato *format*.  Esta función retorna un iterador que
   leerá fragmentos de igual tamaño desde el búfer hasta que se haya
   consumido todo su contenido. El tamaño del búfer en bytes debe ser
   un múltiplo del tamaño requerido por el formato, como se refleja en
   "calcsize()".

   Cada iteración produce una tupla según lo especificado por la
   cadena de formato.

   Added in version 3.4.

struct.calcsize(format)

   Retorna el tamaño de la estructura (y, por lo tanto, del objeto
   bytes generado por "pack(format, ...)") correspondiente a la cadena
   de formato *format*.

## Cadenas de formato

Las cadenas de formato describen el diseño de los datos cuando
empaquetan y desempaquetan datos. Se construyen a partir caracteres de
formato, que especifican el tipo de datos que se
empaquetan/desempaquetan. Además, los caracteres especiales controlan
el orden de bytes, tamaño y alineación. Cada cadena de formato consta
de un carácter de prefijo opcional que describe las propiedades
generales de los datos y uno o más caracteres de formato que describen
los valores de datos actuales y el relleno.

### Orden de bytes, tamaño y alineación

Por defecto, los tipos C se representan en el formato nativo y el
orden de bytes de la máquina, y se alinean correctamente omitiendo
*bytes* de relleno si es necesario (según las reglas utilizadas por el
compilador de C). Se elige este comportamiento para que los bytes de
una estructura empaquetada correspondan correctamente al diseño de
memoria de la estructura C correspondiente. El uso de ordenamiento y
relleno de bytes nativos o formatos estándar depende de la aplicación.

Como alternativa, el primer carácter de la cadena de formato se puede
utilizar para indicar el orden de bytes, el tamaño y la alineación de
los datos empaquetados, según la tabla siguiente:

+-------------+--------------------------+------------+-------------+
| Carácter    | Orden de bytes           | Tamaño     | Alineamien  |
|             |                          |            | to          |
|=============|==========================|============|=============|
## | "@"         | nativo                   | nativo     | nativo      |

## | "="         | nativo                   | standard   | none        |

## | "<"         | little-endian            | standard   | none        |

## | ">"         | big-endian               | standard   | none        |

## | "!"         | red (= big-endian)       | standard   | none        |

Si el primer carácter no es uno de estos, se asume "'@'".

Nota:

  The number 1023 ("0x3ff" in hexadecimal) has the following byte
  representations:

  * "03 ff" in big-endian (">")

  * "ff 03" in little-endian ("<")

  Python example:

  >>> import struct
  >>> struct.pack('>h', 1023)
  b'\x03\xff'
  >>> struct.pack('<h', 1023)
  b'\xff\x03'

El orden de bytes nativo es big-endian o little-endian, dependiendo
del sistema host. Por ejemplo, Intel x86, AMD64 (x86-64) y Apple M1
son little-endian; IBM z y muchas arquitecturas heredadas son big-
endian; ARM e Intel *Itanium* tienen la propiedad de trabajar con
ambos formatos (middle-endian). Utiliza "sys.byteorder" para comprobar
la endianness ("extremidad") de tu sistema.

El tamaño y la alineación nativos se determinan mediante la expresión
"sizeof" del compilador de C.  Esto siempre se combina con el orden de
bytes nativo.

El tamaño estándar depende únicamente del carácter de formato;  ver la
tabla en la sección Caracteres de formato.

Nótese la diferencia entre "'@'" y "'='" : ambos utilizan el orden de
bytes nativo, pero el tamaño y la alineación de este último está
estandarizado.

La forma "'!'" representa el orden de bytes en la red, el cuál siempre
es big-endian tal como se define en IETF RFC 1700.

No hay manera de indicar el orden de bytes no nativo (forzar el
intercambio de bytes); utiliza la elección adecuada de "'<'" o "'>'".

Notas:

1. El relleno solo se agrega automáticamente entre los miembros
   sucesivos de la estructura. No se agrega ningún relleno al
   principio o al final de la estructura codificada.

2. No se añade ningún relleno cuando se utiliza el tamaño y la
   alineación no nativos, por ejemplo, con '<', '>', '=' y '!'.

3. Para alinear el final de una estructura con el requisito de
   alineación de un tipo determinado, termina el formato con el código
   de ese tipo con un conteo repetido de ceros.  Véase Ejemplos.

### Caracteres de formato

Los caracteres de formato tienen el siguiente significado; la
conversión entre los valores de C y Python debe ser obvia dados sus
tipos.  La columna 'Tamaño estándar' hace referencia al tamaño del
valor empaquetado en bytes cuando se utiliza el tamaño estándar; es
decir, cuando la cadena de formato comienza con uno de "'<'", "'>'",
"'!'" o "'='".  Cuando se utiliza el tamaño nativo, el tamaño del
valor empaquetado depende de la plataforma.

+----------+----------------------------+----------------------+------------------+--------------+
| Formato  | Tipo C                     | Tipo Python          | Tamaño estándar  | Notas        |
|==========|============================|======================|==================|==============|
## | "x"      | byte de relleno            | sin valor            |                  | (7)          |

## | "c"      | char                       | bytes de longitud 1  | 1                |              |

## | "b"      | signed char                | int                  | 1                | (2)          |

## | "B"      | unsigned char              | int                  | 1                | (2)          |

## | (2)      | _Bool                      | bool                 | 1                | (1)          |

## | "h"      | short                      | int                  | 2                | (2)          |

## | "H"      | unsigned short             | int                  | 2                | (2)          |

## | "i"      | int                        | int                  | 4                | (2)          |

## | "I"      | unsigned int               | int                  | 4                | (2)          |

## | "l"      | long                       | int                  | 4                | (2)          |

## | "L"      | unsigned long              | int                  | 4                | (2)          |

## | "q"      | long long                  | int                  | 8                | (2)          |

## | "Q"      | unsigned long long         | int                  | 8                | (2)          |

## | "n"      | "ssize_t"                  | int                  |                  | (2), (3)     |

## | "N"      | "size_t"                   | int                  |                  | (2), (3)     |

## | "e"      | _Float16                   | float                | 2                | (4), (6)     |

## | "f"      | float                      | float                | 4                | (4)          |

## | "d"      | double                     | float                | 8                | (4)          |

## | "F"      | float complex              | complex              | 8                | (10)         |

## | "D"      | double complex             | complex              | 16               | (10)         |

## | "s"      | char[]                     | bytes                |                  | (9)          |

## | "p"      | char[]                     | bytes                |                  | (8)          |

## | "P"      | void*                      | int                  |                  | (2), (5)     |

Distinto en la versión 3.3: Soporte añadido para los formatos "'n'" y
"'N'".

Distinto en la versión 3.6: Soporte añadido para el formato "'e'".

Distinto en la versión 3.14: Added support for the "'F'" and "'D'"
formats.

Ver también:

  The "array" and ctypes modules, as well as third-party modules like
  numpy, use similar -- but slightly different -- type codes.

Notas:

1. The "'?'" conversion code corresponds to the _Bool type defined by
   C standards since C99.  In standard mode, it is represented by one
   byte.

2. Al intentar empaquetar un no entero mediante cualquiera de los
   códigos de conversión de enteros, si el no entero tiene un método
   "__index__()", se llama a ese método para convertir el argumento en
   un entero antes de empaquetar.

   Distinto en la versión 3.2: Agregado el uso del método
   "__index__()" para los no enteros.

3. Los códigos de conversión "'n'" y "'N'" solo están disponibles para
   el tamaño nativo (seleccionado como predeterminado o con el
   carácter de orden de bytes "'@'"). Para el tamaño estándar, puedes
   usar cualquiera de los otros formatos enteros que se ajusten a tu
   aplicación.

4. Para los códigos de conversión "'f'", "'d'" y "'e'", la
   representación empaquetada utiliza el formato IEEE 754 binary32,
   binary64 o binary16 (para "'f'", "'d'" o "'e'" respectivamente),
   independientemente del formato de punto flotante utilizado por la
   plataforma.

5. El carácter de formato "'P'" solo está disponible para el orden
   nativo de bytes (seleccionado como predeterminado o con el carácter
   de orden de bytes "'@'"). El carácter de orden de bytes "'='" elige
   utilizar el orden little- o big-endian basado en el sistema host.
   El módulo *struct* no interpreta esto como un orden nativo, por lo
   que el formato "'P'" no está disponible.

6. The IEEE 754 binary16 "half precision" type was introduced in the
   2008 revision of the IEEE 754 standard. It has a sign bit, a 5-bit
   exponent and 11-bit precision (with 10 bits explicitly stored), and
   can represent numbers between approximately "6.1e-05" and "6.5e+04"
   at full precision. This type is not widely supported by C
   compilers: it's available as _Float16 type, if the compiler
   supports the Annex H of the C23 standard.  On a typical machine, an
   unsigned short can be used for storage, but not for math
   operations. See the Wikipedia page on the half-precision floating-
   point format for more information.

7. Al empaquetar, "'x'" inserta un byte NUL.

8. The "'p'" format character encodes a "Pascal string", meaning a
   short variable-length string stored in a *fixed number of bytes*,
   given by the count. The first byte stored is the length of the
   string, or 255, whichever is smaller.  The bytes of the string
   follow.  If the byte string passed in to "pack()" is too long
   (longer than the count minus 1), only the leading "count-1" bytes
   of the string are stored.  If the byte string is shorter than
   "count-1", it is padded with null bytes so that exactly count bytes
   in all are used.  Note that for "unpack()", the "'p'" format
   character consumes "count" bytes, but that the "bytes" object
   returned can never contain more than 255 bytes. When packing,
   arguments of types "bytes" and "bytearray" are accepted.

9. For the "'s'" format character, the count is interpreted as the
   length of the byte string, not a repeat count like for the other
   format characters; for example, "'10s'" means a single 10-byte
   string mapping to or from a single Python byte string, while
   "'10c'" means 10 separate one byte character elements (e.g.,
   "cccccccccc") mapping to or from ten different Python byte objects.
   (See Ejemplos for a concrete demonstration of the difference.) If a
   count is not given, it defaults to 1.  For packing, the byte string
   is truncated or padded with null bytes as appropriate to make it
   fit. For unpacking, the resulting "bytes" object always has exactly
   the specified number of bytes.  As a special case, "'0s'" means a
   single, empty byte string (while "'0c'" means 0 characters). When
   packing, arguments of types "bytes" and "bytearray" are accepted.

10. For the "'F'" and "'D'" format characters, the packed
    representation uses the IEEE 754 binary32 and binary64 format for
    components of the complex number, regardless of the floating-point
    format used by the platform. Note that complex types ("F" and "D")
    are available unconditionally, despite complex types being an
    optional feature in C. As specified in the C11 standard, each
    complex type is represented by a two-element C array containing,
    respectively, the real and imaginary parts.

Un carácter de formato puede ir precedido de un número de recuento que
repite tantas veces el carácter.  Por ejemplo, la cadena de formato
"'4h'" significa exactamente lo mismo que "'hhhh'" .

Se omiten los caracteres de espacio entre formatos; sin embargo, un
recuento y su formato no deben contener espacios en blanco.

Al empaquetar un valor "x" utilizando uno de los formatos enteros
("'b'", "'B'", "'h'", "'H'", "'i'", "'I'", "'l'", "'L'", "'q'",
"'Q'"), si "x" está fuera de un rango válido para ese formato,
entonces se lanza la excepción "struct.error".

Distinto en la versión 3.1: Anteriormente, algunos de los formatos
enteros ajustaban los valores fuera de rango y lanzaban
"DeprecationWarning" en vez de "struct.error".

Para el carácter de formato "'?'", el valor retornado es "True" o
"False". Al empaquetar, se utiliza el valor verdadero del objeto del
argumento. Se empaquetará 0 o 1 en la representación *bool* nativa o
estándar, y cualquier valor distinto de cero será "True" al
desempaquetar.

### Ejemplos

Nota:

  Los ejemplos de orden de bytes nativos (designados por el prefijo de
  formato "'@'" o la falta de cualquier carácter de prefijo) pueden no
  coincidir con lo que produce la máquina del lector, ya que eso
  depende de la plataforma y el compilador.

Empaqueta y desempaqueta enteros de tres tamaños diferentes,
utilizando el orden *big endian*:

   >>> from struct import *
   >>> pack(">bhl", 1, 2, 3)
   b'\x01\x00\x02\x00\x00\x00\x03'
   >>> unpack('>bhl', b'\x01\x00\x02\x00\x00\x00\x03')
   (1, 2, 3)
   >>> calcsize('>bhl')
   7

Intenta empaquetar un entero que es demasiado grande para el campo
definido:

   >>> pack(">h", 99999)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   struct.error: 'h' format requires -32768 <= number <= 32767

Demuestra la diferencia entre los caracteres de formato "'s'" y "'c'":

   >>> pack("@ccc", b'1', b'2', b'3')
   b'123'
   >>> pack("@3s", b'123')
   b'123'

Los campos desempaquetados se pueden nombrar asignándolos a variables
o ajustando el resultado en una tupla con nombre:

   >>> record = b'raymond   \x32\x12\x08\x01\x08'
   >>> name, serialnum, school, gradelevel = unpack('<10sHHb', record)

   >>> from collections import namedtuple
   >>> Student = namedtuple('Student', 'name serialnum school gradelevel')
   >>> Student._make(unpack('<10sHHb', record))
   Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)

El orden de los caracteres de formato puede afectar el tamaño en el
modo nativo, ya que el relleno está implícito. En el modo estándar, el
usuario es responsable de insertar el relleno que desee. Toma en
cuenta que en la primera llamada "pack" a continuación se agregaron
tres bytes NUL después del "'#'" empaquetado para alinear el siguiente
entero en un límite de cuatro bytes. En este ejemplo, el resultado se
produjo en una máquina little endian:

   >>> pack('@ci', b'#', 0x12131415)
   b'#\x00\x00\x00\x15\x14\x13\x12'
   >>> pack('@ic', 0x12131415, b'#')
   b'\x15\x14\x13\x12#'
   >>> calcsize('@ci')
   8
   >>> calcsize('@ic')
   5

El siguiente formato "'llh0l'" especifica dos bytes de relleno al
final, suponiendo que los tipos *longs* están alineados en los límites
de 4 bytes:

   >>> pack('@llh0l', 1, 2, 3)
   b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x03\x00\x00'

Ver también:

  Módulo "array"
     Almacenamiento binario empaquetado de datos homogéneos.

  Módulo "json"
     Codificador y decodificador JSON.

  Módulo "pickle"
     Serialización de objetos Python.

## Aplicaciones

Two main applications for the "struct" module exist, data interchange
between Python and C code within an application or another application
compiled using the same compiler (native formats), and data
interchange between applications using agreed upon data layout
(standard formats).  Generally speaking, the format strings
constructed for these two domains are distinct.

### Formatos nativos

Al construir cadenas de formato que imitan diseños nativos, el
compilador y la arquitectura de la máquina determinan el orden y el
relleno de los bytes. En tales casos, se debe utilizar el carácter de
formato "@" para especificar el orden de bytes nativo y el tamaño de
los datos. Los bytes de relleno internos normalmente se insertan
automáticamente. Es posible que se necesite un código de formato de
repetición cero al final de una cadena de formato para redondear hasta
el límite de bytes correcto para una alineación adecuada de fragmentos
de datos consecutivos.

Considera estos dos ejemplos sencillos (en una máquina little-endian
de 64 bits):

   >>> calcsize('@lhl')
   24
   >>> calcsize('@llh')
   18

Los datos no se rellenan hasta un límite de 8 bytes al final de la
segunda cadena de formato sin el uso de relleno adicional. Un código
de formato de repetición cero resuelve ese problema:

   >>> calcsize('@llh0l')
   24

El código de formato "'x'" se puede utilizar para especificar la
repetición, pero para formatos nativos es mejor utilizar un formato de
repetición cero como "'0l'".

De forma predeterminada, se utiliza el orden y la alineación de bytes
nativos, pero es mejor ser explícito y utilizar el carácter de prefijo
"'@'".

### Formatos estándar

Cuando intercambia datos más allá de su proceso, como redes o
almacenamiento, sé preciso. Especifica el orden de bytes, el tamaño y
la alineación exactos. No asumas que coinciden con el orden nativo de
una máquina en particular. Por ejemplo, el orden de los bytes de la
red es big-endian, mientras que muchas CPU populares son little-
endian. Al definir esto explícitamente, el usuario no necesita
preocuparse por las especificaciones de la plataforma en la que se
ejecuta su código. El primer carácter normalmente debería ser "<" o
">" (o "!"). El relleno es responsabilidad del programador. El
carácter de formato de repetición cero no funcionará. En su lugar, el
usuario debe agregar explícitamente "'x'" bytes de relleno donde sea
necesario. Revisando los ejemplos de la sección anterior, tenemos:

   >>> calcsize('<qh6xq')
   24
   >>> pack('<qh6xq', 1, 2, 3) == pack('@lhl', 1, 2, 3)
   True
   >>> calcsize('@llh')
   18
   >>> pack('@llh', 1, 2, 3) == pack('<qqh', 1, 2, 3)
   True
   >>> calcsize('<qqh6x')
   24
   >>> calcsize('@llh0l')
   24
   >>> pack('@llh0l', 1, 2, 3) == pack('<qqh6x', 1, 2, 3)
   True

No se garantiza que los resultados anteriores (ejecutados en una
máquina de 64 bits) coincidan cuando se ejecutan en diferentes
máquinas. Por ejemplo, los siguientes ejemplos se ejecutaron en una
máquina de 32 bits:

   >>> calcsize('<qqh6x')
   24
   >>> calcsize('@llh0l')
   12
   >>> pack('@llh0l', 1, 2, 3) == pack('<qqh6x', 1, 2, 3)
   False

## Clases

The "struct" module also defines the following type:

class struct.Struct(format)

   Retorna un nuevo objeto Struct que escribe y lee datos binarios
   según la cadena de formato *format*. Crear un objeto "Struct" una
   vez y llamar a sus métodos es más eficaz que llamar a las funciones
   a nivel de módulo con el mismo formato, ya que la cadena de formato
   solo se compila una vez.

   Nota:

     Las versiones compiladas de las cadenas de formato más recientes
     pasadas a las funciones de nivel de módulo se almacenan en caché,
     por lo que los programas que utilizan solo unas pocas cadenas de
     formato no necesitan preocuparse por volver a usar una sola
     instancia "Struct".

   Los objetos Struct compilados admiten los siguientes métodos y
   atributos:

   pack(v1, v2, ...)

      Idéntico a la función "pack()", utilizando el formato compilado.
      ("len(result)" será igual a "size".)

   pack_into(buffer, offset, v1, v2, ...)

      Idéntico a la función "pack_into()", utilizando el formato
      compilado.

   unpack(buffer)

      Idéntico a la función "unpack()", utilizando el formato
      compilado. El tamaño del búfer en bytes debe ser igual a "size".

   unpack_from(buffer, offset=0)

      Idéntico a la función "unpack_from()", utilizando el formato
      compilado. El tamaño del búfer en bytes, comenzando en la
      posición *offset*, debe ser al menos "size".

   iter_unpack(buffer)

      Idéntico a la función "iter_unpack()", utilizando el formato
      compilado. El tamaño del búfer en bytes debe ser un múltiplo de
      "size".

      Added in version 3.4.

   format

      Cadena de formato utilizada para construir este objeto Struct.

      Distinto en la versión 3.7: El tipo de cadena de formato es
      ahora "str" en lugar de "bytes".

   size

      El tamaño calculado de la estructura (y, por lo tanto, del
      objeto bytes generado por el método "pack()") correspondiente a
      "format".

   Distinto en la versión 3.13: The *repr()* of structs has changed.
   It is now:

   >>> Struct('i')
   Struct('i')
