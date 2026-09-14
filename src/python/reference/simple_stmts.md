---
title: 7. Declaraciones simples
source_url: https://docs.python.org/es/3
source_path: reference/simple_stmts.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4840
---

# 7. Declaraciones simples

Una declaración simple se compone dentro de una sola línea lógica.
Pueden producirse varias declaraciones simples en una sola línea
separada por punto y coma.  La sintaxis de las declaraciones simples
es:

   simple_stmt: expression_stmt
                | assert_stmt
                | assignment_stmt
                | augmented_assignment_stmt
                | annotated_assignment_stmt
                | pass_stmt
                | del_stmt
                | return_stmt
                | yield_stmt
                | raise_stmt
                | break_stmt
                | continue_stmt
                | import_stmt
                | future_stmt
                | global_stmt
                | nonlocal_stmt
                | type_stmt

## 7.1. Declaraciones de tipo expresión

Las declaraciones de tipo expresión son usadas (en su mayoría
interactivamente) para computar y escribir un valor, o (usualmente)
para llamar a un método (una función que no retorna un resultado
significativo;  en Python, los métodos retornan el valor "None").
Otros usos de las declaraciones de tipo expresión son permitidas y
ocasionalmente útiles. La sintaxis para una declaración de tipo
expresión es:

   expression_stmt: starred_expression

Una declaración de tipo expresión evalúa la lista de expresiones (que
puede ser una única expresión).

En modo interactivo, si el valor no es "None", es convertido a cadena
de caracteres usando la función built-in "repr()" y la cadena
resultante es escrita en la salida estándar en una línea por si sola
(excepto si el resultado es "None", entonces el procedimiento llamado
no produce ninguna salida.)

## 7.2. Declaraciones de asignación

Las declaraciones de asignación son usadas para (volver a) unir
nombres a valores y para modificar atributos o elementos de objetos
mutables:

   assignment_stmt: (target_list "=")+ (starred_expression | yield_expression)
   target_list:     target ("," target)* [","]
   target:          identifier
                    | "(" [target_list] ")"
                    | "[" [target_list] "]"
                    | attributeref
                    | subscription
                    | "*" target

(See section Primarios for the syntax definitions for *attributeref*
and *subscription*.)

Una declaración de asignación evalúa la lista de expresiones (recuerda
que ésta puede ser una única expresión o una lista separada por comas,
la última produce una tupla) y asigna el único objeto resultante a
cada una de las listas de objetivos, de izquierda a derecha.

Assignment is defined recursively depending on the form of the target
(list). When a target is part of a mutable object (an attribute
reference or subscription), the mutable object must ultimately perform
the assignment and decide about its validity, and may raise an
exception if the assignment is unacceptable.  The rules observed by
various types and the exceptions raised are given with the definition
of the object types (see section Jerarquía de tipos estándar).

La asignación de un objeto a una lista de destino, opcionalmente entre
paréntesis o corchetes, se define de forma recursiva de la siguiente
manera.

* Si la lista de destino es un único objeto sin terminar en coma,
  opcionalmente entre paréntesis, el objeto es asignado a ese
  objetivo.

* Sino:

  * Si la lista de objetivos contiene un objetivo prefijado con un
    asterisco, llamado objetivo “destacado”: El objeto debe ser
    iterable con al menos tantos elementos como objetivos en la lista
    de objetivos, menos uno. Los primeros elementos del iterable se
    asignan, de izquierda a derecha, a los objetivos antes del
    objetivo destacado. Los elementos finales del iterable se asignan
    a los objetivos después del objetivo destacado. Luego se asigna
    una lista de los elementos restantes en el iterable al objetivo
    destacado (la lista puede estar vacía).

  * Sino: el objeto debe ser iterable con el mismo número de elementos
    que los elementos en la lista de objetivos, y los elementos son
    asignados a sus respectivos objetivos de izquierda a derecha.

La asignación de un objeto a un único objetivo se define a
continuación de manera recursiva.

