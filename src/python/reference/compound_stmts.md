---
title: 8. Sentencias compuestas
source_url: https://docs.python.org/es/3
source_path: reference/compound_stmts.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: reference
order: 4750
---

# 8. Sentencias compuestas

Las sentencias compuestas contienen (grupos de) otras sentencias;
estas afectan o controlan la ejecución de esas otras sentencias de
alguna manera. En general, las sentencias compuestas abarcan varias
líneas, aunque en representaciones simples una sentencia compuesta
completa puede estar contenida en una línea.

Las sentencias "if", "while" y "for" implementan construcciones de
control de flujo tradicionales. "try" especifica gestores de excepción
o código de limpieza para un grupo de sentencias, mientras que las
sentencias "with" permite la ejecución del código de inicialización y
finalización alrededor de un bloque de código. Las definiciones de
función y clase también son sentencias sintácticamente compuestas.

Una sentencia compuesta consta de una o más 'cláusulas'. Una cláusula
consta de un encabezado y una 'suite'. Los encabezados de cláusula de
una declaración compuesta particular están todos en el mismo nivel de
indentación. Cada encabezado de cláusula comienza con una palabra
clave de identificación única y termina con dos puntos. Una suite es
un grupo de sentencias controladas por una cláusula. Una suite puede
ser una o más sentencias simples separadas por punto y coma en la
misma línea como el encabezado, siguiendo los dos puntos del
encabezado, o puede ser una o puede ser una o más declaraciones
indentadas en líneas posteriores. Solo la última forma de una suite
puede contener sentencias compuestas anidadas; lo siguiente es ilegal,
principalmente porque no estaría claro a qué cláusula "if" seguido de
la cláusula "else" hace referencia:

   if test1: if test2: print(x)

También tenga en cuenta que el punto y coma se une más apretado que
los dos puntos en este contexto, de modo que en el siguiente ejemplo,
todas o ninguna de las llamadas "print()" se ejecutan:

   if x < y < z: print(x); print(y); print(z)

Resumiendo:

   compound_stmt: if_stmt
                  | while_stmt
                  | for_stmt
                  | try_stmt
                  | with_stmt
                  | match_stmt
                  | funcdef
                  | classdef
                  | async_with_stmt
                  | async_for_stmt
                  | async_funcdef
   suite:         stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
   statement:     stmt_list NEWLINE | compound_stmt
   stmt_list:     simple_stmt (";" simple_stmt)* [";"]

Tenga en cuenta que las sentencias siempre terminan en un "NEWLINE"
posiblemente seguida de "DEDENT". También tenga en cuenta que las
cláusulas de continuación opcionales siempre comienzan con una palabra
clave que no puede iniciar una sentencia, por lo tanto, no hay
ambigüedades (el problema de 'colgado "if"' se resuelve en Python al
requerir que las sentencias anidadas "if" deben estar indentadas).

El formato de las reglas gramaticales en las siguientes secciones
coloca cada cláusula en una línea separada para mayor claridad.

## 8.1. La sentencia "if"

La sentencia "if" se usa para la ejecución condicional:

   if_stmt: "if" assignment_expression ":" suite
            ("elif" assignment_expression ":" suite)*
            ["else" ":" suite]

Selecciona exactamente una de las suites evaluando las expresiones una
por una hasta que se encuentre una verdadera (vea la sección
Operaciones booleanas para la definición de verdadero y falso);
entonces esa suite se ejecuta (y ninguna otra parte de la sentencia
"if" se ejecuta o evalúa). Si todas las expresiones son falsas, se
ejecuta la suite de cláusulas "else", si está presente.

## 8.2. La sentencia "while"

La sentencia "while" se usa para la ejecución repetida siempre que una
expresión sea verdadera:

   while_stmt: "while" assignment_expression ":" suite
               ["else" ":" suite]

Esto prueba repetidamente la expresión y, si es verdadera, ejecuta la
primera suite; si la expresión es falsa (que puede ser la primera vez
que se prueba), se ejecuta el conjunto de cláusulas "else", si está
presente, y el bucle termina.

La sentencia "break" ejecutada en la primer suite termina el bucle sin
ejecutar la suite de cláusulas "else". La sentencia "continue"
ejecutada en la primera suite omite el resto de la suite y vuelve a
probar la expresión.

## 8.3. La sentencia "for"

La sentencia "for" se usa para iterar sobre los elementos de una
secuencia (como una cadena de caracteres, tupla o lista) u otro objeto
iterable:

   for_stmt: "for" target_list "in" starred_expression_list ":" suite
             ["else" ":" suite]

The "starred_expression_list" expression is evaluated once; it should
yield an *iterable* object. An *iterator* is created for that
iterable. The first item provided by the iterator is then assigned to
the target list using the standard rules for assignments (see
Declaraciones de asignación), and the suite is executed. This repeats
for each item provided by the iterator. When the iterator is
exhausted, the suite in the "else" clause, if present, is executed,
and the loop terminates.

La sentencia "break" ejecutada en la primera suite termina el bucle
sin ejecutar el conjunto de cláusulas "else". La sentencia "continue"
ejecutada en la primera suite omite el resto de las cláusulas y
continúa con el siguiente elemento, o con la cláusula "else" si no hay
un elemento siguiente.

El bucle "for" realiza asignaciones a las variables en la lista. Esto
sobrescribe todas las asignaciones anteriores a esas variables,
incluidas las realizadas en la suite del bucle "for":

   for i in range(10):
       print(i)
       i = 5             # this will not affect the for-loop
                         # because i will be overwritten with the next
                         # index in the range

Los nombres en la lista no se eliminan cuando finaliza el bucle, pero
si la secuencia está vacía, el bucle no les habrá asignado nada.
Sugerencia: el tipo incorporado "range()" representa secuencias
aritméticas inmutables de números enteros; por ejemplo, iterar sobre
"range(3)" genera sucesivamente 0, 1, y luego 2.

Distinto en la versión 3.11: Los elementos destacados ahora están
permitidos en la lista de expresiones.

## 8.4. La sentencia "try"

La sentencia "try" especifica controladores de excepciones y/o código
de limpieza para un grupo de sentencias:

   try_stmt:  try1_stmt | try2_stmt | try3_stmt
   try1_stmt: "try" ":" suite
              ("except" [expression ["as" identifier]] ":" suite)+
              ["else" ":" suite]
              ["finally" ":" suite]
   try2_stmt: "try" ":" suite
              ("except" "*" expression ["as" identifier] ":" suite)+
              ["else" ":" suite]
              ["finally" ":" suite]
   try3_stmt: "try" ":" suite
              "finally" ":" suite

Se puede encontrar información adicional sobre las excepciones en la
sección Excepciones, e información sobre el uso de la sentencia
"raise", para lanzar excepciones se puede encontrar en la sección La
declaración raise.

Distinto en la versión 3.14: Support for optionally dropping grouping
parentheses when using multiple exception types. See **PEP 758**.

### 8.4.1. Cláusula "except"

Las cláusulas "except" especifican uno o más controladores de
excepciones. Cuando no se produce ninguna excepción en la cláusula
"try", no se ejecuta ningún controlador de excepciones. Cuando ocurre
una excepción en la suite "try", se inicia una búsqueda de un
controlador de excepciones. Esta búsqueda inspecciona las cláusulas
"except" a su vez hasta que se encuentra una que coincida con la
excepción. Una cláusula "except" sin expresión, si está presente, debe
ser la última; coincide con cualquier excepción.

For an "except" clause with an expression, the expression must
evaluate to an exception type or a tuple of exception types.
Parentheses can be dropped if multiple exception types are provided
and the "as" clause is not used. The raised exception matches an
"except" clause whose expression evaluates to the class or a *non-
virtual base class* of the exception object, or to a tuple that
contains such a class.

Si ninguna cláusula "except" coincide con la excepción, la búsqueda de
un controlador de excepciones continúa en el código circundante y en
la pila de invocaciones. [1]

Si la evaluación de una expresión en el encabezado de una cláusula
"except" genera una excepción, la búsqueda original de un controlador
se cancela y comienza una búsqueda de la nueva excepción en el código
circundante y en la pila de llamadas (se trata como si toda la
sentencia "try" generara la excepción).

