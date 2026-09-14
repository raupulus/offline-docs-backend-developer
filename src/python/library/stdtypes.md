---
title: Tipos integrados
source_url: https://docs.python.org/es/3
source_path: library/stdtypes.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3910
---

# Tipos integrados

Esta sección describe los tipos de datos estándar que vienen incluidos
en el intérprete.

Los principales tipos de datos son: numéricos, secuencias, mapas,
clases, instancias y excepciones.

Algunas clases de tipo colección son mutables. Los métodos que añaden,
retiran u ordenan sus miembros en su lugar, y a no ser que retornen un
elemento concreto, nunca retornan la propia instancia contenedora,
sino "None".

Algunas operaciones son soportadas por varios tipos de objetos
diferentes; por ejemplo, prácticamente todos los objetos pueden ser
comparados por igualdad, evaluados para ser considerados como valores
booleanos, o representarse en forma de cadena de caracteres (ya sea
con la función "repr()" o con la función ligeramente diferente
"str()"). Esta última es la usada implícitamente cuando un objeto se
escribe con la función "print()".

## Evaluar como valor verdadero/falso

Cualquier objeto puede ser evaluado como si fuera un valor verdadero o
falso, para ser usado directamente en sentencias "if" o "while", o
como un operador en una operación booleana como las que veremos más
adelante.

By default, an object is considered true unless its class defines
either a "__bool__()" method that returns "False" or a "__len__()"
method that returns zero, when called with the object. [1] If one of
the methods raises an exception when called, the exception is
propagated and the object does not have a truth value (for example,
"NotImplemented"). Here are most of the built-in objects considered
false:

* constantes definidas para tener valor falso: "None" y "False".

* cero en cualquiera de los diferentes tipos numéricos: "0", "0.0",
  "0j", "Decimal(0)", "Fraction(0, 1)"

* cualquier colección o secuencia vacía: "''", "()", "[]", "{}",
  "set()", "range(0)"

Las operaciones y funciones integradas que tienen como resultado un
booleano siempre retornan "0" o "False" para un valor falso, y "1" o
"True" para un valor verdadero, a no ser que se indique otra cosa.
(Hay una excepción importante: Las operaciones booleanas "or" y "and"
siempre retornan uno de los dos operadores.)

## Operaciones booleanas --- "and", "or", "not"

Estas son las operaciones booleanas, ordenadas de menor a mayor
prioridad:

+---------------+-----------------------------------+---------+
| Operación     | Resultado                         | Notas   |
|===============|===================================|=========|
| "x or y"      | si *x* es verdad, entonces *x*,   | (1)     |
## |               | si no, *y*                        |         |

| "x and y"     | si *x* es falso, entonces *x*, si | (2)     |
## |               | no, *y*                           |         |

| "not x"       | si *x* es falso, entonces "True", | (3)     |
## |               | si no, "False"                    |         |

Notas:

1. Este operador usa lógica cortocircuitada, por lo que solo evalúa el
   segundo argumento si el primero es falso.

2. Este operador usa lógica cortocircuitada, por lo que solo evalúa el
   segundo argumento si el primero es verdadero.

3. El operador "not" tiene menos prioridad que los operadores no
   booleanos, así que "not a == b" se interpreta como "not (a == b)",
   y "a == not b" es un error sintáctico.

## Comparaciones

Existen ocho operadores de comparación en Python. Todos comparten el
mismo nivel de prioridad (que es mayor que el nivel de las operaciones
booleanas). Las comparaciones pueden encadenarse de cualquier manera;
por ejemplo, "x < y <= z" equivale a "x < y and y <= z", excepto
porque *y* solo se evalúa una vez (no obstante, en ambos casos *z* no
se evalúa si no es verdad que "x < y").

Esta tabla resume las operaciones de comparación:

+--------------+---------------------------+
| Operación    | Significado               |
|==============|===========================|
## | "<"          | estrictamente menor que   |

## | "<="         | menor o igual que         |

## | ">"          | estrictamente mayor que   |

## | ">="         | mayor o igual que         |

## | "=="         | igual que                 |

## | "!="         | diferente que             |

| "is"         | igualdad a nivel de       |
|              | identidad (Son el mismo   |
## |              | objeto)                   |

| "is not"     | desigualdad a nivel de    |
|              | identidad (no son el      |
## |              | mismo objeto)             |

Unless stated otherwise, objects of different types never compare
equal. The "==" operator is always defined but for some object types
(for example, class objects) is equivalent to "is". The "<", "<=", ">"
and ">=" operators are only defined where they make sense; for
example, they raise a "TypeError" exception when one of the arguments
is a complex number.

Las instancias de una clase que no son idénticas normalmente se
comparan como diferentes, a no ser que la clase defina el método
"__eq__()".

Las instancias de una clase no pueden ordenarse con respecto a otras
instancias de la misma clase, ni con otro tipo de objetos, a no ser
que la clase defina suficientes métodos "__lt__()", "__le__()",
"__gt__()" y "__ge__()" (en general, "__lt__()" y "__eq__()" son
suficientes, si solo necesitas los significados convencionales de los
operadores de comparación).

El comportamiento de los operadores "is" e "is not" no se puede
personalizar; además, se pueden aplicar a dos objetos cualquiera y
nunca lanzar una excepción.

Dos operaciones más con la misma prioridad sintáctica, "in" y "not
in", son compatibles con tipos que son *iterable* o implementan el
método "__contains__()".

## Tipos numéricos --- "int", "float", "complex"

Existen tres tipos numéricos distintos: *números enteros*, *números de
punto flotante* y *números complejos*. Además, los booleanos son un
subtipo de los números enteros. Los números enteros tienen una
precisión ilimitada. Los números de punto flotante se implementan
normalmente utilizando double en C; la información sobre la precisión
y la representación interna de los números de punto flotante para la
máquina en la que se ejecuta el programa está disponible en
"sys.float_info". Los números complejos tienen una parte real y una
imaginaria, que son cada una un número de punto flotante. Para extraer
estas partes de un número complejo *z*, utilice "z.real" y "z.imag".
(La biblioteca estándar incluye los tipos numéricos adicionales
"fractions.Fraction", para números racionales, y "decimal.Decimal",
para números de punto flotante con precisión definible por el
usuario).

Los números se crean mediante literales numéricos o como resultado de
funciones y operadores integrados. Los literales enteros sin adornos
(incluidos los números hexadecimales, octales y binarios) generan
números enteros. Los literales numéricos que contienen un punto
decimal o un signo de exponente generan números de punto flotante. Si
se añade "'j'" o "'J'" a un literal numérico, se obtiene un número
imaginario (un número complejo con una parte real cero) que se puede
sumar a un entero o un flotante para obtener un número complejo con
partes reales e imaginarias.

Las funciones constructoras "int()", "float()" y "complex()" se pueden
usar para generar números de cada tipo determinado.

Python fully supports mixed arithmetic: when a binary arithmetic
operator has operands of different built-in numeric types, the operand
with the "narrower" type is widened to that of the other:

* If both arguments are complex numbers, no conversion is performed;

* if either argument is a complex or a floating-point number, the
  other is converted to a floating-point number;

* otherwise, both must be integers and no conversion is necessary.

Arithmetic with complex and real operands is defined by the usual
mathematical formula, for example:

   x + complex(u, v) = complex(x + u, v)
   x * complex(u, v) = complex(x * u, x * v)

A comparison between numbers of different types behaves as though the
exact values of those numbers were being compared. [2]

Todos los tipos numéricos (menos los complejos) soportan las
siguientes operaciones (para las prioridades de las operaciones, véase
Prioridad de operador):

+-----------------------+-----------------------------------+-----------+----------------------+
| Operación             | Resultado                         | Notas     | Documentación        |
|                       |                                   |           | completa             |
|=======================|===================================|===========|======================|
## | "x + y"               | suma de *x* e *y*                 |           |                      |

## | "x - y"               | resta de *x* e *y*                |           |                      |

## | "x * y"               | multiplicación de *x* por *y*     |           |                      |

## | "x / y"               | división de *x* entre *y*         |           |                      |

| "x // y"              | división entera a la baja de *x*  | (1)(2)    |                      |
## |                       | entre *y*                         |           |                      |

## | "x % y"               | resto o residuo de "x / y"        | (2)       |                      |

## | "-x"                  | valor de *x*, negado              |           |                      |

## | "+x"                  | valor de *x*, sin cambiar         |           |                      |

| "abs(x)"              | valor absoluto de la magnitud de  |           | "abs()"              |
## |                       | *x*                               |           |                      |

## | "int(x)"              | valor de *x* convertido a entero  | (3)(6)    | "int()"              |

| "float(x)"            | valor de *x* convertido a número  | (4)(6)    | "float()"            |
## |                       | de coma flotante                  |           |                      |

| "complex(re, im)"     | un número complejo, con parte     | (6)       | "complex()"          |
|                       | real *re* y parte imaginaria      |           |                      |
|                       | *im*. El valor de *im* por        |           |                      |
## |                       | defecto vale cero.                |           |                      |

## | "c.conjugate()"       | conjugado del número complejo *c* |           |                      |

| "divmod(x, y)"        | el par de valores "(x // y, x %   | (2)       | "divmod()"           |
## |                       | y)"                               |           |                      |

## | "pow(x, y)"           | *x* elevado a *y*                 | (5)       | "pow()"              |

## | "x ** y"              | *x* elevado a *y*                 | (5)       |                      |

Notas:

1. También conocida como división entera a la baja. Para operandos de
   tipo "int", el resultado será de tipo "int". Para operandos de tipo
   "float", el resultado será de tipo "float". En general, el
   resultado es un número entero en el sentido matemático, pero no
   necesariamente de tipo entero "int". El resultado se redondea de
   forma automática hacia menos infinito: "1//2" es "0", "(-1)//2" es
   "-1", "1//(-2)" es "-1" y "(-1)//(-2)" es "0".

2. No es apropiada para números complejos. Es preferible convertir a
   valores en coma flotante usando la función "abs()" si fuera
   apropiado.

3. La conversión de "float" a "int" trunca y descarta la parte
   fraccionaria. Consulte las funciones "math.floor()" y "math.ceil()"
   para conocer conversiones alternativas.

4. float también acepta las cadenas de caracteres "*nan*" e "*inf*",
   con un prefijo opcional "+" o "-", para los valores *Not a Number*
   (*NaN*) e infinito positivo o negativo.

5. Python define "pow(0, 0)" y "0 ** 0" para que valgan "1", como es
   práctica habitual en los lenguajes de programación.

6. Los literales numéricos aceptables incluyen los dígitos desde el
   "0" hasta el "9", así como cualquier carácter Unicode equivalente
   (puntos de código con la propiedad "Nd").

   Consulte the Unicode Standard para obtener una lista completa de
   puntos de código con la propiedad "Nd".

Todas las clases derivadas de "numbers.Real" ("int" y "float") también
soportan las siguientes operaciones:

+----------------------+-----------------------------------------------+
| Operación            | Resultado                                     |
|======================|===============================================|
## | "math.trunc(x)"      | *x* truncado a "Integral"                     |

| "round(x[, n])"      | El valor de *x* redondeado a *n* dígitos,     |
|                      | redondeando la mitad al número par más        |
|                      | cercano (redondeo del banquero). Si no se     |
## |                      | especifica valor para *n*, se asume 0.        |

## | "math.floor(x)"      | el mayor número "Integral" que sea <= *x*     |

## | "math.ceil(x)"       | el menor número "Integral" que sea >= *x*     |

Para más operaciones numéricas consulta los módulos "math" y "cmath".

### Operaciones de bits en números enteros

Las operaciones a nivel de bit solo tienen sentido con números
enteros. El resultado de una de estas operaciones se calcula como si
se hubiera realizado en una representación en complemento a dos que
tuviera un número infinito de bits de signo.

La prioridad de todas las operaciones de bits son menores que las
operaciones numéricas, pero mayores que las comparaciones; la
operación unaria "~" tiene la misma prioridad que las otras
operaciones unarias numéricas ("+" y "-").

Esta tabla lista las operaciones de bits, ordenadas de menor a mayor
prioridad:

+--------------+----------------------------------+------------+
| Operación    | Resultado                        | Notas      |
|==============|==================================|============|
| "x | y"      | la operación *or* entre *x* e    | (4)        |
## |              | *y*                              |            |

| "x ^ y"      | la operación *exclusive or*      | (4)        |
## |              | entre *x* e *y*                  |            |

| "x & y"      | la operación *and* entre *x* e   | (4)        |
## |              | *y*                              |            |

| "x << n"     | valor de *x* desplazado a la     | (1)(2)     |
## |              | izquierda *n* bits               |            |

| "x >> n"     | valor de *x* desplazado a la     | (1)(3)     |
## |              | derecha *n* bits                 |            |

## | "~x"         | invierte los bits de *x*         |            |

Notas:

1. Los desplazamientos negativos son ilegales y lanzarán una excepción
   de tipo "ValueError".

2. Un desplazamiento de *n* bits a la izquierda es equivalente a
   multiplicar por "pow(2, n)".

3. Un desplazamiento de *n* bits a la derecha es equivalente a
   efectuar la división entera a la baja entre "pow(2, n)".

4. Realizar estos cálculos con al menos un bit extra de signo en una
   representación finita de un número en complemento a dos (un ancho
   de bits de trabajo de "1 + max(x.bit_length(), y.bit_length())" o
   más) es suficiente para obtener el mismo resultado que si se
   hubiera realizado con un número infinito de bits de signo.

### Métodos adicionales de los enteros

El tipo int implementa la *clase base abstracta* "numbers.Integral".
Además, proporciona los siguientes métodos:

int.bit_length()

   Retorna el número de bits necesarios para representar un número
   entero, excluyendo el bit de signo y los ceros a la izquierda:

      >>> n = -37
      >>> bin(n)
      '-0b100101'
      >>> n.bit_length()
      6

   De forma más precisa, si "x" es distinto de cero, entonces
   "x.bit_length()" es el único número entero positivo "k" tal que
   "2**(k-1) <= abs(x) < 2**k". De igual manera, cuando "abs(x)" es lo
   suficientemente pequeño para tener un logaritmo redondeado
   correctamente, entonces "k = 1 + int(log(abs(x), 2))". Si "x" es
   cero, entonces "x.bit_length()" retorna "0".

   Equivale a:

      def bit_length(self):
          s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
          s = s.lstrip('-0b') # remove leading zeros and minus sign
          return len(s)       # len('100101') --> 6

   Added in version 3.1.

int.bit_count()

   Retorna el número de unos en la representación binaria del valor
   absoluto del entero. Esto también se conoce como el recuento de la
   población. Ejemplo:

      >>> n = 19
      >>> bin(n)
      '0b10011'
      >>> n.bit_count()
      3
      >>> (-n).bit_count()
      3

   Equivale a:

      def bit_count(self):
          return bin(self).count("1")

   Added in version 3.10.

int.to_bytes(length=1, byteorder='big', *, signed=False)

   Retorna un arreglo de bytes que representan el número entero.

   >>> (1024).to_bytes(2, byteorder='big')
   b'\x04\x00'
   >>> (1024).to_bytes(10, byteorder='big')
   b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
   >>> (-1024).to_bytes(10, byteorder='big', signed=True)
   b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
   >>> x = 1000
   >>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
   b'\xe8\x03'

   El número entero se representa usando el número de bits indicados
   con *length* y el valor predeterminado es 1. Se lanzará la
   excepción "OverflowError" si no se puede representar el entero con
   ese número de bits.

   El argumento *byteorder* determina el orden de representación del
   número entero y el valor predeterminado es ""big"". Si *byteorder*
   es ""big"", el byte más significativo ocupa la primera posición del
   arreglo del byte. Si *byteorder* es ""little"", el byte más
   significativo estará en la última posición.

   El parámetro *signed* determina si se usa el complemento a dos para
   representar los números enteros. Si *signed* es "False", y se usa
   un valor entero negativo, se lanzará la excepción "OverflowError".
   El valor por defecto para *signed* es "False".

   Los valores predeterminados se pueden utilizar para convertir
   cómodamente un entero en un objeto de un solo byte:

      >>> (65).to_bytes()
      b'A'

   Sin embargo, al utilizar los argumentos predeterminados, no intente
   convertir un valor mayor que 255 o obtendrá un "OverflowError".

   Equivale a:

      def to_bytes(n, length=1, byteorder='big', signed=False):
          if byteorder == 'little':
              order = range(length)
          elif byteorder == 'big':
              order = reversed(range(length))
          else:
              raise ValueError("byteorder must be either 'little' or 'big'")

          return bytes((n >> i*8) & 0xff for i in order)

   Added in version 3.2.

   Distinto en la versión 3.11: Se agregaron valores de argumentos
   predeterminados para "length" y "byteorder".

classmethod int.from_bytes(bytes, byteorder='big', *, signed=False)

   Retorna el número entero que se representa por el arreglo de bytes.

   >>> int.from_bytes(b'\x00\x10', byteorder='big')
   16
   >>> int.from_bytes(b'\x00\x10', byteorder='little')
   4096
   >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
   -1024
   >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
   64512
   >>> int.from_bytes([255, 0, 0], byteorder='big')
   16711680

   El argumento *bytes* debe ser o bien un *objeto tipo binario* o un
   iterable que produzca bytes.

   El argumento *byteorder* determina el orden de representación del
   número entero y el valor predeterminado es ""big"". Si *byteorder*
   es ""big"", el byte más significativo ocupa la primera posición en
   el arreglo del byte. Si *byteorder* es ""little"", el byte más
   significativo estará en la última posición. Para solicitar el orden
   de bytes nativo del sistema host, usa "sys.byteorder" como valor de
   orden de bytes.

   El argumento *signed* indica si se representará el número entero
   usando complemento a dos.

   Equivale a:

      def from_bytes(bytes, byteorder='big', signed=False):
          if byteorder == 'little':
              little_ordered = list(bytes)
          elif byteorder == 'big':
              little_ordered = list(reversed(bytes))
          else:
              raise ValueError("byteorder must be either 'little' or 'big'")

          n = sum(b << i*8 for i, b in enumerate(little_ordered))
          if signed and little_ordered and (little_ordered[-1] & 0x80):
              n -= 1 << 8*len(little_ordered)

          return n

   Added in version 3.2.

   Distinto en la versión 3.11: Se agregó valor de argumento
   predeterminado para "byteorder".

int.as_integer_ratio()

   Devuelve un par de números enteros cuyo cociente es igual al entero
   original y tiene un denominador positivo. El cociente entero de los
   números enteros (números naturales) es siempre el entero como
   numerador y "1" como denominador.

   Added in version 3.8.

int.is_integer()

   Devuelve "True". Existe para compatibilidad de tipo pato con
   "float.is_integer()".

   Added in version 3.12.

### Métodos adicionales de float

El tipo float implementa la *clase base abstracta* "numbers.Real". Los
números float tienen además los siguientes métodos.

classmethod float.from_number(x)

   Class method to return a floating-point number constructed from a
   number *x*.

   If the argument is an integer or a floating-point number, a
   floating-point number with the same value (within Python's
   floating-point precision) is returned.  If the argument is outside
   the range of a Python float, an "OverflowError" will be raised.

   For a general Python object "x", "float.from_number(x)" delegates
   to "x.__float__()". If "__float__()" is not defined then it falls
   back to "__index__()".

   Added in version 3.14.

float.as_integer_ratio()

   Devuelve un par de números enteros cuyo cociente es exactamente
   igual al número flotante original. El cociente está en su mínima
   expresión y tiene un denominador positivo. Genera "OverflowError"
   en los números infinitos y "ValueError" en los números NaN.

float.is_integer()

   Retorna "True" si el valor en coma flotante es finita con valor
   integral, y "False" en caso contrario:

      >>> (-2.0).is_integer()
      True
      >>> (3.2).is_integer()
      False

Hay dos métodos que convierten desde y hacia cadenas de caracteres en
hexadecimal. Como los valores en coma flotante en Python se almacenan
internamente en binario, las conversiones desde o hacia cadenas
*decimales* pueden implicar un pequeño error de redondeo. Pero con
cadenas de caracteres en hexadecimal, las cadenas se corresponden y
permiten representar de forma exacta los números en coma flotante.
Esto puede ser útil, ya sea a la hora de depurar errores, o en
procesos numéricos.

float.hex()

   Retorna la representación de un valor en coma flotante en forma de
   cadena de caracteres en hexadecimal. Para números finitos, la
   representación siempre empieza con el prefijo "0x", y con una "p"
   justo antes del exponente.

classmethod float.fromhex(s)

   Método de clase que retorna el valor en coma flotante que se
   representa por la cadena de caracteres en hexadecimal *s*. La
   cadena de caracteres *s* puede tener espacios en blanco al
   principio o al final.

Nótese que "float.hex()" es un método de instancia, mientras que
"float.fromhex()" es un método de clase.

Una cadena de caracteres en hexadecimal sigue este formato:

   [sign] ['0x'] integer ['.' fraction] ['p' exponent]

donde el componente opcional "sign" puede ser o bien "+" o "-", las
componentes "integer" y "fraction" son cadenas de caracteres que solo
usan dígitos hexadecimales, y "exponent" es un número decimal,
precedido con un signo opcional. No se distingue entre mayúsculas y
minúsculas, y debe haber al menos un dígito hexadecimal tanto en la
parte entera como en la fracción. Esta sintaxis es similar a la
sintaxis especificada en la sección 6.4.4.2 del estándar C99, y es
también la sintaxis usada en Java desde la versión 1.5. En particular,
la salida de "float.hex()" se puede usar como una cadena de caracteres
en hexadecimal en código C o Java, y las cadenas de caracteres
hexadecimal producidas por el carácter de formato "%a" en C, o por el
método Java, "Double.toHexString", son aceptadas por
"float.fromhex()".

Nótese que el valor del exponente se expresa en decimal, no en
hexadecimal, e indica la potencia de 2 por la que debemos multiplicar
el coeficiente. Por ejemplo, la cadena de caracteres hexadecimal
"0x3.a7p10" representa el número en coma flotante "(3 + 10./16 +
7./16**2) * 2.0**10", o "3740.0":

   >>> float.fromhex('0x3.a7p10')
   3740.0

Si aplicamos la operación inversa a "3740.0" retorna una cadena de
caracteres hexadecimal diferente que, aun así, representa el mismo
número:

   >>> float.hex(3740.0)
   '0x1.d380000000000p+11'

### Additional Methods on Complex

The "complex" type implements the "numbers.Complex" *abstract base
class*. "complex" also has the following additional methods.

classmethod complex.from_number(x)

   Class method to convert a number to a complex number.

   For a general Python object "x", "complex.from_number(x)" delegates
   to "x.__complex__()".  If "__complex__()" is not defined then it
   falls back to "__float__()".  If "__float__()" is not defined then
   it falls back to "__index__()".

   Added in version 3.14.

### Calculo del *hash* de tipos numéricos

Para los números "x" y "y", posiblemente de tipos diferentes, es un
requisito que "hash(x) == hash(y)" siempre que "x == y" (consulte la
documentación del método "__hash__()" para obtener más detalles). Para
facilitar la implementación y la eficiencia en una variedad de tipos
numéricos (incluidos "int", "float", "decimal.Decimal" y
"fractions.Fraction"), el hash de Python para tipos numéricos se basa
en una única función matemática que se define para cualquier número
racional y, por lo tanto, se aplica a todas las instancias de "int" y
"fractions.Fraction", y a todas las instancias finitas de "float" y
"decimal.Decimal". Esencialmente, esta función se da por reducción
módulo "P" para un primo fijo "P". El valor de "P" se pone a
disposición de Python como el atributo "modulus" de "sys.hash_info".

Actualmente, el número primo usado es "P = 2**31 - 1" para máquinas de
32 bits, y "P = 2**61 - 1" en máquinas de 64 bits.

Aquí están las reglas en detalle:

* Si "x = m / n" es un número racional no negativo y "n" no es
  divisible por "P", se define "hash(x)" como "m * invmod(n, P) % P",
  donde "invmod(n, P)" retorna la inversa de "n" módulo "P".

* Si "x = m / n" es un número racional no negativo y "n" es divisible
  por "P" (pero no así "m"), entonces "n" no tiene módulo inverso de
  "P" y no se puede aplicar la regla anterior; en este caso, "hash(x)"
  retorna el valor constante definido en "sys.hash_info.inf".

* Si "x = m / n" es un número racional negativo se define "hash(x)"
  como "-hash(-x)". Si el resultado fuera "-1", lo cambia por "-2".

* Los valores concretos "sys.hash_info.inf" y "-sys.hash_info.inf" se
  usan como valores *hash* para infinito positivo o infinito negativo
  (respectivamente).

* Para un número complejo "z" (una instancia de la clase "complex"),
  el valor de *hash* se calcula combinando los valores de *hash* de la
  parte real e imaginaria, usando la fórmula "hash(z.real) +
  sys.hash_info.imag * hash(z.imag)", módulo reducido
  "2**sys.hash_info.width", de forma que el valor obtenido esté en
  rango "range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width
  - 1))". De nuevo, si el resultado fuera "-1", se reemplaza por "-2".

Para clarificar las reglas previas, aquí mostramos un ejemplo de
código Python, equivalente al cálculo realizado en la función *hash*,
para calcular el *hash* de un número racional de tipo "float" o
"complex":

   import sys, math

   def hash_fraction(m, n):
       """Compute the hash of a rational number m / n.

       Assumes m and n are integers, with n positive.
       Equivalent to hash(fractions.Fraction(m, n)).

       """
       P = sys.hash_info.modulus
       # Remove common factors of P.  (Unnecessary if m and n already coprime.)
       while m % P == n % P == 0:
           m, n = m // P, n // P

       if n % P == 0:
           hash_value = sys.hash_info.inf
       else:
           # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
           # pow(n, P-2, P) gives the inverse of n modulo P.
           hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
       if m < 0:
           hash_value = -hash_value
       if hash_value == -1:
           hash_value = -2
       return hash_value

   def hash_float(x):
       """Compute the hash of a float x."""

       if math.isnan(x):
           return object.__hash__(x)
       elif math.isinf(x):
           return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
       else:
           return hash_fraction(*x.as_integer_ratio())

   def hash_complex(z):
       """Compute the hash of a complex number z."""

       hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
       # do a signed reduction modulo 2**sys.hash_info.width
       M = 2**(sys.hash_info.width - 1)
       hash_value = (hash_value & (M - 1)) - (hash_value & M)
       if hash_value == -1:
           hash_value = -2
       return hash_value

## Tipo Booleano --- "bool"

Los valores booleanos representan valores de verdad. El tipo "bool"
tiene exactamente dos instancias constantes: "True" y "False".

La función incorporada "bool()" convierte cualquier valor en un
booleano, si el valor puede interpretarse como un valor de verdad
(consulte la sección Evaluar como valor verdadero/falso más arriba).

Para operaciones lógicas, utilice boolean operators, "and", "or" y
"not". Al aplicar los operadores bit a bit "&", "|", "^" a dos
booleanos, devuelven un booleano equivalente a las operaciones lógicas
"y", "o", "xor". Sin embargo, los operadores lógicos "and", "or" y
"!=" deberían preferirse a "&", "|" y "^".

