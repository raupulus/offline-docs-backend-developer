---
title: '"array" --- Efficient arrays of numeric values'
source_url: https://docs.python.org/es/3
source_path: library/array.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1550
---

# "array" --- Efficient arrays of numeric values

======================================================================

This module defines an object type which can compactly represent an
array of basic values: characters, integers, floating-point numbers.
Arrays are mutable *sequence* types and behave very much like lists,
except that the type of objects stored in them is constrained.  The
type is specified at object creation time by using a *type code*,
which is a single character.  The following type codes are defined:

+-------------+----------------------+---------------------+-------------------------+---------+
| Código de   | Tipo C               | Tipo Python         | Tamaño mínimo en bytes  | Notas   |
| tipo        |                      |                     |                         |         |
|=============|======================|=====================|=========================|=========|
## | "'b'"       | signed char          | int                 | 1                       |         |

## | "'B'"       | unsigned char        | int                 | 1                       |         |

## | "'u'"       | wchar_t              | Carácter unicode    | 2                       | (1)     |

## | "'w'"       | Py_UCS4              | Carácter unicode    | 4                       | (2)     |

## | "'h'"       | signed short         | int                 | 2                       |         |

## | "'H'"       | unsigned short       | int                 | 2                       |         |

## | "'i'"       | signed int           | int                 | 2                       |         |

## | "'I'"       | unsigned int         | int                 | 2                       |         |

## | "'l'"       | signed long          | int                 | 4                       |         |

## | "'L'"       | unsigned long        | int                 | 4                       |         |

## | "'q'"       | signed long long     | int                 | 8                       |         |

## | "'Q'"       | unsigned long long   | int                 | 8                       |         |

## | "'f'"       | float                | float               | 4                       |         |

## | "'d'"       | double               | float               | 8                       |         |

Notas:

1. Puede ser de 16 bits o 32 bits según la plataforma.

   Distinto en la versión 3.9: "array('u')" now uses "wchar_t" as C
   type instead of deprecated "Py_UNICODE". This change doesn't affect
   its behavior because "Py_UNICODE" is alias of "wchar_t" since
   Python 3.3.

   Deprecated since version 3.3, will be removed in version 3.16:
   Please migrate to "'w'" typecode.

2. Added in version 3.13.

Ver también:

  The ctypes and struct modules, as well as third-party modules like
  numpy, use similar -- but slightly different -- type codes.

The actual representation of values is determined by the machine
architecture (strictly speaking, by the C implementation).  The actual
size can be accessed through the "array.itemsize" attribute.

The module defines the following item:

array.typecodes

   Una cadena de caracteres con todos los códigos de tipos disponible.

El módulo define los siguientes tipos:

class array.array(typecode[, initializer])

   A new array whose items are restricted by *typecode*, and
   initialized from the optional *initializer* value, which must be a
   "bytes" or "bytearray" object, a Unicode string, or iterable over
   elements of the appropriate type.

   If given a "bytes" or "bytearray" object, the initializer is passed
   to the new array's "frombytes()" method; if given a Unicode string,
   the initializer is passed to the "fromunicode()" method; otherwise,
   the initializer's iterator is passed to the "extend()" method to
   add initial items to the array.

   Array objects support the ordinary mutable *sequence* operations of
   indexing, slicing, concatenation, and multiplication.  When using
   slice assignment, the assigned value must be an array object with
   the same type code; in all other cases, "TypeError" is raised.
   Array objects also implement the buffer interface, and may be used
   wherever *bytes-like objects* are supported.

   Arrays are generic over the type of their contents.

   Lanza un evento de auditoría "array.__new__" con argumentos
   "typecode", "initializer".

   typecode

      El carácter typecode utilizado para crear el arreglo.

   itemsize

      La longitud en bytes de un elemento del arreglo en su
      representación interna.

   append(value, /)

      Append a new item with the specified value to the end of the
      array.

   buffer_info()

      Return a tuple "(address, length)" giving the current memory
      address and the length in elements of the buffer used to hold
      array's contents.  The size of the memory buffer in bytes can be
      computed as "array.buffer_info()[1] * array.itemsize".  This is
      occasionally useful when working with low-level (and inherently
      unsafe) I/O interfaces that require memory addresses, such as
      certain "ioctl()" operations.  The returned numbers are valid as
      long as the array exists and no length-changing operations are
      applied to it.

      Nota:

        Cuando utilizamos objetos tipo arreglo escritos en C o C++ (la
        única manera de utilizar esta información de forma más
        efectiva), tiene más sentido utilizar interfaces buffer que
        soporten objetos del tipo arreglo. Este método es mantenido
        con retro compatibilidad y tiene que ser evitado en el nuevo
        código. Las interfaces de buffer son documentadas en Protocolo
        búfer.

   byteswap()

      "Byteswap" todos los elementos del arreglo. Solo es soportado
      para valores de tamaño 1,2,3,4 o 8 bytes; para otros valores se
      lanza "RuntimeError". Es útil cuando leemos información de un
      fichero en una máquina con diferente orden de bytes.

   count(value, /)

      Return the number of occurrences of *value* in the array.

   extend(iterable, /)

      Añade los elementos del *iterable* al final del arreglo. Si el
      *iterable* es de otro arreglo, este debe ser *exactamente* del
      mismo tipo; si no, se lanza "TypeError". Si el *iterable* no es
      un arreglo, este debe de ser un iterable y sus elementos deben
      ser del tipo correcto para ser añadidos al arreglo.

   frombytes(buffer, /)

      Appends items from the *bytes-like object*, interpreting its
      content as an array of machine values (as if it had been read
      from a file using the "fromfile()" method).

      Added in version 3.2: "fromstring()" is renamed to "frombytes()"
      for clarity.

   fromfile(f, n, /)

      Lee *n* elementos (como valores de máquina) del *file object*
      *f* y los añade al final del arreglo. Si hay menos de *n*
      elementos disponibles, se lanza "EOFError", pero los elementos
      que estaban disponibles todavía se insertan en el arreglo.

   fromlist(list, /)

      Añade los elementos de la lista. Es equivalente a "for x in
      list: a.append(x)" excepto que si hay un error de tipo, el
      arreglo no se modifica.

   fromunicode(ustr, /)

      Extends this array with data from the given Unicode string. The
      array must have type code "'u'" or "'w'"; otherwise a
      "ValueError" is raised. Use
      "array.frombytes(unicodestring.encode(enc))" to append Unicode
      data to an array of some other type.

   index(value[, start[, stop]])

      Return the smallest *i* such that *i* is the index of the first
      occurrence of *value* in the array.  The optional arguments
      *start* and *stop* can be specified to search for *value* within
      a subsection of the array.  Raise "ValueError" if *value* is not
      found.

      Distinto en la versión 3.10: Se agregaron parámetros opcionales
      *start* y *stop*.

   insert(index, value, /)

      Insert a new item *value* in the array before position *index*.
      Negative values are treated as being relative to the end of the
      array.

   pop(index=-1, /)

      Elimina el elemento con índice *i* del arreglo y lo retorna. El
      argumento opcional por defecto es "-1", en caso de utilizar el
      argumento por defecto el ultimo elemento es eliminado y
      retornado.

   remove(value, /)

      Remove the first occurrence of *value* from the array.

   clear()

      Remove all elements from the array.

      Added in version 3.13.

   reverse()

      Invierte el orden de los elementos en el arreglo.

   tobytes()

      Convierte el arreglo en un arreglo de valores máquina y retorna
      una representación en formato de bytes (la misma secuencia de
      bytes que se deben escribir en un fichero por el método
      "tofile()".)

      Added in version 3.2: "tostring()" is renamed to "tobytes()" for
      clarity.

   tofile(f, /)

      Escribe todos los elementos (incluido elementos máquina) a el
      *file object* *f*.

   tolist()

      Convierte el arreglo a una lista ordinaria con los mismos
      elementos.

   tounicode()

      Convert the array to a Unicode string.  The array must have a
      type "'u'" or "'w'"; otherwise a "ValueError" is raised. Use
      "array.tobytes().decode(enc)" to obtain a Unicode string from an
      array of some other type.

The string representation of array objects has the form
"array(typecode, initializer)". The *initializer* is omitted if the
array is empty, otherwise it is a Unicode string if the *typecode* is
"'u'" or "'w'", otherwise it is a list of numbers. The string
representation is guaranteed to be able to be converted back to an
array with the same type and value using "eval()", so long as the
"array" class has been imported using "from array import array".
Variables "inf" and "nan" must also be defined if it contains
corresponding floating-point values. Examples:

   array('l')
   array('w', 'hello \u2641')
   array('l', [1, 2, 3, 4, 5])
   array('d', [1.0, 2.0, 3.14, -inf, nan])

Ver también:

  Módulo "struct"
     Empaquetado y desempaquetado de datos binarios heterogéneos.

  NumPy
     El paquete NumPy define otro tipo de arreglo.