Cuando se encuentra una cláusula "except" coincidente, la excepción se
asigna al destino especificado después de la palabra clave "as" en esa
cláusula "except", si está presente, y se ejecuta el conjunto de la
cláusula "except". Todas las cláusulas "except" deben tener un bloque
ejecutable. Cuando se alcanza el final de este bloque, la ejecución
continúa normalmente después de la instrucción "try" completa. (Esto
significa que si existen dos controladores anidados para la misma
excepción y la excepción se produce en la cláusula "try" del
controlador interno, el controlador externo no controlará la
excepción).

When an exception has been assigned using "as target", it is cleared
at the end of the "except" clause.  This is as if:

   except E as N:
       foo

was translated to:

   except E as N:
       try:
           foo
       finally:
           del N

Esto significa que la excepción debe asignarse a un nombre diferente
para poder hacer referencia a ella después de la cláusula "except".
Las excepciones se borran porque con el rastreo adjunto, forman un
ciclo de referencia con el marco de la pila, manteniendo todos los
locales en ese marco vivos hasta que ocurra la próxima recolección de
elementos no utilizados.

Antes de que se ejecute el conjunto de una cláusula "except" , la
excepción se almacena en el módulo "sys", donde puede ser accesible
desde dentro del cuerpo de la cláusula "except" llamando a la
"sys.excepcion()". Cuando se sale de un *handler* de excepciones, la
excepción almacenada en el módulo "sys" se restablece a su valor
anterior:

   >>> print(sys.exception())
   None
   >>> try:
   ...     raise TypeError
   ... except:
   ...     print(repr(sys.exception()))
   ...     try:
   ...          raise ValueError
   ...     except:
   ...         print(repr(sys.exception()))
   ...     print(repr(sys.exception()))
   ...
   TypeError()
   ValueError()
   TypeError()
   >>> print(sys.exception())
   None

### 8.4.2. Cláusula "except*"

The "except*" clause(s) specify one or more handlers for groups of
exceptions ("BaseExceptionGroup" instances). A "try" statement can
have either "except" or "except*" clauses, but not both. The exception
type for matching is mandatory in the case of "except*", so "except*:"
is a syntax error. The type is interpreted as in the case of "except",
but matching is performed on the exceptions contained in the group
that is being handled. A "TypeError" is raised if a matching type is a
subclass of "BaseExceptionGroup", because that would have ambiguous
semantics.

When an exception group is raised in the try block, each "except*"
clause splits (see "split()") it into the subgroups of matching and
non-matching exceptions. If the matching subgroup is not empty, it
becomes the handled exception (the value returned from
"sys.exception()") and assigned to the target of the "except*" clause
(if there is one). Then, the body of the "except*" clause executes. If
the non-matching subgroup is not empty, it is processed by the next
"except*" in the same manner. This continues until all exceptions in
the group have been matched, or the last "except*" clause has run.

After all "except*" clauses execute, the group of unhandled exceptions
is merged with any exceptions that were raised or re-raised from
within "except*" clauses. This merged exception group propagates on:

   >>> try:
   ...     raise ExceptionGroup("eg",
   ...         [ValueError(1), TypeError(2), OSError(3), OSError(4)])
   ... except* TypeError as e:
   ...     print(f'caught {type(e)} with nested {e.exceptions}')
   ... except* OSError as e:
   ...     print(f'caught {type(e)} with nested {e.exceptions}')
   ...
   caught <class 'ExceptionGroup'> with nested (TypeError(2),)
   caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
     + Exception Group Traceback (most recent call last):
     |   File "<doctest default[0]>", line 2, in <module>
     |     raise ExceptionGroup("eg",
     |         [ValueError(1), TypeError(2), OSError(3), OSError(4)])
     | ExceptionGroup: eg (1 sub-exception)
     +-+---------------- 1 ----------------
       | ValueError: 1
       +------------------------------------

If the exception raised from the "try" block is not an exception group
and its type matches one of the "except*" clauses, it is caught and
wrapped by an exception group with an empty message string. This
ensures that the type of the target "e" is consistently
"BaseExceptionGroup":

   >>> try:
   ...     raise BlockingIOError
   ... except* BlockingIOError as e:
   ...     print(repr(e))
   ...
   ExceptionGroup('', (BlockingIOError(),))

"break", "continue" and "return" cannot appear in an "except*" clause.

### 8.4.3. La sentencia "else"

La cláusula opcional "else" se ejecuta si el flujo de control sale de
la suite "try", no se produjo ninguna excepción, y no se ejecutó la
sentencia "return", "continue" o "break". Las excepciones en la
cláusula "else" no se gestionaron con las cláusulas precedentes
"except".

### 8.4.4. Cláusula "finally"

If "finally" is present, it specifies a 'cleanup' handler.  The "try"
clause is executed, including any "except" and "else" clauses. If an
exception occurs in any of the clauses and is not handled, the
exception is temporarily saved. The "finally" clause is executed.  If
there is a saved exception it is re-raised at the end of the "finally"
clause. If the "finally" clause raises another exception, the saved
exception is set as the context of the new exception. If the "finally"
clause executes a "return", "break" or "continue" statement, the saved
exception is discarded. For example, this function returns 42.

   def f():
       try:
           1/0
       finally:
           return 42

La información de excepción no está disponible para el programa
durante la ejecución de la cláusula "finally".

Cuando se ejecuta una sentencia "return", "break" o "continue" en el
conjunto "try" de una sentencia "try"..."finally", la cláusula
"finally" también se ejecuta 'al salir'.

The return value of a function is determined by the last "return"
statement executed.  Since the "finally" clause always executes, a
"return" statement executed in the "finally" clause will always be the
last one executed. The following function returns 'finally'.

   def foo():
       try:
           return 'try'
       finally:
           return 'finally'

Distinto en la versión 3.8: Antes de Python 3.8, una declaración
"continue" era ilegal en la cláusula "finally" debido a un problema
con la implementación.

Distinto en la versión 3.14: The compiler emits a "SyntaxWarning" when
a "return", "break" or "continue" appears in a "finally" block (see
**PEP 765**).

## 8.5. La sentencia "with"

La sentencia "with" se usa para ajustar la ejecución de un bloque con
métodos definidos por un administrador de contexto (ver sección
Gestores de Contexto en la Declaración with). Esto permite que los
patrones de uso comunes "try"..."except"..."finally" se encapsulen
para una reutilización conveniente.

   with_stmt:          "with" ( "(" with_stmt_contents ","? ")" | with_stmt_contents ) ":" suite
   with_stmt_contents: with_item ("," with_item)*
   with_item:          expression ["as" target]

La ejecución de la sentencia "with" con un "item" se realiza de la
siguiente manera:

1. La expresión de contexto (la expresión dada en "with_item") se
   evalúa para obtener un administrador de contexto.

2. El administrador de contexto "__enter__()" se carga para su uso
   posterior.

3. El administrador de contexto "__exit__()" se carga para su uso
   posterior.

4. Se invoca el método "__enter__()" del administrador de contexto.

5. Si se incluyó el destino en la declaración "with", se le asigna el
   valor de retorno de "__enter__()".

   Nota:

     La declaración "with" garantiza que si el método "__enter__()"
     regresa sin error, entonces siempre se llamará a "__exit__()".
     Por lo tanto, si se produce un error durante la asignación a la
     lista de destino, se trataría de la misma manera que si el error
     ocurriera dentro del suite. Consulte el paso 7 a continuación.

6. La suite se ejecuta.

7. Se invoca el método "__exit__()" del administrador de contexto. Si
   una excepción causó la salida de la suite, su tipo, valor y rastreo
   se pasan como argumentos a "__exit__()". De lo contrario, se
   proporcionan tres argumentos "None".

   Si se salió de la suite debido a una excepción, y el valor de
   retorno del método "__exit__()" fue falso, la excepción se vuelve a
   plantear. Si el valor de retorno era verdadero, la excepción se
   suprime y la ejecución continúa con la declaración que sigue a la
   declaración "with".

   Si se salió de la suite por cualquier motivo que no sea una
   excepción, el valor de retorno de "__exit__()" se ignora y la
   ejecución continúa en la ubicación normal para el tipo de salida
   que se tomó.