Obsoleto desde la versión 3.12: El uso del operador de inversión bit a
bit "~" está obsoleto y generará un error en Python 3.16.

"bool" es una subclase de "int" (consulte Tipos numéricos --- int,
float, complex). En muchos contextos numéricos, "False" y "True" se
comportan como los números enteros 0 y 1, respectivamente. Sin
embargo, no se recomienda confiar en esto; realice la conversión
explícitamente utilizando "int()".

## Tipos de iteradores

Python soporta el concepto de iteradores sobre contenedores. Esto se
implementa usando dos métodos diferentes: Estos son usados por las
clases definidas por el usuario para soportar iteración. Las
secuencias, que se describirán con mayor detalle, siempre soportan la
iteración.

Es necesario definir un método para que los objetos contenedores
proporcionen compatibilidad *iterable*:

container.__iter__()

   Retorna un objeto *iterator*. Este objeto es requerido para
   soportar el protocolo de iteración que se describe a continuación.
   Si un contenedor soporta diferentes tipos de iteración, se pueden
   implementar métodos adicionales para estos iteradores. (Por
   ejemplo, un tipo de contenedor que puede soportar distintas formas
   de iteración podría ser una estructura de tipo árbol que
   proporcione a la vez un recorrido en profundidad o en anchura).
   Este método se corresponde al *slot* "tp_iter" de la estructura
   usada para los objetos Python en la API Python/C.

Los objetos iteradores en si necesitan definir los siguientes dos
métodos, que forma juntos el *iterator protocol*:

iterator.__iter__()

   Retorna el propio objeto *iterator*. Este método es necesario para
   permitir tanto a los contenedores como a los iteradores usar la
   palabras clave "for" o "in". Este método se corresponde con el
   *slot* "tp_iter" de la estructura usada para los objetos Python en
   la API Python/C.

iterator.__next__()

   Retorna el siguiente elemento del *iterator*. Si no hubiera más
   elementos, lanza la excepción "StopIteration". Este método se
   corresponde con el *slot* "tp_iternext" de la estructura usada para
   los objetos Python en la API Python/C.

Python define varios objetos iteradores que permiten iterar sobre las
secuencias, ya sean generales o específicas, diccionarios y otras
estructuras de datos especializadas. Los tipos específicos no son tan
importantes como la implementación del protocolo iterador.

Una vez que la ejecución del método "__next__()" lanza la excepción
"StopIteration", debe continuar haciéndolo en subsiguientes llamadas
al método. Si una implementación no cumple esto, se considera rota.

### Tipos generador

Python's *generator*s provide a convenient way to implement the
iterator protocol.  If a container object's "__iter__()" method is
implemented as a generator, it will automatically return an iterator
object (technically, a generator object) supplying the "__iter__()"
and "__next__()" methods. More information about generators can be
found in the documentation for the yield expression.

## Tipos secuencia --- "list", "tuple", "range"

Hay tres tipos básicos de secuencia: listas, tuplas y objetos de tipo
rango. Existen tipos de secuencia especiales usados para el procesado
de datos binarios y cadenas de caracteres que se describirán en
secciones específicas.

### Operaciones comunes de las secuencias

Las operaciones de la siguiente tabla están soportadas por la mayoría
de los tipos secuencia, tanto mutables como inmutables. La clase ABC
"collections.abc.Sequence" se incluye para facilitar la implementación
correcta de estas operaciones en nuestros propios tipos de secuencias.

La tabla lista las operaciones ordenadas de menor a mayor prioridad.
En la tabla, *s* y *t* representan secuencias del mismo tipo, *n*,
*i*, *j* y *k* son números enteros y *x* es un objeto arbitrario que
cumple con cualquier restricción de tipo o valor impuesta por *s*.

Las operaciones "in" y "not in" tienen la misma prioridad que los
operadores de comparación. Las operaciones "+" (concatenación) y "*"
(repetición) tienen la misma prioridad que sus equivalentes numéricos.
[3]

+----------------------------+----------------------------------+------------+
| Operación                  | Resultado                        | Notas      |
|============================|==================================|============|
| "x in s"                   | "True" si un elemento de *s* es  | (1)        |
|                            | igual a *x*, "False" en caso     |            |
## |                            | contrario                        |            |

| "x not in s"               | "False" si un elemento de *s* es | (1)        |
|                            | igual a *x*, "True" en caso      |            |
## |                            | contrario                        |            |

## | "s + t"                    | la concatenación de *s* y *t*    | (6)(7)     |

| "s * n" o "n * s"          | equivale a concatenar *s*        | (2)(7)     |
## |                            | consigo mismo *n* veces          |            |

| "s[i]"                     | El elemento *i-esimo* de *s*,    | (3)(8)     |
## |                            | empezando a contar en 0          |            |

| "s[i:j]"                   | el segmento de *s* desde *i*     | (3)(4)     |
## |                            | hasta *j*                        |            |

| "s[i:j:k]"                 | el segmento de *s* desde *i*     | (3)(5)     |
## |                            | hasta *j*, con paso *k*          |            |

## | "len(s)"                   | longitud de *s*                  |            |

## | "min(s)"                   | el elemento más pequeño de *s*   |            |

## | "max(s)"                   | el elemento más grande de *s*    |            |

También se pueden comparar secuencias del mismo tipo. En particular,
las tuplas y las listas se comparan por orden lexicográfico,
comparando los elementos en la misma posición. Esto significa que,
para que se consideren iguales, todos los elementos correspondientes
deben ser iguales entre si, y las dos secuencias deben ser del mismo
tipo y de la misma longitud. (Para más detalles, véase Comparaciones
en la referencia del lenguaje).

Los iteradores directos e inversos sobre secuencias mutables acceden a
valores al usar un índice. Este índice continuará avanzando (o
retrocediendo) incluso si la secuencia subyacente está mutada. El
iterador termina solo cuando se encuentra un "IndexError" o un
"StopIteration" (o cuando el índice cae por debajo de cero).

Notas:

1. Aunque las operaciones "in" y "not in" se usan generalmente para
   comprobar si un elemento está dentro de un contenedor, en algunas
   secuencias especializadas (como "str", "bytes" y "bytearray")
   también se pueden usar para comprobar si está incluida una
   secuencia:

      >>> "gg" in "eggs"
      True

2. Valores de *n* menores que "0" se consideran como "0" (que produce
   una secuencia vacía del mismo tipo que *s*). Nótese que los
   elementos de la secuencia *s* no se copian, sino que se referencian
   múltiples veces. Esto a menudo confunde a programadores noveles de
   Python; considérese:

      >>> lists = [[]] * 3
      >>> lists
      [[], [], []]
      >>> lists[0].append(3)
      >>> lists
      [[3], [3], [3]]

   Lo que ha pasado es que "[[]]" es una lista de un elemento, siendo
   este elemento una lista vacía, así que los tres elementos de "[[]]
   * 3" son referencias a la misma lista vacía. Modificar cualquiera
   de los elementos de "lists" modifica la lista inicial. Para crear
   una lista de listas independientes entre si, se puede hacer:

      >>> lists = [[] for i in range(3)]
      >>> lists[0].append(3)
      >>> lists[1].append(5)
      >>> lists[2].append(7)
      >>> lists
      [[3], [5], [7]]

   Se puede consultar una explicación más completa en esta entrada de
   la lista de preguntas más frecuentes ¿Cómo puedo crear una lista
   multidimensional?.

3. Si *i* o *j* es negativo, el índice es relativo al final de la
   secuencia *s*: Se realiza la sustitución "len(s) + i" o "len(s) +
   j". Nótese que "-0" sigue siendo "0".

4. The slice of *s* from *i* to *j* is defined as the sequence of
   items with index *k* such that "i <= k < j".

   * If *i* is omitted or "None", use "0".

   * If *j* is omitted or "None", use "len(s)".

   * If *i* or *j* is less than "-len(s)", use "0".

   * If *i* or *j* is greater than "len(s)", use "len(s)".

   * If *i* is greater than or equal to *j*, the slice is empty.

5. El segmento de *s*, desde *i* hasta *j* con paso *k*, se define
   como la secuencia de elementos con índice "x = i + n*k" tal que "0
   <= n < (j-i)/k". En otras palabras, los índices son "i", "i+k",
   "i+2*k", "i+3*k" y así consecutivamente, hasta que se alcance el
   valor de *j* (pero sin incluir nunca *j*). Cuando *k* es positivo,
   *i* y *j* se limitan al valor de "len(s)", si fueran mayores. Si
   *k* es negativo, *i* y *j* se reducen de "len(s) - 1". Si *i* o *j*
   se omiten o su valor es "None", se convierten es valores "finales"
   (donde el sentido de final depende del signo de *k*). Nótese que
   *k* no puede valer "0". Si *k* vale "None", se considera como "1".

6. La concatenación de secuencias inmutables siempre produce un nuevo
   objeto. Esto significa que construir una secuencia usando la
   concatenación tiene un coste en ejecución cuadrático respecto al
   tamaño de la secuencia final. Para obtener un rendimiento lineal,
   se puede optar por una de las alternativas siguientes:

   * en vez de concatenar objetos de tipo "str", se puede construir
     una lista y usar finalmente el método "str.join()", o bien
     utilizar una instancia de la clase "io.StringIO" y recuperar el
     valor final completo

   * de forma similar, en vez de concatenar objetos de tipo "bytes" se
     puede usar el método "bytes.join()", la clase "io.BytesIO", o se
     puede realizar una modificación interna usando un objeto de la
     clase "bytearray". Los objetos de tipo "bytearray" son mutables y
     tienen un mecanismo interno de gestión muy eficiente

   * en vez de concatenar tuplas (instancias de "tuple"), usar una
     lista ("list") y expandirla

   * para otros tipos, investiga la documentación relevante de la
     clase

7. Algunos tipos de secuencia (como la clase "range") solo soportan
   elementos que siguen un patrón específico, y por tanto no soportan
   la concatenación ni la repetición.

8. An "IndexError" is raised if *i* is outside the sequence range.

-[ Sequence Methods ]-

Sequence types also support the following methods:

sequence.count(value, /)

   Return the total number of occurrences of *value* in *sequence*.

sequence.index(value[, start[, stop]])

   Return the index of the first occurrence of *value* in *sequence*.

   Raises "ValueError" if *value* is not found in *sequence*.

   The *start* or *stop* arguments allow for efficient searching of
   subsections of the sequence, beginning at *start* and ending at
   *stop*. This is roughly equivalent to "start +
   sequence[start:stop].index(value)", only without copying any data.

   Prudencia:

     Not all sequence types support passing the *start* and *stop*
     arguments.

### Tipos de secuencia inmutables

La única operación que las secuencias inmutables implementan
generalmente, y que no esta definida también en las secuencias
mutables, es el soporte para el cálculo de la función predefinida
"hash()".

Este soporte permite usar secuencias inmutables, como por ejemplo las
instancias de la clase "tuple", como claves para diccionarios
("dict"), así como ser almacenadas en conjuntos ("set") o conjuntos
congelados ("frozenset").

Intentar calcular el *hash* de una secuencia inmutable que contenga
objetos mutables producirá una excepción de tipo "TypeError".

### Tipos de secuencia mutables

Las operaciones de la siguiente tabla están definidas para todas los
tipos de secuencia mutables. La clase ABC
"collections.abc.MutableSequence" se incluye para facilitar la
implementación correcta de un tipo de secuencia propio.

En la tabla, *s* es una instancia de una secuencia de tipo mutable,
*t* es cualquier objeto iterable y *x* es un objeto arbitrario que
cumple las restricciones de tipo y valor que vengan impuestas por *s*
(como ejemplo, la clase "bytearray" solo acepta enteros que cumplan la
condición "0 <= x <= 255").

+--------------------------------+----------------------------------+-----------------------+
| Operación                      | Resultado                        | Notas                 |
|================================|==================================|=======================|
| "s[i] = x"                     | el elemento *i* de *s* es        |                       |
## |                                | reemplazado por *x*              |                       |

## | "del s[i]"                     | removes item *i* of *s*          |                       |

| "s[i:j] = t"                   | el segmento de valores de *s*    |                       |
|                                | que van de *i* a *j* es          |                       |
|                                | reemplazada por el contenido del |                       |
## |                                | iterador *t*                     |                       |