* Si el objetivo es un identificador (nombre):

  * Si el nombre no ocurre en una declaración "global" o "nonlocal" en
    el actual bloque de código: el nombre es unido al objeto del
    actual espacio de nombres local.

  * Por otra parte: el nombre es unido al objeto en el nombre de
    espacio global o el nombre de espacio exterior determinado por
    "nonlocal", respectivamente.

  El nombre se vuelve a unir si ya ha estado unido. Esto puede hacer
  que el recuento de referencia para el objeto previamente vinculado
  al nombre llegue a cero, provocando que el objeto se desasigne y se
  llame a su destructor (si tiene uno).

* Si el destino es una referencia de atributo: se evalúa la expresión
  primaria en la referencia. Debe producir un objeto con atributos
  asignables; si este no es el caso, una excepción "TypeError" es
  lanzada.  Luego se le pide a ese objeto que asigne el objeto
  asignado al atributo dado; si no puede realizar la tarea, lanza una
  excepción (generalmente pero no necesariamente "AttributeError").

  Nota: Si el objeto es una instancia de clase y la referencia de
  atributo ocurre en ambos lados del operador de asignación, la
  expresión del lado derecho, "a.x" puede acceder a un atributo de
  instancia o (si no existe un atributo de instancia) a una clase
  atributo. El objetivo del lado izquierdo "a.x" siempre se establece
  como un atributo de instancia, creándolo si es necesario. Por lo
  tanto, las dos ocurrencias de "a.x" no necesariamente se refieren al
  mismo atributo: si la expresión del lado derecho se refiere a un
  atributo de clase, el lado izquierdo crea un nuevo atributo de
  instancia como el objetivo de la asignación:

     class Cls:
         x = 3             # class variable
     inst = Cls()
     inst.x = inst.x + 1   # writes inst.x as 4 leaving Cls.x as 3

  This description does not necessarily apply to descriptor
  attributes, such as properties created with "@property".

* If the target is a subscription: The primary expression in the
  reference is evaluated. Next, the subscript expression is evaluated.
  Then, the primary's "__setitem__()" method is called with two
  arguments: the subscript and the assigned object.

  Typically, "__setitem__()" is defined on mutable sequence objects
  (such as lists) and mapping objects (such as dictionaries), and
  behaves as follows.

  Si el primario es un objeto de secuencia mutable (como una lista),
  el subíndice debe producir un número entero. Si es negativo, se le
  suma la longitud de la secuencia. El valor resultante debe ser un
  número entero no negativo menor que la longitud de la secuencia, y
  se le pide a la secuencia que asigne el objeto asignado a su
  elemento con ese índice. Si el índice está fuera de rango,
  "IndexError" se lanza (la asignación a una secuencia suscrita no
  puede agregar nuevos elementos a una lista).

  If the primary is a mapping object (such as a dictionary), the
  subscript must have a type compatible with the mapping's key type,
  and the mapping is then asked to create a key/value pair which maps
  the subscript to the assigned object.  This can either replace an
  existing key/value pair with the same key value, or insert a new
  key/value pair (if no key with the same value existed).

  If the target is a slicing: The primary expression should evaluate
  to a mutable sequence object (such as a list). The assigned object
  should be *iterable*. The slicing's lower and upper bounds should be
  integers; if they are "None" (or not present), the defaults are zero
  and the sequence's length. If either bound is negative, the
  sequence's length is added to it.  The resulting bounds are clipped
  to lie between zero and the sequence's length, inclusive.  Finally,
  the sequence object is asked to replace the slice with the items of
  the assigned sequence.  The length of the slice may be different
  from the length of the assigned sequence, thus changing the length
  of the target sequence, if the target sequence allows it.

Aunque la definición de asignación implica que las superposiciones
entre el lado izquierdo y el lado derecho son ‘simultáneas’ (por
ejemplo, "a, b = b, a" intercambia dos variables), las superposiciones
*dentro* de la colección de las variables asignadas ocurren de
izquierda a derecha, lo que a veces genera confusión. Por ejemplo, el
siguiente programa imprime "[0, 2]":

   x = [0, 1]
   i = 0
   i, x[i] = 1, 2         # i is updated, then x[i] is updated
   print(x)