El siguiente código:

   with EXPRESSION as TARGET:
       SUITE

es semánticamente equivalente a:

   manager = (EXPRESSION)
   enter = manager.__enter__
   exit = manager.__exit__
   value = enter()
   hit_except = False

   try:
       TARGET = value
       SUITE
   except:
       hit_except = True
       if not exit(*sys.exc_info()):
           raise
   finally:
       if not hit_except:
           exit(None, None, None)

except that implicit special method lookup is used for "__enter__()"
and "__exit__()".

Con más de un elemento, los administradores de contexto se procesan
como si varias sentencias "with" estuvieran anidadas:

   with A() as a, B() as b:
       SUITE

es semánticamente equivalente a:

   with A() as a:
       with B() as b:
           SUITE

También puedes escribir administradores de contexto de múltiples ítems
en múltiples lineas si los ítems están entre paréntesis. Por ejemplo:

   with (
       A() as a,
       B() as b,
   ):
       SUITE

Distinto en la versión 3.1: Soporte para múltiples expresiones de
contexto.

Distinto en la versión 3.10: Soporte para el uso de paréntesis de
agrupación para separar la declaración en múltiples líneas.

Ver también:

  **PEP 343** - La sentencia "with"
     La especificación, antecedentes y ejemplos de la sentencia de
     Python "with".

## 8.6. La sentencia "match"

Added in version 3.10.

La declaración match es usada para coincidencia de patrones.
Sintaxis:

   match_stmt:   'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
   subject_expr: flexible_expression "," [flexible_expression_list [',']]
                 | assignment_expression
   case_block:   'case' patterns [guard] ":" suite

Nota:

  Esta sección utiliza comillas simples para denotar las palabras
  clave suaves.

La coincidencia de patrones toma un patrón como entrada (delante de
"case") y un valor de búsqueda (delante de "match").  El patrón (que
puede contener subpatrones) es comparado con el valor de búsqueda.
Los resultados son:

* Una coincidencia exitosa o fallida (también llamada éxito o fracaso
  de un patrón).

* Una posible vinculación de los valores coincidentes con un nombre.
  Los requisitos previos para esto se discuten abajo.

Las palabras clave "match" y "case" son palabras clave suaves.

Ver también:

  * **PEP 634** -- Coincidencia de patrones estructurales:
    Especificación

  * **PEP 636** -- Coincidencia de patrones estructurales: Tutorial

### 8.6.1. Resumen

A continuación, un resumen del flujo lógico de una declaración de
coincidencia:

1. Se evalúa la expresión "subject_expr" y se obtiene un valor sujeto
   resultante. Si la expresión contiene una coma, se construye una
   tupla utilizando las reglas estándar.

2. Se intenta coincidir cada patrón en un "case_block" con el valor
   sujeto. Las reglas específicas para el éxito o el fracaso se
   describen abajo. El intento de coincidencia también puede enlazar
   algunos o todos los nombres independientes dentro del patrón. Las
   reglas precisas de enlace de patrones varían según el tipo de
   patrón y se especifican a continuación.  **Los enlaces de nombre
   realizados durante una coincidencia de patrones exitosa sobreviven
   al bloque ejecutado y se pueden usar después de la declaración de
   coincidencia**.

   Nota:

     Durante las coincidencias de patrones fallidas, algunos
     subpatrones pueden tener éxito.  No confíe en que los enlaces se
     realicen para una coincidencia fallida.  Por el contrario, no
     confíe en que las variables permanezcan sin cambios después de
     una coincidencia fallida.  El comportamiento exacto depende de la
     implementación y puede variar.  Esta es una decisión intencional
     para permitir que diferentes implementaciones añadan
     optimizaciones.

3. Si el patrón es exitoso, se evalúa la protección correspondiente
   (si está presente). En este caso se garantiza que todos los enlaces
   de nombres han ocurrido.

   * Si la protección se evalúa como verdadera o no existe, se ejecuta
     el "block" dentro de "case_block".

   * En caso contrario, se intenta con el siguiente "case_block" como
     se ha descrito anteriormente.

   * Si no hay más bloques de casos, la declaración de coincidencia se
     completa.

Nota:

  Por lo general, los usuarios no deben confiar en que se evalúe un
  patrón.  Dependiendo de la implementación, el intérprete puede
  almacenar en caché los valores o utilizar otras optimizaciones que
  omitan las evaluaciones repetidas.

Un ejemplo de declaración de coincidencia:

   >>> flag = False
   >>> match (100, 200):
   ...    case (100, 300):  # No coinciden: 200 != 300
   ...        print('Case 1')
   ...    case (100, 200) if flag:  # Coinciden, pero la guardia falla
   ...        print('Case 2')
   ...    case (100, y):  # Coinciden, y vincula `y` a 200
   ...        print(f'Case 3, y: {y}')
   ...    case _:  # Patrón no se intentó
   ...        print('Case 4, I match anything!')
   ...
   Case 3, y: 200

En este caso, "if flag" es una protección.  Lea más sobre eso en la
siguiente sección.

### 8.6.2. Protecciones

   guard: "if" assignment_expression

Una "guard" (que es parte del "case") debe ser exitosa para que el
código dentro de "case" sea ejecutado.  Toma la forma: "if" seguida de
una expresión.

El flujo lógico de un bloque "case" con una "guard" es el siguiente:

1. Se comprueba que el patrón del bloque "case" fue exitoso.  Si el
   patrón falló, el "guard" no se evalúa y se comprueba el siguiente
   bloque "case".

2. Si el patrón tuvo éxito, se evalúa el "guard".

   * Si la condición del "guard" es verdadera, se selecciona el bloque
     de ese caso.

   * Si la condición del "guard" es falsa, el bloque de ese caso no es
     seleccionado.

   * Si el "guard" lanza una excepción durante la evaluación, se
     levanta la excepción.

Se permite que las protecciones tengan efectos secundarios, ya que son
expresiones.  La evaluación de la protección debe ir desde el primer
al último bloque de casos, uno a la vez, saltando los bloques de casos
cuyo(s) patrón(es) no tenga(n) éxito. (Es decir, la evaluación de las
protecciones debe realizarse en orden.) La evaluación de las
protecciones debe detenerse una vez que se selecciona un bloque de
casos.

### 8.6.3. Bloques de Casos Irrefutables

Un bloque de casos irrefutable es un bloque de casos que coincide con
todo.  Una declaración de coincidencia puede tener como máximo un
bloque de casos irrefutable, y debe ser el último.

Un bloque de casos se considera irrefutable si no tiene protección y
su patrón es irrefutable.  Un patrón se considera irrefutable si
podemos demostrar, solo por su sintaxis, que siempre tendrá éxito.
Solo los siguientes patrones son irrefutables:

* patrones AS cuyo lado izquierdo es irrefutable

* Patrones OR que contienen al menos un patrón irrefutable

* Patrones de captura

* Patrones comodín

* patrones irrefutables entre paréntesis

### 8.6.4. Patrones

Nota:

  Esta sección utiliza notaciones gramaticales más allá del estándar
  EBNF:

  * la notación "SEP.RULE+" es la abreviación de "RULE (SEP RULE)*"

  * la notación "!RULE" es la abreviación de una aserción de
    anticipación negativa

La sintaxis de nivel superior para "patrones" es:

   patterns:       open_sequence_pattern | pattern
   pattern:        as_pattern | or_pattern
   closed_pattern: | literal_pattern
                   | capture_pattern
                   | wildcard_pattern
                   | value_pattern
                   | group_pattern
                   | sequence_pattern
                   | mapping_pattern
                   | class_pattern

Las descripciones a continuación incluirán una descripción "en
términos simples" de lo que hace un patrón con fines ilustrativos
(créditos a Raymond Hettinger por un documento que inspiró la mayoría
de las descripciones). Tenga en cuenta que estas descripciones tienen
únicamente fines ilustrativos y que **may not** refleja la
implementación subyacente. Además, no cubren todos los formularios
válidos.

