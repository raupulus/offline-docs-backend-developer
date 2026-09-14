---
title: '"operator" --- Standard operators as functions'
source_url: https://docs.python.org/es/3
source_path: library/operator.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3360
---

# "operator" --- Standard operators as functions

**Código fuente:** Lib/operator.py

======================================================================

The "operator" module exports a set of efficient functions
corresponding to the intrinsic operators of Python.  For example,
"operator.add(x, y)" is equivalent to the expression "x+y". Many
function names are those used for special methods, without the double
underscores.  For backward compatibility, many of these have a variant
with the double underscores kept. The variants without the double
underscores are preferred for clarity.

Las funciones se dividen en categorías que realizan comparaciones de
objetos, operaciones lógicas, operaciones matemáticas y operaciones
sobre secuencias.

Las funciones de comparación de objetos son útiles para todos los
objetos, y llevan el nombre de los operadores de comparación
enriquecida que soportan:

operator.lt(a, b)
operator.le(a, b)
operator.eq(a, b)
operator.ne(a, b)
operator.ge(a, b)
operator.gt(a, b)
operator.__lt__(a, b)
operator.__le__(a, b)
operator.__eq__(a, b)
operator.__ne__(a, b)
operator.__ge__(a, b)
operator.__gt__(a, b)

   Realiza "comparaciones enriquecidas" entre *a* y *b*.
   Específicamente, "lt(a, b)" es equivalente a "a < b", "le(a, b)" es
   equivalente a "a <= b", "eq(a, b)" es equivalente a "a == b",
   "ne(a, b)" es equivalente a "a != b", "gt(a, b)" es equivalente a
   "a > b" y "ge(a, b)" es equivalente a "a >= b".  Tenga en cuenta
   que estas funciones pueden retornar cualquier valor, que puede o no
   ser interpretable como un valor booleano.  Consulte Comparaciones
   para obtener más información sobre las comparaciones enriquecidas.

Las operaciones lógicas también son aplicables a todos los objetos, y
admiten pruebas de verdad, pruebas de identidad y operaciones
booleanas:

operator.not_(obj)
operator.__not__(obj)

   Retorna el resultado de "not" *obj*.  (Tenga en cuenta que no hay
   ningún método "__not__()" para las instancias de objeto; solo el
   núcleo del intérprete define esta operación.  El resultado se ve
   afectado por los métodos "__bool__()" y "__len__()".)

operator.truth(obj)

   Retorna "True" si *obj* es verdadero, y "False" de lo contrario.
   Esto equivale a usar el constructor "bool".

operator.is_(a, b)

   Retorna "a is b".  Chequea la identidad del objeto.

operator.is_not(a, b)

   Retorna "a is not b".  Chequea la identidad del objeto.

operator.is_none(a)

   Return "a is None".  Tests object identity.

   Added in version 3.14.

operator.is_not_none(a)

   Return "a is not None".  Tests object identity.

   Added in version 3.14.

Las operaciones matemáticas y a nivel de bits son las más numerosas:

operator.abs(obj)
operator.__abs__(obj)

   Retorna el valor absoluto de *obj*.

operator.add(a, b)
operator.__add__(a, b)

   Retorna "a + b",  para los números *a* y *b*.

operator.and_(a, b)
operator.__and__(a, b)

   Return "a & b".

operator.floordiv(a, b)
operator.__floordiv__(a, b)

   Retorna "a // b".

operator.index(a)
operator.__index__(a)

   Retorna *a* convertido a un número entero. Equivalente a
   "a.__index__()".

   Distinto en la versión 3.10: El resultado siempre tiene el tipo
   exacto "int". Anteriormente, el resultado podría haber sido una
   instancia de una subclase de "int".

operator.inv(obj)
operator.invert(obj)
operator.__inv__(obj)
operator.__invert__(obj)

   Return "~obj".

operator.lshift(a, b)
operator.__lshift__(a, b)

   Return "a << b".

operator.mod(a, b)
operator.__mod__(a, b)

   Retorna "a % b".

operator.mul(a, b)
operator.__mul__(a, b)

   Return "a * b".

operator.matmul(a, b)
operator.__matmul__(a, b)

   Retorna "a @ b".

   Added in version 3.5.