Ver también:

  **PEP 3132** - Desembalaje Iterable Extendido
     La especificación para la función "*target".

### 7.2.1. Declaraciones de asignación aumentada

La asignación aumentada es la combinación, en una sola declaración, de
una operación binaria y una declaración de asignación:

   augmented_assignment_stmt: augtarget augop (expression_list | yield_expression)
   augtarget:                 identifier | attributeref | subscription
   augop:                     "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
                              | ">>=" | "<<=" | "&=" | "^=" | "|="

(Ver sección Primarios para la definición de la sintaxis de los tres
últimos símbolos.)

Una asignación aumentada evalúa el destino (que, a diferencia de las
declaraciones de asignación normales, no puede ser un desempaquetado)
y la lista de expresiones, realiza la operación binaria específica del
tipo de asignación en los dos operandos y asigna el resultado al
destino original.  El objetivo sólo se evalúa una vez.

An augmented assignment statement like "x += 1" can be rewritten as "x
= x + 1" to achieve a similar, but not exactly equal effect. In the
augmented version, "x" is only evaluated once. Also, when possible,
the actual operation is performed *in-place*, meaning that rather than
creating a new object and assigning that to the target, the old object
is modified instead.

A diferencia de las asignaciones normales, las asignaciones aumentadas
evalúan el lado izquierdo *antes* de evaluar el lado derecho.  Por
ejemplo, "a[i] += f(x)" primero busca "a[i]", entonces evalúa "f(x)" y
realiza la suma, y finalmente, vuelve a escribir el resultado en
"a[i]".

Con la excepción de la asignación a tuplas y múltiples objetivos en
una sola instrucción, la asignación realizada por las instrucciones de
asignación aumentada se maneja de la misma manera que las asignaciones
normales. De manera similar, con la excepción del posible
comportamiento *in situ*, la operación binaria realizada por la
asignación aumentada es la misma que las operaciones binarias
normales.

Para destinos que son referencias a atributos, lo mismo que caveat
about class and instance attributes se aplica para asignaciones
regulares.

### 7.2.2. Declaraciones de asignación anotadas

Asignación *Annotation* es la combinación, en una única declaración,
de una variable o anotación de atributo y una declaración de
asignación opcional:

   annotated_assignment_stmt: augtarget ":" expression
                              ["=" (starred_expression | yield_expression)]

The difference from normal Declaraciones de asignación is that only a
single target is allowed.

The assignment target is considered "simple" if it consists of a
single name that is not enclosed in parentheses. For simple assignment
targets, if in class or module scope, the annotations are gathered in
a lazily evaluated annotation scope. The annotations can be evaluated
using the "__annotations__" attribute of a class or module, or using
the facilities in the "annotationlib" module.

If the assignment target is not simple (an attribute, subscript node,
or parenthesized name), the annotation is never evaluated.

Si se anota un nombre en el ámbito de una función, este nombre es
local para ese ámbito. Las anotaciones nunca se evalúan y almacenan en
ámbitos de función.

If the right hand side is present, an annotated assignment performs
the actual assignment as if there was no annotation present. If the
right hand side is not present for an expression target, then the
interpreter evaluates the target except for the last "__setitem__()"
or "__setattr__()" call.

Ver también:

  **PEP 526** - Sintaxis para anotaciones de variable
     La propuesta que agregó sintaxis para anotar los tipos de
     variables (incluidas variables de clase y variables de
     instancia), en lugar de expresarlas a través de comentarios.

  **PEP 484** - Indicadores de tipo
     La propuesta que agregó el módulo "typing" para proporcionar una
     sintaxis estándar para las anotaciones de tipo para ser
     utilizadas en herramientas de análisis estático e IDEs.

Distinto en la versión 3.8: Now annotated assignments allow the same
expressions in the right hand side as regular assignments. Previously,
some expressions (like un-parenthesized tuple expressions) caused a
syntax error.