#### 8.6.4.1. Patrones OR

Un patrón OR son dos o más patrones separados por barras verticales
"|". Sintaxis:

   or_pattern: "|".closed_pattern+

Solo el subpatrón final puede ser irrefutable, y cada subpatrón debe
vincular el mismo conjunto de nombres para evitar ambigüedades.

Un patrón OR hace coincidir cada uno de sus subpatrones a su vez con
el valor del sujeto, hasta que uno tiene éxito. Entonces, el patrón OR
se considera exitoso. De lo contrario, si ninguno de los subpatrones
tiene éxito, el patrón OR falla.

En términos simples, "P1 | P2 | ..." intentará igualar "P1", si falla,
intentará igualar "P2", teniendo éxito inmediatamente si alguno tiene
éxito, fallando en caso contrario.

#### 8.6.4.2. patrones AS

Un patrón AS coincide con un patrón OR a la izquierda de la palabra
clave "as" con un sujeto. Sintaxis:

   as_pattern: or_pattern "as" capture_pattern

Si el patrón OR falla, el patrón AS falla. De lo contrario, el patrón
AS vincula al sujeto con el nombre a la derecha de la palabra clave as
y tiene éxito. "capture_pattern" no puede ser un "_".

En términos simples, "P as NAME" coincidirá con "P" y, en caso de
éxito, establecerá "NAME = <subject>".

#### 8.6.4.3. Patrones literales

Un patrón literal corresponde a la mayoría de literals en Python.
Sintaxis:

   literal_pattern: signed_number
                    | signed_number "+" NUMBER
                    | signed_number "-" NUMBER
                    | strings
                    | "None"
                    | "True"
                    | "False"
   signed_number:   ["-"] NUMBER

The rule "strings" and the token "NUMBER" are defined in the standard
Python grammar.  Triple-quoted strings are supported.  Raw strings and
byte strings are supported.  f-strings and t-strings are not
supported.

Los formularios "signed_number '+' NUMBER" y "signed_number '-'
NUMBER" son para expresar complex numbers; requieren un número real a
la izquierda y un número imaginario a la derecha. P.ej. "3 + 4j".

En términos simples, "LITERAL" solo tendrá éxito si "<subject> ==
LITERAL". Para los singleton "None", "True" y "False", se utiliza el
operador "is".

#### 8.6.4.4. Patrones de captura

Un patrón de captura vincula el valor del sujeto a un nombre.
Sintaxis:

   capture_pattern: !'_' NAME

Un solo guión bajo "_" no es un patrón de captura (esto es lo que
expresa "!'_'"). En su lugar, se trata como un "wildcard_pattern".

En un patrón dado, un nombre dado solo se puede vincular una vez.
P.ej. "case x, x: ..." no es válido mientras "case [x] | x: ..." está
permitido.

Los patrones de captura siempre tienen éxito. El enlace sigue las
reglas de alcance establecidas por el operador de expresión de
asignación en **PEP 572**; el nombre se convierte en una variable
local en el alcance de la función contenedora más cercana, a menos que
haya una declaración "global" o "nonlocal" aplicable.

En términos simples, "NAME" siempre tendrá éxito y establecerá "NAME =
<subject>".

#### 8.6.4.5. Patrones comodín

Un patrón comodín siempre tiene éxito (coincide con cualquier cosa) y
no vincula ningún nombre. Sintaxis:

   wildcard_pattern: '_'

"_" es un soft keyword dentro de cualquier patrón, pero solo dentro de
patrones. Es un identificador, como de costumbre, incluso dentro de
las expresiones de sujeto "match", "guard" sy bloques "case".

En términos simples, "_" siempre tendrá éxito.

#### 8.6.4.6. Patrones de valor

Un patrón de valor representa un valor con nombre en Python. Sintaxis:

   value_pattern: attr
   attr:          name_or_attr "." NAME
   name_or_attr:  attr | NAME

El nombre con puntos en el patrón se busca usando el estándar Python
name resolution rules. El patrón tiene éxito si el valor encontrado se
compara con el valor del sujeto (usando el operador de igualdad "==").

En términos simples, "NAME1.NAME2" solo tendrá éxito si "<subject> ==
NAME1.NAME2"

Nota:

  Si el mismo valor ocurre varias veces en la misma declaración de
  coincidencia, el intérprete puede almacenar en caché el primer valor
  encontrado y reutilizarlo en lugar de repetir la misma búsqueda.
  Este caché está estrictamente vinculado a una ejecución determinada
  de una declaración de coincidencia determinada.

#### 8.6.4.7. Patrones de grupo

Un patrón de grupo permite a los usuarios agregar paréntesis alrededor
de los patrones para enfatizar la agrupación deseada. De lo contrario,
no tiene sintaxis adicional. Sintaxis:

   group_pattern: "(" pattern ")"

En términos simples, "(P)" tiene el mismo efecto que "P".

#### 8.6.4.8. Patrones de secuencia

Un patrón de secuencia contiene varios subpatrones para hacer
coincidir con elementos de secuencia. La sintaxis es similar al
desempaquetado de una lista o tupla.

   sequence_pattern:       "[" [maybe_sequence_pattern] "]"
                           | "(" [open_sequence_pattern] ")"
   open_sequence_pattern:  maybe_star_pattern "," [maybe_sequence_pattern]
   maybe_sequence_pattern: ",".maybe_star_pattern+ ","?
   maybe_star_pattern:     star_pattern | pattern
   star_pattern:           "*" (capture_pattern | wildcard_pattern)

No hay diferencia si se utilizan paréntesis o corchetes para los
patrones de secuencia (es decir, "(...)" vs "[...]").

Nota:

  Un solo patrón encerrado entre paréntesis sin una coma final (por
  ejemplo, "(3 | 4)") es un group pattern. Mientras que un solo patrón
  encerrado entre corchetes (por ejemplo, "[3 | 4]") sigue siendo un
  patrón de secuencia.

A lo sumo, un subpatrón de estrella puede estar en un patrón de
secuencia. El subpatrón de estrella puede ocurrir en cualquier
posición. Si no hay ningún subpatrón de estrella, el patrón de
secuencia es un patrón de secuencia de longitud fija; de lo contrario,
es un patrón de secuencia de longitud variable.

El siguiente es el flujo lógico para hacer coincidir un patrón de
secuencia con un valor de sujeto:

1. Si el valor del sujeto no es una secuencia [2], el patrón de
   secuencia falla.

2. Si el valor del sujeto es una instancia de "str", "bytes" o
   "bytearray", el patrón de secuencia falla.

3. Los pasos subsiguientes dependen de si el patrón de secuencia es de
   longitud fija o variable.

   Si el patrón de secuencia es de longitud fija:

   1. Si la longitud de la secuencia del sujeto no es igual al número
      de subpatrones, el patrón de secuencia falla

   2. Los subpatrones del patrón de secuencia se hacen coincidir con
      sus elementos correspondientes en la secuencia del sujeto de
      izquierda a derecha. El emparejamiento se detiene tan pronto
      como falla un subpatrón. Si todos los subpatrones tienen éxito
      en hacer coincidir su elemento correspondiente, el patrón de
      secuencia tiene éxito.

   De lo contrario, si el patrón de secuencia es de longitud variable:

   1. Si la longitud de la secuencia del sujeto es menor que el número
      de subpatrones sin estrella, el patrón de secuencia falla.

   2. Los subpatrones principales no en estrella se emparejan con sus
      elementos correspondientes como para las secuencias de longitud
      fija.

   3. Si el paso anterior tiene éxito, el subpatrón en estrella
      coincide con una lista formada por los elementos restantes del
      sujeto, excluyendo los elementos restantes correspondientes a
      los subpatrones que no son en estrella que siguen el subpatrón
      en estrella.

   4. Los subpatrones restantes que no son estrellas se emparejan con
      sus elementos temáticos correspondientes, como para una
      secuencia de longitud fija.

   Nota:

     The length of the subject sequence is obtained via "len()" (i.e.
     via the "__len__()" protocol). This length may be cached by the
     interpreter in a similar manner as value patterns.