| "del s[i:j]"                   | removes the elements of "s[i:j]" |                       |
|                                | from the list (same as "s[i:j] = |                       |
## |                                | []")                             |                       |

| "s[i:j:k] = t"                 | los elementos de "s[i:j:k]" son  | (1)                   |
|                                | reemplazados por los elementos   |                       |
## |                                | de *t*                           |                       |

| "del s[i:j:k]"                 | borra los elementos de           |                       |
## |                                | "s[i:j:k]" de la lista           |                       |

| "s += t"                       | extiende *s* con los contenidos  |                       |
|                                | de *t* (en la mayoría de los     |                       |
|                                | casos equivale a                 |                       |
## |                                | "s[len(s):len(s)] = t")          |                       |

| "s *= n"                       | actualiza *s* con su contenido   | (2)                   |
## |                                | repetido *n* veces               |                       |

Notas:

1. Si *k* no es igual a "1", *t* debe tener la misma longitud que el
   segmento a la que reemplaza.

2. El valor de *n* es un entero, o un objeto que implemente el método
   "__index__()". Los valores negativos, junto con el cero, producen
   una lista vacía. Los elementos de la secuencia no son copiados,
   sino que se referencian múltiples veces, tal y como se explicó para
   "s * n" en Operaciones comunes de las secuencias.

-[ Mutable Sequence Methods ]-

Mutable sequence types also support the following methods:

sequence.append(value, /)

   Append *value* to the end of the sequence. This is equivalent to
   writing "seq[len(seq):len(seq)] = [value]".

sequence.clear()

   Added in version 3.3.

   Remove all items from *sequence*. This is equivalent to writing
   "del sequence[:]".

sequence.copy()

   Added in version 3.3.

   Create a shallow copy of *sequence*. This is equivalent to writing
   "sequence[:]".

   Consejo:

     The "copy()" method is not part of the "MutableSequence" "ABC",
     but most concrete mutable sequence types provide it.

sequence.extend(iterable, /)

   Extend *sequence* with the contents of *iterable*. For the most
   part, this is the same as writing "seq[len(seq):len(seq)] =
   iterable".

sequence.insert(index, value, /)

   Insert *value* into *sequence* at the given *index*. This is
   equivalent to writing "sequence[index:index] = [value]".

sequence.pop(index=-1, /)

   Retrieve the item at *index* and also removes it from *sequence*.
   By default, the last item in *sequence* is removed and returned.

sequence.remove(value, /)

   Remove the first item from *sequence* where "sequence[i] == value".

   Raises "ValueError" if *value* is not found in *sequence*.

sequence.reverse()

   Reverse the items of *sequence* in place. This method maintains
   economy of space when reversing a large sequence. To remind users
   that it operates by side-effect, it returns "None".

### Listas

Las listas son secuencia mutables, usadas normalmente para almacenar
colecciones de elementos homogéneos (donde el grado de similitud de
los mismos depende de la aplicación).

class list(iterable=(), /)

   Las listas se pueden construir de diferentes formas:

   * Usando un par de corchetes para definir una lista vacía: "[]"

   * Usando corchetes, separando los elementos incluidos con comas:
     "[a]", "[a, b, c]"

   * Usando una lista intensiva o por comprensión: "[x for x in
     iterable]"

   * Usando el constructor de tipo: "list()" o "list(iterable)"

   La lista se construye con los mismos elementos y en el mismo orden
   que *iterable*, donde *iterable* puede ser una secuencia, un
   contenedor que soporta iteración, o un objeto iterador. Si
   *iterable* es de por si una lista, se construye y retorna una
   copia, como si se hubiera llamado a "iterable[:]". Por ejemplo,
   "list('abc')" retorna "['a', 'b', 'c']" y "list( (1, 2, 3) )"
   retorna "[1, 2, 3]". Si no se pasan parámetros, se construye una
   nueva lista vacía, "[]".

   Muchas otras operaciones también producen listas, incluyendo la
   función incorporada "sorted()".

   Lists are generic over the types of their items.

   Las listas implementan todas las operaciones comunes y mutables
   propias de las secuencias. Además, las listas incorporan los
   siguientes métodos:

   sort(*, key=None, reverse=False)

      Este método ordena la lista *in situ* (se modifica
      internamente), usando únicamente comparaciones de tipo "<". Las
      excepciones no son capturadas internamente: si alguna
      comparación falla, la operación entera de ordenación falla (y la
      lista probablemente haya quedado modificada parcialmente).

      El método "sort()" acepta dos parámetros, que solo pueden
      pasarse por nombre (keyword-only arguments):

      El parámetro *key* especifica una función de un argumento que se
      usa para obtener, para cada elemento de la lista, un valor
      concreto o clave (*key*) a usar en las operaciones de
      comparación (por ejemplo, "key=str.lower"). El elemento clave
      para cada elemento se calcula una única vez y se reutiliza para
      todo el proceso de ordenamiento. El valor por defecto, "None",
      hace que la lista se ordene comparando directamente los
      elementos, sin obtener valores clave.

      La utilidad "functools.cmp_to_key()" se puede usar para
      convertir una función *cmp* del estilo de la versión 2.x a una
      función *key*.

      El valor de *reverse* es un valor booleano. Si se define como
      "True", entonces los elementos de la lista se ordenan como si
      las operaciones de comparación se hubiesen invertido.

      Este método modifica la lista *in situ*, para ahorrar espacio
      cuando se ordena una secuencia muy grande. Para recordar a los
      usuarios que funciona de esta manera, no se retorna la secuencia
      ordenada (puedes usar "sorted()" para obtener de forma explicita
      una nueva secuencia ordenada).

      El método "sort()" es estable. Un algoritmo de ordenación es
      estable si garantiza que no se cambia el orden relativo que
      mantienen inicialmente los elementos que se consideran iguales
      --- esto es útil para realizar ordenaciones en múltiples fases
      (por ejemplo, ordenar por departamento y después por salario).

      Para ver ejemplos de ordenación y un breve tutorial sobre el
      tema, véase Sorting Techniques.

      Mientras una lista está siendo ordenada, los efectos de intentar
      modificarla, o incluso examinarla, no están definidos. La
      implementación en C de Python hace que la lista parezca vacía
      durante la ordenación, y lanza una excepción del tipo
      "ValueError" si detecta un cambio en la lista durante el proceso
      de ordenación.

Ver también:

  For detailed information on thread-safety guarantees for "list"
  objects, see Thread safety for list objects.

### Tuplas

Las tuplas son secuencias inmutables, usadas normalmente para
almacenar colecciones de datos heterogéneos (como las duplas o tuplas
de dos elementos producidas por la función incorporada "enumerate()").
También son usadas en aquellos casos donde se necesite una secuencia
inmutable de datos homogéneos (como por ejemplo permitir el
almacenamiento en un objeto de tipo "set" o "dict").

class tuple(iterable=(), /)

   Las tuplas se pueden construir de diferentes maneras:

   * Usando un par de símbolos de paréntesis, para indicar una tupla
     vacía: "()"

   * Usando una coma al final, para crear una tupla de un único
     elemento: "a," o "(a,)"

   * Separando los elementos por comas: "a, b, c" o "(a, b, c)"

   * Usando la función incorporada "tuple()": "tuple()" o
     "tuple(iterable)"

   El constructor genera una tupla cuyos elementos son los mismos y
   están en el mismo orden que los elementos del *iterable*, donde
   *iterable* puede ser una secuencia, un contenedor que soporta
   iteración, o un objeto de tipo *iterator*. Si *iterable* es ya de
   por si una tupla, se retorna sin cambiar. Por ejemplo,
   "tuple('abc')" retorna "('a', 'b', 'c')" y "tuple( [1, 2, 3] )"
   retorna "(1, 2, 3)". Si no se indica ningún parámetro, el
   constructor creará una nueva tupla vacía. "()".

   Nótese que es la coma la que realmente construye la tupla, no los
   paréntesis. Los paréntesis son opcionales, excepto en el caso de la
   tupla vacía, o cuando se necesitan para evitar una ambigüedad
   sintáctica. Por ejemplo, "f(a, b, c)" es una llamada a una función
   con tres parámetros, pero "f((a, b, c))" es una llamada a una
   función con un único parámetro, en este caso una tupla de tres
   elementos.

   Las tuplas implementan todas las operaciones de secuencia comunes.

   Tuples are generic over the types of their contents. For more
   information, refer to the typing documentation on annotating
   tuples.

Para colecciones de datos heterogéneos donde el acceso por nombre
resulta más claro que por índice, quizá crear una tupla con nombres
("collections.namedtuple()") pueden ser más apropiado.

### Rangos

Los objetos de tipo "range" representan una secuencia inmutable de
números y se usan habitualmente para ejecutar un bucle "for" un número
determinado de veces.

class range(stop, /)
class range(start, stop, step=1, /)

   Los parámetros usados por el constructor del rango deben ser
   números enteros (o bien objetos de tipo "int" o instancias de una
   clase que implemente el método especial "__index__()"). Si el
   parámetro *step* se omite, se asume el valor "1". Si se omite el
   parámetro "start", se toma como "0". Si *step* es cero, se lanza
   una excepción de tipo "ValueError".

   Para un valor positivo de *step*, el contenido del rango "r" viene
   determinado por la fórmula "r[i] = start + step*i" donde "i >= 0" y
   "r[i] < stop".

   Para un valor negativo de *step*, el contenido del rango sigue
   estando determinado por la fórmula "r[i] = start + step*i", pero
   las restricciones ahora son "i >= 0" y "r[i] > stop".

   Un objeto de tipo rango se considera vacío si "r[0]" no cumple con
   las restricciones de valor. Los rangos soportan índices negativos,
   pero estos son interpretados como índices considerados desde el
   final de la secuencia determinada por los índices positivos.

   Los rangos que contengan valores mayores que "sys.maxsize" se
   permiten, pero algunas capacidades (como la función "len()") pueden
   lanzar una excepción de tipo "OverflowError".

   Ejemplos de rangos:

      >>> list(range(10))
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      >>> list(range(1, 11))
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      >>> list(range(0, 30, 5))
      [0, 5, 10, 15, 20, 25]
      >>> list(range(0, 10, 3))
      [0, 3, 6, 9]
      >>> list(range(0, -10, -1))
      [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
      >>> list(range(0))
      []
      >>> list(range(1, 0))
      []

   Los rangos implementan todas las operaciones comunes de las
   secuencias, excepto la concatenación y la repetición (esto es
   porque los objetos de tipo rango solamente pueden representar
   secuencias que siguen un patrón estricto, y tanto la repetición
   como la concatenación pueden romperlo).

   start

      El valor del parámetro *start* ("0" si no se utiliza el
      parámetro)

   stop

      El valor del parámetro *stop*

   step

      El valor del parámetro *step* ("1" si no se utiliza el
      parámetro)

La ventaja de usar un objeto de tipo "range" en vez de uno de tipo
"list" o "tuple" es que con "range" siempre se usa una cantidad fija
(y pequeña) de memoria, independientemente del rango que represente
(ya que solamente necesita almacenar los valores para "start", "stop"
y "step", y calcula los valores intermedios a medida que los va
necesitando).

Los objetos rango implementan la clase ABC "collections.abc.Sequence",
y proporcionan capacidades como comprobación de inclusión, búsqueda de
elementos por índice, operaciones de segmentación y soporte de índices
negativos (véase Tipos secuencia --- list, tuple, range):

>>> r = range(0, 20, 2)
>>> r
range(0, 20, 2)
>>> 11 in r
False
>>> 10 in r
True
>>> r.index(10)
5
>>> r[5]
10
>>> r[:5]
range(0, 10, 2)
>>> r[-1]
18

La comparación entre rangos usando los operadores "==" y "!=" se
realiza como con las secuencias. Esto es, dos rangos se consideran
iguales si representan exactamente la misma secuencia de elementos.
(Fíjate que, según esta definición, dos rangos pueden considerarse
iguales aunque tengan diferentes valores para "start", "stop" y
"step", por ejemplo "range(0) == range(2, 1, 3)" y "range(0, 3, 2) ==
range(0, 4, 2)").

Distinto en la versión 3.2: Implementa la secuencia ABC. Soporta
operaciones de segmentación e índices negativos. Comprueba si un
entero de tipo "int" está incluido en un rango que se realiza en un
tiempo constante, en lugar de iterar a través de todos los elementos.

Distinto en la versión 3.3: Define los operadores '==' y '!=' para
comparar rangos en base a la secuencia de valores que definen (en vez
de compararse en base a la identidad).Se agregan los atributos
"start", "stop" y "step".

Ver también:

  * El linspace recipe muestra cómo implementar una versión perezosa
    de rango adecuada para aplicaciones de punto flotante.

## Text and Binary Sequence Type Methods Summary

The following table summarizes the text and binary sequence types
methods by category.

+----------------------------+--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
| Category                   | "str" methods                                                         | "bytes" and "bytearray" methods                                               |
|============================|====================|============|============|========================|======================|============|============|==============================|
| Formatting                 | "str.format()"                                                        |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.format_map()"                                                    |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | f-strings                                                             |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            | Formateo de cadenas al estilo *printf*                                | Usando el formateo tipo printf con bytes                                      |

| Searching and Replacing    | "str.find()"       | "str.rfind()"                                    | "bytes.find()"       | "bytes.rfind()"                                        |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.index()"      | "str.rindex()"                                   | "bytes.index()"      | "bytes.rindex()"                                       |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.startswith()"                                                    | "bytes.startswith()"                                                          |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.endswith()"                                                      | "bytes.endswith()"                                                            |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.count()"                                                         | "bytes.count()"                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            | "str.replace()"                                                       | "bytes.replace()"                                                             |

| Splitting and Joining      | "str.split()"                   | "str.rsplit()"                      | "bytes.split()"                   | "bytes.rsplit()"                          |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.splitlines()"                                                    | "bytes.splitlines()"                                                          |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.partition()"                                                     | "bytes.partition()"                                                           |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.rpartition()"                                                    | "bytes.rpartition()"                                                          |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            | "str.join()"                                                          | "bytes.join()"                                                                |

| String Classification      | "str.isalpha()"                                                       | "bytes.isalpha()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isdecimal()"                                                     |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isdigit()"                                                       | "bytes.isdigit()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isnumeric()"                                                     |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isalnum()"                                                       | "bytes.isalnum()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isidentifier()"                                                  |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.islower()"                                                       | "bytes.islower()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isupper()"                                                       | "bytes.isupper()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.istitle()"                                                       | "bytes.istitle()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.isspace()"                                                       | "bytes.isspace()"                                                             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            | "str.isprintable()"                                                   |                                                                               |

| Case Manipulation          | "str.lower()"                                                         | "bytes.lower()"                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.upper()"                                                         | "bytes.upper()"                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.casefold()"                                                      |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.capitalize()"                                                    | "bytes.capitalize()"                                                          |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.title()"                                                         | "bytes.title()"                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            | "str.swapcase()"                                                      | "bytes.swapcase()"                                                            |

| Padding and Stripping      | "str.ljust()"                   | "str.rjust()"                       | "bytes.ljust()"                   | "bytes.rjust()"                           |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.center()"                                                        | "bytes.center()"                                                              |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.expandtabs()"                                                    | "bytes.expandtabs()"                                                          |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.strip()"                                                         | "bytes.strip()"                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.lstrip()"                               | "str.rstrip()"         | "bytes.lstrip()"                               | "bytes.rstrip()"             |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.removeprefix()"                                                  | "bytes.removeprefix()"                                                        |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            | "str.removesuffix()"                                                  | "bytes.removesuffix()"                                                        |

| Translation and Encoding   | "str.translate()"                                                     | "bytes.translate()"                                                           |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.maketrans()"                                                     | "bytes.maketrans()"                                                           |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
|                            | "str.encode()"                                                        |                                                                               |
|                            +--------------------+------------+------------+------------------------+----------------------+------------+------------+------------------------------+
## |                            |                                                                       | "bytes.decode()"                                                              |

## Cadenas de caracteres --- "str"

La información textual se representa en Python con objetos de tipo
"str", normalmente llamados cadenas de caracteres o simplemente
*strings*. Las cadenas de caracteres son secuencias inmutables de
puntos de código Unicode. Las cadenas se pueden definir de diferentes
maneras:

* Comillas simples: "'permite incluir comillas "dobles"'"

* Comillas dobles: ""permite incluir comillas 'simples'""

* Triples comillas: ya sea con comillas simples "'''Triples comillas
  simples'''" o dobles """"Triples comillas dobles""""

Las cadenas definidas con comillas tripes pueden incluir varias líneas
- todos los espacios en blancos incluidos se incorporan a la cadena de
forma literal.

Cadenas literales que forman parte de una expresión y que solo estén
separados por espacios en blanco, se convertirán implícitamente a una
única cadena. Esto es, "("spam " "eggs") == "spam eggs"".

Consulte Literales de cadenas y bytes para obtener más información
sobre las distintas formas de literal de cadena, incluido escape
sequences compatible y el prefijo "r" ("sin procesar") que deshabilita
la mayoría del procesamiento de secuencias de escape.

Las cadenas de caracteres también se pueden crear usando el
constructor "str".

Como no hay un tipo separado para los "caracteres", indexar una cadena
produce una cadena de longitud 1. Esto es, para una cadena de
caracteres no vacía *s*, "s[0] == s[0:1]".

Tampoco hay una versión mutable de las cadenas de caracteres, pero el
método "str.join()" o la clase "io.StringIO" pueden usarse para
construir de forma eficiente una cadena de caracteres a partir de
fragmentos.

Distinto en la versión 3.3: Para facilitar la compatibilidad hacia
atrás con la versión 2, el prefijo "u" se permite en las cadenas de
caracteres. No tiene ningún efecto en la interpretación del literal y
no se puede combinar con el prefijo "r".

class str(*, encoding='utf-8', errors='strict')
class str(object)
class str(object, encoding, errors='strict')
class str(object, *, errors)

   Retorna una representación en forma de cadena de caracteres de
   *object*. Si no se proporciona ningún valor, retorna una cadena
   vacía. Si se proporciona, el comportamiento de "str()" depende de
   los valores pasados en los parámetros *encoding* y *errors*, como
   veremos.

   Si no se proporciona ni *encoding* ni *errors*, "str(object)"
   devuelve "type(object).__str__(object)", que es la representación
   de cadena "informal" o fácilmente imprimible de *object*. Para los
   objetos de cadena, se trata de la cadena en sí. Si *object* no
   tiene un método "__str__()", entonces "str()" vuelve a devolver
   "repr(object)".

   Si se indica alguno de los dos parámetros *encoding* o *errors*,
   entonces *object* debe ser un objeto binario o similar (*bytes-like
   object*, es decir, una instancia de "bytes" o "bytearray"). En este
   caso, si *object* es de tipo "bytes" o "bytearray", la llamada a
   "str(bytes, encoding, errors)" es equivalente a
   "bytes.decode(encoding, errors)". Si no, el objeto de tipo *bytes*
   que esta subyacente en el objeto *buffer* se obtiene mediante una
   llamada a "bytes.decode()". Véase Tipos de secuencias binarias ---
   bytes, bytearray y memoryview y Protocolo búfer para más
   información sobre los objetos *buffer*.

   Si se pasa un objeto de tipo "bytes" a la función "str()" sin
   especificar o bien el parámetro *encoding* o bien el *errors*, se
   vuelve al caso normal donde se retorna la representación informal
   de la cadena de caracteres (véase también la "-b" de las opciones
   de línea de órdenes de Python). Por ejemplo:

      >>> str(b'Zoot!')
      "b'Zoot!'"

   Para más información sobre la clase "str" y sus métodos, consulta
   Cadenas de caracteres --- str y la sección Métodos de las cadenas
   de caracteres a continuación. Para las opciones de formateo de
   cadenas, lee las secciones f-strings y Format string syntax.
   También puedes consultar la sección Servicios de procesamiento de
   texto.

### Métodos de las cadenas de caracteres

Todas las cadenas de caracteres implementan las operaciones comunes de
las secuencias, junto con los métodos descritos a continuación.

Las cadenas soportan dos estilos de formateo, uno proporciona un grado
muy completo de flexibilidad y personalización (véase "str.format()",
Format string syntax y Custom string formatting) mientras que el otro
se basa en la función C "printf", que soporta un menor número de tipos
y es ligeramente más complicada de usar, pero es a menudo más rápida
para los casos que puede manejar (Formateo de cadenas al estilo
*printf*).

La sección Servicios de procesamiento de texto de la librería estándar
cubre una serie de módulos que proporcionan varias utilidades para
trabajar con textos (incluyendo las expresiones regulares en el módulo
"re").

str.capitalize()

   Retorna una copia de la cadena con el primer carácter en mayúsculas
   y el resto en minúsculas.

   Distinto en la versión 3.8: El primer carácter se pasa ahora a
   título, más que a mayúsculas. Esto significa que caracteres como
   dígrafos solo tendrán la primera letra en mayúsculas, en vez de
   todo el carácter.

str.casefold()

   Retorna el texto de la cadena, normalizado a minúsculas. Los textos
   así normalizados pueden usarse para realizar búsquedas textuales
   independientes de mayúsculas y minúsculas.

   Casefolding is similar to lowercasing but more aggressive because
   it is intended to remove all case distinctions in a string. For
   example, the German lowercase letter "'ß'" is equivalent to ""ss"".
   Since it is already lowercase, "lower()" would do nothing to "'ß'";
   "casefold()" converts it to ""ss"". For example:

      >>> 'straße'.lower()
      'straße'
      >>> 'straße'.casefold()
      'strasse'

   The casefolding algorithm is described in section 3.13 'Default
   Case Folding' of the Unicode Standard.

   Added in version 3.3.

str.center(width, fillchar=' ', /)

   Return centered in a string of length *width*. Padding is done
   using the specified *fillchar* (default is an ASCII space). The
   original string is returned if *width* is less than or equal to
   "len(s)".  For example:

      >>> 'Python'.center(10)
      '  Python  '
      >>> 'Python'.center(10, '-')
      '--Python--'
      >>> 'Python'.center(4)
      'Python'

str.count(sub[, start[, end]])

   Retorna el número de ocurrencias no solapadas de la cadena *sub* en
   el rango [*start*, *end*]. Los parámetros opcionales *start* y
   *end* se interpretan como en una expresión de segmento.

   If *sub* is empty, returns the number of empty strings between
   characters which is the length of the string plus one. For example:

      >>> 'spam, spam, spam'.count('spam')
      3
      >>> 'spam, spam, spam'.count('spam', 5)
      2
      >>> 'spam, spam, spam'.count('spam', 5, 10)
      1
      >>> 'spam, spam, spam'.count('eggs')
      0
      >>> 'spam, spam, spam'.count('')
      17

str.encode(encoding='utf-8', errors='strict')

   Devuelve la cadena codificada a "bytes".

   El valor predeterminado de *encoding* es "'utf-8'"; consulte
   Codificaciones estándar para conocer los valores posibles.

   *errors* controla cómo se manejan los errores de codificación. Si
   se usa "'strict'" (el valor predeterminado), se genera una
   excepción "UnicodeError". Otros valores posibles son "'ignore'",
   "'replace'", "'xmlcharrefreplace'", "'backslashreplace'" y
   cualquier otro nombre registrado mediante
   "codecs.register_error()". Consulte Manejadores de errores para
   obtener más detalles.

   For performance reasons, the value of *errors* is not checked for
   validity unless an encoding error actually occurs, Modo de
   desarrollo de Python is enabled or a debug build is used. For
   example:

      >>> encoded_str_to_bytes = 'Python'.encode()
      >>> type(encoded_str_to_bytes)
      <class 'bytes'>
      >>> encoded_str_to_bytes
      b'Python'

   Distinto en la versión 3.1: Añadido soporte para poder usar
   parámetros por nombre.

   Distinto en la versión 3.9: El valor del argumento *errors* ahora
   se comprueba en Modo de desarrollo de Python y en debug mode.

str.endswith(suffix[, start[, end]])

   Return "True" if the string ends with the specified *suffix*,
   otherwise return "False".  *suffix* can also be a tuple of suffixes
   to look for.  With optional *start*, test beginning at that
   position.  With optional *end*, stop comparing at that position.
   Using *start* and *end* is equivalent to
   "str[start:end].endswith(suffix)". For example:

      >>> 'Python'.endswith('on')
      True
      >>> 'a tuple of suffixes'.endswith(('at', 'in'))
      False
      >>> 'a tuple of suffixes'.endswith(('at', 'es'))
      True
      >>> 'Python is amazing'.endswith('is', 0, 9)
      True

   See also "startswith()" and "removesuffix()".

str.expandtabs(tabsize=8)

   Return a copy of the string where all tab characters are replaced
   by one or more spaces, depending on the current column and the
   given tab size.  Tab positions occur every *tabsize* characters
   (default is 8, giving tab positions at columns 0, 8, 16 and so on).
   To expand the string, the current column is set to zero and the
   string is examined character by character.  If the character is a
   tab ("\t"), one or more space characters are inserted in the result
   until the current column is equal to the next tab position. (The
   tab character itself is not copied.)  If the character is a newline
   ("\n") or return ("\r"), it is copied and the current column is
   reset to zero.  Any other character is copied unchanged and the
   current column is incremented by one regardless of how the
   character is represented when printed. For example:

      >>> '01\t012\t0123\t01234'.expandtabs()
      '01      012     0123    01234'
      >>> '01\t012\t0123\t01234'.expandtabs(4)
      '01  012 0123    01234'
      >>> print('01\t012\n0123\t01234'.expandtabs(4))
      01  012
      0123    01234

str.find(sub[, start[, end]])

   Return the lowest index in the string where substring *sub* is
   found within the slice "s[start:end]".  Optional arguments *start*
   and *end* are interpreted as in slice notation.  Return "-1" if
   *sub* is not found. For example:

      >>> 'spam, spam, spam'.find('sp')
      0
      >>> 'spam, spam, spam'.find('sp', 5)
      6

   See also "rfind()" and "index()".

   Nota:

     El método "find()" se debe usar solo si se necesita saber la
     posición de la cadena *sub*. Si solo se necesita comprobar si
     *sub* es una parte de *s*, es mejor usar el operador "in":

        >>> 'Py' in 'Python'
        True

str.format(*args, **kwargs)

   Perform a string formatting operation.  The string on which this
   method is called can contain literal text or replacement fields
   delimited by braces "{}".  Each replacement field contains either
   the numeric index of a positional argument, or the name of a
   keyword argument.  Returns a copy of the string where each
   replacement field is replaced with the string value of the
   corresponding argument. For example:

      >>> "The sum of 1 + 2 is {0}".format(1+2)
      'The sum of 1 + 2 is 3'
      >>> "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)
      'The sum of 1 + 2 is 3'
      >>> "{1} expects the {0} Inquisition!".format("Spanish", "Nobody")
      'Nobody expects the Spanish Inquisition!'

   Véase Format string syntax para una descripción de las distintas
   opciones de formateo que se pueden usar.

   Nota:

     Cuando se formatea un número ("int", "float", "complex",
     "decimal.Decimal" y clases derivadas) usando la "n" (por ejemplo,
     "'{:n}'.format(1234)"), la función ajusta temporalmente el valor
     de la variable de entorno local "LC_TYPE" a "LC_NUMERIC" para
     decodificar los campos "decimal_point" y "thousands_sep" de la
     función "localeconv()", si usan caracteres que no son ASCII o si
     ocupan más de un byte, y el valor definido en "LC_NUMERIC" es
     diferente del definido en "LC_CTYPE". Estos cambios temporales
     pueden afectar a otros *threads*.

   Distinto en la versión 3.7: Cuando se formatea un número usando la
   "n", la función puede asignar de forma temporal la variable
   "LC_CTYPE" a "LC_NUMERIC" en algunos casos.

str.format_map(mapping, /)

   Similar a "str.format(**mapping)", pero se usa "mapping" de forma
   directa y no se copia a un diccionario. Esto es útil si "mapping"
   es, por ejemplo, una instancia de una subclase de "dict":

   >>> class Default(dict):
   ...     def __missing__(self, key):
   ...         return key
   ...
   >>> '{name} was born in {country}'.format_map(Default(name='Guido'))
   'Guido was born in country'

   Added in version 3.2.

str.index(sub[, start[, end]])

   Like "find()", but raise "ValueError" when the substring is not
   found. For example:

      >>> 'spam, spam, spam'.index('spam')
      0
      >>> 'spam, spam, spam'.index('eggs')
      Traceback (most recent call last):
        File "<python-input-0>", line 1, in <module>
          'spam, spam, spam'.index('eggs')
          ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
      ValueError: substring not found

   See also "rindex()".

str.isalnum()

   Return "True" if all characters in the string are alphanumeric and
   there is at least one character, "False" otherwise.  A character
   "c" is alphanumeric if one of the following returns "True":
   "c.isalpha()", "c.isdecimal()", "c.isdigit()", or "c.isnumeric()".
   For example:

      >>> 'abc123'.isalnum()
      True
      >>> 'abc123!@#'.isalnum()
      False
      >>> ''.isalnum()
      False
      >>> ' '.isalnum()
      False

str.isalpha()

   Return "True" if all characters in the string are alphabetic and
   there is at least one character, "False" otherwise.  Alphabetic
   characters are those characters defined in the Unicode character
   database as "Letter", i.e., those with general category property
   being one of "Lm", "Lt", "Lu", "Ll", or "Lo".  Note that this is
   different from the Alphabetic property defined in the section 4.10
   'Letters, Alphabetic, and Ideographic' of the Unicode Standard. For
   example:

      >>> 'Letters and spaces'.isalpha()
      False
      >>> 'LettersOnly'.isalpha()
      True
      >>> 'µ'.isalpha()  # non-ASCII characters can be considered alphabetical too
      True

   See Propiedades Unicode.

str.isascii()

   Return "True" if the string is empty or all characters in the
   string are ASCII, "False" otherwise. ASCII characters have code
   points in the range U+0000-U+007F. For example:

      >>> 'ASCII characters'.isascii()
      True
      >>> 'µ'.isascii()
      False

   Added in version 3.7.

str.isdecimal()

   Return "True" if all characters in the string are decimal
   characters and there is at least one character, "False" otherwise.
   Decimal characters are those that can be used to form numbers in
   base 10, such as U+0660, ARABIC-INDIC DIGIT ZERO.  Formally a
   decimal character is a character in the Unicode General Category
   "Nd". For example:

      >>> '0123456789'.isdecimal()
      True
      >>> '٠١٢٣٤٥٦٧٨٩'.isdecimal()  # Arabic-Indic digits zero to nine
      True
      >>> 'alphabetic'.isdecimal()
      False

str.isdigit()

   Return "True" if all characters in the string are digits and there
   is at least one character, "False" otherwise.  Digits include
   decimal characters and digits that need special handling, such as
   the compatibility superscript digits. This covers digits which
   cannot be used to form numbers in base 10, like the Kharosthi
   numbers. Formally, a digit is a character that has the property
   value Numeric_Type=Digit or Numeric_Type=Decimal.

   For example:

      >>> '0123456789'.isdigit()
      True
      >>> '٠١٢٣٤٥٦٧٨٩'.isdigit()  # Arabic-Indic digits zero to nine
      True
      >>> '⅕'.isdigit()  # Vulgar fraction one fifth
      False
      >>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
      (False, True, True)

   See also "isdecimal()" and "isnumeric()".

str.isidentifier()

   Retorna "True" si la cadena de caracteres es un identificador
   válido de acuerdo a la especificación del lenguaje, véase Names
   (identifiers and keywords).

   "keyword.iskeyword()" se puede utilizar para probar si la cadena
   "s" es un identificador reservado, como "def" y "class".

   Ejemplo:

      >>> from keyword import iskeyword

      >>> 'hello'.isidentifier(), iskeyword('hello')
      (True, False)
      >>> 'def'.isidentifier(), iskeyword('def')
      (True, True)

str.islower()

   Retorna "True" si todos los caracteres de la cadena que tengan
   formas en mayúsculas y minúsculas [4] están en minúsculas y hay, al
   menos, un carácter de ese tipo, en caso contrario, retorna "False".

str.isnumeric()

   Return "True" if all characters in the string are numeric
   characters, and there is at least one character, "False" otherwise.
   Numeric characters include digit characters, and all characters
   that have the Unicode numeric value property, e.g. U+2155, VULGAR
   FRACTION ONE FIFTH.  Formally, numeric characters are those with
   the property value Numeric_Type=Digit, Numeric_Type=Decimal or
   Numeric_Type=Numeric. For example:

      >>> '0123456789'.isnumeric()
      True
      >>> '٠١٢٣٤٥٦٧٨٩'.isnumeric()  # Arabic-Indic digits zero to nine
      True
      >>> '⅕'.isnumeric()  # Vulgar fraction one fifth
      True
      >>> '²'.isdecimal(), '²'.isdigit(),  '²'.isnumeric()
      (False, True, True)

   See also "isdecimal()" and "isdigit()".

str.isprintable()

   Return "True" if all characters in the string are printable,
   "False" if it contains at least one non-printable character.

   Here "printable" means the character is suitable for "repr()" to
   use in its output; "non-printable" means that "repr()" on built-in
   types will hex-escape the character.  It has no bearing on the
   handling of strings written to "sys.stdout" or "sys.stderr".

   The printable characters are those which in the Unicode character
   database (see "unicodedata") have a general category in group
   Letter, Mark, Number, Punctuation, or Symbol (L, M, N, P, or S);
   plus the ASCII space 0x20. Nonprintable characters are those in
   group Separator or Other (Z or C), except the ASCII space.

   For example:

      >>> ''.isprintable(), ' '.isprintable()
      (True, True)
      >>> '\t'.isprintable(), '\n'.isprintable()
      (False, False)

   See also "isspace()".

str.isspace()

   Retorna "True" si todos los caracteres de la cadena son espacios en
   blanco y hay, al menos, un carácter, en caso contrario, retorna
   "False".

   For example:

      >>> ''.isspace()
      False
      >>> ' '.isspace()
      True
      >>> '\t\n'.isspace() # TAB and BREAK LINE
      True
      >>> '\u3000'.isspace() # IDEOGRAPHIC SPACE
      True

   Un carácter se considera espacio en blanco si, en la base de datos
   de Unicode (véase "unicodedata"), está clasificado en la categoría
   general "Zs" ("Separador, espacio") o la clase bidireccional es
   "WS", "B" o "S".

   See also "isprintable()".

str.istitle()

   Retorna "True" si las palabras en la cadena tiene forma de título y
   hay, al menos, un carácter, por ejemplo una mayúscula solo puede
   aparecer al principio o después de un carácter que no tenga formas
   alternativas mayúsculas-minúsculas, y las minúsculas solo después
   de carácter que si tiene formas alternativas mayúsculas-minúsculas.
   En caso contrario, retorna "False".

   For example:

      >>> 'Spam, Spam, Spam'.istitle()
      True
      >>> 'spam, spam, spam'.istitle()
      False
      >>> 'SPAM, SPAM, SPAM'.istitle()
      False

   See also "title()".

str.isupper()

   Retorna "True" si todos los caracteres de la cadena que tengan
   formas en mayúsculas y minúsculas [4] están en mayúsculas y hay, al
   menos, un carácter de ese tipo, en caso contrario, retorna "False".

   >>> 'BANANA'.isupper()
   True
   >>> 'banana'.isupper()
   False
   >>> 'baNana'.isupper()
   False
   >>> ' '.isupper()
   False

str.join(iterable, /)

   Return a string which is the concatenation of the strings in
   *iterable*. A "TypeError" will be raised if there are any non-
   string values in *iterable*, including "bytes" objects.  The
   separator between elements is the string providing this method. For
   example:

      >>> ', '.join(['spam', 'spam', 'spam'])
      'spam, spam, spam'
      >>> '-'.join('Python')
      'P-y-t-h-o-n'

   See also "split()".

str.ljust(width, fillchar=' ', /)

   Retorna el texto de la cadena, justificado a la izquierda en una
   cadena de longitud *width*. El carácter de relleno a usar viene
   definido por el parámetro *fillchar* (por defecto se usa el
   carácter espacio ASCII). Si la cadena original tiene una longitud
   "len(s)" igual o superior a *width*, se retorna el texto sin
   modificar.

   For example:

      >>> 'Python'.ljust(10)
      'Python    '
      >>> 'Python'.ljust(10, '.')
      'Python....'
      >>> 'Monty Python'.ljust(10, '.')
      'Monty Python'

   See also "rjust()".

str.lower()

   Return a copy of the string with all the cased characters [4]
   converted to lowercase. For example:

      >>> 'Lower Method Example'.lower()
      'lower method example'

   The lowercasing algorithm used is described in section 3.13
   'Default Case Folding' of the Unicode Standard.

str.lstrip(chars=None, /)

   Retorna una copia de la cadena, eliminado determinados caracteres
   si se encuentren al principio. El parámetro *chars* especifica el
   conjunto de caracteres a eliminar. Si se omite o si se especifica
   "None", se eliminan todos los espacios en blanco. No debe
   entenderse el valor de *chars* como un prefijo, sino que se elimina
   cualquier combinación de sus caracteres:

      >>> '   spacious   '.lstrip()
      'spacious   '
      >>> 'www.example.com'.lstrip('cmowz.')
      'example.com'

   Véase  "str.removeprefix()" para un método que removerá una única
   cadena de prefijo en lugar de todas las ocurrencias dentro de un
   set de caracteres. Por ejemplo:

      >>> 'Arthur: three!'.lstrip('Arthur: ')
      'ee!'
      >>> 'Arthur: three!'.removeprefix('Arthur: ')
      'three!'

static str.maketrans(dict, /)
static str.maketrans(from, to, remove='', /)

   Este método estático retorna una tabla de traducción apta para ser
   usada por el método "str.translate()".

   Si solo se usa un parámetro, este debe ser un diccionario que mapea
   valores de punto Unicode (enteros) o caracteres (cadenas de
   longitud 1) a valores Unicode, cadenas (de cualquier longitud) o
   "None". Las claves se convertirán a ordinales.

   If there are two arguments, they must be strings of equal length,
   and in the resulting dictionary, each character in *from* will be
   mapped to the character at the same position in *to*.  If there is
   a third argument, it must be a string, whose characters will be
   mapped to "None" in the result.

str.partition(sep, /)

   Divide la cadena en la primera ocurrencia de *sep*, y retorna una
   tupla de tres elementos, que contiene la parte anterior al
   separador, el separador en sí y la parte posterior al separador. Si
   no se encuentra el separador, retorna una tupla de tres elementos,
   el primero contiene la cadena original y los dos siguientes son
   cadenas vacías.

   For example:

      >>> 'Monty Python'.partition(' ')
      ('Monty', ' ', 'Python')
      >>> "Monty Python's Flying Circus".partition(' ')
      ('Monty', ' ', "Python's Flying Circus")
      >>> 'Monty Python'.partition('-')
      ('Monty Python', '', '')

   See also "rpartition()".

str.removeprefix(prefix, /)

   If the string starts with the *prefix* string, return
   "string[len(prefix):]". Otherwise, return a copy of the original
   string:

      >>> 'TestHook'.removeprefix('Test')
      'Hook'
      >>> 'BaseTestCase'.removeprefix('Test')
      'BaseTestCase'

   Added in version 3.9.

   See also "removesuffix()" and "startswith()".

str.removesuffix(suffix, /)

   If the string ends with the *suffix* string and that *suffix* is
   not empty, return "string[:-len(suffix)]". Otherwise, return a copy
   of the original string:

      >>> 'MiscTests'.removesuffix('Tests')
      'Misc'
      >>> 'TmpDirMixin'.removesuffix('Tests')
      'TmpDirMixin'

   Added in version 3.9.

   See also "removeprefix()" and "endswith()".

str.replace(old, new, /, count=-1)

   Return a copy of the string with all occurrences of substring *old*
   replaced by *new*.  If *count* is given, only the first *count*
   occurrences are replaced. If *count* is not specified or "-1", then
   all occurrences are replaced. For example:

      >>> 'spam, spam, spam'.replace('spam', 'eggs')
      'eggs, eggs, eggs'
      >>> 'spam, spam, spam'.replace('spam', 'eggs', 1)
      'eggs, spam, spam'

   Distinto en la versión 3.13: *count* es ahora soportado como
   argumento de palabra clave.

str.rfind(sub[, start[, end]])

   Return the highest index in the string where substring *sub* is
   found, such that *sub* is contained within "s[start:end]".
   Optional arguments *start* and *end* are interpreted as in slice
   notation.  Return "-1" on failure. For example:

      >>> 'spam, spam, spam'.rfind('sp')
      12
      >>> 'spam, spam, spam'.rfind('sp', 0, 10)
      6

   See also "find()" and "rindex()".

str.rindex(sub[, start[, end]])

   Like "rfind()" but raises "ValueError" when the substring *sub* is
   not found. For example:

      >>> 'spam, spam, spam'.rindex('spam')
      12
      >>> 'spam, spam, spam'.rindex('eggs')
      Traceback (most recent call last):
        File "<stdin-0>", line 1, in <module>
          'spam, spam, spam'.rindex('eggs')
          ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
      ValueError: substring not found

   See also "index()" and "find()".

str.rjust(width, fillchar=' ', /)

   Retorna el texto de la cadena, justificado a la derecha en una
   cadena de longitud *width*. El carácter de relleno a usar viene
   definido por el parámetro *fillchar* (por defecto se usa el
   carácter espacio ASCII). Si *width* es menor o igual que "len(s)",
   se retorna el texto sin modificar.

   For example:

      >>> 'Python'.rjust(10)
      '    Python'
      >>> 'Python'.rjust(10, '.')
      '....Python'
      >>> 'Monty Python'.rjust(10, '.')
      'Monty Python'

   See also "ljust()" and "zfill()".

str.rpartition(sep, /)

   Divide la cadena en la última ocurrencia de *sep*, y retorna una
   tupla de tres elementos, conteniendo la parte anterior al
   separador, el separador en sí y la parte posterior al separador. Si
   no se encuentra el separador, retorna una tupla de tres elementos,
   los dos primeras son posiciones con cadenas vacías y en la tercera
   la cadena original.

   For example:

      >>> 'Monty Python'.rpartition(' ')
      ('Monty', ' ', 'Python')
      >>> "Monty Python's Flying Circus".rpartition(' ')
      ("Monty Python's Flying", ' ', 'Circus')
      >>> 'Monty Python'.rpartition('-')
      ('', '', 'Monty Python')

   See also "partition()".

str.rsplit(sep=None, maxsplit=-1)

   Retorna una lista con las palabras que componen la cadena de
   caracteres original, usando como separador el valor de *sep*. Si se
   utiliza el parámetro *maxsplit*, se realizan como máximo *maxsplit*
   divisiones, retornando los que están más a la derecha. Si no se
   especifica *sep* o se pasa con valor "None", se usa como separador
   cualquier carácter de espacio en blanco. Si no contamos la
   diferencia de empezar las divisiones desde la derecha, el
   comportamiento de este método "rsplit()" es equivalente al de
   "split()", que se describe con detalle más adelante.

str.rstrip(chars=None, /)

   Return a copy of the string with trailing characters removed.  The
   *chars* argument is a string specifying the set of characters to be
   removed.  If omitted or "None", the *chars* argument defaults to
   removing whitespace.  The *chars* argument is not a suffix; rather,
   all combinations of its values are stripped. For example:

      >>> '   spacious   '.rstrip()
      '   spacious'
      >>> 'mississippi'.rstrip('ipz')
      'mississ'

   See "removesuffix()" for a method that will remove a single suffix
   string rather than all of a set of characters.  For example:

      >>> 'Monty Python'.rstrip(' Python')
      'M'
      >>> 'Monty Python'.removesuffix(' Python')
      'Monty'

   See also "strip()".

str.split(sep=None, maxsplit=-1)

   Retorna una lista con las palabras que componen la cadena de
   caracteres original, usando como separador el valor de *sep*. Si se
   utiliza el parámetro *maxsplit*, se realizan como máximo *maxsplit*
   divisiones (por tanto, la lista resultante tendrá "maxsplit+1"
   elementos). Si no se especifica *maxsplit* o se pasa con valor
   "-1", entonces no hay límite al número de divisiones a realizar (se
   harán todas las que se puedan).

   Si se proporciona *sep*, los delimitadores consecutivos no se
   agrupan y se consideran que delimitan cadenas vacías (por ejemplo,
   "'1,,2'.split(',')" devuelve "['1', '', '2']"). El argumento *sep*
   puede constar de varios caracteres como un único delimitador (para
   dividir con varios delimitadores, utilice "re.split()"). Dividir
   una cadena vacía con un separador especificado devuelve "['']".

   For example:

      >>> '1,2,3'.split(',')
      ['1', '2', '3']
      >>> '1,2,3'.split(',', maxsplit=1)
      ['1', '2,3']
      >>> '1,2,,3,'.split(',')
      ['1', '2', '', '3', '']
      >>> '1<>2<>3<4'.split('<>')
      ['1', '2', '3<4']

   Si no se especifica *sep* o es "None", se usa un algoritmo de
   división diferente: secuencias consecutivas de caracteres de
   espacio en blanco se consideran como un único separador, y el
   resultado no contendrá cadenas vacías ni al principio ni al final
   de la lista, aunque la cadena original tuviera espacios en blanco
   al principio o al final. En consecuencia, dividir una cadena vacía
   o una cadena que solo contenga espacios en blanco usando "None"
   como separador siempre retornará una lista vacía "[]".

   For example:

      >>> '1 2 3'.split()
      ['1', '2', '3']
      >>> '1 2 3'.split(maxsplit=1)
      ['1', '2 3']
      >>> '   1   2   3   '.split()
      ['1', '2', '3']

   If *sep* is not specified or is "None" and  *maxsplit* is "0", only
   leading runs of consecutive whitespace are considered.

   For example:

      >>> "".split(None, 0)
      []
      >>> "   ".split(None, 0)
      []
      >>> "   foo   ".split(maxsplit=0)
      ['foo   ']

   See also "join()" and "rsplit()".

str.splitlines(keepends=False)

   Retorna una lista con las líneas en la cadena, dividiendo por los
   saltos de línea. Los caracteres de salto de línea en sí no se
   incluyen a no ser que se especifique lo contrario pasando el valor
   "True" en al parámetro *keepends*.

   Este método considera como saltos de línea los siguientes
   caracteres. En concreto, estos son un superconjunto de los *saltos
   de líneas universales*.

   +-------------------------+-------------------------------+
   | Representación          | Descripción                   |
   |=========================|===============================|
   | "\n"                    | Salto de línea                |
   +-------------------------+-------------------------------+
   | "\r"                    | Retorno de carro              |
   +-------------------------+-------------------------------+
   | "\r\n"                  | Retorno de carro + salto de   |
   |                         | línea                         |
   +-------------------------+-------------------------------+
   | "\v" o "\x0b"           | Tabulación de línea           |
   +-------------------------+-------------------------------+
   | "\f" o "\x0c"           | Avance de página              |
   +-------------------------+-------------------------------+
   | "\x1c"                  | Separador de archivo          |
   +-------------------------+-------------------------------+
   | "\x1d"                  | Separador de grupo            |
   +-------------------------+-------------------------------+
   | "\x1e"                  | Separador de registro         |
   +-------------------------+-------------------------------+
   | "\x85"                  | Siguiente línea (Código de    |
   |                         | control C1)                   |
   +-------------------------+-------------------------------+
   | "\u2028"                | Separador de línea            |
   +-------------------------+-------------------------------+
   | "\u2029"                | Separador de párrafo          |
   +-------------------------+-------------------------------+

   Distinto en la versión 3.2: Se añadieron "\v" y "\f" a la lista de
   separadores.

   Por ejemplo:

      >>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
      ['ab c', '', 'de fg', 'kl']
      >>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
      ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

   Al contrario que con "split()", cuando se especifica una cadena con
   *sep*, el método retorna una lista vacía para la cadena vacía, y un
   salto de línea al final del texto no produce una línea extra:

      >>> "".splitlines()
      []
      >>> "One line\n".splitlines()
      ['One line']

   Por comparación, "split('\n')" entrega:

      >>> ''.split('\n')
      ['']
      >>> 'Two lines\n'.split('\n')
      ['Two lines', '']

str.startswith(prefix[, start[, end]])

   Retorna "True" si la cadena empieza por *prefix*, en caso contrario
   retorna "False". El valor de *prefix* puede ser también una tupla
   de prefijos por los que buscar. Con el parámetro opcional *start*,
   la comprobación empieza en esa posición de la cadena. Con el
   parámetro opcional *end*, la comprobación se detiene en esa
   posición de la cadena.

   For example:

      >>> 'Python'.startswith('Py')
      True
      >>> 'a tuple of prefixes'.startswith(('at', 'a'))
      True
      >>> 'Python is amazing'.startswith('is', 7)
      True

   See also "endswith()" and "removeprefix()".

str.strip(chars=None, /)

   Return a copy of the string with the leading and trailing
   characters removed. The *chars* argument is a string specifying the
   set of characters to be removed. If omitted or "None", the *chars*
   argument defaults to removing whitespace. The *chars* argument is
   not a prefix or suffix; rather, all combinations of its values are
   stripped.

   Whitespace characters are defined by "str.isspace()".

   For example:

      >>> '   spacious   '.strip()
      'spacious'
      >>> 'www.example.com'.strip('cmowz.')
      'example'

   The outermost leading and trailing *chars* argument values are
   stripped from the string. Characters are removed from the leading
   end until reaching a string character that is not contained in the
   set of characters in *chars*. A similar action takes place on the
   trailing end.

   For example:

      >>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
      >>> comment_string.strip('.#! ')
      'Section 3.2.1 Issue #32'

   See also "rstrip()".

str.swapcase()

   Return a copy of the string with uppercase characters converted to
   lowercase and vice versa. For example:

      >>> 'Hello World'.swapcase()
      'hELLO wORLD'

   Note that it is not necessarily true that "s.swapcase().swapcase()
   == s". For example:

      >>> 'straße'.swapcase().swapcase()
      'strasse'

   See also "str.lower()" and "str.upper()".

str.title()

   Retorna una versión en forma de título de la cadena, con la primera
   letra de cada palabra en mayúsculas y el resto en minúsculas.

   Por ejemplo:

      >>> 'Hello world'.title()
      'Hello World'

   El algoritmo usa una definición sencilla e independiente del
   lenguaje, consistente en considerar una palabra como un grupo de
   letras consecutivas. Esta definición funciona en varios entornos,
   pero implica que, por ejemplo en inglés, los apóstrofos en las
   contracciones y en los posesivos constituyen una separación entre
   palabras, que puede que no sea el efecto deseado:

      >>> "they're bill's friends from the UK".title()
      "They'Re Bill'S Friends From The Uk"

   La función "string.capwords()" no tiene este problema, ya que solo
   divide palabras en espacios.

   Alternativamente, se puede solucionar parcialmente el problema de
   los apóstrofos usando expresiones regulares:

      >>> import re
      >>> def titlecase(s):
      ...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
      ...                   lambda mo: mo.group(0).capitalize(),
      ...                   s)
      ...
      >>> titlecase("they're bill's friends.")
      "They're Bill's Friends."

   See also "istitle()".

str.translate(table, /)

   Devuelve una copia de la cadena en la que se ha asignado cada
   carácter a través de la tabla de traducción dada. La tabla debe ser
   un objeto que implemente la indexación mediante "__getitem__()",
   normalmente *mapping* o *sequence*. Cuando se indexa mediante un
   ordinal Unicode (un entero), el objeto de tabla puede realizar
   cualquiera de las siguientes acciones: devolver un ordinal Unicode
   o una cadena, para asignar el carácter a uno o más caracteres;
   devolver "None", para eliminar el carácter de la cadena de retorno;
   o generar una excepción "LookupError", para asignar el carácter a
   sí mismo.

   Se puede usar "str.maketrans()" para crear un mapa de traducción
   carácter a carácter de diferentes formas.

   Véase también el módulo "codecs" para una aproximación más flexible
   al mapeo de caracteres.

str.upper()

   Retorna una copia de la cadena, con todos los caracteres con formas
   mayúsculas/minúsculas [4] pasados a mayúsculas. Nótese que
   "s.upper().isupper()" puede ser "False" si "s" contiene caracteres
   que no tengan las dos formas, o si la categoría Unicode del
   carácter o caracteres resultantes no es "Lu" (Letra, mayúsculas),
   sino, por ejemplo, "Lt" (Letra, Título).

   The uppercasing algorithm used is described in section 3.13
   'Default Case Folding' of the Unicode Standard.

str.zfill(width, /)

   Retorna una copia de la cadena, rellena por la izquierda con
   dígitos "'0'" de ASCII necesarios para conseguir una cadena de
   longitud *width*. El carácter prefijo de signo ("'+'"/"'-'") se
   gestiona insertando el relleno *después* del carácter de signo en
   vez de antes. Si *width* es menor o igual que "len(s)", se retorna
   la cadena original.

   For example:

      >>> "42".zfill(5)
      '00042'
      >>> "-42".zfill(5)
      '-0042'

   See also "rjust()".

### Formatted String Literals (f-strings)

Added in version 3.6.

Distinto en la versión 3.7: The "await" and "async for" can be used in
expressions within f-strings.

Distinto en la versión 3.8: Added the debug specifier ("=")

Distinto en la versión 3.12: Many restrictions on expressions within
f-strings have been removed. Notably, nested strings, comments, and
backslashes are now permitted.

An *f-string* (formally a *formatted string literal*) is a string
literal that is prefixed with "f" or "F". This type of string literal
allows embedding the results of arbitrary Python expressions within
*replacement fields*, which are delimited by curly brackets ("{}").
Each replacement field must contain an expression, optionally followed
by:

* a *debug specifier* -- an equal sign ("=");

* a *conversion specifier* -- "!s", "!r" or "!a"; and/or

* a *format specifier* prefixed with a colon (":").

See the Lexical Analysis section on f-strings for details on the
syntax of these fields.

#### Debug specifier

Added in version 3.8.

If a debug specifier -- an equal sign ("=") -- appears after the
replacement field expression, the resulting f-string will contain the
expression's source, the equal sign, and the value of the expression.
This is often useful for debugging:

   >>> number = 14.3
   >>> f'{number=}'
   'number=14.3'

Whitespace before, inside and after the expression, as well as
whitespace after the equal sign, is significant --- it is retained in
the result:

   >>> f'{ number  -  4  = }'
   ' number  -  4  = 10.3'

#### Conversion specifier

By default, the value of a replacement field expression is converted
to a string using "str()":

   >>> from fractions import Fraction
   >>> one_third = Fraction(1, 3)
   >>> f'{one_third}'
   '1/3'

When a debug specifier but no format specifier is used, the default
conversion instead uses "repr()":

   >>> f'{one_third = }'
   'one_third = Fraction(1, 3)'

The conversion can be specified explicitly using one of these
specifiers:

* "!s" for "str()"

* "!r" for "repr()"

* "!a" for "ascii()"

Por ejemplo:

   >>> str(one_third)
   '1/3'
   >>> repr(one_third)
   'Fraction(1, 3)'

   >>> f'{one_third!s} is {one_third!r}'
   '1/3 is Fraction(1, 3)'

   >>> string = "¡kočka 😸!"
   >>> ascii(string)
   "'\\xa1ko\\u010dka \\U0001f638!'"

   >>> f'{string = !a}'
   "string = '\\xa1ko\\u010dka \\U0001f638!'"

#### Format specifier

After the expression has been evaluated, and possibly converted using
an explicit conversion specifier, it is formatted using the "format()"
function. If the replacement field includes a *format specifier*
introduced by a colon (":"), the specifier is passed to "format()" as
the second argument. The result of "format()" is then used as the
final value for the replacement field. For example:

   >>> from fractions import Fraction
   >>> one_third = Fraction(1, 3)
   >>> f'{one_third:.6f}'
   '0.333333'
   >>> f'{one_third:_^+10}'
   '___+1/3___'
   >>> >>> f'{one_third!r:_^20}'
   '___Fraction(1, 3)___'
   >>> f'{one_third = :~>10}~'
   'one_third = ~~~~~~~1/3~'

### Template String Literals (t-strings)

An *t-string* (formally a *template string literal*) is a string
literal that is prefixed with "t" or "T".

These strings follow the same syntax and evaluation rules as formatted
string literals, with for the following differences:

* Rather than evaluating to a "str" object, template string literals
  evaluate to a "string.templatelib.Template" object.

* The "format()" protocol is not used. Instead, the format specifier
  and conversions (if any) are passed to a new "Interpolation" object
  that is created for each evaluated expression. It is up to code that
  processes the resulting "Template" object to decide how to handle
  format specifiers and conversions.

* Format specifiers containing nested replacement fields are evaluated
  eagerly, prior to being passed to the "Interpolation" object. For
  instance, an interpolation of the form "{amount:.{precision}f}" will
  evaluate the inner expression "{precision}" to determine the value
  of the "format_spec" attribute. If "precision" were to be "2", the
  resulting format specifier would be "'.2f'".

* When the equals sign "'='" is provided in an interpolation
  expression, the text of the expression is appended to the literal
  string that precedes the relevant interpolation. This includes the
  equals sign and any surrounding whitespace. The "Interpolation"
  instance for the expression will be created as normal, except that
  "conversion" will be set to '"r"' ("repr()") by default. If an
  explicit conversion or format specifier are provided, this will
  override the default behaviour.

### Formateo de cadenas al estilo "*printf*"

Nota:

  The formatting operations described here exhibit a variety of quirks
  that lead to a number of common errors (such as failing to display
  tuples and dictionaries correctly).Using formatted string literals,
  the "str.format()" interface, or "string.Template" may help avoid
  these errors. Each of these alternatives provides their own trade-
  offs and benefits of simplicity, flexibility, and/or extensibility.

Los objetos de cadena tienen una única operación incorporada: el
operador "%" (módulo). También se lo conoce como operador de cadena
*formatting* o *interpolation*. Dado "format % values" (donde *format*
es una cadena), las especificaciones de conversión "%" en *format* se
reemplazan con cero o más elementos de *values*. El efecto es similar
al uso de la función "sprintf()" en el lenguaje C. Por ejemplo:

   >>> print('%s has %d quote types.' % ('Python', 2))
   Python has 2 quote types.

Si *formato* tiene un único marcador, *valores* puede ser un objeto
sencillo, no una tupla. [5] En caso contrario, *valores* debe ser una
tupla con exactamente el mismo número de elementos que marcadores
usados en la cadena de formato, o un único objeto de tipo mapa (por
ejemplo, un diccionario).

Un especificador de conversión consiste en dos o más caracteres y
tiene los siguientes componentes, que deben aparecer en el siguiente
orden:

1. El carácter "'%'", que identifica el inicio del marcador.

2. Una clave de mapeo (opcional), consistente en una secuencia de
   caracteres entre paréntesis, como por ejemplo, "(somename)".

3. Indicador de conversión (opcional), que afecta el resultado de
   ciertas conversiones de tipos.

4. Valor de ancho mínimo (opcional). Si se especifica un "'*'"
   (asterisco), el ancho real se lee del siguiente elemento de la
   tupla *valores*, y el objeto a convertir viene después del ancho
   mínimo, con un indicador de precisión opcional.

5. Precisión (opcional), en la forma "'.'" (punto) seguido de la
   precisión. Si se especifica un "'*'" (asterisco), el valor de
   precisión real se lee del siguiente elemento de la tupla *valores*,
   y el valor a convertir viene después de la precisión.

6. Modificador de longitud (opcional).

7. Tipo de conversión.

Cuando el operador derecho es un diccionario (o cualquier otro objeto
de tipo mapa), los marcadores en la cadena *deben* incluir un valor de
clave entre paréntesis, inmediatamente después del carácter "'%'". El
valor de la clave se usa para seleccionar el valor a formatear desde
el mapa. Por ejemplo:

>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.

En este caso, no se puede usar el especificador "*" en la cadena de
formato (dado que requiere una lista secuencial de parámetros).

Los indicadores de conversión son:

+-----------+-----------------------------------------------------------------------+
| Flag      | Significado                                                           |
|===========|=======================================================================|
| "'#'"     | El valor a convertir usara la "forma alternativa" (que se definirá    |
## |           | más adelante)                                                         |

| "'0'"     | La conversión rellena con ceros por la izquierda para valores         |
## |           | numéricos.                                                            |

| "'-'"     | El valor convertido se ajusta a la izquierda (sobreescribe la         |
## |           | conversión "'0'" si se especifican los dos)                           |

| "' '"     | (Un espacio) Se debe añadir un espacio en blanco antes de un número   |
## |           | positivo (o una cadena vacía) si se usa una conversión con signo.     |

| "'+'"     | Un carácter signo ("'+'" o "'-'") precede a la conversión             |
## |           | (sobreescribe el indicador de "espacio")                              |

Puede estar presente un modificador de longitud ("h", "l" o "L"), pero
se ignora y no es necesario para Python -- por lo que, por ejemplo, la
salida de "%ld" es idéntica a "%d".

Los tipos de conversión son:

+--------------+-------------------------------------------------------+---------+
| Conversión   | Significado                                           | Notas   |
|==============|=======================================================|=========|
## | "'d'"        | Entero decimal con signo.                             |         |

## | "'i'"        | Entero decimal con signo.                             |         |

## | "'o'"        | Valor octal con signo.                                | (1)     |

## | "'u'"        | Obsoleto -- es idéntico a "'d'".                      | (6)     |

## | "'x'"        | Hexadecimal con signo (en minúsculas).                | (2)     |

## | "'X'"        | Hexadecimal con signo (en mayúsculas).                | (2)     |

## | "'e'"        | Formato en coma flotante exponencial (en minúsculas). | (3)     |

## | "'E'"        | Formato en coma flotante exponencial (en mayúsculas). | (3)     |

## | "'f'"        | Formato en coma flotante decimal.                     | (3)     |

## | "'F'"        | Formato en coma flotante decimal.                     | (3)     |

| "'g'"        | Formato de punto flotante. Utiliza el formato         | (4)     |
|              | exponencial en minúsculas si el exponente es menor    |         |
|              | que -4 o igual que la precisión; en caso contrario,   |         |
## |              | utiliza el formato decimal.                           |         |

| "'G'"        | Formato de punto flotante. Utiliza el formato         | (4)     |
|              | exponencial en mayúsculas si el exponente es menor    |         |
|              | que -4 o igual que la precisión; en caso contrario,   |         |
## |              | utiliza el formato decimal.                           |         |

| "'c'"        | Un único carácter (acepta números enteros o cadenas   |         |
## |              | de caracteres de longitud 1).                         |         |

| "'r'"        | Cadena de caracteres (representará cualquier objeto   | (5)     |
## |              | usando la función "repr()").                          |         |

| "'s'"        | Cadena de caracteres (representará cualquier objeto   | (5)     |
## |              | usando la función "str()").                           |         |

| "'a'"        | Cadena de caracteres (representará cualquier objeto   | (5)     |
## |              | usando la función "ascii()").                         |         |

| "'%'"        | No se representa ningún argumento, obteniéndose en el |         |
## |              | resultado la cadena "'%'".                            |         |

For floating-point formats, the result should be correctly rounded to
a given precision "p" of digits after the decimal point.  The rounding
mode matches that of the "round()" builtin.

Notas:

1. La forma alternativa hace que se inserte antes del primer dígito un
   prefijo indicativo del formato octal ("'0o'")

2. La forma alternativa hace que se inserte antes del primer dígito
   uno de los dos prefijos indicativos del formato hexadecimal "'0x'"
   o "'0X'" (que se use uno u otro depende de que indicador de formato
   se haya usado, "'x'" o "'X'").

3. La forma alternativa hace que se incluya siempre el símbolo del
   punto o coma decimal, incluso si no hubiera dígitos después.

   La precisión determina el número de dígitos que vienen después del
   punto decimal, y por defecto es 6.

4. La forma alternativa hace que se incluya siempre el símbolo del
   punto o coma decimal, y los ceros a su derecha no se eliminan, como
   seria el caso en la forma normal.

   La precisión determina el número de dígitos significativos que
   vienen antes y después del punto decimal, y por defecto es 6.

5. Si la precisión es "N", la salida se trunca a "N" caracteres.

6. Véase **PEP 237**.

Como en Python las cadenas de caracteres tiene una longitud explícita,
la conversión de "%s" no requiere que la cadena termine con "'\0'".

Distinto en la versión 3.1: Las conversiones "%f" para números con
valores absolutos mayores que 1e50 ya no son reemplazadas por
conversiones "%g".

## Tipos de secuencias binarias --- "bytes", "bytearray" y "memoryview"

Los tipos básicos para trabajar con datos binarios son las clases
"bytes" y "bytearray". Ambas pueden ser usadas por la clase
"memoryview", que usa el protocolo buffer para acceder a la memoria de
otros objetos binarios sin necesidad de hacer una copia.

El módulo "array" soporta un almacenamiento eficiente de tipos de
datos básicos como enteros de 32 bits o números en formato de doble
precisión en coma flotante IEEE754.

### Objetos de tipo Bytes

Los objetos *bytes* son secuencias inmutables de bytes. Como muchos de
los protocolos binarios más usados se basan en la codificación ASCII
para texto, los objetos *bytes* ofrecen varios métodos que solo son
válidos cuando se trabaja con datos compatibles ASCII y son, en varios
aspectos, muy cercanos a los cadenas de caracteres.

class bytes(source=b'')
class bytes(source, encoding, errors='strict')

   Para empezar, la sintaxis de los valores literales de *bytes* son
   prácticamente iguales que para las cadenas de caracteres, con la
   diferencia de que se añade el carácter "b" como prefijo:

   * Comillas sencillas: "b'Se siguen aceptando comillas "dobles"
     embebidas'"

   * Comillas dobles: "b"Se siguen aceptando comillas 'simples'
     embebidas""

   * Comillas triples: "b'''3 comillas simples'''", "b"""3 comillas
     dobles""""

   Solo se admiten caracteres ASCII en representaciones literales de
   *bytes* (con independencia del tipo de codificación declarado).
   Cualquier valor por encima de 127 debe ser definido usando su
   secuencia de escape.

   Al igual que con las cadenas, los literales de *bytes* pueden usar
   el prefijo "r" para deshabilitar el procesado de las secuencias de
   escape. Véase Literales de cadenas y bytes para más información
   acerca de los diferentes formas de expresar *bytes* de forma
   literal, incluyendo el soporte de secuencias de escape.

   Aunque las secuencias de bytes y sus representaciones se basen en
   texto ASCII, los objetos *bytes* se comportan más como secuencias
   inmutables de números enteros, donde cada elemento de la secuencia
   está restringido a los valores de *x* tal que "0 <= x < 256" (si se
   intenta violar esta restricción se lanzará una excepción de tipo
   "ValueError"). Esto se ha hecho de forma intencionada para
   enfatizar que, aunque muchos formatos binarios incluyen elementos
   basados en caracteres ASCII y pueden ser manipulados mediante
   algunas técnicas de procesado de textos, este no es el caso general
   para los datos binarios (aplicar algoritmos pensados para proceso
   de textos a datos binarios que no se compatibles con ASCII
   normalmente corromperán dichos datos).

   Además de con literales, se pueden crear objetos de tipo *byte* de
   las siguientes maneras:

   * Un secuencia de una longitud especificada rellena con ceros:
     "bytes(10)"

   * A partir de un iterable de números enteros: "bytes(range(20))"

   * Copiando datos binarios ya existentes mediante el protocolo
     *buffer*: "bytes(obj)"

   Véase además la función incorporada bytes.

   Como dos dígitos hexadecimales se corresponden exactamente con un
   byte, suelen usase números hexadecimales para describir datos
   binarios. Por ello, los objetos de tipo *byte* disponen de un
   método adicional para leer datos en ese formato:

   classmethod fromhex(string, /)

      Este método de clase de "bytes" retorna un objeto binario,
      decodificado a partir de la cadena suministrada como parámetro.
      La cadena de caracteres debe consistir en dos dígitos
      hexadecimales por cada byte, ignorándose los caracteres ASCII de
      espacio en blanco, si los hubiera.

      >>> bytes.fromhex('2Ef0 F1f2  ')
      b'.\xf0\xf1\xf2'

      Distinto en la versión 3.7: El método "bytes.fromhex()" ignora
      ahora todos los caracteres ASCII de espacio en blanco, no solo
      el carácter espacio.

      Distinto en la versión 3.14: "bytes.fromhex()" now accepts ASCII
      "bytes" and *bytes-like objects* as input.

   Existe una función que realiza la operación inversa, es decir,
   transforma un objeto binario en una representación textual usando
   hexadecimal.

   hex(*, bytes_per_sep=1)
   hex(sep, bytes_per_sep=1)

      Retorna una cadena de caracteres que contiene dos dígitos
      hexadecimales por cada byte de la instancia.

      >>> b'\xf0\xf1\xf2'.hex()
      'f0f1f2'

      Si quieres que la cadena en hexadecimal sea más fácil de leer,
      se puede especificar un único carácter separador con el
      parámetro *sep* para que se añada a la salida. Por defecto, este
      separador se incluirá entre cada byte. Un segundo parámetro
      opcional, *bytes_per_sep*, controla los espacios. Valores
      positivos calculan la posición del separador desde la derecha,
      los negativos lo hacen desde la izquierda.

      >>> value = b'\xf0\xf1\xf2'
      >>> value.hex('-')
      'f0-f1-f2'
      >>> value.hex('_', 2)
      'f0_f1f2'
      >>> b'UUDDLRLRAB'.hex(' ', -4)
      '55554444 4c524c52 4142'

      Added in version 3.5.

      Distinto en la versión 3.8: El método "bytes.hex()" ahora
      soporta los parámetros opcionales *sep* y *bytes_per_sep*, que
      permiten insertar separadores entre los bytes de la cadena de
      salida.

Como los objetos de tipo *bytes* son secuencias de números enteros
(similares a tuplas), para un objeto binario *b*, "b[0]" retorna un
entero, mientras que "b[0:1]" retorna un objeto de tipo *bytes* de
longitud 1. (Mientras que las cadenas de caracteres siempre retornan
una cadena de longitud 1, ya sea accediendo por índice o mediante una
operación de segmentado).

La representación de los objetos tipo *bytes* usa el formato literal
("b'...'") ya que es, por lo general, más útil que, digamos,
"bytes([46, 46, 46])". Siempre se puede convertir un objeto binario en
una lista de enteros usando "list(b)".

### Objetos de tipo *Bytearray*

Los objetos de tipo "bytearray" son versiones mutables de los objetos
de tipo "bytes".

class bytearray(source=b'')
class bytearray(source, encoding, errors='strict')

   No existe una sintaxis específica para crear objetos de tipo
   *bytearray*, hay que crearlos siempre llamando a su constructor:

   * Creando una secuencia vacía: "bytearray()"

   * Creando una instancia de una longitud determinada, rellena con
     ceros: "bytearray(10)"

   * A partir de un iterable de números enteros:
     "bytearray(range(20))"

   * Copiando datos binarios ya existentes mediante el protocolo
     *buffer*: "bytearray(b'Hi!')"

   Como los objetos *bytearray* son mutables, soportan todas las
   operaciones aplicables a tipos mutables, además de las operaciones
   propias de los *bytearrays* descritas en Operaciones de bytes y
   bytearray.

   Véase también la función incorporada bytearray.

   Como dos dígitos hexadecimales se corresponden exactamente con un
   byte, suelen usase números hexadecimales para describir datos
   binarios. Por ello, los objetos de tipo *bytearray* disponen de un
   método de clase adicional para leer datos en ese formato:

   classmethod fromhex(string, /)

      Este método de clase de "bytearray" retorna un objeto
      *bytearray*, decodificado a partir de la cadena suministrada
      como parámetro. La cadena de caracteres debe consistir en dos
      dígitos hexadecimales por cada byte, ignorándose los caracteres
      ASCII de espacio en blanco, si los hubiera.

      >>> bytearray.fromhex('2Ef0 F1f2  ')
      bytearray(b'.\xf0\xf1\xf2')

      Distinto en la versión 3.7: El método "bytearray.fromhex()"
      ignora ahora todos los caracteres ASCII de espacio en blanco, no
      solo el carácter espacio.

      Distinto en la versión 3.14: "bytearray.fromhex()" now accepts
      ASCII "bytes" and *bytes-like objects* as input.

   Existe una función que realiza la operación inversa, es decir,
   transforma un objeto *bytearray* en una representación textual
   usando hexadecimal.

   hex(*, bytes_per_sep=1)
   hex(sep, bytes_per_sep=1)

      Retorna una cadena de caracteres que contiene dos dígitos
      hexadecimales por cada byte de la instancia.

      >>> bytearray(b'\xf0\xf1\xf2').hex()
      'f0f1f2'

      Added in version 3.5.

      Distinto en la versión 3.8: De forma similar a "bytes.hex()",
      "bytearray.hex()" soporta ahora los parámetros opcionales *sep*
      y *bytes_per_sep* para insertar separadores entre los bytes en
      la cadena hexadecimal de salida.

   resize(size, /)

      Resize the "bytearray" to contain *size* bytes. *size* must be
      greater than or equal to 0.

      If the "bytearray" needs to shrink, bytes beyond *size* are
      truncated.

      If the "bytearray" needs to grow, all new bytes, those beyond
      *size*, will be set to null bytes.

      This is equivalent to:

      >>> def resize(ba, size):
      ...     if len(ba) > size:
      ...         del ba[size:]
      ...     else:
      ...         ba += b'\0' * (size - len(ba))

      Examples:

      >>> shrink = bytearray(b'abc')
      >>> shrink.resize(1)
      >>> (shrink, len(shrink))
      (bytearray(b'a'), 1)
      >>> grow = bytearray(b'abc')
      >>> grow.resize(5)
      >>> (grow, len(grow))
      (bytearray(b'abc\x00\x00'), 5)

      Added in version 3.14.

Como los objetos de tipo *bytearray* son secuencias de números enteros
(similares a listas), para un objeto *bytearray* *b*, "b[0]" retorna
un entero, mientras que "b[0:1]" retorna un objeto de tipo *bytearray*
de longitud 1. (Mientras que las cadenas de caracteres siempre
retornan una cadena de longitud 1, ya sea accediendo por índice o
mediante una operación de segmentado).

La representación de los objetos tipo *bytearray* usa el formato
literal ("bytearray(b'...')") ya que es, por lo general, más útil que,
digamos, "bytearray([46, 46, 46])". Siempre se puede convertir un
objeto *bytearray* en una lista de enteros usando "list(b)".

Ver también:

  For detailed information on thread-safety guarantees for "bytearray"
  objects, see Thread safety for bytearray objects.

### Operaciones de *bytes* y *bytearray*

Ambos tipos, *bytes* y *bytearray* soportan las operaciones comunes de
las secuencias. Los operadores no funcionan solo con operandos del
mismo tipo, sino con cualquier *objeto tipo binario*. Gracias a esta
flexibilidad, estos tipos pueden combinarse libremente en expresiones
sin que se produzcan errores. Sin embargo, el tipo del valor
resultante puede depender del orden de los operandos.

Nota:

  Los métodos de objetos de tipo *bytes* y *bytesarray* no aceptan
  cadenas de caracteres como parámetros, de la misma manera que los
  métodos de las cadenas tampoco aceptan *bytes* como parámetros. Por
  ejemplo, debes escribir:

     a = "abc"
     b = a.replace("a", "f")

  y:

     a = b"abc"
     b = a.replace(b"a", b"f")

Algunas operaciones de *bytes* y *bytearrays* asumen el uso de
formatos binarios compatibles ASCII, y por tanto deben ser evitadas
cuando trabajamos con datos binarios arbitrarios. Estas restricciones
se explican a continuación.

Nota:

  Usar estas operaciones basadas en ASCII para manipular datos
  binarios que no se almacenan en un formato basado en ASCII pueden
  producir corrupción de datos.

Los siguientes métodos de *bytes* y *bytearrays* pueden ser usados con
datos en formatos binarios arbitrarios.

bytes.count(sub[, start[, end]])
bytearray.count(sub[, start[, end]])

   Retorna el número de secuencias no solapadas de la subsecuencia
   *sub* en el rango [*start*, *end*]. Los parámetros opcionales
   *start* y *end* se interpretan como en las operaciones de
   segmentado.

   La subsecuencia a buscar puede ser cualquier *objeto tipo binario*
   o un número entero entre 0 y 255.

   Si *sub* está vacío, devuelve el número de porciones vacías entre
   caracteres, que es la longitud del objeto de bytes más uno.

   Distinto en la versión 3.3: También acepta como subsecuencia un
   número entero entre 0 y 255.

bytes.removeprefix(prefix, /)
bytearray.removeprefix(prefix, /)

   Si los datos binarios comienzan con la cadena *prefix*, retorna
   "bytes[len(prefix):]". De otra manera, retorna una copia de los
   datos binarios originales:

      >>> b'TestHook'.removeprefix(b'Test')
      b'Hook'
      >>> b'BaseTestCase'.removeprefix(b'Test')
      b'BaseTestCase'

   El argumento *prefix* puede ser cualquier *objeto tipo binario*.

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

   Added in version 3.9.

bytes.removesuffix(suffix, /)
bytearray.removesuffix(suffix, /)

   Si los datos binarios terminan con la cadena expresada en *suffix*
   y el argumento *suffix* no está vacío, retorna
   "bytes[:-len(suffix)]". De otra manera, retorna una copia de los
   datos binarios originales:

      >>> b'MiscTests'.removesuffix(b'Tests')
      b'Misc'
      >>> b'TmpDirMixin'.removesuffix(b'Tests')
      b'TmpDirMixin'

   El argumento *suffix* puede ser cualquier *objeto tipo binario*.

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

   Added in version 3.9.

bytes.decode(encoding='utf-8', errors='strict')
bytearray.decode(encoding='utf-8', errors='strict')

   Devuelve los bytes decodificados a un "str".

   El valor predeterminado de *encoding* es "'utf-8'"; consulte
   Codificaciones estándar para conocer los valores posibles.

   *errors* controla cómo se manejan los errores de decodificación. Si
   se usa "'strict'" (el valor predeterminado), se genera una
   excepción "UnicodeError". Otros valores posibles son "'ignore'",
   "'replace'" y cualquier otro nombre registrado mediante
   "codecs.register_error()". Consulte Manejadores de errores para
   obtener más detalles.

   Por razones de rendimiento, no se verifica la validez del valor de
   *errors* a menos que realmente se produzca un error de
   decodificación, se habilite Modo de desarrollo de Python o se
   utilice debug build.

   Nota:

     Pasar el argumento *encoding* a "str" permite decodificar
     cualquier *bytes-like object* directamente, sin necesidad de
     crear un objeto temporal "bytes" o "bytearray".

   Distinto en la versión 3.1: Añadido soporte para poder usar
   parámetros por nombre.

   Distinto en la versión 3.9: El valor del argumento *errors* ahora
   se comprueba en Modo de desarrollo de Python y en debug mode.

bytes.endswith(suffix[, start[, end]])
bytearray.endswith(suffix[, start[, end]])

   Retorna "True" si los datos binarios acaban con el valor indicado
   por *suffix*, en caso contrario retorna "False". El valor de
   *suffix* puede ser también una tupla de sufijos para buscar. Con el
   parámetro opcional *start*, la comparación empieza a partir de esa
   posición. Si se especifica el parámetro opcional *end*, la
   comparación termina en esa posición.

   El sufijo (o sufijos) a buscar puede ser cualquier *objeto tipo
   binario*.

bytes.find(sub[, start[, end]])
bytearray.find(sub[, start[, end]])

   Retorna el mínimo índice dentro de los datos donde se ha encontrado
   la subsecuencia *sub*, de forma que *sub* está contenida en el
   segmento "s[start:end]". Los parámetros opcionales *start* y *end*
   se interpretan como en las operaciones de segmentado. Retorna "-1"
   si no se puede encontrar *sub*.

   La subsecuencia a buscar puede ser cualquier *objeto tipo binario*
   o un número entero entre 0 y 255.

   Nota:

     El método "find()" se debe usar solo si se necesita saber la
     posición de *sub*. Si solo se necesita comprobar si *sub* es una
     parte de *s*, es mejor usar el operador "in":

        >>> b'Py' in b'Python'
        True

   Distinto en la versión 3.3: También acepta como subsecuencia un
   número entero entre 0 y 255.

bytes.index(sub[, start[, end]])
bytearray.index(sub[, start[, end]])

   Como "find()", pero lanza una excepción de tipo "ValueError" si no
   se encuentra la subsecuencia a buscar.

   La subsecuencia a buscar puede ser cualquier *objeto tipo binario*
   o un número entero entre 0 y 255.

   Distinto en la versión 3.3: También acepta como subsecuencia un
   número entero entre 0 y 255.

bytes.join(iterable, /)
bytearray.join(iterable, /)

   Retorna un objeto de tipo *bytes* o *bytearray* que es la
   concatenación de las secuencias binarias en *iterable*. Si alguno
   de los objetos de la secuencia no es un *objeto tipo binario* se
   lanza la excepción "TypeError", incluso si son cadenas de
   caracteres (objetos "str"). El separador entre los distintos
   elementos es el contenido del objeto *bytes* o *bytearray* usando
   para invocar el método.

static bytes.maketrans(from, to, /)
static bytearray.maketrans(from, to, /)

   Este método estático retorna una tabla de traducción apta para ser
   usada por el método "bytes.translate()", que mapea cada carácter en
   *from* en la misma posición en *to*; tanto *from* como *to* deben
   ser *objetos tipo binario* y deben tener la misma longitud.

   Added in version 3.1.

bytes.partition(sep, /)
bytearray.partition(sep, /)

   Divide la secuencia en la primera ocurrencia de *sep*, y retorna
   una tupla de tres elementos que contiene la parte antes del
   separador, el separador en sí o una copia de tipo *bytearray* y la
   parte después del separador. Si no se encuentra el separador,
   retorna una tupla de tres elementos, con la primera posición
   ocupada por la secuencia original, y las dos posiciones siguientes
   rellenas con objetos *bytes* o *bytearray* vacíos.

   El separador a buscar puede ser cualquier *objeto tipo binario*.

bytes.replace(old, new, count=-1, /)
bytearray.replace(old, new, count=-1, /)

   Retorna una copia de la secuencia con todas las ocurrencias de
   *old* sustituidas por *new*. Si se utiliza el parámetro *count*,
   solo se cambian las primeras *count* ocurrencias.

   La subsecuencia a buscar y su reemplazo puede ser cualquier *objeto
   tipo binario*.

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.rfind(sub[, start[, end]])
bytearray.rfind(sub[, start[, end]])

   Retorna el mayor índice dentro de la secuencia *s* donde se puede
   encontrar *sub*, estando *sub* incluida en "s[start:end]". Los
   parámetros opcionales *start* y *end* se interpretan igual que en
   las operaciones de segmentado. Retorna "-1" si no se encuentra
   *sub*.

   La subsecuencia a buscar puede ser cualquier *objeto tipo binario*
   o un número entero entre 0 y 255.

   Distinto en la versión 3.3: También acepta como subsecuencia un
   número entero entre 0 y 255.

bytes.rindex(sub[, start[, end]])
bytearray.rindex(sub[, start[, end]])

   Como el método "rfind()", pero lanza la excepción "ValueError" si
   no se encuentra *sub*.

   La subsecuencia a buscar puede ser cualquier *objeto tipo binario*
   o un número entero entre 0 y 255.

   Distinto en la versión 3.3: También acepta como subsecuencia un
   número entero entre 0 y 255.

bytes.rpartition(sep, /)
bytearray.rpartition(sep, /)

   Divide la secuencia en la primera ocurrencia de *sep*, y retorna
   una tupla de tres elementos que contiene la parte antes del
   separador, el separador en sí o una copia de tipo *bytearray* y la
   parte después del separador. Si no se encuentra el separador,
   retorna una tupla de tres elementos, con las dos primeras
   posiciones rellenas con objetos *bytes* o *bytearray* vacíos, y la
   tercera posición ocupada por la secuencia original.

   El separador a buscar puede ser cualquier *objeto tipo binario*.

bytes.startswith(prefix[, start[, end]])
bytearray.startswith(prefix[, start[, end]])

   Retorna "True" si los datos binarios empiezan con el valor indicado
   por *prefix*, en caso contrario retorna "False". El valor de
   *prefix* puede ser también una tupla de prefijos para buscar. Con
   el parámetro opcional *start*, la comparación empieza a partir de
   esa posición. Si se especifica el parámetro opcional *end*, la
   comparación termina en esa posición.

   El prefijo (o prefijos) a buscar puede ser cualquier *objeto tipo
   binario*.

bytes.translate(table, /, delete=b'')
bytearray.translate(table, /, delete=b'')

   Retorna una copia del objeto *bytes* o *bytearray* donde todas las
   ocurrencias de bytes especificados en el parámetro *delete* han
   sido borrados, y el resto han sido mapeados a través de la tabla de
   traducción indicada, que debe ser un objeto de tipo *bytes* con una
   longitud de 256 elementos.

   Puedes usar el método "bytes.maketrans()" para crear la tabla de
   traducción.

   Se puede ajustar el parámetro *table* a "None" para conseguir una
   traducción que solo borra caracteres:

      >>> b'read this short text'.translate(None, b'aeiou')
      b'rd ths shrt txt'

   Distinto en la versión 3.6: El parámetro *delete* se puede ahora
   especificar por nombre.

Los siguientes métodos de los objetos *bytes* y *bytearray* presentan
un comportamiento por defecto que asume el uso de formatos binarios
compatibles con ASCII, pero aun así pueden ser usados con datos
binarios arbitrarios usando los parámetros apropiados. Nótese que
todos los métodos de *bytearray* en esta sección nunca operan in situ,
sino que siempre retornan objetos nuevos.

bytes.center(width, fillbyte=b' ', /)
bytearray.center(width, fillbyte=b' ', /)

   Retorna una copia del objeto centrado en una secuencia de longitud
   *width*. El relleno se realiza usando el valor definido en el
   parámetro *fillbyte* (por defecto, el carácter espacio en ASCII).
   Para los objetos de tipo "bytes", se retorna la secuencia original
   intacta si *width* es menor o igual que "len(s)".

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.ljust(width, fillbyte=b' ', /)
bytearray.ljust(width, fillbyte=b' ', /)

   Retorna una copia del objeto justificado por la izquierda en una
   secuencia de longitud *width*. El relleno se realiza usando el
   valor definido en el parámetro *fillbyte* (por defecto, el carácter
   espacio en ASCII). Para los objetos de tipo "bytes", se retorna la
   secuencia original intacta si *width* es menor o igual que
   "len(s)".

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.lstrip(bytes=None, /)
bytearray.lstrip(bytes=None, /)

   Return a copy of the sequence with specified leading bytes removed.
   The *bytes* argument is a binary sequence specifying the set of
   byte values to be removed.  If omitted or "None", the *bytes*
   argument defaults to removing ASCII whitespace.  The *bytes*
   argument is not a prefix; rather, all combinations of its values
   are stripped:

      >>> b'   spacious   '.lstrip()
      b'spacious   '
      >>> b'www.example.com'.lstrip(b'cmowz.')
      b'example.com'

   La secuencia binaria que especifica el conjunto bytes a ser
   eliminados puede ser cualquier *objeto de tipo binario*. Véase
   "removeprefix()" para un método que removerá una única cadena de
   prefijo en lugar de todas las ocurrencias dentro de un set de
   caracteres. Por ejemplo:

      >>> b'Arthur: three!'.lstrip(b'Arthur: ')
      b'ee!'
      >>> b'Arthur: three!'.removeprefix(b'Arthur: ')
      b'three!'

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.rjust(width, fillbyte=b' ', /)
bytearray.rjust(width, fillbyte=b' ', /)

   Retorna una copia del objeto justificado por la derecha en una
   secuencia de longitud *width*. El relleno se realiza usando el
   valor definido en el parámetro *fillbyte* (por defecto, el carácter
   espacio en ASCII). Para los objetos de tipo "bytes", se retorna la
   secuencia original intacta si *width* es menor o igual que
   "len(s)".

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.rsplit(sep=None, maxsplit=-1)
bytearray.rsplit(sep=None, maxsplit=-1)

   Divide una secuencia binaria en subsecuencias del mismo tipo,
   usando como separador el valor de *sep*. Si se utiliza el parámetro
   *maxsplit*, se realizan como máximo *maxsplit* divisiones,
   retornando los que están más a la derecha. Si no se especifica
   *sep* o se pasa con valor "None", se usa como separador el carácter
   espacio en ASCII. Si no contamos la diferencia de empezar las
   divisiones desde la derecha, el comportamiento de este método
   "rsplit()" es equivalente al de "split()", que se describe con
   detalle más adelante.

bytes.rstrip(bytes=None, /)
bytearray.rstrip(bytes=None, /)

   Return a copy of the sequence with specified trailing bytes
   removed.  The *bytes* argument is a binary sequence specifying the
   set of byte values to be removed.  If omitted or "None", the
   *bytes* argument defaults to removing ASCII whitespace.  The
   *bytes* argument is not a suffix; rather, all combinations of its
   values are stripped:

      >>> b'   spacious   '.rstrip()
      b'   spacious'
      >>> b'mississippi'.rstrip(b'ipz')
      b'mississ'

   La secuencia binaria que especifica el conjunto bytes a ser
   eliminados puede ser cualquier *objeto de tipo binario*. Véase
   "removesuffix()" para un método que removerá una única cadena de
   sufijo en lugar de todas las ocurrencias dentro de un set de
   caracteres. Por ejemplo:

      >>> b'Monty Python'.rstrip(b' Python')
      b'M'
      >>> b'Monty Python'.removesuffix(b' Python')
      b'Monty'

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.split(sep=None, maxsplit=-1)
bytearray.split(sep=None, maxsplit=-1)

   Divide una secuencia binaria en subsecuencias del mismo tipo,
   usando como separador el valor de *sep*. Si se utiliza el parámetro
   *maxsplit* y es un número positivo, se realizan como máximo
   *maxsplit* divisiones (resultando en una secuencia de como mucho
   "maxsplit+1" elementos). Si no se especifica *maxsplit* o se pasa
   "'-1", no hay límite al número de divisiones (se hacen todas las
   posibles divisiones).

   Si se proporciona *sep*, los delimitadores consecutivos no se
   agrupan y se consideran que delimitan subsecuencias vacías (por
   ejemplo, "b'1,,2'.split(b',')" devuelve "[b'1', b'', b'2']"). El
   argumento *sep* puede consistir en una secuencia multibyte como un
   único delimitador. Dividir una secuencia vacía con un separador
   especificado devuelve "[b'']" o "[bytearray(b'')]" según el tipo de
   objeto que se esté dividiendo. El argumento *sep* puede ser
   cualquier *bytes-like object*.

   Por ejemplo:

      >>> b'1,2,3'.split(b',')
      [b'1', b'2', b'3']
      >>> b'1,2,3'.split(b',', maxsplit=1)
      [b'1', b'2,3']
      >>> b'1,2,,3,'.split(b',')
      [b'1', b'2', b'', b'3', b'']
      >>> b'1<>2<>3<4'.split(b'<>')
      [b'1', b'2', b'3<4']

   Si no se especifica *sep* o es "None", se usa un algoritmo de
   división diferente: secuencias consecutivas de caracteres de
   espacio en ASCII se consideran como un único separador, y el
   resultado no contendrá cadenas vacías ni al principio ni al final
   de la lista, aunque la cadena original tuviera espacios en blanco
   al principio o al final. En consecuencia, dividir una secuencia
   vacía o que solo contenga espacios en blanco usando "None" como
   separador siempre retornará una lista vacía "[]".

   Por ejemplo:

      >>> b'1 2 3'.split()
      [b'1', b'2', b'3']
      >>> b'1 2 3'.split(maxsplit=1)
      [b'1', b'2 3']
      >>> b'   1   2   3   '.split()
      [b'1', b'2', b'3']

bytes.strip(bytes=None, /)
bytearray.strip(bytes=None, /)

   Return a copy of the sequence with specified leading and trailing
   bytes removed. The *bytes* argument is a binary sequence specifying
   the set of byte values to be removed.  If omitted or "None", the
   *bytes* argument defaults to removing ASCII whitespace. The *bytes*
   argument is not a prefix or suffix; rather, all combinations of its
   values are stripped:

      >>> b'   spacious   '.strip()
      b'spacious'
      >>> b'www.example.com'.strip(b'cmowz.')
      b'example'

   La secuencia binaria de bytes a eliminar debe ser un *objeto tipo
   binario*.

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

Los siguientes métodos de los objetos *bytes* y *bytearray* asumen el
uso de formatos binarios compatibles con ASCII, y no deben ser usados
con datos binarios arbitrarios. Nótese que todos los métodos de
*bytearray* en esta sección nunca operan in situ, sino que siempre
retornan objetos nuevos.

bytes.capitalize()
bytearray.capitalize()

   Retorna una copia de la secuencia con cada byte interpretado como
   un carácter ASCII, y el primer byte en mayúsculas y el resto en
   minúsculas. Los valores que no sean ASCII no se ven modificados.

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.expandtabs(tabsize=8)
bytearray.expandtabs(tabsize=8)

   Retorna una copia de la secuencia, con todos los caracteres ASCII
   *tab* reemplazados por uno o más espacios ASCII, dependiendo de la
   columna actual y del tamaño definido para el tabulador. Las
   posiciones de tabulación ocurren cada *tabsize* caracteres (siendo
   el valor por defecto de *tabsize* 8, lo que produce las posiciones
   de tabulación 0, 8, 16,...). Para expandir la secuencia, la columna
   actual se pone a cero y se va examinando byte a byte. Si se
   encuentra un tabulador, ("b'\t'"), se insertan uno o más espacios
   hasta que sea igual a la siguiente posición de tabulación. (El
   carácter tabulador en sí es descartado). Si el byte es un indicador
   de salto de línea ("b'\n'") o de retorno ("b'\r'"), se copia y el
   valor de columna actual se vuelve a poner a cero. Cualquier otro
   carácter es copiado sin cambios y hace que el contador de columna
   se incremente en 1, sin tener en cuenta como se representa impreso
   el byte:

      >>> b'01\t012\t0123\t01234'.expandtabs()
      b'01      012     0123    01234'
      >>> b'01\t012\t0123\t01234'.expandtabs(4)
      b'01  012 0123    01234'

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.isalnum()
bytearray.isalnum()

   Retorna "True" si todos los bytes de la secuencia son caracteres
   alfabéticos ASCII o caracteres decimales ASCII y la secuencia no
   está vacía, en cualquier otro caso retorna "False". Los caracteres
   alfabéticos ASCII son los bytes incluidos en la secuencia
   "b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'". Los
   caracteres decimales ASCII son los bytes incluidos en la secuencia
   "b'0123456789'".

   Por ejemplo:

      >>> b'ABCabc1'.isalnum()
      True
      >>> b'ABC abc1'.isalnum()
      False

bytes.isalpha()
bytearray.isalpha()

   Retorna "True" si todos los bytes de la secuencia son caracteres
   alfabéticos ASCII y la secuencia no está vacía, en cualquier otro
   caso retorna "False". Los caracteres alfabéticos ASCII son los
   bytes incluidos en la secuencia
   "b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'".

   Por ejemplo:

      >>> b'ABCabc'.isalpha()
      True
      >>> b'ABCabc1'.isalpha()
      False

bytes.isascii()
bytearray.isascii()

   Retorna "True" si la secuencia está vacía o si todos los bytes de
   la secuencia son caracteres ASCII, en cualquier otro caso retorna
   "False". Los caracteres ASCII son los bytes incluidos en el rango
   0-0x7F.

   Added in version 3.7.

bytes.isdigit()
bytearray.isdigit()

   Retorna "True" si todos los bytes de la secuencia son caracteres
   decimales ASCII y la secuencia no está vacía, en cualquier otro
   caso retorna "False". Los caracteres decimales ASCII son los bytes
   incluidos en la secuencia "b'0123456789'".

   Por ejemplo:

      >>> b'1234'.isdigit()
      True
      >>> b'1.23'.isdigit()
      False

bytes.islower()
bytearray.islower()

   Retorna "True" si hay al menos un carácter ASCII en minúsculas, y
   no hay ningún carácter ASCII en mayúsculas, en cualquier otro caso
   retorna "False".

   Por ejemplo:

      >>> b'hello world'.islower()
      True
      >>> b'Hello world'.islower()
      False

   Los caracteres ASCII en minúsculas son los bytes incluidos en la
   secuencia "b'abcdefghijklmnopqrstuvwxyz'". Los caracteres ASCII en
   mayúsculas son los bytes en la secuencia
   "b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'".

bytes.isspace()
bytearray.isspace()

   Retorna "True" si todos los bytes de la secuencia son caracteres
   ASCII de espacio en blanco y la secuencia no está vacía, en
   cualquier otro caso retorna "False". Los caracteres de espacio en
   blanco ASCII son los bytes incluidos en la secuencia "b'
   \t\n\r\x0b\f'" (espacio, tabulador, nueva línea, retorno de carro,
   tabulador vertical y avance de página).

bytes.istitle()
bytearray.istitle()

   Retorna "True" si la secuencia ASCII está en forma de título, y la
   secuencia no está vacía, en cualquier otro caso retorna "False".
   Véase el método "bytes.title()" para más detalles en la definición
   de "En forma de título".

   Por ejemplo:

      >>> b'Hello World'.istitle()
      True
      >>> b'Hello world'.istitle()
      False

bytes.isupper()
bytearray.isupper()

   Retorna "True" si hay al menos un carácter ASCII en mayúsculas, y
   no hay ningún carácter ASCII en minúsculas, en cualquier otro caso
   retorna "False".

   Por ejemplo:

      >>> b'HELLO WORLD'.isupper()
      True
      >>> b'Hello world'.isupper()
      False

   Los caracteres ASCII en minúsculas son los bytes incluidos en la
   secuencia "b'abcdefghijklmnopqrstuvwxyz'". Los caracteres ASCII en
   mayúsculas son los bytes en la secuencia
   "b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'".

bytes.lower()
bytearray.lower()

   Retorna una copia de la secuencia con todos los caracteres ASCII en
   mayúsculas sustituidos por su versión correspondiente en
   minúsculas.

   Por ejemplo:

      >>> b'Hello World'.lower()
      b'hello world'

   Los caracteres ASCII en minúsculas son los bytes incluidos en la
   secuencia "b'abcdefghijklmnopqrstuvwxyz'". Los caracteres ASCII en
   mayúsculas son los bytes en la secuencia
   "b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'".

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.splitlines(keepends=False)
bytearray.splitlines(keepends=False)

   Retorna una lista de las líneas en la secuencia binaria, usando
   como separadores los *saltos de líneas universales*. Los caracteres
   usados como separadores no se incluyen en la lista de resultados a
   no ser que se pase el parámetro *keepends* a "True".

   Por ejemplo:

      >>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
      [b'ab c', b'', b'de fg', b'kl']
      >>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
      [b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']

   Al contrario que el método "split()", cuando se especifica una
   cadena delimitadora con el parámetro *sep*, este método retorna una
   lista vacía para la cadena vacía, y un carácter de salto de línea
   al final de la secuencia no resulta en una línea extra:

      >>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
      ([b''], [b'Two lines', b''])
      >>> b"".splitlines(), b"One line\n".splitlines()
      ([], [b'One line'])

bytes.swapcase()
bytearray.swapcase()

   Retorna una copia de la secuencia con todos los caracteres ASCII en
   minúsculas sustituidos por su versión correspondiente en
   mayúsculas, y viceversa.

   Por ejemplo:

      >>> b'Hello World'.swapcase()
      b'hELLO wORLD'

   Los caracteres ASCII en minúsculas son los bytes incluidos en la
   secuencia "b'abcdefghijklmnopqrstuvwxyz'". Los caracteres ASCII en
   mayúsculas son los bytes en la secuencia
   "b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'".

   A diferencia de "str.swapcase()", siempre ocurre lo mismo con
   "bin.swapcase().swapcase() == bin" para las versiones binarias. Las
   conversiones de mayúsculas y minúsculas son simétricas en ASCII,
   aunque esto no suele ser así para puntos de código Unicode
   arbitrarios.

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.title()
bytearray.title()

   Retorna una versión en forma de título de la secuencia binaria, con
   la primera letra de cada palabra en mayúsculas y el resto en
   minúsculas. Los valores de bytes sin mayúsculas y minúsculas se
   dejan sin modificar.

   Por ejemplo:

      >>> b'Hello world'.title()
      b'Hello World'

   Los caracteres ASCII en minúsculas son los bytes incluidos en la
   secuencia "b'abcdefghijklmnopqrstuvwxyz'". Los caracteres ASCII en
   mayúsculas son los bytes en la secuencia
   "b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'". El resto de los caracteres no
   presentan diferencias entre mayúsculas y minúsculas.

   El algoritmo usa una definición sencilla e independiente del
   lenguaje, consistente en considerar una palabra como un grupo de
   letras consecutivas. Esta definición funciona en varios entornos,
   pero implica que, por ejemplo en inglés, los apóstrofos en las
   contracciones y en los posesivos constituyen una separación entre
   palabras, que puede que no sea el efecto deseado:

      >>> b"they're bill's friends from the UK".title()
      b"They'Re Bill'S Friends From The Uk"

   Se puede solucionar parcialmente el problema de los apóstrofos
   usando expresiones regulares:

      >>> import re
      >>> def titlecase(s):
      ...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
      ...                   lambda mo: mo.group(0)[0:1].upper() +
      ...                              mo.group(0)[1:].lower(),
      ...                   s)
      ...
      >>> titlecase(b"they're bill's friends.")
      b"They're Bill's Friends."

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.upper()
bytearray.upper()

   Retorna una copia de la secuencia con todos los caracteres ASCII en
   minúsculas sustituidos por su versión correspondiente en
   mayúsculas.

   Por ejemplo:

      >>> b'Hello World'.upper()
      b'HELLO WORLD'

   Los caracteres ASCII en minúsculas son los bytes incluidos en la
   secuencia "b'abcdefghijklmnopqrstuvwxyz'". Los caracteres ASCII en
   mayúsculas son los bytes en la secuencia
   "b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'".

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

bytes.zfill(width, /)
bytearray.zfill(width, /)

   Retorna una copia de la secuencia rellenada por la izquierda con
   los caracteres ASCII "b'0'" necesarios para conseguir una cadena de
   longitud *width*. El carácter prefijo de signo ("b'+'"/"b'-'") se
   gestiona insertando el relleno *después* del carácter de signo en
   vez de antes. Para objetos "bytes", se retorna la secuencia
   original si *width* es menor o igual que "len(s)".

   Por ejemplo:

      >>> b"42".zfill(5)
      b'00042'
      >>> b"-42".zfill(5)
      b'-0042'

   Nota:

     La versión *bytearray* de este método *no* opera in situ -
     siempre produce un nuevo objeto, aún si no se hubiera realizado
     ningún cambio.

### Usando el formateo tipo "printf" con bytes

Nota:

  Las operaciones de formateo explicadas aquí tienen una serie de
  peculiaridades que conducen a ciertos errores comunes (como fallar
  al representar tuplas y diccionarios correctamente). Si el valor a
  representar es una tupla o un diccionario, hay que envolverlos en
  una tupla.

Los objetos binarios ("bytes"/"bytearray") tienen una operación
incorporada: el operador "%" (módulo). Esta operación se conoce
también como operador de *formateo* o de *interpolación*. Dada la
expresión "formato % valores" (donde *formato* es un objeto binario),
las especificaciones de conversión indicadas en la cadena con el
símbolo "%" son reemplazadas por cero o más elementos de *valores*. El
efecto es similar a usar la función del lenguaje C "sprintf()".

Si *formato* tiene un único marcador, *valores* puede ser un objeto
sencillo, no una tupla. [5] En caso contrario, *valores* debe ser una
tupla con exactamente el mismo número de elementos que marcadores
usados en el objeto binario, o un único objeto de tipo mapa (por
ejemplo, un diccionario).

Un especificador de conversión consiste en dos o más caracteres y
tiene los siguientes componentes, que deben aparecer en el siguiente
orden:

1. El carácter "'%'", que identifica el inicio del marcador.

2. Una clave de mapeo (opcional), consistente en una secuencia de
   caracteres entre paréntesis, como por ejemplo, "(somename)".

3. Indicador de conversión (opcional), que afecta el resultado de
   ciertas conversiones de tipos.

4. Valor de ancho mínimo (opcional). Si se especifica un "'*'"
   (asterisco), el ancho real se lee del siguiente elemento de la
   tupla *valores*, y el objeto a convertir viene después del ancho
   mínimo, con un indicador de precisión opcional.

5. Precisión (opcional), en la forma "'.'" (punto) seguido de la
   precisión. Si se especifica un "'*'" (asterisco), el valor de
   precisión real se lee del siguiente elemento de la tupla *valores*,
   y el valor a convertir viene después de la precisión.

6. Modificador de longitud (opcional).

7. Tipo de conversión.

Cuando el argumento derecho es un diccionario (o cualquier otro objeto
de tipo mapa), los marcadores en el objeto binario *deben* incluir un
valor de clave entre paréntesis, inmediatamente después del carácter
"'%'". El valor de la clave se usa para seleccionar el valor a
formatear desde el mapa. Por ejemplo:

>>> print(b'%(language)s has %(number)03d quote types.' %
...       {b'language': b"Python", b"number": 2})
b'Python has 002 quote types.'

En este caso, no se puede usar el especificador "*" en la cadena de
formato (dado que requiere una lista secuencial de parámetros).

Los indicadores de conversión son:

+-----------+-----------------------------------------------------------------------+
| Flag      | Significado                                                           |
|===========|=======================================================================|
| "'#'"     | El valor a convertir usara la "forma alternativa" (que se definirá    |
## |           | más adelante)                                                         |

| "'0'"     | La conversión rellena con ceros por la izquierda para valores         |
## |           | numéricos.                                                            |

| "'-'"     | El valor convertido se ajusta a la izquierda (sobreescribe la         |
## |           | conversión "'0'" si se especifican los dos)                           |

| "' '"     | (Un espacio) Se debe añadir un espacio en blanco antes de un número   |
## |           | positivo (o una cadena vacía) si se usa una conversión con signo.     |

| "'+'"     | Un carácter signo ("'+'" o "'-'") precede a la conversión             |
## |           | (sobreescribe el indicador de "espacio")                              |

Puede estar presente un modificador de longitud ("h", "l" o "L"), pero
se ignora y no es necesario para Python -- por lo que, por ejemplo, la
salida de "%ld" es idéntica a "%d".

Los tipos de conversión son:

+--------------+-------------------------------------------------------+---------+
| Conversión   | Significado                                           | Notas   |
|==============|=======================================================|=========|
## | "'d'"        | Entero decimal con signo.                             |         |

## | "'i'"        | Entero decimal con signo.                             |         |

## | "'o'"        | Valor octal con signo.                                | (1)     |

## | "'u'"        | Obsoleto -- es idéntico a "'d'".                      | (8)     |

## | "'x'"        | Hexadecimal con signo (en minúsculas).                | (2)     |

## | "'X'"        | Hexadecimal con signo (en mayúsculas).                | (2)     |

## | "'e'"        | Formato en coma flotante exponencial (en minúsculas). | (3)     |

## | "'E'"        | Formato en coma flotante exponencial (en mayúsculas). | (3)     |

## | "'f'"        | Formato en coma flotante decimal.                     | (3)     |

## | "'F'"        | Formato en coma flotante decimal.                     | (3)     |

| "'g'"        | Formato de punto flotante. Utiliza el formato         | (4)     |
|              | exponencial en minúsculas si el exponente es menor    |         |
|              | que -4 o igual que la precisión; en caso contrario,   |         |
## |              | utiliza el formato decimal.                           |         |

| "'G'"        | Formato de punto flotante. Utiliza el formato         | (4)     |
|              | exponencial en mayúsculas si el exponente es menor    |         |
|              | que -4 o igual que la precisión; en caso contrario,   |         |
## |              | utiliza el formato decimal.                           |         |

| "'c'"        | Byte único (acepta números enteros o binarios de un   |         |
## |              | único byte).                                          |         |

| "'b'"        | Bytes (cualquier objeto que siga al buffer protocol o | (5)     |
## |              | tenga "__bytes__()").                                 |         |

| "'s'"        | "'s'" es un alias de "'b'" y solo debe ser usado para | (6)     |
## |              | bases de código Python2/3.                            |         |

| "'a'"        | Bytes (convierte cualquier objeto Python usando       | (5)     |
## |              | "repr(obj).encode('ascii','backslashreplace')").      |         |

| "'r'"        | "'r'" es un alias de "'a'" y solo debe ser usado para | (7)     |
## |              | bases de código Python2/3.                            |         |

| "'%'"        | No se representa ningún argumento, obteniéndose en el |         |
## |              | resultado la cadena "'%'".                            |         |

Notas:

1. La forma alternativa hace que se inserte antes del primer dígito un
   prefijo indicativo del formato octal ("'0o'")

2. La forma alternativa hace que se inserte antes del primer dígito
   uno de los dos prefijos indicativos del formato hexadecimal "'0x'"
   o "'0X'" (que se use uno u otro depende de que indicador de formato
   se haya usado, "'x'" o "'X'").

3. La forma alternativa hace que se incluya siempre el símbolo del
   punto o coma decimal, incluso si no hubiera dígitos después.

   La precisión determina el número de dígitos que vienen después del
   punto decimal, y por defecto es 6.

4. La forma alternativa hace que se incluya siempre el símbolo del
   punto o coma decimal, y los ceros a su derecha no se eliminan, como
   seria el caso en la forma normal.

   La precisión determina el número de dígitos significativos que
   vienen antes y después del punto decimal, y por defecto es 6.

5. Si la precisión es "N", la salida se trunca a "N" caracteres.

6. "b'%s'" está obsoleto, pero no se retirará durante la serie 3.x.

7. "b'%r'" está obsoleto, pero no se retirará durante la serie 3.x.

8. Véase **PEP 237**.

Nota:

  La versión *bytearray* de este método *no* opera in situ - siempre
  produce un nuevo objeto, aún si no se hubiera realizado ningún
  cambio.

Ver también: **PEP 461** - Añadiendo % formatea a bytes y bytearray

Added in version 3.5.

### Vistas de memoria

Los objetos de tipo "memoryview" permiten al código Python acceder a
los datos internos de objetos que soporten el protocolo buffer sin
necesidad de hacer copias.

class memoryview(object)

      Crea un "memoryview" que referencia *object*. La variable
      *object* debe soportar el protocolo buffer. Los objetos
      incorporados que soportan el protocolo buffer incluyen los
      "bytes" y "bytearray".

      La clase "memoryview" usa el concepto de *elemento*, que es la
      unidad de memoria atómica gestionada por el objeto original
      *object*. Para muchos tipos de datos simples como "bytes" y
      "bytearray", un elemento es un único byte, pero otros tipos,
      como la clase "array.array" pueden tener elementos más grandes.

      "memoryview"s are generic over the type of their underlying
      data.

      "len(view)" es igual a la longitud de "tolist", que es la
      representación de lista anidada de la vista. Si es "view.ndim =
      1", es igual a la cantidad de elementos de la vista.

      Distinto en la versión 3.12: Si es "view.ndim == 0", "len(view)"
      ahora genera "TypeError" en lugar de devolver 1.

      El atributo "itemsize" le dará la cantidad de bytes en un solo
      elemento.

      Un objeto de tipo "memoryview" soporta operaciones de segmentado
      y acceso por índices a sus datos. Un segmentado unidimensional
      producirá una sub-vista:

         >>> v = memoryview(b'abcefg')
         >>> v[1]
         98
         >>> v[-1]
         103
         >>> v[1:4]
         <memory at 0x7f3ddc9f4350>
         >>> bytes(v[1:4])
         b'bce'

      Si "format" es uno de los especificadores de formato nativos del
      módulo "struct", el indexado con un número entero o una tupla de
      números enteros también es posible, y retorna un único
      *elemento* con el tipo adecuado. Objetos *memoryview*
      unidimensionales pueden ser indexados con un entero o con una
      tupla de enteros. Los *memoryview* con múltiples dimensiones
      pueden ser indexados con tuplas de exactamente *ndim* enteros,
      donde *ndim* es el número de dimensiones. Vistas *memoryviews*
      con cero dimensiones pueden ser indexados con una tupla vacía.

      Aquí hay un ejemplo con un formato que no es un byte:

         >>> import array
         >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
         >>> m = memoryview(a)
         >>> m[0]
         -11111111
         >>> m[-1]
         44444444
         >>> m[::2].tolist()
         [-11111111, -33333333]

      Si el objeto usado para crear la vista es modificable, la vista
      *memoryview* soporta asignación unidimensional mediante
      segmentos. Sin embargo, no se permite el cambio de tamaño:

         >>> data = bytearray(b'abcefg')
         >>> v = memoryview(data)
         >>> v.readonly
         False
         >>> v[0] = ord(b'z')
         >>> data
         bytearray(b'zbcefg')
         >>> v[1:4] = b'123'
         >>> data
         bytearray(b'z123fg')
         >>> v[2:3] = b'spam'
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         ValueError: memoryview assignment: lvalue and rvalue have different structures
         >>> v[2:6] = b'spam'
         >>> data
         bytearray(b'z1spam')

      Las vistas de memoria unidimensionales de tipos *hashable* (solo
      lectura) con formatos 'B', 'b' o 'c' también se pueden codificar
      en hash. El hash se define como "hash(m) == hash(m.tobytes())":

         >>> v = memoryview(b'abcefg')
         >>> hash(v) == hash(b'abcefg')
         True
         >>> hash(v[2:4]) == hash(b'ce')
         True
         >>> hash(v[::-2]) == hash(b'abcefg'[::-2])
         True

      Distinto en la versión 3.3: Ahora es posible dividir las vistas
      de memoria unidimensionales. Las vistas de memoria
      unidimensionales con formatos 'B', 'b' o 'c' ahora son
      *hashable*.

      Distinto en la versión 3.4: los objetos *memoryview* son
      registrados automáticamente con la clase
      "collections.abc.Sequence"

      Distinto en la versión 3.5: los objetos *memoryviews* se pueden
      ahora acceder usando como índices una tupla de números enteros.

      Distinto en la versión 3.14: memoryview is now a *generic type*.

      La clase "memoryview" tiene varios métodos:

      __eq__(exporter)

         Un objeto *memoryview* y un exportador **PEP 3118** son
         iguales si sus formas son equivalentes y todos los valores
         correspondientes son iguales cuando los formatos respectivos
         de los operandos son interpretados usando la sintaxis de
         "struct".

         Para el subconjunto de formatos de "struct" soportados
         actualmente por "tolist()", "v" y "w" son iguales si
         "v.tolist() == w.tolist()":

            >>> import array
            >>> a = array.array('I', [1, 2, 3, 4, 5])
            >>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
            >>> c = array.array('b', [5, 3, 1])
            >>> x = memoryview(a)
            >>> y = memoryview(b)
            >>> x == a == y == b
            True
            >>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
            True
            >>> z = y[::-2]
            >>> z == c
            True
            >>> z.tolist() == c.tolist()
            True

         Si cualquiera de las cadenas de formato no es soportada por
         el módulo "struct", entonces la comparación de los objetos
         siempre los considerará diferentes (incluso si las cadenas de
         formato y el contenido del *buffer* son idénticos):

            >>> from ctypes import BigEndianStructure, c_long
            >>> class BEPoint(BigEndianStructure):
            ...     _fields_ = [("x", c_long), ("y", c_long)]
            ...
            >>> point = BEPoint(100, 200)
            >>> a = memoryview(point)
            >>> b = memoryview(point)
            >>> a == point
            False
            >>> a == b
            False

         Tenga en cuenta que, al igual que con los números de punto
         flotante, "v is w" no implica *not* o "v == w" para los
         objetos de vista de memoria.

         Distinto en la versión 3.3: Versiones previas comparaban la
         memoria directamente, sin considerar ni el formato de los
         elementos ni la estructura lógica del arreglo.

      tobytes(order='C')

         Retorna los datos en el *buffer* en forma de cadena de bytes.
         Equivale a llamar al constructor de la clase "bytes" en el
         objeto *memoryview*:

            >>> m = memoryview(b"abc")
            >>> m.tobytes()
            b'abc'
            >>> bytes(m)
            b'abc'

         Para arreglos no contiguos el resultado es igual a la
         representación en forma de lista aplanada, con todos los
         elementos convertidos a bytes. El método "tobytes()" soporta
         todos los formatos de cadenas de caracteres, incluidos
         aquellos que no se encuentran en la sintaxis del módulo
         "struct".

         Added in version 3.8: El valor de *order* puede ser {'C',
         'F', 'A'}. Cuando *order* es 'C' o 'F', los datos en el
         arreglo original se convierten al orden de C o Fortran. Para
         vistas contiguas, 'A' retorna una copia exacta de la memoria
         física. En particular, el orden en memoria de Fortran se
         mantiene inalterado. Para vistas no contiguas, los datos se
         convierten primero a C. Definir *order=None* es lo mismo que
         *order='C'*.

      hex(*, bytes_per_sep=1)
      hex(sep, bytes_per_sep=1)

         Retorna una cadena de caracteres que contiene dos dígitos
         hexadecimales por cada byte en el *buffer*:

            >>> m = memoryview(b"abc")
            >>> m.hex()
            '616263'

         Added in version 3.5.

         Distinto en la versión 3.8: De forma similar a "bytes.hex()",
         "memoryview.hex()" soporta ahora los parámetros opcionales
         *sep* y *bytes_per_sep* para insertar separadores entre los
         bytes en la cadena hexadecimal de salida.

      tolist()

         Retorna los datos en el *buffer* como una lista de elementos.

            >>> memoryview(b'abc').tolist()
            [97, 98, 99]
            >>> import array
            >>> a = array.array('d', [1.1, 2.2, 3.3])
            >>> m = memoryview(a)
            >>> m.tolist()
            [1.1, 2.2, 3.3]

         Distinto en la versión 3.3: El método "tolist()" soporta
         ahora todos los formatos nativos de un solo carácter
         definidos en el módulo "struct", así como las
         representaciones de múltiples dimensiones.

      toreadonly()

         Retorna una versión de solo lectura del objeto *memoryview*.
         El objeto original permanece inalterado:

            >>> m = memoryview(bytearray(b'abc'))
            >>> mm = m.toreadonly()
            >>> mm.tolist()
            [97, 98, 99]
            >>> mm[0] = 42
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: cannot modify read-only memory
            >>> m[0] = 43
            >>> mm.tolist()
            [43, 98, 99]

         Added in version 3.8.

      release()

         Libera el buffer subyacente expuesto por el objeto
         *memoryview*. Muchos objetos realizan operaciones especiales
         cuando una vista los está conteniendo (por ejemplo, un objeto
         "bytearray" temporalmente prohíbe el cambio de tamaño); la
         llamada a *release()* sirve para eliminar estas restricciones
         (así como para tratar con los recursos pendientes) lo más
         pronto posible.

         Después de llamar a este método, cualquier operación
         posterior en la vista genera un "ValueError" (excepto el
         propio "release()", que se puede llamar varias veces):

            >>> m = memoryview(b'abc')
            >>> m.release()
            >>> m[0]
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ValueError: operation forbidden on released memoryview object

         El protocolo de gestión de contexto puede ser usado para
         obtener un efecto similar, usando la sentencia "with":

            >>> with memoryview(b'abc') as m:
            ...     m[0]
            ...
            97
            >>> m[0]
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ValueError: operation forbidden on released memoryview object

         Added in version 3.2.

      cast(format, /)
      cast(format, shape, /)

         Transforma el formato o el tamaño de un objeto *memoryview*.
         El parámetro *shape* por defecto vale
         "[byte_length//new_itemsize]", lo que significa que el
         resultado será unidimensional. El valor de retorno es un
         nuevo objeto de tipo *memoryview*, pero el buffer en sí no se
         copia. Las transformaciones pueden ser 1D -> C-*contiguo* y
         C-contiguo -> 1D.

         El formato de destino está restringido a un formato nativo de
         un solo elemento en la sintaxis "struct". Uno de los formatos
         debe ser un formato de bytes ('B', 'b' o 'c'). La longitud en
         bytes del resultado debe ser la misma que la longitud
         original. Tenga en cuenta que todas las longitudes en bytes
         pueden depender del sistema operativo.

         Transforma de "1D/long" a bytes "1D/unsigned":

            >>> import array
            >>> a = array.array('l', [1,2,3])
            >>> x = memoryview(a)
            >>> x.format
            'l'
            >>> x.itemsize
            8
            >>> len(x)
            3
            >>> x.nbytes
            24
            >>> y = x.cast('B')
            >>> y.format
            'B'
            >>> y.itemsize
            1
            >>> len(y)
            24
            >>> y.nbytes
            24

         Transforma de "1D/unsigned" a bytes "1D/char":

            >>> b = bytearray(b'zyz')
            >>> x = memoryview(b)
            >>> x[0] = b'a'
            Traceback (most recent call last):
              ...
            TypeError: memoryview: invalid type for format 'B'
            >>> y = x.cast('c')
            >>> y[0] = b'a'
            >>> b
            bytearray(b'ayz')

         Transforma de "1D/bytes" a "3D/ints" a caracteres
         "1D/signed":

            >>> import struct
            >>> buf = struct.pack("i"*12, *list(range(12)))
            >>> x = memoryview(buf)
            >>> y = x.cast('i', shape=[2,2,3])
            >>> y.tolist()
            [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
            >>> y.format
            'i'
            >>> y.itemsize
            4
            >>> len(y)
            2
            >>> y.nbytes
            48
            >>> z = y.cast('b')
            >>> z.format
            'b'
            >>> z.itemsize
            1
            >>> len(z)
            48
            >>> z.nbytes
            48

         Transforma de *long* "1D/unsigned" a *long* "2D/unsigned":

            >>> buf = struct.pack("L"*6, *list(range(6)))
            >>> x = memoryview(buf)
            >>> y = x.cast('L', shape=[2,3])
            >>> len(y)
            2
            >>> y.nbytes
            48
            >>> y.tolist()
            [[0, 1, 2], [3, 4, 5]]

         Added in version 3.3.

         Distinto en la versión 3.5: El formato de origen ya no está
         restringido cuando se transforma a una vista de bytes.

      count(value, /)

         Count the number of occurrences of *value*.

         Added in version 3.14.

   index(value, start=0, stop=sys.maxsize, /)

         Return the index of the first occurrence of *value* (at or
         after index *start* and before index *stop*).

         Raises a "ValueError" if *value* cannot be found.

         Added in version 3.14.

      Hay disponibles varios atributos de solo lectura:

      obj

         El objeto subyacente del *memoryview*:

            >>> b  = bytearray(b'xyz')
            >>> m = memoryview(b)
            >>> m.obj is b
            True

         Added in version 3.3.

      nbytes

         "nbytes == product(shape) * itemsize == len(m.tobytes())".
         Este es el espacio, medido en bytes, que usará el arreglo en
         una representación continua. No tiene que ser necesariamente
         igual a "len(m)":

            >>> import array
            >>> a = array.array('i', [1,2,3,4,5])
            >>> m = memoryview(a)
            >>> len(m)
            5
            >>> m.nbytes
            20
            >>> y = m[::2]
            >>> len(y)
            3
            >>> y.nbytes
            12
            >>> len(y.tobytes())
            12

         Arreglos de múltiples dimensiones:

            >>> import struct
            >>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
            >>> x = memoryview(buf)
            >>> y = x.cast('d', shape=[3,4])
            >>> y.tolist()
            [[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
            >>> len(y)
            3
            >>> y.nbytes
            96

         Added in version 3.3.

      readonly

         Un booleano que indica si la memoria es de solo lectura.

      format

         Una cadena de caracteres que contiene el formato (en el
         estilo del módulo "struct") para cada elemento de la vista.
         Un objeto *memoryview* se puede crear a partir de un
         exportador con textos de formato arbitrarios, pero algunos
         métodos (como, por ejemplo, "tolist()") están restringidos a
         usar formatos de elementos nativos sencillos.

         Distinto en la versión 3.3: el formato "'B'" se gestiona
         ahora de acuerdo a la sintaxis descrita en el módulo
         "struct". Esto significa que "memoryview(b'abc')[0] ==
         b'abc'[0] == 97".

      itemsize

         El tamaño en bytes de cada elemento del objeto *memoryview*:

            >>> import array, struct
            >>> m = memoryview(array.array('H', [32000, 32001, 32002]))
            >>> m.itemsize
            2
            >>> m[0]
            32000
            >>> struct.calcsize('H') == m.itemsize
            True

      ndim

         Un número entero que indica cuantas dimensiones de un arreglo
         multi-dimensional representa la memoria.

      shape

         Una tupla de números enteros, de longitud "ndim", que indica
         la forma de la memoria en un arreglo de *N* dimensiones.

         Distinto en la versión 3.3: Una tupla vacía, en vez de
         "None", cuando "ndim = 0".

      strides

         Una tupla de números enteros, de longitud "ndim", que indica
         el tamaño en bytes para acceder a cada dimensión del arreglo.

         Distinto en la versión 3.3: Una tupla vacía, en vez de
         "None", cuando "ndim = 0".

      suboffsets

         De uso interno para los arreglos estilo *PIL*. El valor es
         solo informativo.

      c_contiguous

         Un booleano que indica si la memoria es *contiguous* al
         estilo C.

         Added in version 3.3.

      f_contiguous

         Un booleano que indica si la memoria es *contiguous* al
         estilo Fortran.

         Added in version 3.3.

      contiguous

         Un booleano que indica si la memoria es *contiguous*.

         Added in version 3.3.

For information on the thread safety of "memoryview" objects in the
*free-threaded build*, see Thread safety for memoryview objects.

## Conjuntos --- "set", "frozenset"

Un objeto de tipo *set* es una colección no ordenada de distintos
objetos *hashable*. Los casos de uso habituales incluyen comprobar la
pertenencia al conjunto de un elemento, eliminar duplicados de una
secuencia y realizar operaciones matemáticas como la intersección, la
unión, la diferencia o la diferencia simétrica. (Para otros tipos de
contenedores véanse las clases incorporadas "dict", "list", y "tuple",
así como el módulo "collections").

Como otras colecciones, los conjuntos soportan "x in set", "len(set)"
y "for x in set". Como es una colección sin orden, los conjuntos no
registran ni la posición ni el orden de inserción de los elementos.
Por lo mismo, los conjuntos no soportan indexado, ni operaciones de
segmentado, ni otras capacidades propias de las secuencias.

There are currently two built-in set types, "set" and "frozenset". The
"set" type is mutable --- the contents can be changed using methods
like "add()" and "remove()". Since it is mutable, it has no hash value
and cannot be used as either a dictionary key or as an element of
another set. The "frozenset" type is immutable and *hashable* --- its
contents cannot be altered after it is created; it can therefore be
used as a dictionary key or as an element of another set.

Se pueden crear conjuntos no vacíos (*sets*, no *frozensets*)
escribiendo una lista de elementos separados por comas, entre llaves,
por ejemplo "{'jack', 'sjoerd'}", además de con el constructor de la
clase "set".

El constructor para ambas clases se usa de la misma forma:

class set(iterable=(), /)
class frozenset(iterable=(), /)

   Retorna un nuevo *set* o *frozenset*, tomando los elementos a
   partir de *iterable*. Los elementos de un conjunto tienen que tener
   la propiedad de ser *hashable*. Para representar conjuntos
   anidados, o conjuntos de conjuntos, los conjuntos interiores tienen
   que ser instancias de "frozenset". Si no se especifica el parámetro
   *iterable*, se retorna un conjunto vacío.

Los conjuntos (*sets*) se pueden construir de diferentes formas:

* Usando una lista de elementos separados por coma entre corchetes:
  "{'jack', 'sjoerd'}"

* Usando un *set comprehention*: "{c for c in 'abracadabra' if c not
  in 'abc'}"

* Usando un constructor de tipo: "set()", "set('foobar')", "set(['a',
  'b', 'foo'])"

Las instancias de "set" y "frozenset" proporcionan las siguientes
operaciones:

len(s)

   Retorna el número de elementos en el conjunto *s* (cardinalidad de
   *s*).

x in s

   Comprueba que el elemento *x* está incluido en *s*.

x not in s

   Comprueba que el elemento *x* no está incluido en *s*.

frozenset.isdisjoint(other, /)
set.isdisjoint(other, /)

   Retorna "True" si el conjunto no tienen ningún elemento en común
   con *other*. Dos conjuntos son disjuntos si y solo si su
   intersección es el conjunto vacío.

frozenset.issubset(other, /)
set.issubset(other, /)

set <= other

   Comprueba si cada elemento del conjunto también se encuentra en
   *other*.

set < other

   Comprueba si el conjunto es un subconjunto propio de *other*, es
   decir, "set <= other and set != other".

frozenset.issuperset(other, /)
set.issuperset(other, /)

set >= other

   Comprueba que cada elemento de *other* está incluido en el
   conjunto.

set > other

   Comprueba si el conjunto es un superconjunto propio de *other*, es
   decir, "set >= other and set != other".

frozenset.union(*others)
set.union(*others)

set | other | ...

   Retorna un conjunto nuevo que contiene todos los elementos del
   conjunto y de *others*.

frozenset.intersection(*others)
set.intersection(*others)

set & other & ...

   Retorna un conjunto nuevo que contiene todos los elementos que
   están a la vez en conjunto y en *others*.

frozenset.difference(*others)
set.difference(*others)

set - other - ...

   Retorna un conjunto nuevo que contiene todos los elementos del
   conjunto y que no están incluidos en *others*.

frozenset.symmetric_difference(other, /)
set.symmetric_difference(other, /)

set ^ other

   Retorna un conjunto nuevo que contiene elementos que están
   incluidos en el conjunto o en *others*, pero no en los dos a la
   vez.

frozenset.copy()
set.copy()

   Retorna una copia superficial del conjunto.

Note, the non-operator versions of "union()", "intersection()",
"difference()", "symmetric_difference()", "issubset()", and
"issuperset()" methods will accept any iterable as an argument.  In
contrast, their operator based counterparts require their arguments to
be sets.  This precludes error-prone constructions like "set('abc') &
'cbs'" in favor of the more readable "set('abc').intersection('cbs')".

Ambas clases "set" y "frozenset" soportan comparaciones entre sí. Dos
conjuntos son iguales si y solo si cada elemento de cada conjunto está
incluido en el otro (cada uno de ellos es subconjunto del otro). Un
conjunto es menor que otro si y solo si el primero es un subconjunto
propio del segundo (es un subconjunto, pero no son iguales). Un
conjunto es mayor que otro si y solo si el primero es un superconjunto
propio del segundo (es un superconjunto, pero no son iguales).

Las instancias de "set" se comparan con las instancias de "frozenset"
en base a sus elementos. Por ejemplo "set('abc') == frozenset('abc')"
retorna "True" y lo mismo hace "set('abc') in
set([frozenset('abc')])".

Las comparaciones de subconjunto e igualdad no son tan generales que
permitan una función de ordenación total. Por ejemplo, dos conjuntos
cualesquiera que no estén vacíos y que sean disjuntos no son iguales y
tampoco son subconjuntos uno del otro, así que todas estas operaciones
retornan "False": "a<b", "a==b" o "a>b".

Como los conjuntos solo definen un orden parcial (relaciones de
conjuntos), la salida del método "list.sort()" no está definida para
listas de conjuntos.

Los elementos de un conjunto, al igual que las claves de un
diccionario, deben ser *hashable*.

Las operaciones binarias que mezclan instancias de "set" y "frozenset"
retornan el tipo del primer operando. Por ejemplo: "frozenset('ab') |
set('bc')" retornará una instancia de "frozenset".

La siguiente tabla muestra las operaciones disponibles para la clase
"set" que no son aplicables a los conjuntos inmutables "frozenset":

set.update(*others)

set |= other | ...

   Actualiza el conjunto, añadiendo los elementos que se encuentren en
   *others*.

set.intersection_update(*others)

set &= other & ...

   Actualiza el conjunto, manteniendo solo los elementos que se
   encuentren en si mismo y en *others*.

set.difference_update(*others)

set -= other | ...

   Actualiza el conjunto, eliminado los elementos que se encuentren en
   *others*.

set.symmetric_difference_update(other, /)

set ^= other

   Actualiza el conjunto, manteniendo solo los elementos que se
   encuentren en el conjunto o en *others*, pero no en los dos a la
   vez.

set.add(elem, /)

   Añade al conjunto el elemento *elem*.

set.remove(elem, /)

   Elimina del conjunto el elemento *elem*. Lanza la excepción
   "KeyError" si *elem* no estaba incluido en el conjunto.

set.discard(elem, /)

   Elimina del conjunto el elemento *elem*, si estuviera incluido.

set.pop()

   Elimina y retorna un elemento cualquiera del conjunto. Lanza la
   excepción "KeyError" si el conjunto está vacío.

set.clear()

   Elimina todos los elementos del conjunto.

Note, the non-operator versions of the "update()",
"intersection_update()", "difference_update()", and
"symmetric_difference_update()" methods will accept any iterable as an
argument.

Note, the *elem* argument to the "__contains__()", "remove()", and
"discard()" methods may be a set.  To support searching for an
equivalent frozenset, a temporary one is created from *elem*.

Ver también:

  For detailed information on thread-safety guarantees for "set"
  objects, see Thread safety for set objects.

  Sets and frozensets are generic over the type of their elements.

## Tipos mapa --- "dict"

Un objeto de tipo *mapping* relaciona valores (que deben ser
*hashable*) con objetos de cualquier tipo. Los mapas son objetos
mutables. En este momento solo hay un tipo estándar de mapa, los
*dictionary*. (Para otros tipos contenedores, véanse las clases
incorporadas "list", "set", y "tuple", así como el módulo
"collections").

Las claves de un diccionario son valores arbitrarios *almost*. Los
valores que no sean *hashable*, es decir, los valores que contienen
listas, diccionarios u otros tipos mutables (que se comparan por valor
en lugar de por identidad de objeto) no se pueden utilizar como
claves. Los valores que se comparan como iguales (como "1", "1.0" y
"True") se pueden utilizar indistintamente para indexar la misma
entrada de diccionario.

class dict(**kwargs)
class dict(mapping, /, **kwargs)
class dict(iterable, /, **kwargs)

   Retorna un diccionario creado a partir de un parámetro opcional por
   posición, y por una serie de parámetros por nombre, también
   opcionales.

   Los diccionarios se pueden construir de diferentes formas:

   * Usando una lista separada por comas de pares "key: value" entre
     llaves: "{'jack': 4098, 'sjoerd': 4127}" o "{4098: 'jack', 4127:
     'sjoerd'}"

   * Usando una comprensión de diccionario: "{}", "{x: x ** 2 for x in
     range(10)}"

   * Usando un constructor de tipo: "dict()", "dict([('foo', 100),
     ('bar', 200)])", "dict(foo=100, bar=200)"

   If no positional argument is given, an empty dictionary is created.
   If a positional argument is given and it defines a "keys()" method,
   a dictionary is created by calling "__getitem__()" on the argument
   with each returned key from the method.  Otherwise, the positional
   argument must be an *iterable* object.  Each item in the iterable
   must itself be an iterable with exactly two elements.  The first
   element of each item becomes a key in the new dictionary, and the
   second element the corresponding value.  If a key occurs more than
   once, the last value for that key becomes the corresponding value
   in the new dictionary.

   Si se usan parámetros por nombre, los nombres de los parámetros y
   los valores asociados se añaden al diccionario creado a partir del
   parámetro por posición. Si un valor de clave ya estaba presente, el
   valor pasado con el parámetro por nombre reemplazará el valor del
   parámetro por posición.

   Dictionaries compare equal if and only if they have the same "(key,
   value)" pairs (regardless of ordering). Order comparisons ('<',
   '<=', '>=', '>') raise "TypeError".  To illustrate dictionary
   creation and equality, the following examples all return a
   dictionary equal to "{"one": 1, "two": 2, "three": 3}":

      >>> a = dict(one=1, two=2, three=3)
      >>> b = {'one': 1, 'two': 2, 'three': 3}
      >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
      >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
      >>> e = dict({'three': 3, 'one': 1, 'two': 2})
      >>> f = dict({'one': 1, 'three': 3}, two=2)
      >>> a == b == c == d == e == f
      True

   Si queremos definir claves con parámetros por nombre, como en el
   primer ejemplo, entonces los valores de clave solo puede ser
   cadenas de texto conteniendo identificadores de Python válidos. En
   los otros casos, se puede usar cualquier valor como clave.

   Los diccionarios mantienen de forma interna el orden de inserción.
   Actualizar una clave no modifica ese orden. Las claves que vuelven
   a ser insertadas después de haber sido borradas se añaden al
   final.:

      >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
      >>> d
      {'one': 1, 'two': 2, 'three': 3, 'four': 4}
      >>> list(d)
      ['one', 'two', 'three', 'four']
      >>> list(d.values())
      [1, 2, 3, 4]
      >>> d["one"] = 42
      >>> d
      {'one': 42, 'two': 2, 'three': 3, 'four': 4}
      >>> del d["two"]
      >>> d["two"] = None
      >>> d
      {'one': 42, 'three': 3, 'four': 4, 'two': None}

   Distinto en la versión 3.7: Se garantiza que el orden del
   diccionario es el de inserción. Este comportamiento era un detalle
   de implementación en CPython desde la versión 3.6.

   Dictionaries are generic over two types, signifying (respectively)
   the types of the dictionary's keys and values.

   Estas son las operaciones soportados por los diccionarios (y que,
   por tanto, deberían ser soportados por los tipos de mapa
   personalizados):

   list(d)

      Retorna una lista de todas las claves usadas en el diccionario
      *d*.

   len(d)

      Retorna el número de elementos almacenados en el diccionario
      *d*.

   d[key]

      Retorna el elemento dentro de *d* almacenado bajo la clave
      *key*. Lanza una excepción de tipo "KeyError" si la clave *key*
      no se encuentra en el diccionario *d*.

      If a subclass of dict defines a method "__missing__()" and *key*
      is not present, the "d[key]" operation calls that method with
      the key *key* as argument.  The "d[key]" operation then returns
      or raises whatever is returned or raised by the
      "__missing__(key)" call. No other operations or methods invoke
      "__missing__()". If "__missing__()" is not defined, "KeyError"
      is raised. "__missing__()" must be a method; it cannot be an
      instance variable:

         >>> class Counter(dict):
         ...     def __missing__(self, key):
         ...         return 0
         ...
         >>> c = Counter()
         >>> c['red']
         0
         >>> c['red'] += 1
         >>> c['red']
         1

      The example above shows part of the implementation of
      "collections.Counter". A different "__missing__()" method is
      used by "collections.defaultdict".

   d[key] = value

      Asigna el valor *value* a "d[key]".

   del d[key]

      Elimina "d[key]" de *d*. Lanza una excepción "KeyError" si *key*
      no está en el mapa.

   key in d

      Retorna "True" si *d* tiene una entrada en la clave *key*,
      "False" en caso contrario.

   key not in d

      Equivale a "not key in d".

   iter(d)

      Retorna un iterador que recorre todas las claves de un
      diccionario. Es una forma abreviada de "iter(d.keys())".

   clear()

      Elimina todos los elementos del diccionario.

   copy()

      Retorna una copia superficial del diccionario.

   classmethod fromkeys(iterable, value=None, /)

      Crea un nuevo diccionario con las claves obtenidos a partir del
      *iterable* y con valor *value*.

      El método "fromkeys()" es un método de clase que retorna un
      diccionario nuevo. El valor de *value* por defecto es "None".
      Todos los valores harán referencia a una única instancia, por lo
      que en general no tiene sentido que *value* sea un objeto
      mutable, como una lista vacía. Para poder obtener valores
      diferentes, se puede usar mejor un diccionario por comprensión.

   get(key, default=None, /)

      Retorna el elemento dentro de *d* almacenado bajo la clave
      *key*, si *key* está en el diccionario; si no, retorna
      *default*. El valor de *default* por defecto es "None", por lo
      que esta función nunca lanza la excepción "KeyError".

   items()

      Retorna una nueva vista de los elementos del diccionario (pares
      "(key, value)"). Véase la documentación de los objetos vistas.

   keys()

      Retorna una nueva vista de las claves del diccionario. Véase la
      documentación de las vistas.

   pop(key, /)
   pop(key, default, /)

      Si *key* está en el diccionario, lo elimina del diccionario y
      retorna su valor; si no está, retorna *default*. Si no se
      especifica valor para *default* y la *key* no se encuentra en el
      diccionario, se lanza la excepción "KeyError".

   popitem()

      Elimina y retorna una pareja "(key, value)" del diccionario. Las
      parejas se retornan en el orden LIFO (*last-in, first-out*:
      Último en entrar, primero en salir).

      El método "popitem()" es útil para recorrer y a la vez vaciar un
      diccionario, un proceso usado a menudo en algoritmos de
      conjuntos. Si el diccionario está vacío, llamar a "popitem()"
      lanza la excepción "KeyError".

      Distinto en la versión 3.7: El orden *LIFO* ahora está
      garantizado. En versiones anteriores, el método "popitem()"
      retorna una pareja clave/valor arbitraria.

   reversed(d)

      Retorna un iterador que recorre las claves en orden inverso. Es
      una forma abreviada de "reversed(d.keys())".

      Added in version 3.8.

   setdefault(key, default=None, /)

      Si *key* está incluida en el diccionario, retorna el valor
      almacenado. Si no, inserta con la clave *key* el valor definido
      en *default* y retorna *default*. El valor por defecto de
      *default* es "None".

   update(**kwargs)
   update(mapping, /, **kwargs)
   update(iterable, /, **kwargs)

      Update the dictionary with the key/value pairs from *mapping* or
      *iterable* and *kwargs*, overwriting existing keys.  Return
      "None".

      "update()" accepts either another object with a "keys()" method
      (in which case "__getitem__()" is called with every key returned
      from the method) or an iterable of key/value pairs (as tuples or
      other iterables of length two). If keyword arguments are
      specified, the dictionary is then updated with those key/value
      pairs: "d.update(red=1, blue=2)".

   values()

      Retorna una nueva vista de los valores del diccionario. Véase la
      documentación sobre objetos vistas.

      Una comparación de igualdad entre una vista "dict.values()" y
      otra siempre retornará "False". Esto también pasa cuando se
      compara "dict.values()" consigo mismo:

         >>> d = {'a': 1}
         >>> d.values() == d.values()
         False

   d | other

      Crea un nuevo diccionario con las claves y valores fusionados de
      *d* y *other*, por lo cual ambos deben ser diccionarios. Los
      valores de *other* tienen prioridad cuando *d* y *other* tienen
      claves compartidas.

      Added in version 3.9.

   d |= other

      Actualiza el diccionario *d* con las claves y valores de
      *other*, el cual podría ser ya sea un a *mapping* o un
      *iterable* de pares clave/valor. Los valores de *other* tienen
      prioridad cuando *d* y *other* tienen claves compartidas.

      Added in version 3.9.

   Tanto los diccionarios como las vistas basadas en diccionarios son
   reversibles:

      >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
      >>> d
      {'one': 1, 'two': 2, 'three': 3, 'four': 4}
      >>> list(reversed(d))
      ['four', 'three', 'two', 'one']
      >>> list(reversed(d.values()))
      [4, 3, 2, 1]
      >>> list(reversed(d.items()))
      [('four', 4), ('three', 3), ('two', 2), ('one', 1)]

   Distinto en la versión 3.8: Los diccionarios son ahora reversibles.

Ver también:

  Se puede usar un objeto de tipo "types.MappingProxyType" para crear
  una vista de solo lectura de un objeto "dict".

Ver también:

  For detailed information on thread-safety guarantees for "dict"
  objects, see Thread safety for dict objects.

### Objetos tipos vista de diccionario

Los objetos retornados por los métodos "dict.keys()", "dict.values()"
y "dict.items()" son objetos tipo vista o *view*. Estos objetos
proporcionan una vista dinámica del contenido del diccionario, lo que
significa que si el diccionario cambia, las vistas reflejan estos
cambios.

Las vistas de un diccionario pueden ser iteradas para retornar sus
datos respectivos, y soportan operaciones de comprobación de
pertenencia:

len(dictview)

   Retorna el número de entradas en un diccionario.

iter(dictview)

   Retorna un iterador sobre las claves, valores o elementos
   (representados en forma de tuplas "(key, value)") de un
   diccionario.

   Las claves y los valores se iteran en orden de inserción. Esto
   permite la creación de parejas "(value, key)" usando la función
   "zip()": "pairs = zip(d.values(), d.keys())". Otra forma de crear
   la misma lista es "pairs = [(v, k) for (k, v) in d.items()]".

   Iterar sobre un diccionario a la vez que se borran o añaden
   entradas puede lanzar una excepción de tipo "RuntimeError", o puede
   provocar que no se iteren sobre todas las entradas.

   Distinto en la versión 3.7: Se garantiza que el orden de los
   diccionarios es el de inserción.

x in dictview

   Retorna "True" si *x* está incluido en las claves, los valores o
   los elementos del diccionario (en el último caso, *x* debe ser una
   tupla "(key, value)").

reversed(dictview)

   Retorna un iterador inverso sobre las claves, los valores o los
   elementos del diccionario. El orden de la vista será el inverso del
   orden de inserción.

   Distinto en la versión 3.8: Las vistas de un diccionario no son
   reversibles.

dictview.mapping

   Retorna un "types.MappingProxyType" que envuelve el diccionario
   original al que se refiere la vista.

   Added in version 3.10.

Las vistas de claves son similares a conjuntos, ya que sus entradas
son únicas y *hashable*. Las vistas de elementos también tienen
operaciones similares a conjuntos, ya que los pares (clave, valor) son
únicos y las claves se pueden codificar en hash. Si todos los valores
de una vista de elementos también se pueden codificar en hash, la
vista de elementos puede interoperar con otros conjuntos. (Las vistas
de valores no se tratan como similares a conjuntos, ya que las
entradas generalmente no son únicas). Para las vistas similares a
conjuntos, están disponibles todas las operaciones definidas para la
clase base abstracta "collections.abc.Set" (por ejemplo, "==", "<" o
"^"). Al utilizar operadores de conjunto, las vistas similares a
conjuntos aceptan cualquier iterable como el otro operando, a
diferencia de los conjuntos que solo aceptan conjuntos como entrada.

Un ejemplo de uso de una vista de diccionario:

   >>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
   >>> keys = dishes.keys()
   >>> values = dishes.values()

   >>> # iteration
   >>> n = 0
   >>> for val in values:
   ...     n += val
   ...
   >>> print(n)
   504

   >>> # Las llaves y los valores se iteran en el mismo orden (orden de inserción)
   >>> list(keys)
   ['eggs', 'sausage', 'bacon', 'spam']
   >>> list(values)
   [2, 1, 1, 500]

   >>> # Los objetos vista son dinámicos y reflejan cambios de diccionario.
   >>> del dishes['eggs']
   >>> del dishes['sausage']
   >>> list(keys)
   ['bacon', 'spam']

   >>> # operaciones de conjunto
   >>> keys & {'eggs', 'bacon', 'salad'}
   {'bacon'}
   >>> keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}
   True
   >>> keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}
   True

   >>> # recuperar un proxy de solo lectura para el diccionario original
   >>> values.mapping
   mappingproxy({'bacon': 1, 'spam': 500})
   >>> values.mapping['spam']
   500

## Tipos gestores de contexto

La expresión "with" de Python soporta el concepto de un contexto en
tiempo de ejecución definido mediante un gestor de contexto. Para
implementar esto, se permite al usuario crear clases para definir
estos contextos definiendo dos métodos, uno a ejecutar antes de entrar
del bloque de código y otro a ejecutar justo después de salir del
mismo:

contextmanager.__enter__()

   Entra en el contexto en tiempo de ejecución, y retorna o bien este
   objeto u otro relacionado con el contexto. El valor retornado por
   este método se vincula al identificador que viene tras la palabra
   clave "as" usada en la sentencia "with" que define el contexto.

   Un ejemplo de gestor de contexto que se retorna a si mismo es un
   objeto de tipo *file object*. Los objetos de tipo "File" se
   retornan a si mismo en la llamada a "__enter__()", lo que permite
   que "open()" sea usado como gestores de contexto en una sentencia
   "with".

   Un ejemplo de gestor de contexto que retorna otro objeto
   relacionado en el que define la función "decimal.localcontext()".
   Este gestor define el contexto de uso en operaciones decimales a
   partir de una copia del contexto original, y retorna esa copia. De
   esta manera se puede cambiar el contexto decimal dentro del cuerpo
   del "with" sin afectar al código fuera de "with".

contextmanager.__exit__(exc_type, exc_val, exc_tb)

   Sale del contexto y retorna un indicador booleano que indica si se
   debe ignorar cualquier posible excepción que hubiera ocurrido
   dentro del mismo. Si se produce una excepción mientras se ejecutan
   las sentencias definidas en el cuerpo de la sentencia "with", los
   parámetros de esta función contienen el tipo y valor de la
   excepción, así como la información relativa a la traza de
   ejecución. Si no se produce ninguna excepción, los tres parámetros
   valen "None".

   Returning a true value from this method will cause the "with"
   statement to suppress the exception and continue execution with the
   statement immediately following the "with" statement. Otherwise the
   exception continues propagating after this method has finished
   executing.

   If this method raises an exception while handling an earlier
   exception from the "with" block, the new exception is raised, and
   the original exception is stored in its "__context__" attribute.

   La excepción que se pasa nunca debe volver a generarse
   explícitamente; en su lugar, este método debe devolver un valor
   falso para indicar que el método se completó correctamente y no
   desea suprimir la excepción generada. Esto permite que el código de
   administración de contexto detecte fácilmente si un método
   "__exit__()" ha fallado o no.

Python define varios gestores de contexto para facilitar la sincronía
entre hilos, asegurarse del cierre de ficheros y otros objetos
similares y para modificar de forma simple el contexto para las
expresiones aritméticas con decimales. Los tipos específicos no se
tratan especialmente fuera de su implementación del protocolo de
administración de contexto. Véase el módulo "contextlib" para algunos
ejemplos.

Los *generator* de Python y el decorador definidos en la clase
"contextlib.contextmanager" permiten implementar de forma sencilla
estos protocolos. Si una función generadora se decora con la clase
"contextlib.contextmanager", retornará un gestor de contexto que
incluye los métodos necesarios "__enter__()" y "__exit__()", en vez
del iterador que se produciría si no se decora la función generadora.

Nótese que no hay una ranura específica para ninguno de estos métodos
en la estructura usada para los objetos Python en el nivel de la API
de Python/C. Objetos que quieran definir estos métodos deben
implementarlos como métodos normales de Python. Comparado con la
complejidad de definir un contexto en tiempo de ejecución, lo
complejidad de una búsqueda simple en un diccionario es mínima.

## Tipos de anotaciones de type — alias genérico, Union

Los tipos principales integrados para *anotaciones de tipo* son alias
genérico y Union.

### Tipo Alias Genérico

Los objetos "GenericAlias" generalmente se crean para suscribir a una
clase. Se utilizan con mayor frecuencia con clases contenedoras, como
"list" o "dict". Por ejemplo, "list[int]" es un objeto "GenericAlias"
que se creó para suscribir la clase "list" con el argumento "int". Los
objetos "GenericAlias" están pensados principalmente para usar con
*anotaciones de tipo*.

Nota:

  Generalmente solo es posible suscribir a una clase si ésta
  implementa el método especial "__class_getitem__()".

El objeto "GenericAlias" actúa como *proxy* para *tipo genérico*,
implementando *parameterized generics*.

Para una clase contenedora, el argumento (o los argumentos)
proporcionado(s) a una suscripción de la clase puede indicar el tipo
(o tipos) de los elementos que contiene un objeto. Por ejemplo, se
puede usar "set[bytes]" en anotaciones de tipo para significar un
"set" en el que todos los elementos son del tipo "bytes".

Para una clase que define el método "__class_getitem__()" pero no es
un contenedor, el argumento (o los argumentos) proporcionado(s) a una
suscripción de la clase a menudo indicarán el tipo (o los tipos) de
retorno de uno o más métodos definidos en un objeto. Por ejemplo, las
"expresiones regulares" se pueden usar tanto para el tipo de datos
"str" y el tipo de datos "bytes":

* Si "x = re.search('foo', 'foo')", "x" será un objeto re.Match donde
  los valores de retorno de "x.group(0)" y "x[0]" serán de tipo "str".
  Podemos representar este tipo de objeto en anotaciones de type con
  el "GenericAlias" de "re.Match[str]".

* Si "y = re.search(b'bar', b'bar')", (nótese que "b" es para
  "bytes"), "y" también será una instancia de "re.Match", pero los
  valores de retorno de "y.group(0)" y "y[0]" serán de tipo "bytes".
  En anotaciones de type, representaríamos esta variedad de objetos
  re.Match con "re.Match[bytes]".

"GenericAlias" objects are instances of the class
"types.GenericAlias", which can also be used to create "GenericAlias"
objects directly. Specializations of user-defined generic classes may
not be instances of "types.GenericAlias", but they provide similar
functionality.

T[X, Y, ...]

   Crea un "GenericAlias" que representa un tipo "T" parametrizado por
   tipos *X*, *Y* y más dependiendo de la "T" usada. Por ejemplo, una
   función espera un "list" que contenga elementos "float":

      def average(values: list[float]) -> float:
          return sum(values) / len(values)

   Otro ejemplo para el *mapping* de objetos, usando un "dict", el
   cual es un tipo genérico que espera dos parámetros de tipo que
   representan el tipo de la clave y el tipo del valor. En este
   ejemplo, la función espera un "dict" con claves de tipo "str" y
   valores de tipo "int":

      def send_post_request(url: str, body: dict[str, int]) -> None:
          ...

Las funciones integradas "isinstance()" y "issubclass()" no aceptan
tipos "GenericAlias" como segundo argumento:

   >>> isinstance([1, 2], list[str])
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: isinstance() argument 2 cannot be a parameterized generic

Python en tiempo de ejecución no hace cumplir las *anotaciones de
tipo*. Esto se extiende para tipos genéricos y sus parámetros. Cuando
se crea un objeto contenedor desde un "GenericAlias", los elementos
del contenedor no se verifican con su tipo. Por ejemplo, el siguiente
código no es recomendado en lo absoluto, pero correrá sin errores:

   >>> t = list[str]
   >>> t([1, 2, 3])
   [1, 2, 3]

Además, los genéricos parametrizados borran parámetros de type durante
la creación de objetos:

   >>> t = list[str]
   >>> type(t)
   <class 'types.GenericAlias'>

   >>> l = t()
   >>> type(l)
   <class 'list'>

Instances of "GenericAlias" are not classes at runtime, even though
they behave like classes (they can be instantiated and subclassed):

   >>> import inspect
   >>> inspect.isclass(list[int])
   False

This is true for user-defined generics also.

Llamando a "repr()" o "str()" en un genérico se muestra el tipo
parametrizado:

   >>> repr(list[int])
   'list[int]'

   >>> str(list[int])
   'list[int]'

El método "__getitem__()" de contenedores genéricos lanzarán una
excepción para rechazar los errores como "dict[str][str]":

   >>> dict[str][str]
   Traceback (most recent call last):
     ...
   TypeError: dict[str] is not a generic class

Sin embargo, estas expresiones son válidas cuando se usan variables de
type. El índice debe tener tantos elementos como los elementos de
variable de type en los "__args__" del objeto "GenericAlias":

   >>> from typing import TypeVar
   >>> Y = TypeVar('Y')
   >>> dict[str, Y][int]
   dict[str, int]

#### Clases genéricas estándar

Las siguientes clases de la biblioteca estándar soportan genéricos
parametrizados. Esta lista no es exhaustiva.

* "tuple"

* "list"

* "dict"

* "set"

* "frozenset"

* "type"

* "asyncio.Future"

* "asyncio.Task"

* "collections.deque"

* "collections.defaultdict"

* "collections.OrderedDict"

* "collections.Counter"

* "collections.ChainMap"

* "collections.abc.Awaitable"

* "collections.abc.Coroutine"

* "collections.abc.AsyncIterable"

* "collections.abc.AsyncIterator"

* "collections.abc.AsyncGenerator"

* "collections.abc.Iterable"

* "collections.abc.Iterator"

* "collections.abc.Generator"

* "collections.abc.Reversible"

* "collections.abc.Container"

* "collections.abc.Collection"

* "collections.abc.Callable"

* "collections.abc.Set"

* "collections.abc.MutableSet"

* "collections.abc.Mapping"

* "collections.abc.MutableMapping"

* "collections.abc.Sequence"

* "collections.abc.MutableSequence"

* "collections.abc.ByteString"

* "collections.abc.MappingView"

* "collections.abc.KeysView"

* "collections.abc.ItemsView"

* "collections.abc.ValuesView"

* "contextlib.AbstractContextManager"

* "contextlib.AbstractAsyncContextManager"

* "dataclasses.Field"

* "functools.cached_property"

* "functools.partialmethod"

* "os.PathLike"

* "queue.LifoQueue"

* "queue.Queue"

* "queue.PriorityQueue"

* "queue.SimpleQueue"

* re.Pattern

* re.Match

* "shelve.BsdDbShelf"

* "shelve.DbfilenameShelf"

* "shelve.Shelf"

* "types.MappingProxyType"

* "weakref.WeakKeyDictionary"

* "weakref.WeakMethod"

* "weakref.WeakSet"

* "weakref.WeakValueDictionary"

#### Atributos especiales de los objetos "GenericAlias"

Todos los genéricos parametrizados implementan atributos especiales de
solo lectura.

genericalias.__origin__

   Este atributo apunta a la clase genérica no parametrizada:

      >>> list[int].__origin__
      <class 'list'>

genericalias.__args__

   Este atributo es una clase "tuple" (posiblemente de longitud 1) de
   tipos genéricos pasados al método original "__class_getitem__()" de
   la clase genérica:

      >>> dict[str, list[int]].__args__
      (<class 'str'>, list[int])

genericalias.__parameters__

   Este atributo es una tupla (posiblemente vacía) computada
   perezosamente con las variables de tipo únicas encontradas en
   "__args__":

      >>> from typing import TypeVar

      >>> T = TypeVar('T')
      >>> list[T].__parameters__
      (~T,)

   Nota:

     Un objeto "GenericAlias" con "typing.ParamSpec" parámetros puede
     no tener los "__parameters__" correctos después de la sustitución
     porque "typing.ParamSpec" está destinado principalmente a la
     verificación de tipos estáticos.

genericalias.__unpacked__

   Un booleano que es verdadero si el alias ha sido desempaquetado
   usando el operador "*" (véase "TypeVarTuple").

   Added in version 3.11.

Ver también:

  **PEP 484** - Type Hints
     Presentación del marco de trabajo de Python para anotaciones de
     tipo.

  **PEP 585** - Sugerencias de tipo genéricas en colecciones estándar
     Introducción a la capacidad de parametrizar de forma nativa
     clases de la biblioteca estándar, siempre que implementen el
     método de clase especial "__class_getitem__()".

  Genéricos, tipos genéricos definidos por el usuario y
  "typing.Generic"
     Documentación sobre cómo implementar clases genéricas que se
     pueden parametrizar en tiempo de ejecución y que los validadores
     estático de tipos pueden entender.

Added in version 3.9.

### Tipo de conversión

A union object holds the value of the "|" (bitwise or) operation on
multiple type objects.  These types are intended primarily for *type
annotations*. The union type expression enables cleaner type hinting
syntax compared to subscripting "typing.Union".

X | Y | ...

   Define un objeto de conversión que contiene tipos *X*, *Y*, etc. "X
   | Y" significa X o Y. Es equivalente a "typing.Union[X, Y]". Por
   ejemplo, la siguiente función espera un argumento de tipo "int" or
   "float":

      def square(number: int | float) -> int | float:
          return number ** 2

   Nota:

     El operando "|" no se puede utilizar en tiempo de ejecución para
     definir uniones en las que uno o más miembros sean una referencia
     hacia delante. Por ejemplo, "int | "Foo"", donde ""Foo"" es una
     referencia a una clase que aún no se ha definido, fallará en
     tiempo de ejecución. Para las uniones que incluyen referencias
     hacia delante, presente la expresión completa como una cadena,
     por ejemplo, ""int | Foo"".

union_object == other

   Los objetos de conversión se pueden probar para determinar su
   igualdad con otros objetos de conversión. Detalles:

   * Las conversiones de conversión se aplanan:

        (int | str) | float == int | str | float

   * Se eliminan los tipos redundantes:

        int | str | int == int | str

   * Al comparar conversiones, se ignora el orden:

        int | str == str | int

   * It creates instances of "typing.Union":

        int | str == typing.Union[int, str]
        type(int | str) is typing.Union

   * Los tipos opcionales se pueden escribir como una unión con
     "None":

        str | None == typing.Optional[str]

isinstance(obj, union_object)

issubclass(obj, union_object)

   Las llamadas a "isinstance()" y "issubclass()" también son
   compatibles con un objeto de conversión:

      >>> isinstance("", int | str)
      True

   Sin embargo, no se puede comprobar parameterized generics en
   objetos de unión:

      >>> isinstance(1, int | list[int])  # short-circuit evaluation
      True
      >>> isinstance([1], int | list[int])
      Traceback (most recent call last):
        ...
      TypeError: isinstance() argument 2 cannot be a parameterized generic

The user-exposed type for the union object can be accessed from
"typing.Union" and used for "isinstance()" checks:

   >>> import typing
   >>> isinstance(int | str, typing.Union)
   True
   >>> typing.Union()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: cannot create 'typing.Union' instances

Nota:

  Se agregó el método "__or__()" para objetos de tipo para admitir la
  sintaxis "X | Y". Si una metaclase implementa "__or__()", la Unión
  puede anularlo:

     >>> class M(type):
     ...     def __or__(self, other):
     ...         return "Hello"
     ...
     >>> class C(metaclass=M):
     ...     pass
     ...
     >>> C | int
     'Hello'
     >>> int | C
     int | C

Ver también:

  **PEP 604** — PEP propone la sintaxis "X | Y" y tipo Conversión.

Added in version 3.10.

Distinto en la versión 3.14: Union objects are now instances of
"typing.Union". Previously, they were instances of "types.UnionType",
which remains an alias for "typing.Union".

## Otros tipos predefinidos

El intérprete soporta otros tipos de objetos variados. La mayoría de
ellos solo implementan una o dos operaciones.

### Módulos

La única operación especial que implementan los módulos es el acceso
como atributos: "m.name", donde *m* es un módulo y *name* accede a un
nombre definido en la tabla de símbolos del módulo *m*. También se
puede asignar valores a los atributos de un módulo (nótese que la
sentencia "import" no es, estrictamente hablando, una operación del
objeto de tipo módulo; la sentencia "import foo" no requiere la
existencia de un módulo llamado *foo*, sino una *definición* (externa)
de un módulo *foo* en alguna parte).

Un atributo especial de cada módulo es "__dict__". Es un diccionario
que contiene la tabla de símbolos del módulo. Cambiar el diccionario
cambiará por tanto el contenido de la tabla de símbolos, pero no es
posible realizar una asignación directa al atributo "__dict__" (se
puede realizar una asignación como "m.__dict__['a'] = 1", que define
el valor de "m.a" como "1", pero no se puede hacer "m.__dict__ = {}").
No se recomienda manipular los contenidos del atributo "__dict__"
directamente.

Los módulos incluidos en el intérprete se escriben así: "<module 'sys'
(built-in)>". Si se cargan desde un archivo, se escriben como "<module
'os' from '/usr/local/lib/pythonX.Y/os.pyc'>".

### Clases e instancias de clase

Véase Objetos, valores y tipos y Definiciones de clase para más
información.

### Funciones

Los objetos de tipo función se crean mediante definiciones de función.
La única operación posible con un objeto de tipo función es llamarla:
"func(argument-list)".

Hay dos tipos de funciones: Las funciones básicas o predefinidas y las
funciones definidas por el usuario. Las dos soportan la misma
operación (ser llamadas), pero la implementación es diferente, de ahí
que se consideren de distintos tipo.

Véase Definiciones de funciones para más información.

### Métodos

Methods are functions that are called using the attribute notation.
There are two flavors: built-in methods (such as "append()" on lists)
and class instance method. Built-in methods are described with the
types that support them.

Si accede a un método (una función definida en un espacio de nombres
de clase) a través de una instancia, obtendrá un objeto especial: un
objeto *método enlazado* (también llamado instance method). Cuando se
lo llama, agregará el argumento "self" a la lista de argumentos. Los
métodos enlazados tienen dos atributos especiales de solo lectura:
"m.__self__" es el objeto en el que opera el método y "m.__func__" es
la función que implementa el método. Llamar a "m(arg-1, arg-2, ...,
arg-n)" es completamente equivalente a llamar a
"m.__func__(m.__self__, arg-1, arg-2, ..., arg-n)".

Al igual que function objects, los objetos de método enlazados admiten
la obtención de atributos arbitrarios. Sin embargo, dado que los
atributos de método se almacenan en realidad en el objeto de función
subyacente ("method.__func__"), no se permite configurar atributos de
método en métodos enlazados. Intentar configurar un atributo en un
método da como resultado que se genere un "AttributeError". Para
configurar un atributo de método, debe configurarlo explícitamente en
el objeto de función subyacente:

   >>> class C:
   ...     def method(self):
   ...         pass
   ...
   >>> c = C()
   >>> c.method.whoami = 'my name is method'  # can't set on the method
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'method' object has no attribute 'whoami'
   >>> c.method.__func__.whoami = 'my name is method'
   >>> c.method.whoami
   'my name is method'

Véase Métodos de instancia para más información.

### Objetos código

La implementación utiliza objetos de código para representar código
Python ejecutable "pseudocompilado", como el cuerpo de una función. Se
diferencian de los objetos de función porque no contienen una
referencia a su entorno de ejecución global. Los objetos de código son
devueltos por la función "compile()" incorporada y se pueden extraer
de los objetos de función a través de su atributo "__code__". Consulte
también el módulo "code".

Al acceder a "__code__" se genera un auditing event
"object.__getattr__" con argumentos "obj" y ""__code__"".

Un objeto de tipo código puede ser evaluado o ejecutando pasándolo
como parámetros a las funciones incorporadas "exec()" o "eval()" (que
también aceptan código Python en forma de cadena de caracteres).

Véase Jerarquía de tipos estándar para más información.

### Objetos Tipo

Los objetos de tipo Tipo (*Type*) representan a los distintos tipos de
datos. El tipo de un objeto particular puede ser consultado usando la
función incorporada "type()". Los objetos Tipo no tienen ninguna
operación especial. El módulo "types" define nombres para todos los
tipos básicos definidos en la biblioteca estándar.

Los tipos se escriben de la siguiente forma: "<class 'int'>".

### El objeto nulo (*Null*)

Todas las funciones que no definen de forma explícita un valor de
retorno retornan este objeto. Los objetos nulos no soportan ninguna
operación especial. Solo existe un único objeto nulo, llamado "None"
(un nombre predefinido o básico). La expresión "type(None)()" produce
el mismo objeto "None", esto se conoce como *Singleton*.

Se escribe "None".

### El objeto puntos suspensivos (*Ellipsis*)

This object is commonly used to indicate that something is omitted. It
supports no special operations.  There is exactly one ellipsis object,
named "Ellipsis" (a built-in name).  "type(Ellipsis)()" produces the
"Ellipsis" singleton.

Se puede escribir como "Ellipsis" o "...".

In typical use, "..." as the "Ellipsis" object appears in a few
different places, for instance:

* In type annotations, such as callable arguments or tuple elements.

* As the body of a function instead of a pass statement.

* In third-party libraries, such as Numpy's slicing and striding.

Python also uses three dots in ways that are not "Ellipsis" objects,
for instance:

* Doctest's "ELLIPSIS", as a pattern for missing content.

* The default Python prompt of the *interactive* shell when partial
  input is incomplete.

Lastly, the Python documentation often uses three dots in conventional
English usage to mean omitted content, even in code examples that also
use them as the "Ellipsis".

### El objeto *NotImplemented*

Este objeto se devuelve a partir de comparaciones y operaciones
binarias cuando se les pide que operen en tipos que no admiten.
Consulte Comparaciones para obtener más información. Hay exactamente
un objeto "NotImplemented". "type(NotImplemented)()" produce la
instancia singleton.

Se escribe como "NotImplemented".

### Objetos internos

Consulte Jerarquía de tipos estándar para obtener esta información.
Describe stack frame objects, traceback objects y los objetos de
sector.

## Atributos especiales

La implementación añade unos cuantos atributos de solo lectura a
varios tipos de objetos, cuando resulta relevante. Algunos de estos
atributos son reportados por la función incorporada "dir()".

definition.__name__

   El nombre de la clase, función, método, descriptor o instancia
   generadora.

definition.__qualname__

   El nombre calificado (*qualified name*) de la clase, función,
   método, descriptor o instancia generadora.

   Added in version 3.3.

definition.__module__

   El nombre del módulo en el que se definió una clase o función.

definition.__doc__

   La cadena de documentación de una clase o función, o "None" si no
   está definida.

definition.__type_params__

   type parameters de clases y funciones genéricas y type aliases.
   Para clases y funciones que no sean genéricas, será una tupla
   vacía.

   Added in version 3.12.

## Limitación de longitud de conversión de cadena de tipo entero

CPython tiene un límite global para conversiones entre "int" y "str"
para mitigar los ataques de denegación de servicio. Este límite *solo*
se aplica a decimales u otras bases numéricas que no sean potencias de
dos. Las conversiones hexadecimales, octales y binarias son
ilimitadas. Se puede configurar el límite.

El tipo "int" en CPython es un número de longitud arbitraria
almacenado en formato binario (comúnmente conocido como "bignum"). No
existe ningún algoritmo que pueda convertir una cadena en un entero
binario o un entero binario en una cadena en tiempo lineal; *unless*
tiene como base una potencia de 2. Incluso los algoritmos más
conocidos para la base 10 tienen una complejidad subcuadrática.
Convertir un valor grande como "int('1' * 500_000)" puede llevar más
de un segundo en una CPU rápida.

Limitar el tamaño de la conversión ofrece una forma práctica de evitar
**CVE 2020-10735**.

El límite se aplica al número de caracteres de dígitos en la cadena de
entrada o salida cuando estaría involucrado un algoritmo de conversión
no lineal. Los guiones bajos y el signo no se cuentan para el límite.

Cuando una operación excede el límite, se lanza una excepción
"ValueError":

   >>> import sys
   >>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
   >>> _ = int('2' * 5432)
   Traceback (most recent call last):
   ...
   ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
   >>> i = int('2' * 4300)
   >>> len(str(i))
   4300
   >>> i_squared = i*i
   >>> len(str(i_squared))
   Traceback (most recent call last):
   ...
   ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
   >>> len(hex(i_squared))
   7144
   >>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal no tiene límite.

El límite predeterminado es de 4300 dígitos como se indica en
"sys.int_info.default_max_str_digits". El límite más bajo que se puede
configurar es de 640 dígitos como se indica en
"sys.int_info.str_digits_check_threshold".

Verificación:

   >>> import sys
   >>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
   >>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
   >>> msg = int('578966293710682886880994035146873798396722250538762761564'
   ...           '9252925514383915483333812743580549779436104706260696366600'
   ...           '571186405732').to_bytes(53, 'big')
   ...

Added in version 3.11.

### APIs afectadas

La limitación solo se aplica a conversiones potencialmente lentas
entre "int" y "str" o "bytes":

* "int(string)" con base predeterminada a 10.

* "int(string, base)" para todas las bases que no sean una potencia de
  2.

* "str(integer)".

* "repr(integer)".

* cualquier otra conversión de cadena a base 10, por ejemplo,
  "f"{integer}"", ""{}".format(integer)" o "b"%d" % integer".

Las limitaciones no se aplican a funciones con un algoritmo lineal:

* "int(string, base)" con base 2, 4, 8, 16 o 32.

* "int.from_bytes()" y "int.to_bytes()".

* "hex()", "oct()", "bin()".

* Format specification mini-language para números hexadecimales,
  octales y binarios.

* "str" a "float".

* "str" a "decimal.Decimal".

### Configuración del límite

Antes de que se inicie Python, puedes usar una variable de entorno o
un indicador de línea de comandos del intérprete para configurar el
límite:

* "PYTHONINTMAXSTRDIGITS", por ejemplo, "PYTHONINTMAXSTRDIGITS=640
  python3" para configurar el límite a 640 o "PYTHONINTMAXSTRDIGITS=0
  python3" para desactivar la limitación.

* "-X int_max_str_digits", por ejemplo, "python3 -X
  int_max_str_digits=640"

* "sys.flags.int_max_str_digits" contiene el valor de
  "PYTHONINTMAXSTRDIGITS" o "-X int_max_str_digits". Si tanto la
  variable de entorno como la opción "-X" están configuradas, la
  opción "-X" tiene prioridad. Un valor de *-1* indica que ambas
  opciones no estaban configuradas, por lo que se utilizó un valor de
  "sys.int_info.default_max_str_digits" durante la inicialización.

Desde el código, puedes inspeccionar el límite actual y configurar uno
nuevo al usar estas APIs de "sys":

* "sys.get_int_max_str_digits()" y "sys.set_int_max_str_digits()" son
  un getter y un setter para el límite de todo el intérprete. Los
  subintérpretes tienen su propio límite.

La información sobre los valores predeterminados y mínimos se puede
encontrar en "sys.int_info":

* "sys.int_info.default_max_str_digits" es el límite predeterminado
  compilado.

* "sys.int_info.str_digits_check_threshold" es el valor más bajo
  aceptado para el límite (aparte de 0, que lo desactiva).

Added in version 3.11.

Prudencia:

  Configurar un límite bajo *puede* generar problemas. Si bien es
  raro, existe un código que contiene constantes enteras en decimal en
  su origen que excede el umbral mínimo. Una consecuencia de
  configurar el límite es que el código fuente de Python que contiene
  literales enteros decimales más grandes que el límite encontrará un
  error durante el análisis, generalmente en el momento de inicio o en
  el momento de importación o incluso en el momento de instalación -
  en cualquier momento y actualizado, ".pyc" no existe ya para el
  código. Una solución para la fuente que contiene constantes tan
  grandes es convertirlas a la forma hexadecimal "0x" ya que no tiene
  límite.Prueba tu aplicación minuciosamente si utilizas un límite
  bajo. Asegúrate de que tus pruebas se ejecuten con el límite
  configurado temprano a través del entorno o del indicador para que
  se aplique durante el inicio e incluso durante cualquier paso de
  instalación que pueda invocar a Python para precompilar las fuentes
  ".py" a los archivos ".pyc".

### Configuración recomendada

Se espera que el valor predeterminado
"sys.int_info.default_max_str_digits" sea razonable para la mayoría de
las aplicaciones. Si su aplicación requiere un límite diferente,
configúrelo desde el punto de entrada principal mediante un código
independiente de la versión de Python, ya que estas API se agregaron
en versiones de parches de seguridad anteriores a la 3.12.

Por ejemplo:

   >>> import sys
   >>> if hasattr(sys, "set_int_max_str_digits"):
   ...     upper_bound = 68000
   ...     lower_bound = 4004
   ...     current_limit = sys.get_int_max_str_digits()
   ...     if current_limit == 0 or current_limit > upper_bound:
   ...         sys.set_int_max_str_digits(upper_bound)
   ...     elif current_limit < lower_bound:
   ...         sys.set_int_max_str_digits(lower_bound)

Si necesitas deshabilitarlo por completo, configúralo en "0".

-[ Notas al pie ]-

[1] Se puede consultar información adicional sobre estos métodos
    especiales en el manual de referencia de Python (Personalización
    básica).

[2] En consecuencia, la lista "[1, 2]" se considera igual que "[1.0,
    2.0]", y de forma similar para las tuplas.

[3] Deben haberlo hecho, ya que el analizador no puede decir el tipo
    de operandos.

[4] Los caracteres con versiones mayúsculas/minúsculas son aquellos
    cuya categoría general corresponde con "Lu" (Letra, Mayúscula),
    "Ll" (Letra, minúscula) o "Lt" (Letra, *titlecase*).

[5] Para formatear solo una tupla se debe, por tanto, usar una tupla
    conteniendo un único elemento, que sería la tupla a ser
    formateada.