operator.neg(obj)
operator.__neg__(obj)

   Retorna *obj* negado ("-obj").

operator.or_(a, b)
operator.__or__(a, b)

   Return "a | b".

operator.pos(obj)
operator.__pos__(obj)

   Return "+obj".

operator.pow(a, b)
operator.__pow__(a, b)

   Return "a ** b".

operator.rshift(a, b)
operator.__rshift__(a, b)

   Return "a >> b".

operator.sub(a, b)
operator.__sub__(a, b)

   Retorna "a - b".

operator.truediv(a, b)
operator.__truediv__(a, b)

   Retorna  "a / b" donde 2/3 es .66 en lugar de 0. Esto también se
   conoce como división "real" (*true division*).

operator.xor(a, b)
operator.__xor__(a, b)

   Return "a ^ b".

Las operaciones que funcionan con secuencias (y algunas de ellas
también con mapeos) incluyen:

operator.concat(a, b)
operator.__concat__(a, b)

   Retorna "a + b" para las secuencias *a* y *b*.

operator.contains(a, b)
operator.__contains__(a, b)

   Retorna el resultado del chequeo "b in a". Notar que los operandos
   se invirtieron.

operator.countOf(a, b)

   Retorna el número de ocurrencias de *b* en *a*.

operator.delitem(a, b)
operator.__delitem__(a, b)

   Remueve el valor de *a* en el índice *b*.

operator.getitem(a, b)
operator.__getitem__(a, b)

   Retorna el valor de *a* en el índice *b*.

operator.indexOf(a, b)

   Retorna el índice de la primera ocurrencia de *b* en *a*.

operator.setitem(a, b, c)
operator.__setitem__(a, b, c)

   Establece el valor de *a* en el índice *b* a *c*.

operator.length_hint(obj, default=0)

   Retorna un largo estimativo del objeto *obj*. Primero intenta
   retornar su largo real, luego un estimativo usando
   "object.__length_hint__()", y finalmente retorna un valor
   predeterminado.

   Added in version 3.4.

La siguiente operación funciona con invocables:

operator.call(obj, /, *args, **kwargs)
operator.__call__(obj, /, *args, **kwargs)

   Retorna "obj(*args, **kwargs)".

   Added in version 3.11.

The "operator" module also defines tools for generalized attribute and
item lookups.  These are useful for making fast field extractors as
arguments for "map()", "sorted()", "itertools.groupby()", or other
functions that expect a function argument.

operator.attrgetter(attr)
operator.attrgetter(*attrs)

   Retorna un objeto invocable que obtiene *attr* de su operando. Si
   se solicita más de un atributo, retorna una tupla de los atributos.
   Los nombres de los atributos también pueden contener puntos. Por
   ejemplo:

   * Después de "f = attrgetter('name')", la llamada "f(b)" retorna
     "b.name".

   * Después de "f = attrgetter('name', 'date')", la llamada "f(b)"
     retorna "(b.name, b.date)".

   * Después de "f = attrgetter('name.first', 'name.last')", la
     llamada "f(b)" retorna "(b.name.first, b.name.last)".

   Equivalente a:

      def attrgetter(*items):
          if any(not isinstance(item, str) for item in items):
              raise TypeError('attribute name must be a string')
          if len(items) == 1:
              attr = items[0]
              def g(obj):
                  return resolve_attr(obj, attr)
          else:
              def g(obj):
                  return tuple(resolve_attr(obj, attr) for attr in items)
          return g

      def resolve_attr(obj, attr):
          for name in attr.split("."):
              obj = getattr(obj, name)
          return obj