En términos simples, "[P1, P2, P3," ... ", P<N>]" solo coincide si
ocurre todo lo siguiente:

* comprobar que "<subject>" es una secuencia

* "len(subject) == <N>"

* "P1" coincide con "<subject>[0]" (tenga en cuenta que esta
  coincidencia también puede vincular nombres)

* "P2" coincide con "<subject>[1]" (tenga en cuenta que esta
  coincidencia también puede vincular nombres)

* ... y así sucesivamente para el patrón/elemento correspondiente.

#### 8.6.4.9. Patrones de mapeo

Un patrón de asignación contiene uno o más patrones clave-valor. La
sintaxis es similar a la construcción de un diccionario. Sintaxis:

   mapping_pattern:     "{" [items_pattern] "}"
   items_pattern:       ",".key_value_pattern+ ","?
   key_value_pattern:   (literal_pattern | value_pattern) ":" pattern
                        | double_star_pattern
   double_star_pattern: "**" capture_pattern

Como máximo, un patrón de estrella doble puede estar en un patrón de
mapeo. El patrón de estrella doble debe ser el último subpatrón del
patrón de mapeo.

No se permiten claves duplicadas en patrones de mapeo. Las claves
literales duplicadas lanzarán un "SyntaxError". Dos claves que de otro
modo tendrían el mismo valor lanzarán un "ValueError" en tiempo de
ejecución.

El siguiente es el flujo lógico para hacer coincidir un patrón de
mapeo con un valor de sujeto:

1. Si el valor del sujeto no es una asignación [3], el patrón de
   asignación falla.

2. Si cada clave dada en el patrón de mapeo está presente en el mapeo
   del sujeto, y el patrón para cada clave coincide con el elemento
   correspondiente del mapeo del sujeto, el patrón de mapeo tiene
   éxito.

3. Si se detectan claves duplicadas en el patrón de mapeo, el patrón
   se considera inválido. Se lanza un "SyntaxError" para valores
   literales duplicados; o un "ValueError" para claves con nombre del
   mismo valor.

Nota:

  Key-value pairs are matched using the two-argument form of the
  mapping subject's "get()" method.  Matched key-value pairs must
  already be present in the mapping, and not created on-the-fly via
  "__missing__()" or "__getitem__()".

En términos simples, "{KEY1: P1, KEY2: P2, ... }" solo coincide si
ocurre todo lo siguiente:

* comprobar "<subject>" es un mapeo

* "KEY1 in <subject>"

* "P1" coincide con "<subject>[KEY1]"

* ... y así sucesivamente para el par correspondiente de KEY / patrón.

#### 8.6.4.10. Patrones de clase

Un patrón de clase representa una clase y sus argumentos posicionales
y de palabras clave (si los hay). Sintaxis:

   class_pattern:       name_or_attr "(" [pattern_arguments ","?] ")"
   pattern_arguments:   positional_patterns ["," keyword_patterns]
                        | keyword_patterns
   positional_patterns: ",".pattern+
   keyword_patterns:    ",".keyword_pattern+
   keyword_pattern:     NAME "=" pattern

La misma palabra clave no debe repetirse en los patrones de clase.

El siguiente es el flujo lógico para hacer coincidir un patrón de
clase con un valor de materia:

1. Si "name_or_attr" no es una instancia del "type" incorporado,
   genere "TypeError".

2. Si el valor del sujeto no es una instancia de "name_or_attr"
   (probado a través de "isinstance()"), el patrón de clase falla.

3. Si no hay argumentos de patrón, el patrón tiene éxito. De lo
   contrario, los pasos siguientes dependen de si están presentes
   patrones de argumentos de posición o de palabras clave.

   Para varios tipos integrados (especificados a continuación), se
   acepta un único subpatrón posicional que coincidirá con todo el
   tema; para estos tipos, los patrones de palabras clave también
   funcionan como para otros tipos.

   Si solo hay patrones de palabras clave, se procesan de la siguiente
   manera, uno por uno:

   1. The keyword is looked up as an attribute on the subject.

      * Si esto lanza una excepción distinta de "AttributeError", la
        excepción aparece.

      * Si esto lanza "AttributeError", el patrón de clase ha fallado.

      * De lo contrario, el subpatrón asociado con el patrón de
        palabra clave se compara con el valor del atributo del sujeto.
        Si esto falla, el patrón de clase falla; si esto tiene éxito,
        la coincidencia continúa con la siguiente palabra clave.

   2. If all keyword patterns succeed, the class pattern succeeds.

   Si hay algún patrón posicional presente, se convierte en patrones
   de palabras clave utilizando el atributo "__match_args__" en la
   clase "name_or_attr" antes de hacer coincidir:

   1. The equivalent of "getattr(cls, "__match_args__", ())" is
      called.

      * Si esto lanza una excepción, la excepción surge.

      * Si el valor retornado no es una tupla, la conversión falla y
        se lanza "TypeError".

      * Si hay más patrones posicionales que
        "len(cls.__match_args__)", se lanza "TypeError".

      * De lo contrario, el patrón posicional "i" se convierte en un
        patrón de palabra clave utilizando "__match_args__[i]" como
        palabra clave. "__match_args__[i]" debe ser una cadena; si no,
        se lanza "TypeError".

      * Si hay palabras clave duplicadas, se lanza "TypeError".

      Ver también:

        Personalización de argumentos posicionales en la coincidencia
        de patrones de clase

   2. Once all positional patterns have been converted to keyword
      patterns, the match proceeds as if there were only keyword
      patterns.

   Para los siguientes tipos integrados, el manejo de subpatrones
   posicionales es diferente:

   * "bool"

   * "bytearray"

   * "bytes"

   * "dict"

   * "float"

   * "frozenset"

   * "int"

   * "list"

   * "set"

   * "str"

   * "tuple"

   Estas clases aceptan un solo argumento posicional, y el patrón allí
   se compara con el objeto completo en lugar de con un atributo. Por
   ejemplo, "int(0|1)" coincide con el valor "0", pero no con el valor
   "0.0".

En términos simples, "CLS(P1, attr=P2)" solo coincide si ocurre lo
siguiente:

* "isinstance(<subject>, CLS)"

* convierta "P1" en un patrón de palabra clave usando
  "CLS.__match_args__"

* Para cada argumento de palabra clave "attr=P2":

  * "hasattr(<subject>, "attr")"

  * "P2" coincide con "<subject>.attr"

* ... y así sucesivamente para el par de patrón / argumento de palabra
  clave correspondiente.

Ver también:

  * **PEP 634** -- Coincidencia de patrones estructurales:
    Especificación

  * **PEP 636** -- Coincidencia de patrones estructurales: Tutorial

## 8.7. Definiciones de funciones

Una definición de función define una función objeto determinada por el
usuario (consulte la sección Jerarquía de tipos estándar):

   funcdef:                   [decorators] "def" funcname [type_params] "(" [parameter_list] ")"
                              ["->" expression] ":" suite
   decorators:                decorator+
   decorator:                 "@" assignment_expression NEWLINE
   parameter_list:            defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
                                | parameter_list_no_posonly
   parameter_list_no_posonly: defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                              | parameter_list_starargs
   parameter_list_starargs:   "*" [star_parameter] ("," defparameter)* ["," [parameter_star_kwargs]]
                              | "*" ("," defparameter)+ ["," [parameter_star_kwargs]]
                              | parameter_star_kwargs
   parameter_star_kwargs:     "**" parameter [","]
   parameter:                 identifier [":" expression]
   star_parameter:            identifier [":" ["*"] expression]
   defparameter:              parameter ["=" expression]
   funcname:                  identifier

Una definición de función es una sentencia ejecutable. Su ejecución
vincula el nombre de la función en el espacio de nombres local actual
a un objeto de función (un contenedor alrededor del código ejecutable
para la función). Este objeto de función contiene una referencia al
espacio de nombres global actual como el espacio de nombres global que
se utilizará cuando se llama a la función.

La definición de la función no ejecuta el cuerpo de la función; esto
se ejecuta solo cuando se llama a la función. [4]