Distinto en la versión 3.14: Annotations are now lazily evaluated in a
separate annotation scope. If the assignment target is not simple,
annotations are never evaluated.

## 7.3. La declaración "assert"

Las declaraciones de afirmación son una forma conveniente de insertar
afirmaciones de depuración en un programa:

   assert_stmt: "assert" expression ["," expression]

La forma simple, "assert expressionn", es equivalente a

   if __debug__:
       if not expression: raise AssertionError

La forma extendida, "assert expression1, expression2", es equivalente
a

   if __debug__:
       if not expression1: raise AssertionError(expression2)

These equivalences assume that "__debug__" and "AssertionError" refer
to the built-in variables with those names.  In the current
implementation, the built-in variable "__debug__" is "True" under
normal circumstances, "False" when optimization is requested (command
line option "-O").  The current code generator emits no code for an
"assert" statement when optimization is requested at compile time.
Note that it is unnecessary to include the source code for the
expression that failed in the error message; it will be displayed as
part of the stack trace.

Asignaciones a "__debug__" son ilegales.  El valor para la variable se
determina cuando arranca el intérprete.

## 7.4. La declaración "pass"

   pass_stmt: "pass"

"pass" es una operación nula --- cuando se ejecuta, no sucede nada. Es
útil como marcador de posición cuando se requiere una declaración
sintácticamente, pero no es necesario ejecutar código, por ejemplo:

   def f(arg): pass    # a function that does nothing (yet)

   class C: pass       # a class with no methods (yet)

## 7.5. La declaración "del"

   del_stmt: "del" target_list

La eliminación se define de forma recursiva de manera muy similar a la
forma en que se define la asignación. En lugar de explicarlo con todos
los detalles, aquí hay algunas sugerencias.

La eliminación de una lista de objetivos elimina cada objetivo de
forma recursiva, de izquierda a derecha.

Deletion of a name removes the binding of that name from the local or
global namespace, depending on whether the name occurs in a "global"
statement in the same code block.  Trying to delete an unbound name
raises a "NameError" exception.

Deletion of attribute references and subscriptions is passed to the
primary object involved; deletion of a slicing is in general
equivalent to assignment of an empty slice of the right type (but even
this is determined by the sliced object).

Distinto en la versión 3.2: Anteriormente era ilegal eliminar un
nombre del espacio de nombres local si aparece como una variable libre
en un bloque anidado.

## 7.6. La declaración "return"

   return_stmt: "return" [expression_list]

El "return" sólo puede ocurrir sintácticamente anidado en una
definición de función, no dentro de una definición de clase anidada.

Si una lista de expresiones es presente, ésta es evaluada, sino es
substituida por "None" .

"return" deja la llamada a la función actual con la lista de
expresiones (o "None") como valor de retorno.

Cuando "return" pasa el control de una sentencia "try" con una
cláusula "finally", esa cláusula "finally" se ejecuta antes de dejar
realmente la función.

En una función generadora, la declaración "return" indica que el
generador ha acabado y hará que "StopIteration" se lance. El valor
retornado (si lo hay) se utiliza como argumento para construir
"StopIteration" y se convierte en el atributo "StopIteration.value".

En una función de generador asíncrono, una declaración "return" vacía
indica que el generador asíncrono ha acabado y va a lanzar un
"StopAsyncIteration".  Una declaración "return" no vacía es un error
de sintaxis en una función generadora asíncrona.

## 7.7. La declaración "yield"

   yield_stmt: yield_expression

A "yield" statement is semantically equivalent to a yield expression.
The "yield" statement can be used to omit the parentheses that would
otherwise be required in the equivalent yield expression statement.
For example, the yield statements

   yield <expr>
   yield from <expr>

son equivalentes a las funciones que producen declaraciones

   (yield <expr>)
   (yield from <expr>)

Yield expressions and statements are only used when defining a
*generator* function, and are only used in the body of the generator
function.  Using "yield" in a function definition is sufficient to
cause that definition to create a generator function instead of a
normal function.