operator.itemgetter(item)
operator.itemgetter(*items)

   Return a callable object that fetches *item* from its operand using
   the operand's "__getitem__()" method.  If multiple items are
   specified, returns a tuple of lookup values.  For example:

   * Después de "f = itemgetter(2)", la llamada "f(r)" retorna "r[2]".

   * Después de "g = itemgetter(2, 5, 3)", la llamada "g(r)" retorna
     "(r[2], r[5], r[3])".

   Equivalente a:

      def itemgetter(*items):
          if len(items) == 1:
              item = items[0]
              def g(obj):
                  return obj[item]
          else:
              def g(obj):
                  return tuple(obj[item] for item in items)
          return g

   The items can be any type accepted by the operand's "__getitem__()"
   method.  Dictionaries accept any *hashable* value.  Lists, tuples,
   and strings accept an index or a slice:

   >>> itemgetter(1)('ABCDEFG')
   'B'
   >>> itemgetter(1, 3, 5)('ABCDEFG')
   ('B', 'D', 'F')
   >>> itemgetter(slice(2, None))('ABCDEFG')
   'CDEFG'
   >>> soldier = dict(rank='captain', name='dotterbart')
   >>> itemgetter('rank')(soldier)
   'captain'

   Ejemplos que utilizan "itemgetter()" para obtener campos
   específicos de un registro tupla:

   >>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
   >>> getcount = itemgetter(1)
   >>> list(map(getcount, inventory))
   [3, 2, 5, 1]
   >>> sorted(inventory, key=getcount)
   [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

operator.methodcaller(name, /, *args, **kwargs)

   Retorna un objeto invocable que a su vez invoca al método *name*
   sobre su operando. Si se pasan argumentos adicionales y/o
   argumentos por palabra clave, estos serán a su vez pasados al
   método. Por ejemplo:

   * Después de "f = methodcaller('name')", la llamada "f(b)" retorna
     "b.name()".

   * Después de "f = methodcaller('name', 'foo', bar=1)", la llamada
     "f(b)" retorna "b.name('foo', bar=1)".

   Equivalente a:

      def methodcaller(name, /, *args, **kwargs):
          def caller(obj):
              return getattr(obj, name)(*args, **kwargs)
          return caller

## Asignación de operadores a funciones

This table shows how abstract operations correspond to operator
symbols in the Python syntax and the functions in the "operator"
module.

+-------------------------+---------------------------+-----------------------------------------+
| Operación               | Sintaxis                  | Función                                 |
|=========================|===========================|=========================================|
## | Adición                 | "a + b"                   | "add(a, b)"                             |

## | Concatenación           | "seq1 + seq2"             | "concat(seq1, seq2)"                    |

## | Chequeo de pertenencia  | "obj in seq"              | "contains(seq, obj)"                    |

## | División                | "a / b"                   | "truediv(a, b)"                         |

## | División                | "a // b"                  | "floordiv(a, b)"                        |

| Bitwise And, or         | "a & b"                   | "and_(a, b)"                            |
## | Intersection            |                           |                                         |

| Bitwise Exclusive Or,   | "a ^ b"                   | "xor(a, b)"                             |
## | or Symmetric Difference |                           |                                         |

| Bitwise Inversion, or   | "~ a"                     | "invert(a)"                             |
## | Complement              |                           |                                         |

## | Bitwise Or, or Union    | "a | b"                   | "or_(a, b)"                             |

## | Exponenciación          | "a ** b"                  | "pow(a, b)"                             |

## | Identidad               | "a is b"                  | "is_(a, b)"                             |

## | Identidad               | "a is not b"              | "is_not(a, b)"                          |

## | Identidad               | "a is None"               | "is_none(a)"                            |

## | Identidad               | "a is not None"           | "is_not_none(a)"                        |

## | Asignación indexada     | "obj[k] = v"              | "setitem(obj, k, v)"                    |

## | Eliminación indexada    | "del obj[k]"              | "delitem(obj, k)"                       |

## | Indexado                | "obj[k]"                  | "getitem(obj, k)"                       |

| Desplazamiento a        | "a << b"                  | "lshift(a, b)"                          |
| izquierda (*left        |                           |                                         |
## | shift*)                 |                           |                                         |

## | Módulo                  | "a % b"                   | "mod(a, b)"                             |

## | Multiplicación          | "a * b"                   | "mul(a, b)"                             |

| Multiplicación de       | "a @ b"                   | "matmul(a, b)"                          |
## | matrices                |                           |                                         |

## | Negación (aritmética)   | "- a"                     | "neg(a)"                                |

## | Negación (lógica)       | "not a"                   | "not_(a)"                               |

## | Positivo                | "+ a"                     | "pos(a)"                                |

| Desplazamiento a        | "a >> b"                  | "rshift(a, b)"                          |
## | derecha (*right shift*) |                           |                                         |

## | Asignación por segmento | "seq[i:j] = values"       | "setitem(seq, slice(i, j), values)"     |

| Eliminación por         | "del seq[i:j]"            | "delitem(seq, slice(i, j))"             |
## | segmento                |                           |                                         |

## | Segmentación            | "seq[i:j]"                | "getitem(seq, slice(i, j))"             |

## | Formateo de cadenas     | "s % obj"                 | "mod(s, obj)"                           |

## | Sustracción             | "a - b"                   | "sub(a, b)"                             |

## | Chequeo de verdad       | "obj"                     | "truth(obj)"                            |

## | Ordenado                | "a < b"                   | "lt(a, b)"                              |

## | Ordenado                | "a <= b"                  | "le(a, b)"                              |

## | Igualdad                | "a == b"                  | "eq(a, b)"                              |

## | Diferencia              | "a != b"                  | "ne(a, b)"                              |

## | Ordenado                | "a >= b"                  | "ge(a, b)"                              |

## | Ordenado                | "a > b"                   | "gt(a, b)"                              |

## Operadores *In-place*

Muchas operaciones tienen una versión *"in-place"*. Abajo se listan
las funciones que proveen un acceso más primitivo a operadores *in-
place* que la sintaxis usual; por ejemplo, el *statement* "x += y" es
equivalente a "x = operator.iadd(x, y)". Otra forma de decirlo es que
"z = operator.iadd(x, y)" es equivalente a la sentencia (*statement*)
compuesta "z = x; z += y".

En esos ejemplo, notar que cuando se invoca un método *in-place*, el
cómputo y la asignación se realizan en dos pasos separados. Las
funciones *in-place* que se listan aquí debajo solo hacen el primer
paso, llamar al método *in-place*. El segundo paso, la asignación, no
se gestiona.

Para objetivos inmutables como cadenas de caracteres, números, y
tuplas, el valor actualizado es computado, pero no es asignado de
nuevo a la variable de entrada:

>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'

Para objetivos mutables como listas y diccionarios, el método *in-
place* realiza la actualización, así que no es necesaria una
asignación subsiguiente:

>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

operator.iadd(a, b)
operator.__iadd__(a, b)

   "a = iadd(a, b)" es equivalente a "a += b".

operator.iand(a, b)
operator.__iand__(a, b)

   "a = iand(a, b)" es equivalente a "a &= b".

operator.iconcat(a, b)
operator.__iconcat__(a, b)

   "a = iconcat(a, b)" es equivalente a "a += b" para dos *a* y *b*
   secuencias.

operator.ifloordiv(a, b)
operator.__ifloordiv__(a, b)

   "a = ifloordiv(a, b)" es equivalente a "a //= b".

operator.ilshift(a, b)
operator.__ilshift__(a, b)

   "a = ilshift(a, b)" es equivalente a "a <<= b".

operator.imod(a, b)
operator.__imod__(a, b)

   "a = imod(a, b)" es equivalente a "a %= b".

operator.imul(a, b)
operator.__imul__(a, b)

   "a = imul(a, b)" es equivalente a "a *= b".

operator.imatmul(a, b)
operator.__imatmul__(a, b)

   "a = imul(a, b)" es equivalente a "a *= b".

   Added in version 3.5.

operator.ior(a, b)
operator.__ior__(a, b)

   "a = ior(a, b)" es equivalente a "a |= b".

operator.ipow(a, b)
operator.__ipow__(a, b)

   "a = ipow(a, b)" es equivalente a "a **= b".

operator.irshift(a, b)
operator.__irshift__(a, b)

   "a = irshift(a, b)" es equivalente a "a >>= b".

operator.isub(a, b)
operator.__isub__(a, b)

   "a = isub(a, b)" es equivalente a "a -= b".

operator.itruediv(a, b)
operator.__itruediv__(a, b)

   "a = itruediv(a, b)" es equivalente a "a /= b".

operator.ixor(a, b)
operator.__ixor__(a, b)

   "a = ixor(a, b)" es equivalente a "a ^= b".