Una definición de función puede estar envuelta por una o más
expresiones *decorator*. Las expresiones de decorador se evalúan
cuando se define la función, en el ámbito que contiene la definición
de la función. El resultado debe ser invocable, la cual se invoca con
el objeto de función como único argumento. El valor retornado está
vinculado al nombre de la función en lugar del objeto de la función.
Se aplican múltiples decoradores de forma anidada. Por ejemplo, el
siguiente código

   @f1(arg)
   @f2
   def func(): pass

es más o menos equivalente a

   def func(): pass
   func = f1(arg)(f2(func))

excepto que la función original no está vinculada temporalmente al
nombre "func".

Distinto en la versión 3.9: Las funciones se pueden decorar con
cualquier "assignment_expression" válido. Anteriormente, la gramática
era mucho más restrictiva; ver **PEP 614** para más detalles.

Una lista de parámetros del tipo se puede dar entre corchetes entre el
nombre de la función y el paréntesis de apertura para su lista de
parámetros. Esto indica a los verificadores de tipo estático que la
función es genérica. En ejecución, los parámetros de tipo pueden
recuperarse del atributo "__type_params__". Consulte Funciones
genéricas para más información.

Distinto en la versión 3.12: Los parámetros de tipo lista son nuevos
en Python 3.12.

Cuando uno o más *parameters* tienen la forma *parameter* "="
*expression*, se dice que la función tiene "valores de parámetros
predeterminados". Para un parámetro con un valor predeterminado, el
correspondiente *argument* puede omitirse desde una llamada, en cuyo
caso se sustituye el valor predeterminado del parámetro. Si un
parámetro tiene un valor predeterminado, todos los parámetros
siguientes hasta el ""*"" también deben tener un valor predeterminado
--- esta es una restricción sintáctica que la gramática no expresa.

**Default parameter values are evaluated from left to right when the
function definition is executed.** This means that the expression is
evaluated once, when the function is defined, and that the same "pre-
computed" value is used for each call.  This is especially important
to understand when a default parameter value is a mutable object, such
as a list or a dictionary: if the function modifies the object (e.g.
by appending an item to a list), the default parameter value is in
effect modified.  This is generally not what was intended.  A way
around this is to use "None" as the default, and explicitly test for
it in the body of the function, for example:

   def whats_on_the_telly(penguin=None):
       if penguin is None:
           penguin = []
       penguin.append("property of the zoo")
       return penguin

La semántica de llamadas de función se describe con más detalle en la
sección Invocaciones. Una llamada a la función siempre asigna valores
a todos los parámetros mencionados en la lista de parámetros, ya sea
desde argumentos de posición, desde argumentos por palabra clave o
desde valores predeterminados. Si está presente la forma
""*identifier"", se inicializa en una tupla que recibe cualquier
parámetro posicional excedente, por defecto en la tupla vacía. Si el
formulario ""**identifier"" está presente, se inicializa a una nueva
asignación ordenada que recibe cualquier exceso de argumentos por
palabra clave, por defecto a una nueva asignación vacía del mismo
tipo. Los parámetros después de ""*"" o ""*identifier"" son parámetros
solo por palabra clave y solo pueden pasarse con argumentos de
palabras claves usadas.

Distinto en la versión 3.8: La sintaxis del parámetro de función "/"
se puede utilizar para indicar parámetros de posición únicamente.
Consulte **PEP 570** para obtener más detalles.

Parameters may have an *annotation* of the form "": expression""
following the parameter name.  Any parameter may have an annotation,
even those of the form "*identifier" or "**identifier". (As a special
case, parameters of the form "*identifier" may have an annotation "":
*expression"".) Functions may have "return" annotation of the form
""-> expression"" after the parameter list.  These annotations can be
any valid Python expression.  The presence of annotations does not
change the semantics of a function. See Annotations for more
information on annotations.

Distinto en la versión 3.11: Parámetros de la forma ""*identifier""
puede tener una anotación "": *expression"". Consulte **PEP 646**.

También es posible crear funciones anónimas (funciones no vinculadas a
un nombre), para uso inmediato en expresiones. Utiliza expresiones
lambda, descritas en la sección Lambdas. Tenga en cuenta que la
expresión lambda es simplemente una abreviatura para una definición de
función simplificada; una función definida en una sentencia ""def""
puede pasarse o asignarse a otro nombre al igual que una función
definida por una expresión lambda. La forma ""def"" es en realidad más
poderosa ya que permite la ejecución de múltiples sentencias y
anotaciones.

**Nota del programador:** Las funciones son objetos de la primera-
clase. Una sentencia ""def"" ejecutada dentro de una definición de
función define una función local que se puede retornar o pasar. Las
variables libres utilizadas en la función anidada pueden acceder a las
variables locales de la función que contiene el def. Vea la sección
Nombres y vínculos para más detalles.

Ver también:

  **PEP 3107** - Anotaciones de funciones
     La especificación original para anotaciones de funciones.

  **PEP 484** - Sugerencias de tipo
     Definición de un significado estándar para anotaciones:
     sugerencias de tipo.

  **PEP 526** - Sintaxis para anotaciones variables
     Capacidad para escribir anotaciones de tipo para declaraciones de
     variables, incluidas variables de clase y variables de instancia.

  **PEP 563** - Evaluación pospuesta de anotaciones
     Admite referencias directas dentro de las anotaciones conservando
     las anotaciones en forma de cadena de caracteres en tiempo de
     ejecución en lugar de una evaluación apresurada.

  **PEP 318** - Decoradores para Funciones y Métodos
     Decoradores de función y método se introdujeron en **PEP 3129**.

## 8.8. Definiciones de clase

Una definición de clase define un objeto de clase (ver sección
Jerarquía de tipos estándar):

   classdef:    [decorators] "class" classname [type_params] [inheritance] ":" suite
   inheritance: "(" [argument_list] ")"
   classname:   identifier

Una definición de clase es una sentencia ejecutable. La lista de
herencia generalmente proporciona una lista de clases base (consulte
Metaclases para usos más avanzados), por lo que cada elemento de la
lista debe evaluar a un objeto de clase que permita la
subclasificación. Las clases sin una lista de herencia heredan, por
defecto, de la clase base "object"; por lo tanto,

   class Foo:
       pass

es equivalente a

   class Foo(object):
       pass

La suite de la clase se ejecuta en un nuevo marco de ejecución (ver
Nombres y vínculos), usando un espacio de nombres local recién creado
y el espacio de nombres global original. (Por lo general, el bloque
contiene principalmente definiciones de funciones). Cuando la suite de
la clase finaliza la ejecución, su marco de ejecución se descarta pero
se guarda su espacio de nombres local. [5] Luego se crea un objeto de
clase utilizando la lista de herencia para las clases base y el
espacio de nombres local guardado para el diccionario de atributos. El
nombre de la clase está vinculado a este objeto de clase en el espacio
de nombres local original.

El orden en que se definen los atributos en el cuerpo de la clase se
conserva en el "__dict__" de la nueva clase. Tenga en cuenta que esto
es confiable solo justo después de crear la clase y solo para las
clases que se definieron utilizando la sintaxis de definición.

La creación de clases se puede personalizar en gran medida usando
metaclasses.

Las clases también se pueden decorar: al igual que cuando se decoran
funciones,

   @f1(arg)
   @f2
   class Foo: pass

es más o menos equivalente a

   class Foo: pass
   Foo = f1(arg)(f2(Foo))

Las reglas de evaluación para las expresiones de decorador son las
mismas que para los decoradores de funciones. El resultado se vincula
al nombre de la clase.

Distinto en la versión 3.9: Las clases se pueden decorar con cualquier
"assignment_expression" válido. Anteriormente, la gramática era mucho
más restrictiva; ver **PEP 614** para más detalles.

Una lista de parámetros del tipo definida inmediatamente después de un
nombre de clase debe ir entre corchetes. Esto indica a los
verificadores de tipo estático que la clase es genérica. En ejecución,
el tipo de parámetros puede retirarse del atributo de la clase
"__type_params__". Para más información consulte Clases genéricas.