Para todos los detalles de la semántica de "yield", referirse a la
sección Expresiones yield.

## 7.8. La declaración "raise"

   raise_stmt: "raise" [expression ["from" expression]]

Si no hay expresiones presentes, "raise" vuelve a lanzar la excepción
que se está manejando actualmente, que también se conoce como
*excepción activa*. Si actualmente no hay una excepción activa, se
lanza una excepción "RuntimeError" que indica que se trata de un
error.

De lo contrario, "raise" evalúa la primera expresión como el objeto de
excepción.  Debe ser una subclase o una instancia de "BaseException".
Si es una clase, la instancia de excepción se obtendrá cuando sea
necesario creando una instancia de la clase sin argumentos.

El *type* de la excepción es la instancia de la clase excepción, el
*value* es la propia instancia.

A traceback object is normally created automatically when an exception
is raised and attached to it as the "__traceback__" attribute. You can
create an exception and set your own traceback in one step using the
"with_traceback()" exception method (which returns the same exception
instance, with its traceback set to its argument), like so:

   raise Exception("foo occurred").with_traceback(tracebackobj)

The "from" clause is used for exception chaining: if given, the second
*expression* must be another exception class or instance. If the
second expression is an exception instance, it will be attached to the
raised exception as the "__cause__" attribute (which is writable). If
the expression is an exception class, the class will be instantiated
and the resulting exception instance will be attached to the raised
exception as the "__cause__" attribute. If the raised exception is not
handled, both exceptions will be printed:

   >>> try:
   ...     print(1 / 0)
   ... except Exception as exc:
   ...     raise RuntimeError("Something bad happened") from exc
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       print(1 / 0)
             ~~^~~
   ZeroDivisionError: division by zero

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError("Something bad happened") from exc
   RuntimeError: Something bad happened

A similar mechanism works implicitly if a new exception is raised when
an exception is already being handled.  An exception may be handled
when an "except" or "finally" clause, or a "with" statement, is used.
The previous exception is then attached as the new exception's
"__context__" attribute:

   >>> try:
   ...     print(1 / 0)
   ... except:
   ...     raise RuntimeError("Something bad happened")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       print(1 / 0)
             ~~^~~
   ZeroDivisionError: division by zero

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError("Something bad happened")
   RuntimeError: Something bad happened

Exception chaining can be explicitly suppressed by specifying "None"
in the "from" clause:

   >>> try:
   ...     print(1 / 0)
   ... except:
   ...     raise RuntimeError("Something bad happened") from None
   ...
   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
   RuntimeError: Something bad happened

Se puede encontrar información adicional sobre excepciones en la
sección Excepciones, e información sobre manejo de excepciones en la
sección La sentencia try.

Distinto en la versión 3.3: "None" ahora es permitido como "Y" en
"raise X from Y".Added the "__suppress_context__" attribute to
suppress automatic display of the exception context.

Distinto en la versión 3.11: Si el rastreo de la excepción activa se
modifica en una cláusula "except", una instrucción "raise" posterior
vuelve a generar la excepción con el rastreo modificado.
Anteriormente, la excepción se volvía a generar con el rastreo que
tenía cuando se detectó.

## 7.9. La declaración "break"

   break_stmt: "break"

"break" solo puede ocurrir sintácticamente anidado en un bucle "for" o
"while", pero no anidado en una función o definición de clase dentro
de ese bucle.

Termina el bucle adjunto más cercano, omitiendo la cláusula "else"
opcional si el bucle tiene una.

Si un bucle "for" es terminado por "break", el objetivo de control de
bucle mantiene su valor actual.

Cuando "break" pasa el control de una sentencia "try" con una cláusula
"finally", esa cláusula "finally" se ejecuta antes de dejar realmente
el bucle.

## 7.10. La declaración "continue"

   continue_stmt: "continue"

"continue" sólo puede ocurrir sintácticamente anidado en el ciclo
"for" o "while", pero no anidado en una función o definición de clase
dentro de ese ciclo.  Continúa con la siguiente iteración del bucle
envolvente más cercano.