Distinto en la versión 3.12: Los parámetros de tipo lista son nuevos
en Python 3.12.

** Nota del programador: ** Las variables definidas en la definición
de la clase son atributos de clase; son compartidos por instancias.
Los atributos de instancia se pueden establecer en un método con
"self.name = value". Se puede acceder a los atributos de clase e
instancia a través de la notación ""self.name"", y un atributo de
instancia oculta un atributo de clase con el mismo nombre cuando se
accede de esta manera. Los atributos de clase se pueden usar como
valores predeterminados para los atributos de instancia, pero el uso
de valores mutables puede generar resultados inesperados. Descriptors
se puede usar para crear variables de instancia con diferentes
detalles de implementación.

Ver también:

  **PEP 3115** - Metaclases en Python 3000
     La propuesta que cambió la declaración de metaclases a la
     sintaxis actual y la semántica de cómo se construyen las clases
     con metaclases.

  **PEP 3129** - Decoradores de clase
     La propuesta que agregó decoradores de clase. Los decoradores de
     funciones y métodos se introdujeron en **PEP 318**.

## 8.9. Corrutinas

Added in version 3.5.

### 8.9.1. Definición de la función corrutina

   async_funcdef: [decorators] "async" "def" funcname "(" [parameter_list] ")"
                  ["->" expression] ":" suite

La ejecución de corrutinas de Python se puede suspender y reanudar en
muchos puntos (consulte *coroutine*). Las expresiones "await", "async
for" y "async with" solo se pueden utilizar en el cuerpo de una
función de corrutina.

Las funciones definidas con la sintaxis "async def" siempre son
funciones de corrutina, incluso si no contienen palabras claves
"await" o "async".

Es un error del tipo "SyntaxError" usar una expresión "yield from"
dentro del cuerpo de una función de corrutina.

Un ejemplo de una función corrutina:

   async def func(param1, param2):
       do_stuff()
       await some_coroutine()

Distinto en la versión 3.7: "await" y "async" ahora son palabras
clave; anteriormente solo se los trataba como tales dentro del cuerpo
de una función de rutina.

### 8.9.2. La sentencia "async for"

   async_for_stmt: "async" for_stmt

Un *asynchronous iterable* proporciona un método "__aiter__" que
retorna directamente un *asynchronous iterator*, que puede llamar a
código asincrónico en su método "__anext__".

La sentencia "async for" permite una iteración apropiada sobre
iteradores asincrónicos.

El siguiente código:

   async for TARGET in ITER:
       SUITE
   else:
       SUITE2

Es semánticamente equivalente a:

   iter = (ITER).__aiter__()
   running = True

   while running:
       try:
           TARGET = await iter.__anext__()
       except StopAsyncIteration:
           running = False
       else:
           SUITE
   else:
       SUITE2

except that implicit special method lookup is used for "__aiter__()"
and "__anext__()".

Es un error del tipo "SyntaxError" usar una sentencia "async for"
fuera del cuerpo de una función de corrutina.

### 8.9.3. La sentencia "async with"

   async_with_stmt: "async" with_stmt

Un *asynchronous context manager* es un *context manager* que puede
suspender la ejecución en sus métodos *enter* y *exit*.

El siguiente código:

   async with EXPRESSION as TARGET:
       SUITE

es semánticamente equivalente a:

   manager = (EXPRESSION)
   aenter = manager.__aenter__
   aexit = manager.__aexit__
   value = await aenter()
   hit_except = False

   try:
       TARGET = value
       SUITE
   except:
       hit_except = True
       if not await aexit(*sys.exc_info()):
           raise
   finally:
       if not hit_except:
           await aexit(None, None, None)

except that implicit special method lookup is used for "__aenter__()"
and "__aexit__()".

Es un error del tipo "SyntaxError" usar una sentencia "async with"
fuera del cuerpo de una función de corrutina.

Ver también:

  **PEP 492** - Corrutinas con sintaxis "async" y "await"
     La propuesta que convirtió a las corrutinas en un concepto
     independiente adecuado en Python, y agregó una sintaxis de
     soporte.

## 8.10. Listas de tipo parámetro

Added in version 3.12.

Distinto en la versión 3.13: Compatibilidad para valores
predeterminados se añadió (Consulte **PEP 696**).

   type_params:  "[" type_param ("," type_param)* "]"
   type_param:   typevar | typevartuple | paramspec
   typevar:      identifier (":" expression)? ("=" expression)?
   typevartuple: "*" identifier ("=" expression)?
   paramspec:    "**" identifier ("=" expression)?

Functions (incluyendo coroutines), classes y  type aliases debe
contener un parámetro de tipo lista:

   def max[T](args: list[T]) -> T:
       ...

   async def amax[T](args: list[T]) -> T:
       ...

   class Bag[T]:
       def __iter__(self) -> Iterator[T]:
           ...

       def add(self, arg: T) -> None:
           ...

   type ListOrSet[T] = list[T] | set[T]

Semánticamente, esto indica que la función, clase, o alias de tipo es
genérico sobre una variable. Esta información en principalmente usada
por verificadores de tipo estático, y en ejecución, los objetos
genéricos se comportan de forma muy similar a sus homólogos no
genéricos.

Los tipos de parámetros son declarados entre corchetes  ("[]")
inmediatamente después del nombre de la función, clase o alias. El
tipo de parámetro es accesible en el ámbito del objeto genérico, pero
no  en otro lugar.  Así, después de una declaración "def func[T]():
pass", el nombre "T" no está disponible en el ámbito del módulo. A
continuación, se describe con más precisión la semántica de los
objetos genéricos. El ámbito de los parámetros de tipo se modela con
una función especial (técnicamente, una ámbito de anotación) que
envuelve la creación del objeto genérico.

Funciones genéricas, clases y aliases de tipo tienen un atributo
:"__type_params__" que lista sus parámetros de tipo.

Los tipos de parámetros  son de tres tipos:

* "typing.TypeVar", introducido por un nombre plano (p.j., "T").
  Sistemáticamente, esto representa un único tipo para un verificador
  de tipos.

* "typing.TypeVarTuple",  introducido por un nombre precedido de un
  asterisco (p.j, "*Ts"). Semánticamente, representa una tupla de
  cualquier número de tipos.

* "typing.ParamSpec",  introducido por un nombre precedido de dos
  asterisco (p.j, "*P"). Semánticamente, representa los parámetros de
  una llamada.

Las declaraciones "typing.TypeVar" pueden definir *bounds* y
*constraints* con dos puntos (":") seguidos de una expresión. Una sola
expresión después de los dos puntos indica un límite (por ejemplo, "T:
int"). Semánticamente, esto significa que "typing.TypeVar" solo puede
representar tipos que sean un subtipo de este límite. Una tupla de
expresiones entre paréntesis después de los dos puntos indica un
conjunto de restricciones (por ejemplo, "T: (str, bytes)"). Cada
miembro de la tupla debe ser un tipo (de nuevo, esto no se aplica en
tiempo de ejecución). Las variables de tipo restringido solo pueden
tomar uno de los tipos de la lista de restricciones.

Para "typing.TypeVar"s declarados utilizando la sintaxis de lista de
parámetros de tipo, los límites y restricciones no se evalúan cuando
se crea el objeto genérico, sino solo cuando se accede explícitamente
al valor a través de los atributos "__bound__" y "__constraints__".
Para ello, los límites o restricciones se evalúan en un ámbito de
anotación separado.

"typing.TypeVarTuple" s y "typing.ParamSpec" s no pueden tener límites
ni restricciones.

Los tres sabores de parámetros de tipo también pueden tener un *valor
predeterminado*, lo que se usa cuando el parámetro de tipo no se
proporciona explícitamente. Esto se añade adjuntando un solo signo
igual ("=") seguido por una expresión. Como los límites y
restricciones del tipo variables, el valor predeterminado no se evalúa
cuando el objeto se crea, solamente cuando se accede el atributo
"__default__" del parámetro del tipo. Con este fin, el valor
predeterminado se evalúa en un ámbito de anotación separado. Si no se
especifica un valor predeterminado para un parámetro de tipo, el
atributo "__default__" se establece en el objeto de centinela especial
"typing.NoDefault".

El siguiente ejemplo indica el conjunto completo de declaraciones de
parámetros de tipo permitidas:

   def overly_generic[
      SimpleTypeVar,
      TypeVarWithDefault = int,
      TypeVarWithBound: int,
      TypeVarWithConstraints: (str, bytes),
      *SimpleTypeVarTuple = (int, float),
      **SimpleParamSpec = (str, bytearray),
   ](
      a: SimpleTypeVar,
      b: TypeVarWithDefault,
      c: TypeVarWithBound,
      d: Callable[SimpleParamSpec, TypeVarWithConstraints],
      *e: SimpleTypeVarTuple,
   ): ...

### 8.10.1. Funciones genéricas

Las funciones genéricas son declaradas de la siguiente forma:

   def func[T](arg: T): ...

Esta sintaxis es equivalente a:

   annotation-def TYPE_PARAMS_OF_func():
       T = typing.TypeVar("T")
       def func(arg: T): ...
       func.__type_params__ = (T,)
       return func
   func = TYPE_PARAMS_OF_func()

Aquí "annotation-def" indica un ámbito de anotación, que en realidad
no está vinculado a ningún nombre en tiempo de ejecución. (Se ha
tomado otra libertad en la traducción: la sintaxis no pasa por el
acceso a atributos en el módulo "typing", sino que crea una instancia
de "typing.TypeVar" directamente).

Las anotaciones de las funciones genéricas se evalúan dentro del
ámbito de anotación utilizado para declarar los parámetros de tipo,
pero no así los valores por defecto y los decoradores de la función.

El siguiente ejemplo ilustra las reglas de alcance para estos casos,
así como para otros tipos de parámetros de tipo:

   @decorator
   def func[T: int, *Ts, **P](*args: *Ts, arg: Callable[P, T] = some_default):
       ...

Excepto para la lazy-evaluation del "TypeVar" vinculada, esto es
equivalente a:

   DEFAULT_OF_arg = some_default

   annotation-def TYPE_PARAMS_OF_func():

       annotation-def BOUND_OF_T():
           return int
       # In reality, BOUND_OF_T() is evaluated only on demand.
       T = typing.TypeVar("T", bound=BOUND_OF_T())

       Ts = typing.TypeVarTuple("Ts")
       P = typing.ParamSpec("P")

       def func(*args: *Ts, arg: Callable[P, T] = DEFAULT_OF_arg):
           ...

       func.__type_params__ = (T, Ts, P)
       return func
   func = decorator(TYPE_PARAMS_OF_func())

Los nombres en mayúsculas como "DEFAULT_OF_arg" no se vinculan en
tiempo de ejecución.

### 8.10.2. Clases genéricas

Las clases genéricas son declaradas de la siguiente forma:

   class Bag[T]: ...

Esta sintaxis es equivalente a:

   annotation-def TYPE_PARAMS_OF_Bag():
       T = typing.TypeVar("T")
       class Bag(typing.Generic[T]):
           __type_params__ = (T,)
           ...
       return Bag
   Bag = TYPE_PARAMS_OF_Bag()

Aquí de nuevo "annotation-def" (no es una palabra clave real) indica
un ámbito de anotación, y el nombre "TYPE_PARAMS_OF_Bag" no está
vinculado en tiempo de ejecución.

Las clases genéricas heredan implícitamente de "typing.Generic". Las
clases base y los argumentos de palabra clave de las clases genéricas
se evalúan dentro del ámbito del tipo para los parámetros de tipo, y
los decoradores se evalúan fuera de ese ámbito. Esto se ilustra con
este ejemplo:

   @decorator
   class Bag(Base[T], arg=T): ...

Esto es equivalente a:

   annotation-def TYPE_PARAMS_OF_Bag():
       T = typing.TypeVar("T")
       class Bag(Base[T], typing.Generic[T], arg=T):
           __type_params__ = (T,)
           ...
       return Bag
   Bag = decorator(TYPE_PARAMS_OF_Bag())

### 8.10.3. Alias de tipo genérico

La declaración "type" también se puede usar para crear un alias de
tipo genérico:

   type ListOrSet[T] = list[T] | set[T]

Excepto para la evaluación perezosa del valor, esto es equivalente a:

   annotation-def TYPE_PARAMS_OF_ListOrSet():
       T = typing.TypeVar("T")

       annotation-def VALUE_OF_ListOrSet():
           return list[T] | set[T]
       # In reality, the value is lazily evaluated
       return typing.TypeAliasType("ListOrSet", VALUE_OF_ListOrSet(), type_params=(T,))
   ListOrSet = TYPE_PARAMS_OF_ListOrSet()

Aquí, "annotation-def" (no es una palabra clave real) indica un ámbito
de anotación. Los nombres en mayúsculas como
"TYPE_PARAMS_OF_ListOrSet" no están vinculados en tiempo de ejecución.

## 8.11. Annotations

Distinto en la versión 3.14: Annotations are now lazily evaluated by
default.

Variables and function parameters may carry *annotations*, created by
adding a colon after the name, followed by an expression:

   x: annotation = 1
   def f(param: annotation): ...

Functions may also carry a return annotation following an arrow:

   def f() -> annotation: ...

Annotations are conventionally used for *type hints*, but this is not
enforced by the language, and in general annotations may contain
arbitrary expressions. The presence of annotations does not change the
runtime semantics of the code, except if some mechanism is used that
introspects and uses the annotations (such as "dataclasses" or
"@functools.singledispatch").

By default, annotations are lazily evaluated in an annotation scope.
This means that they are not evaluated when the code containing the
annotation is evaluated. Instead, the interpreter saves information
that can be used to evaluate the annotation later if requested. The
"annotationlib" module provides tools for evaluating annotations.

If the future statement "from __future__ import annotations" is
present, all annotations are instead stored as strings:

   >>> from __future__ import annotations
   >>> def f(param: annotation): ...
   >>> f.__annotations__
   {'param': 'annotation'}

This future statement will be deprecated and removed in a future
version of Python, but not before Python 3.13 reaches its end of life
(see **PEP 749**). When it is used, introspection tools like
"annotationlib.get_annotations()" and "typing.get_type_hints()" are
less likely to be able to resolve annotations at runtime.

-[ Notas al pie ]-

[1] La excepción se propaga a la pila de invocación a menos que haya
    una cláusula "finally" que provoque otra excepción. Esa nueva
    excepción hace que se pierda la anterior.

[2] En la coincidencia de patrones, una secuencia se define como una
    de las siguientes:

    * una clase que hereda de "collections.abc.Sequence"

    * una clase de Python que se ha registrado como
      "collections.abc.Sequence"

    * una clase incorporada que tiene su conjunto de bits (CPython)
      "Py_TPFLAGS_SEQUENCE"

    * una clase que hereda de cualquiera de los anteriores

    Las siguientes clases de biblioteca estándar son secuencias:

    * "array.array"

    * "collections.deque"

    * "list"

    * "memoryview"

    * "range"

    * "tuple"

    Nota:

      Los valores de sujeto de tipo "str", "bytes" y "bytearray" no
      coinciden con los patrones de secuencia.

[3] En la coincidencia de patrones, un mapeo se define como uno de los
    siguientes:

    * una clase que hereda de "collections.abc.Mapping"

    * una clase de Python que se ha registrado como
      "collections.abc.Mapping"

    * una clase incorporada que tiene su conjunto de bits (CPython)
      "Py_TPFLAGS_MAPPING"

    * una clase que hereda de cualquiera de los anteriores

    Las clases de biblioteca estándar "dict" y
    "types.MappingProxyType" son asignaciones.

[4] Una cadena de caracteres literal que aparece como la primera
    declaración en el cuerpo de la función se transforma en el
    atributo "__doc__" y por lo tanto en *docstring* de la función.

[5] Una cadena de caracteres literal que aparece como la primera
    declaración en el cuerpo de la clase se transforma en el elemento
    del espacio de nombre "__doc__" y, por lo tanto, de la clase
    *docstring*.