Cuando "continue" pasa el control de una sentencia "try" con una
cláusula "finally", esa cláusula "finally" se ejecuta antes de empezar
realmente el siguiente ciclo del bucle.

## 7.11. La declaración "import"

   import_stmt:     "import" module ["as" identifier] ("," module ["as" identifier])*
                    | "from" relative_module "import" identifier ["as" identifier]
                    ("," identifier ["as" identifier])*
                    | "from" relative_module "import" "(" identifier ["as" identifier]
                    ("," identifier ["as" identifier])* [","] ")"
                    | "from" relative_module "import" "*"
   module:          (identifier ".")* identifier
   relative_module: "."* module | "."+

La declaración básica de importación (sin la cláusula "from") es
ejecutada en 2 pasos:

1. encontrar un módulo, cargarlo e inicializarlo en caso de ser
   necesario

2. define a name or names in the current namespace for the scope where
   the "import" statement occurs, just as an assignment statement
   would (including "global" and "nonlocal" semantics).

Cuando la declaración contiene varias cláusulas (separadas por comas),
los dos pasos se llevan a cabo por separado para cada cláusula, como
si las cláusulas se hubieran separado en declaraciones de importación
individuales.

The details of the first step, finding and loading modules, are
described in greater detail in the section on the import system, which
also describes the various types of packages and modules that can be
imported, as well as all the hooks that can be used to customize the
import system. Note that failures in this step may indicate either
that the module could not be located, *or* that an error occurred
while initializing the module, which includes execution of the
module's code.

Si el módulo solicitado se recupera correctamente, estará disponible
en el espacio de nombres local de una de estas tres formas:

* Si el nombre del módulo va seguido de "as`", entonces el nombre
  siguiente "as" está vinculado directamente al módulo importado.

* Si no se especifica ningún otro nombre y el módulo que se está
  importando es un módulo de nivel superior, el nombre del módulo se
  enlaza en el espacio de nombres local como una referencia al módulo
  importado

* Si el módulo que se está importando *no* es un módulo de nivel
  superior, entonces el nombre del paquete de nivel superior que
  contiene el módulo se enlaza en el espacio de nombres local como una
  referencia al paquete de nivel superior. Se debe acceder al módulo
  importado utilizando su nombre calificado completo en lugar de
  directamente

La forma "from" usa un complejo un poco más complicado:

1. encuentra el módulo especificado en la cláusula "from", cargando e
   inicializándolo si es necesario;

2. para cada uno de los identificadores especificados en la cláusula
   "import":

   1. compruebe si el módulo importado tiene un atributo con ese
      nombre

   2. de lo contrario, intente importar un submódulo con ese nombre y
      luego verifique el módulo importado nuevamente para ese atributo

   3. si el atributo no se encuentra, "ImportError" es lanzada.

   4. otherwise, a reference to that value is stored in the current
      namespace, using the name in the "as" clause if it is present,
      otherwise using the attribute name

Ejemplos:

   import foo                 # foo imported and bound locally
   import foo.bar.baz         # foo, foo.bar, and foo.bar.baz imported, foo bound locally
   import foo.bar.baz as fbb  # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as fbb
   from foo.bar import baz    # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as baz
   from foo import attr       # foo imported and foo.attr bound as attr

Si la lista de identificadores se reemplaza por una estrella ("’*’"),
todos los nombres públicos definidos en el módulo se enlazan en el
espacio de nombres local para el ámbito donde ocurre la declaración
"import".

The *public names* defined by a module are determined by checking the
module's namespace for a variable named "__all__"; if defined, it must
be a sequence of strings which are names defined or imported by that
module. Names containing non-ASCII characters must be in the
normalization form NFKC; see Non-ASCII characters in names for
details.  The names given in "__all__" are all considered public and
are required to exist.  If "__all__" is not defined, the set of public
names includes all names found in the module's namespace which do not
begin with an underscore character ("'_'").  "__all__" should contain
the entire public API. It is intended to avoid accidentally exporting
items that are not part of the API (such as library modules which were
imported and used within the module).

La forma de importación comodín --- "from module import *" --- sólo se
permite a nivel módulo.  Intentar usarlo en una definición de clase o
función lanza una "SyntaxError".

Al especificar qué módulo importar, no es necesario especificar el
nombre absoluto del módulo. Cuando un módulo o paquete está contenido
dentro de otro paquete, es posible realizar una importación relativa
dentro del mismo paquete superior sin tener que mencionar el nombre
del paquete. Al usar puntos iniciales en el módulo o paquete
especificado después de "from", puede especificar qué tan alto
recorrer la jerarquía actual del paquete sin especificar nombres
exactos. Un punto inicial significa el paquete actual donde existe el
módulo que realiza la importación. Dos puntos significan un nivel de
paquete. Tres puntos son dos niveles, etc. Entonces, si ejecuta "from
. import mod" de un módulo en el paquete "pkg" terminará importando
"pkg.mod". Si ejecuta "from ..subpkg2 import mod" desde dentro de
"pkg.subpkg1", importará "pkg.subpkg2.mod". La especificación para las
importaciones relativas está contenida en la sección Paquete
Importaciones relativas.

"importlib.import_module()" se proporciona para soportar aplicaciones
que determinan dinámicamente los módulos a cargar.

Lanza un auditing event "import" con argumentos "module", "filename",
"sys.path", "sys.meta_path", "sys.path_hooks".

### 7.11.1. Declaraciones Futuras

Una *future statement* es una directiva para el compilador para
indicar que un módulo en particular debe compilarse usando la sintaxis
o semántica que estará disponible en una versión futura específica de
Python donde la característica se convierte en estándar.

La declaración futura está destinada a facilitar la migración a
futuras versiones de Python que introducen cambios incompatibles en el
lenguaje.  Permite el uso de las nuevas funciones por módulo antes del
lanzamiento en el que la función se convierte en estándar.

   future_stmt: "from" "__future__" "import" feature ["as" identifier]
                ("," feature ["as" identifier])*
                | "from" "__future__" "import" "(" feature ["as" identifier]
                ("," feature ["as" identifier])* [","] ")"
   feature:     identifier

Una declaración futura debe aparecer cerca de la parte superior del
módulo. Las únicas líneas que pueden aparecer antes de una declaración
futura son:

* el docstring del módulo (si hay),

* comentarios,

* lineas en blanco, y

* otras declaraciones futuras.

La única característica en Python 3.7 que requiere el uso la
declaración futuro es "annotations".

108/5000 Python 3 aún reconoce todas las características históricas
habilitadas por la declaración futura. La lista incluye
"absolute_import", "division", "generators", "generator_stop",
"unicode_literals", "print_function", "nested_scopes" y
"with_statement". Todos son redundantes porque siempre están
habilitados y solo se conservan para compatibilidad con versiones
anteriores.

Una declaración futura se reconoce y se trata especialmente en el
momento de la compilación: los cambios en la semántica de las
construcciones centrales a menudo se implementan generando código
diferente. Incluso puede darse el caso de que una nueva característica
introduzca una nueva sintaxis incompatible (como una nueva palabra
reservada), en cuyo caso el compilador puede necesitar analizar el
módulo de manera diferente. Tales decisiones no pueden postergarse
hasta el tiempo de ejecución.

Para cualquier versión dada, el compilador sabe qué nombres de
características se han definido y lanza un error en tiempo de
compilación si una declaración futura contiene una característica que
no conoce.

La semántica del tiempo de ejecución directo es la misma que para
cualquier declaración de importación: hay un módulo estándar
"__future__", que se describe más adelante, y se importará de la forma
habitual en el momento en que se ejecute la declaración futura.

La interesante semántica del tiempo de ejecución depende de la
característica específica habilitada por la declaración futura.

Notar que no hay nada especial a cerca de la declaración:

   import __future__ [as name]

Esa no es una declaración futura; es una declaración de importación
ordinaria sin restricciones especiales de semántica o sintaxis.

Code compiled by calls to the built-in functions "exec()" and
"compile()" that occur in a module "M" containing a future statement
will, by default, use the new syntax or semantics associated with the
future statement.  This can be controlled by optional arguments to
"compile()" --- see the documentation of that function for details.

Una declaración futura escrita en una prompt interactiva del
intérprete entrará en vigencia durante el resto de la sesión de dicho
intérprete.  Si un intérprete se inicia con la opción "-i", se le pasa
un nombre de script para ejecutar, y el script incluye una declaración
futura, ésta estará en efecto en la sesión interactiva iniciada
después de que se ejecute el script.

Ver también:

  **PEP 236** - Vuelta al __future__
     La propuesta original para el mecanismo __future__.

## 7.12. La declaración "global"

   global_stmt: "global" identifier ("," identifier)*

The "global" statement causes the listed identifiers to be interpreted
as globals. It would be impossible to assign to a global variable
without "global", although free variables may refer to globals without
being declared global.

The "global" statement applies to the entire current scope (module,
function body or class definition). A "SyntaxError" is raised if a
variable is used or assigned to prior to its global declaration in the
scope.

At the module level, all variables are global, so a "global" statement
has no effect. However, variables must still not be used or assigned
to prior to their "global" declaration. This requirement is relaxed in
the interactive prompt (*REPL*).

** Nota del programador: ** "global" es una directiva para el
analizador.  Se aplica solo al código analizado al mismo tiempo que la
declaración "global". En particular, una declaración "global"
contenida en una cadena u objeto de código suministrado a la función
incorporada "exec()" no afecta el bloque de código *que contiene* la
llamada a la función, y el código contenido en dicha función una
cadena no se ve afectada por la declaración "global" en el código que
contiene la llamada a la función.  Lo mismo se aplica a las funciones
"eval()" y "compile()".

## 7.13. La declaración "nonlocal"

   nonlocal_stmt: "nonlocal" identifier ("," identifier)*

When the definition of a function or class is nested (enclosed) within
the definitions of other functions, its nonlocal scopes are the local
scopes of the enclosing functions. The "nonlocal" statement causes the
listed identifiers to refer to names previously bound in nonlocal
scopes. It allows encapsulated code to rebind such nonlocal
identifiers.  If a name is bound in more than one nonlocal scope, the
nearest binding is used. If a name is not bound in any nonlocal scope,
or if there is no nonlocal scope, a "SyntaxError" is raised.

The "nonlocal" statement applies to the entire scope of a function or
class body. A "SyntaxError" is raised if a variable is used or
assigned to prior to its nonlocal declaration in the scope.

Ver también:

  **PEP 3104** - Acceso a Nombres de Ámbitos externos
     La especificación para la declaración "nonlocal".

**Programmer's note:** "nonlocal" is a directive to the parser and
applies only to code parsed along with it.  See the note for the
"global" statement.

## 7.14. The "type" statement

   type_stmt: 'type' identifier [type_params] "=" expression

The "type" statement declares a type alias, which is an instance of
"typing.TypeAliasType".

For example, the following statement creates a type alias:

   type Point = tuple[float, float]

This code is roughly equivalent to:

   annotation-def VALUE_OF_Point():
       return tuple[float, float]
   Point = typing.TypeAliasType("Point", VALUE_OF_Point())

"annotation-def" indicates an annotation scope, which behaves mostly
like a function, but with several small differences.

The value of the type alias is evaluated in the annotation scope. It
is not evaluated when the type alias is created, but only when the
value is accessed through the type alias's "__value__" attribute (see
Evaluación perezosa). This allows the type alias to refer to names
that are not yet defined.

Type aliases may be made generic by adding a type parameter list after
the name. See Alias de tipo genérico for more.

"type" is a soft keyword.

Added in version 3.12.

Ver también:

  **PEP 695** - Type Parameter Syntax
     Introduced the "type" statement and syntax for generic classes
     and functions.
