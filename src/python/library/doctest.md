---
title: '"doctest" --- Test interactive Python examples'
source_url: https://docs.python.org/es/3
source_path: library/doctest.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2370
---

# "doctest" --- Test interactive Python examples

**Código fuente:** Lib/doctest.py

======================================================================

The "doctest" module searches for pieces of text that look like
interactive Python sessions, and then executes those sessions to
verify that they work exactly as shown.  There are several common ways
to use doctest:

* Para revisar que los docstrings de un módulo están al día al
  verificar que todos los ejemplos interactivos todavía trabajan como
  está documentado.

* Para realizar pruebas de regresión al verificar que los ejemplos
  interactivos de un archivo de pruebas o un objeto de pruebas trabaje
  como sea esperado.

* Para escribir documentación de tutorial para un paquete,
  generosamente ilustrado con ejemplos de entrada-salida. Dependiendo
  si los ejemplos o el texto expositivo son enfatizados, tiene el
  sabor de "pruebas literarias" o "documentación ejecutable".

Aquí hay un módulo de ejemplo completo pero pequeño:

   """
   This is the "example" module.

   The example module supplies one function, factorial().  For example,

   >>> factorial(5)
   120
   """

   def factorial(n):
       """Return the factorial of n, an exact integer >= 0.

       >>> [factorial(n) for n in range(6)]
       [1, 1, 2, 6, 24, 120]
       >>> factorial(30)
       265252859812191058636308480000000
       >>> factorial(-1)
       Traceback (most recent call last):
           ...
       ValueError: n must be >= 0

       Factorials of floats are OK, but the float must be an exact integer:
       >>> factorial(30.1)
       Traceback (most recent call last):
           ...
       ValueError: n must be exact integer
       >>> factorial(30.0)
       265252859812191058636308480000000

       It must also not be ridiculously large:
       >>> factorial(1e100)
       Traceback (most recent call last):
           ...
       OverflowError: n too large
       """

       import math
       if not n >= 0:
           raise ValueError("n must be >= 0")
       if math.floor(n) != n:
           raise ValueError("n must be exact integer")
       if n+1 == n:  # catch a value like 1e300
           raise OverflowError("n too large")
       result = 1
       factor = 2
       while factor <= n:
           result *= factor
           factor += 1
       return result

   if __name__ == "__main__":
       import doctest
       doctest.testmod()

If you run "example.py" directly from the command line, "doctest"
works its magic:

   $ python example.py
   $

There's no output!  That's normal, and it means all the examples
worked.  Pass "-v" to the script, and "doctest" prints a detailed log
of what it's trying, and prints a summary at the end:

   $ python example.py -v
   Trying:
       factorial(5)
   Expecting:
       120
   ok
   Trying:
       [factorial(n) for n in range(6)]
   Expecting:
       [1, 1, 2, 6, 24, 120]
   ok

Y demás, eventualmente terminando con:

   Trying:
       factorial(1e100)
   Expecting:
       Traceback (most recent call last):
           ...
       OverflowError: n too large
   ok
   2 items passed all tests:
      1 test in __main__
      6 tests in __main__.factorial
   7 tests in 2 items.
   7 passed.
   Test passed.
   $

That's all you need to know to start making productive use of
"doctest"! Jump in.  The following sections provide full details.
Note that there are many examples of doctests in the standard Python
test suite and libraries. Especially useful examples can be found in
the standard test file "Lib/test/test_doctest/test_doctest.py".

Added in version 3.13: Output is colorized by default and can be
controlled using environment variables.

## Uso simple: verificar ejemplos en docstrings

The simplest way to start using doctest (but not necessarily the way
you'll continue to do it) is to end each module "M" with:

   if __name__ == "__main__":
       import doctest
       doctest.testmod()

"doctest" then examines docstrings in module "M".

Ejecutar el módulo como un script causa que los ejemplos en los
docstrings se ejecuten y sean verificados:

   python M.py

No mostrará nada a menos que un ejemplo falle, en cuyo caso el ejemplo
fallido o ejemplos fallidos y sus causas de la falla son imprimidas a
stdout, y la línea final de salida es "***Test Failed*** N failures.",
donde *N* es el número de ejemplos que fallaron.

Ejecútalo con el modificador "-v" en su lugar:

   python M.py -v

y un reporte detallado de todos los ejemplos intentados es impreso a
la salida estándar, junto con resúmenes clasificados  al final.

You can force verbose mode by passing "verbose=True" to "testmod()",
or prohibit it by passing "verbose=False".  In either of those cases,
"sys.argv" is not examined by "testmod()" (so passing "-v" or not has
no effect).

There is also a command line shortcut for running "testmod()", see
section Command-line Usage.

Para más información de "testmod()", consulte la sección API básica.

## Uso Simple: Verificar ejemplos en un Archivo de Texto

Otra simple aplicación de doctest es probar ejemplos interactivos en
un archivo de texto.  Esto puede ser hecho con la función
"testfile()":

   import doctest
   doctest.testfile("example.txt")

Este script corto ejecuta y verifica cualquier ejemplo interactivo de
Python contenido en el archivo "example.txt". El contenido del archivo
es tratado como si fuese un solo gran docstring; ¡el archivo no
necesita contener un programa de Python! Por ejemplo, tal vez
"example.txt" contenga esto:

   The ``example`` module
   ======================

   Using ``factorial``
   -------------------

   This is an example text file in reStructuredText format.  First import
   ``factorial`` from the ``example`` module:

       >>> from example import factorial

   Now use it:

       >>> factorial(6)
       120

Ejecutar "doctest.testfile("example.txt")" entonces encuentra el error
en esta documentación:

   File "./example.txt", line 14, in example.txt
   Failed example:
       factorial(6)
   Expected:
       120
   Got:
       720

As with "testmod()", "testfile()" won't display anything unless an
example fails.  If an example does fail, then the failing example(s)
and the cause(s) of the failure(s) are printed to stdout, using the
same format as "testmod()".

Por defecto, "testfile()" busca archivos en el directorio del módulo
al que se llama. Véase la sección API básica para una descripción de
los argumentos opcionales que pueden ser usados para decirle que
busque archivos en otros lugares.

Como "testmod()", la verbosidad de "testfile()" puede ser establecida
con el modificador de la línea de comandos "-v" o con el argumento por
palabra clave opcional *verbose*.

There is also a command line shortcut for running "testfile()", see
section Command-line Usage.

Para más información en "testfile()", véase la sección API básica.

## Command-line Usage

The "doctest" module can be invoked as a script from the command line:

   python -m doctest [-v] [-o OPTION] [-f] file [file ...]

-v, --verbose

   Detailed report of all examples tried is printed to standard
   output, along with assorted summaries at the end:

      python -m doctest -v example.py

   This will import "example.py" as a standalone module and run
   "testmod()" on it. Note that this may not work correctly if the
   file is part of a package and imports other submodules from that
   package.

   If the file name does not end with ".py", "doctest" infers that it
   must be run with "testfile()" instead:

      python -m doctest -v example.txt

-o, --option <option>

   Option flags control various aspects of doctest's behavior, see
   section Banderas de Opción.

   Added in version 3.4.

-f, --fail-fast

   This is shorthand for "-o FAIL_FAST".

   Added in version 3.4.

## Cómo funciona

Esta sección examina en detalle cómo funciona doctest: qué docstrings
revisa, cómo encuentra ejemplos interactivos, qué contexto de
ejecución usa, cómo maneja las excepciones, y cómo las banderas pueden
ser usadas para controlar su comportamiento. Esta es la información
que necesitas saber para escribir ejemplos de doctest; para
información sobre ejecutar doctest en estos ejemplos, véase las
siguientes secciones.

### ¿Qué docstrings son examinados?

Se busca en el docstring del módulo, y todos los docstrings de las
funciones, clases, y métodos.  Los objetos importados en el módulo no
se buscan.

In addition, there are cases when you want tests to be part of a
module but not part of the help text, which requires that the tests
not be included in the docstring. Doctest looks for a module-level
variable called "__test__" and uses it to locate other tests. If
"M.__test__" exists, it must be a dict, and each entry maps a (string)
name to a function object, class object, or string. Function and class
object docstrings found from "M.__test__" are searched, and strings
are treated as if they were docstrings.  In output, a key "K" in
"M.__test__" appears with name "M.__test__.K".

For example, place this block of code at the top of "example.py":

   __test__ = {
       'numbers': """
   >>> factorial(6)
   720

   >>> [factorial(n) for n in range(6)]
   [1, 1, 2, 6, 24, 120]
   """
   }

The value of "example.__test__["numbers"]" will be treated as a
docstring and all the tests inside it will be run. It is important to
note that the value can be mapped to a function, class object, or
module; if so, "doctest" searches them recursively for docstrings,
which are then scanned for tests.

Todas las clases encontradas se buscan recursivamente de manera
similar, para probar docstrings en sus métodos contenidos y clases
anidadas.

Nota:

  "doctest" can only automatically discover classes and functions that
  are defined at the module level or inside other classes.Since nested
  classes and functions only exist when an outer function is called,
  they cannot be discovered. Define them outside to make them visible.

### ¿Cómo se reconocen los ejemplos de docstring?

En la mayoría de los casos un copiar y pegar de una sesión de consola
interactiva funciona bien, pero doctest no está intentando hacer una
emulación exacta de ningún shell específico de Python.

   >>> # comments are ignored
   >>> x = 12
   >>> x
   12
   >>> if x == 13:
   ...     print("yes")
   ... else:
   ...     print("no")
   ...     print("NO")
   ...     print("NO!!!")
   ...
   no
   NO
   NO!!!
   >>>

Cualquier salida esperada debe seguir inmediatamente el final de la
línea "'>>>'" o "'...'" conteniendo el código, y la salida esperada
(si la hubiera) se extiende hasta el siguiente "'>>>'" o la línea en
blanco.

La letra pequeña:

* La salida esperada no puede contener una línea de espacios en
  blanco, ya que ese tipo de línea se toma para indicar el fin de la
  salida esperada. Si la salida esperada de verdad contiene una línea
  en blanco, pon "<BLANKLINE>" en tu ejemplo de doctest en cada lugar
  donde una línea en blanco sea esperada.

* Todos los caracteres de tabulación se expanden a espacios, usando
  paradas de tabulación de 8 -columnas. Las tabulaciones generadas por
  el código en pruebas no son modificadas. Ya que todas las
  tabulaciones en la salida de prueba *son* expandidas, significa que
  si el código de salida incluye tabulaciones, la única manera de que
  el doctest pueda pasar es si la opción "NORMALIZE_WHITESPACE" o
  directive está en efecto. Alternativamente, la prueba puede ser
  reescrita para capturar la salida y compararla a un valor esperado
  como parte de la prueba. Se llegó a este tratamiento de tabulaciones
  en la fuente a través de prueba y error, y ha demostrado ser la
  manera menos propensa a errores de manejarlos. Es posible usar un
  algoritmo diferente para manejar tabulaciones al escribir una clase
  "DocTestParser" personalizada.

* La salida a stdout es capturada, pero no la salida a stderr (los
  rastreos de la excepción son capturados a través de maneras
  diferentes).

* Si continuas una línea poniendo una barra invertida en una sesión
  interactiva, o por cualquier otra razón usas una barra invertida,
  debes usar un docstring crudo, que preservará tus barras invertidas
  exactamente como las escribes:

     >>> def f(x):
     ...     r'''Backslashes in a raw docstring: m\n'''
     ...
     >>> print(f.__doc__)
     Backslashes in a raw docstring: m\n

  De otra manera, la barra invertida será interpretada como parte de
  una cadena. Por ejemplo, el "\n" arriba sería interpretado como un
  carácter de nueva línea. Alternativamente, puedes duplicar cada
  barra invertida en  la versión de doctest (y no usar una cadena de
  caracteres cruda):

     >>> def f(x):
     ...     '''Backslashes in a raw docstring: m\\n'''
     ...
     >>> print(f.__doc__)
     Backslashes in a raw docstring: m\n

* La columna inicial no importa:

     >>> assert "Easy!"
           >>> import math
               >>> math.floor(1.9)
               1

  y tantos espacios en blanco al principio se eliminan de la salida
  esperada como aparece en la línea "'>>>'" inicial que empezó el
  ejemplo.

### ¿Cuál es el contexto de ejecución?

By default, each time "doctest" finds a docstring to test, it uses a
*shallow copy* of "M"'s globals, so that running tests doesn't change
the module's real globals, and so that one test in "M" can't leave
behind crumbs that accidentally allow another test to work.  This
means examples can freely use any names defined at top-level in "M",
and names defined earlier in the docstring being run. Examples cannot
see names defined in other docstrings.

Puedes forzar el uso de tus propios diccionarios como contexto de
ejecución al pasar "globs=your_dict" a "testmod()" o "testfile()" en
su lugar.

### ¿Y las excepciones?

No hay problema, siempre que el rastreo sea la única salida producida
por el ejemplo: sólo copia el rastreo.  [1] Ya que los rastreos
contienen detalles que probablemente cambien rápidamente (por ejemplo,
rutas de archivos exactas y números de línea), este es un caso donde
doctest trabaja duro para ser flexible en lo que acepta.

Ejemplo simple:

   >>> [1, 2, 3].remove(42)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: list.remove(x): x not in list

El doctest tiene éxito si se lanza "ValueError", con el detalle
"list.remove(x): x not in list" como se muestra.

La salida esperada para una excepción debe empezar con una cabecera de
rastreo, que puede ser una de las siguientes dos líneas, con el mismo
sangrado de la primera línea del ejemplo:

   Traceback (most recent call last):
   Traceback (innermost last):

La cabecera de rastreo es seguida por una pila de rastreo opcional,
cuyo contenido es ignorado por doctest.  La pila de rastreo es
típicamente omitida, o copiada palabra por palabra de una sesión
interactiva.

La pila de rastreo es seguida por la parte más interesante: la línea o
líneas conteniendo el tipo de excepción y detalle. Esto es usualmente
la última línea de un rastreo, pero se puede extender a través de
múltiples líneas si la excepción tiene un detalle de varias líneas:

   >>> raise ValueError('multi\n    line\ndetail')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: multi
       line
   detail

Las últimas tres líneas (empezando con "ValueError") son comparados
con el tipo de excepción y detalle, y el resto es ignorado.

La mejor práctica es omitir la pila de rastreo, a menos que añada
valor de documentación significante al ejemplo. Por lo que el último
ejemplo es probablemente mejor como:

   >>> raise ValueError('multi\n    line\ndetail')
   Traceback (most recent call last):
       ...
   ValueError: multi
       line
   detail

Note que los rastreos son tratados de manera especial. En particular,
en el ejemplo reescrito, el uso de "..." es independiente de la opción
"ELLIPSIS" de doctest. Se pueden excluir los puntos suspensivos en ese
ejemplo, así como también pueden haber tres (o trescientas) comas o
dígitos, o una transcripción sangrada de un *sketch* de Monty Python.

Algunos detalles que debes leer una vez, pero no necesitarás recordar:

* Doctest no puede adivinar si tu salida esperada vino de una
  excepción de rastreo o de una impresión ordinaria. Así que, un
  ejemplo que espera "ValueError: 42 is prime" pasará, ya sea si de
  hecho se lance "ValueError" o si el ejemplo simplemente imprime ese
  texto de rastreo. En la práctica, la salida ordinaria raramente
  comienza con una línea de cabecera de rastreo, por lo que esto no
  crea problemas reales.

* Cada línea de la pila de rastreo (si se presenta) debe estar más
  sangrada que la primera línea del ejemplo, *o* empezar con un
  carácter no alfanumérico. la primera línea que sigue a la cabecera
  de rastreo sangrada de igual forma y empezando con un alfanumérico
  es considerado el inicio del detalle de la excepción. Por supuesto
  que esto es lo correcto para rastreos genuinos.

* Cuando se especifica la opción "IGNORE_EXCEPTION_DETAIL" de doctest.
  todo lo que sigue a los dos puntos más a la izquierda y cualquier
  otra información del módulo en el nombre de la excepción se ignora.

* The interactive shell omits the traceback header line for some
  "SyntaxError"s.  But doctest uses the traceback header line to
  distinguish exceptions from non-exceptions.  So in the rare case
  where you need to test a "SyntaxError" that omits the traceback
  header, you will need to manually add the traceback header line to
  your test example.

* En el caso de algunas excepciones Python señala la posición donde
  ocurrió el error usando un marcador "^":

     >>> 1 + None
       File "<stdin>", line 1
         1 + None
         ~~^~~~~~
     TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

  Ya que las líneas mostrando la posición del error vienen antes del
  tipo de excepción y detalle, no son revisadas por doctest. Por
  ejemplo, el siguiente test pasaría, a pesar de que pone el marcador
  "^" en la posición equivocada:

     >>> 1 + None
       File "<stdin>", line 1
         1 + None
         ^~~~~~~~
     TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

### Banderas de Opción

Varias banderas de opción controlan diversos aspectos del
comportamiento de doctest. Los nombres simbólicos para las banderas
son proporcionados como constantes del módulo, que se pueden conectar
mediante *OR* bit a bit  y pasar a varias funciones. Los nombres
también pueden ser usados en las directivas de doctest, y se pueden
pasar a la interfaz de la línea de comandos de doctest a través de la
opción "-o".

El primer grupo de opciones definen las semánticas de la prueba,
controlando aspectos de cómo doctest decide si la salida de hecho
concuerda con la salida esperada del ejemplo:

doctest.DONT_ACCEPT_TRUE_FOR_1

   Por defecto, si un bloque de salida esperada contiene sólo "1", se
   considera igual a un bloque de salida real conteniendo sólo "1" o
   "true", y similarmente para "0" contra "False". Cuando se
   especifica "DONT_ACCEPT_TRUE_FOR_1`", no se permite ninguna
   sustitución.  El comportamiento por defecto atiende a que Python
   cambió el tipo de retorno de muchas funciones de enteros a
   booleanos; los doctest esperando salidas "de pequeño enteros"
   todavía trabajan en estos casos. Esta opción probablemente se vaya,
   pero no por muchos años.

doctest.DONT_ACCEPT_BLANKLINE

   Por defecto, si un bloque de salida esperada contiene una línea que
   sólo tiene la cadena de caracteres "<BLANKLINE>", entonces esa
   línea corresponderá a una línea en blanco en la salida real. Ya que
   una línea en blanca auténtica delimita la salida esperada, esta es
   la única manera de comunicar que una línea en blanco es esperada.
   Cuando se especifica "DONT_ACCEPT_BLANKLINE", esta substitución no
   se permite.

doctest.NORMALIZE_WHITESPACE

   Cuando se especifica, todas las secuencias de espacios en blanco
   (vacías y nuevas líneas) son tratadas como iguales. Cualquier
   secuencia de espacios en blanco dentro de la salida esperada
   corresponderá a cualquier secuencia de espacios en blanco dentro de
   la salida real. Por defecto, los espacios en blanco deben
   corresponderse exactamente.  "NORMALIZE_WHITESPACE" es
   especialmente útil cuando una línea de la salida esperada es muy
   larga, y quieres envolverla a través de múltiples líneas en tu
   código fuente.

doctest.ELLIPSIS

   Cuando se especifica, un marcador de puntos suspensivos ("...") en
   la salida esperada puede corresponder a cualquier cadena de
   caracteres en la salida real. Esto incluye las cadenas de
   caracteres que abarcan límites de líneas, y cadenas de caracteres
   vacías, por lo que es mejor mantener su uso simple. Usos
   complicados pueden conducir a los mismo tipos de sorpresa de "ups,
   coincidió demasiado" que ".*" es propenso a hacer en expresiones
   regulares.

doctest.IGNORE_EXCEPTION_DETAIL

   Cuando se especifica, las excepciones que doctest espera, pasarán
   siempre que sea lanzada una excepción del tipo esperado, incluso si
   los detalles (mensaje y nombre completo de la excepción) no
   coinciden.

   Por ejemplo, si se espera "ValueError: 42", el test pasará si la
   verdadera excepción lanzada es "ValueError: 3*14", pero fallará si
   es lanzada un "TypeError". También ignorará cualquier nombre
   completo incluido antes de la clase de la excepción, lo cual puede
   variar entre implementaciones y versiones de Python y
   bibliotecas/código en uso. Por lo tanto, las tres variaciones
   funcionarán con la bandera especificada:

      >>> raise Exception('message')
      Traceback (most recent call last):
      Exception: message

      >>> raise Exception('message')
      Traceback (most recent call last):
      builtins.Exception: message

      >>> raise Exception('message')
      Traceback (most recent call last):
      __main__.Exception: message

   Tenga en cuenta que "ELLIPSIS" también puede ser usado para ignorar
   detalles del mensaje de la excepción, pero dicha prueba aún podría
   fallar si el nombre del modulo está presente o si hay coincidencias
   exactas.

   Distinto en la versión 3.2: "IGNORE_EXCEPTION_DETAIL" también
   ignora cualquier información relacionada al módulo conteniendo la
   excepción bajo prueba.

doctest.SKIP

   Cuando se especifica, no ejecuta el ejemplo del todo. Puede ser
   útil en contextos donde los ejemplos de doctest sirven como
   documentación y casos de prueba a la vez, y un ejemplo debe ser
   incluido para propósitos de documentación, pero no debe ser
   revisado. P. ej., la salida del ejemplo puede ser aleatoria, o el
   ejemplo puede depender de recursos que no estarían disponibles para
   el controlador de pruebas.

   La bandera *SKIP* también se puede usar para temporalmente "quitar"
   ejemplos.

doctest.COMPARISON_FLAGS

   Una máscara de bits o juntadas lógicamente todas las banderas de
   arriba.

El segundo grupo de opciones controla cómo las fallas de las pruebas
son reportadas:

doctest.REPORT_UDIFF

   Cuando se especifica, las fallas que involucran salidas multilínea
   esperadas y reales son mostradas usando una diferencia (*diff*)
   unificada.

doctest.REPORT_CDIFF

   Cuando se especifica, las fallas que involucran salidas multilínea
   esperadas y reales se mostrarán usando una diferencia (*diff*)
   contextual.

doctest.REPORT_NDIFF

   Cuando se especifica, las diferencias son computadas por
   "difflib.Differ", usando el mismo algoritmo que la popular utilidad
   "ndiff.py". Este es el único método que marca diferencias dentro de
   líneas también como a través de líneas. Por ejemplo, si una línea
   de salida esperada contiene el dígito "1" donde la salida actual
   contiene la letra "l", se inserta una línea con una marca de
   inserción marcando la posición de las columnas que no coinciden.

doctest.REPORT_ONLY_FIRST_FAILURE

   Cuando se especifica, muestra el primer ejemplo fallido en cada
   doctest, pero suprime la salida para todos ejemplos restantes. Esto
   evitará que doctest reporte los ejemplos correctos que se rompen
   por causa de fallos tempranos; pero también puede esconder ejemplos
   incorrectos que fallen independientemente de la primera falla.
   Cuando se especifica "REPORT_ONLY_FIRST_FAILURE", los ejemplos
   restantes aún se ejecutan, y aún cuentan para el número total de
   fallas reportadas, sólo se suprime la salida.

doctest.FAIL_FAST

   Cuando se especifica, sale después del primer ejemplo fallido y no
   intenta ejecutar los ejemplos restantes. Por consiguiente, el
   número de fallas reportadas será como mucho 1. Esta bandera puede
   ser útil durante la depuración, ya que los ejemplos después de la
   primera falla ni siquiera producirán salida de depuración.

doctest.REPORTING_FLAGS

   Una máscara de bits o todas las banderas de reporte arriba
   combinadas.

There is also a way to register new option flag names, though this
isn't useful unless you intend to extend "doctest" internals via
subclassing:

doctest.register_optionflag(name)

   Crea una nueva bandera de opción con un nombre dado, y retorna el
   valor entero de la nueva bandera. se puede usar
   "register_optionflag()" cuando se hereda "OutputChecker" o
   "DocTestRunner" para crear nuevas opciones que sean compatibles con
   tus clases heredadas. "register_optionflag()" siempre debe ser
   llamado usando la siguiente expresión:

      MY_FLAG = register_optionflag('MY_FLAG')

### Directivas

Se pueden usar las directivas de doctest para modificar las banderas
de opción para un ejemplo individual. Las directivas de doctest son
comentarios de Python especiales que siguen el código fuente de un
ejemplo:

   directive:             "#" "doctest:" directive_options
   directive_options:     directive_option ("," directive_option)*
   directive_option:      on_or_off directive_option_name
   on_or_off:             "+" | "-"
   directive_option_name: "DONT_ACCEPT_BLANKLINE" | "NORMALIZE_WHITESPACE" | ...

No se permite el espacio en blanco entre el "+" o "-" y el nombre de
la opción de directiva (*directive option name*). El nombre de la
opción de directiva puede ser cualquiera de los nombres de las
banderas de opciones explicadas arriba.

Las directivas de doctest de un ejemplo modifican el comportamiento de
doctest para ese único ejemplo. Usa "+" para habilitar el
comportamiento nombrado, o "-" para deshabilitarlo.

Por ejemplo, esta prueba se ejecuta con normalidad:

   >>> print(list(range(20)))  # doctest: +NORMALIZE_WHITESPACE
   [0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
   10,  11, 12, 13, 14, 15, 16, 17, 18, 19]

Sin la directiva esto fallaría, porque de hecho la salida verdadera no
tiene dos espacios en blanco antes de cada elemento de la lista, y
además porque la la salida verdadera está en una sola línea. Mientras
tanto, la siguiente prueba también pasa, y de la misma forma requiere
de directivas para hacerlo:

   >>> print(list(range(20)))  # doctest: +ELLIPSIS
   [0, 1, ..., 18, 19]

Se pueden usar varias directivas en una sola línea, separadas por
comas:

   >>> print(list(range(20)))  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
   [0,    1, ...,   18,    19]

Si las diferentes directivas se usan para un sólo ejemplo, entonces
estas se combinarán:

   >>> print(list(range(20)))  # doctest: +ELLIPSIS
   ...                         # doctest: +NORMALIZE_WHITESPACE
   [0,    1, ...,   18,    19]

Como se muestran en los ejemplos anteriores, puedes añadir líneas de
"..." a tus ejemplos conteniendo sólo directivas. Puede ser útil
cuando un ejemplo es demasiado largo para que una directiva pueda
caber cómodamente en la misma línea:

   >>> print(list(range(5)) + list(range(10, 20)) + list(range(30, 40)))
   ... # doctest: +ELLIPSIS
   [0, ..., 4, 10, ..., 19, 30, ..., 39]

Tenga en cuenta que ya que todas las opciones están deshabilitadas por
defecto, y las directivas sólo aplican a los ejemplos en los que
aparecen, habilitarlas (a través de "+" en la directiva) usualmente es
la única opción significativa. Sin embargo, las banderas de opciones
también pueden ser pasadas a funciones que ejecutan doctests,
estableciendo valores por defecto diferentes. En tales casos,
deshabilitar una opción a través de "-" en una directiva puede ser
útil.

### Advertencias

"doctest" is serious about requiring exact matches in expected output.
If even a single character doesn't match, the test fails.  This will
probably surprise you a few times, as you learn exactly what Python
does and doesn't guarantee about output.  For example, when printing a
set, Python doesn't guarantee that the element is printed in any
particular order, so a test like

   >>> foo()
   {"spam", "eggs"}

¡es vulnerable! Una solución puede ser hacer:

   >>> foo() == {"spam", "eggs"}
   True

en su lugar. Otra es hacer

   >>> d = sorted(foo())
   >>> d
   ['eggs', 'spam']

Existen otros casos, pero ya captas la idea.

Otra mala idea es imprimir elementos que tienen la dirección de un
objeto, como por ejemplo

   >>> id(1.0)  # certain to fail some of the time
   7948648
   >>> class C: pass
   >>> C()  # the default repr() for instances embeds an address
   <C object at 0x00AC18F0>

Con la directiva "ELLIPSIS" podemos sacar ventaja del último ejemplo:

   >>> C()  # doctest: +ELLIPSIS
   <C object at 0x...>

Floating-point numbers are also subject to small output variations
across platforms, because Python defers to the platform C library for
some floating-point calculations, and C libraries vary widely in
quality here.

   >>> 1000**0.1  # risky
   1.9952623149688797
   >>> round(1000**0.1, 9) # safer
   1.995262315
   >>> print(f'{1000**0.1:.4f}') # much safer
   1.9953

Números de la forma "I/2.**J" son seguros a lo largo de todas las
plataformas, y yo frecuentemente planeo ejemplos de doctest para
producir números de esa forma:

   >>> 3./4  # utterly safe
   0.75

Las facciones simples también son más fáciles de entender para las
personas, y eso conduce a una mejor documentación.

## API básica

Las funciones "testmod()" y "testfile()" proporcionan una interfaz
simple para doctest que debe ser suficiente para la mayoría de los
usos básicos. Para una introducción menos formal a estas funciones,
véase las secciones Uso simple: verificar ejemplos en docstrings y Uso
Simple: Verificar ejemplos en un Archivo de Texto.

doctest.testfile(filename, module_relative=True, name=None, package=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, parser=DocTestParser(), encoding=None)

   Todos los argumentos excepto *filename* son opcionales, y deben ser
   especificados en forma de palabras claves.

   Prueba los ejemplos en el archivo con nombre *filename*. Retorna
   "(failure_count, test_count)".

   El argumento opcional *module_relative* especifica cómo el nombre
   de archivo debe ser interpretado:

   * Si *module_relative* es "True" (el valor por defecto), entonces
     *filename* especifica una ruta relativa al módulo que es
     independiente del SO. Por defecto, esta ruta es relativa al
     directorio del módulo que lo invoca; pero si el argumento
     *package* es especificado, entonces es relativo a ese paquete.
     Para asegurar la independencia del SO, *filename* debe usar
     caracteres "/" para separar segmentos, y no puede ser una ruta
     absoluta (por ejemplo., no puede empezar con "/").

   * Si *module_relative* es "False", entonces *filename* especifica
     una ruta especifica del SO. La ruta puede ser absoluta o
     relativa; las rutas relativas son resueltas con respecto al
     directorio de trabajo actual.

   El argumento opcional *name* proporciona el nombre de la prueba;
   por defecto, o si es "None", se usa "os.path.basename(filename)".

   El argumento opcional *package* es un paquete de Python o el nombre
   de una paquete de Python cuyo directorio debe ser usado como el
   directorio base para un nombre de archivo relativo al módulo. Si no
   se especifica ningún paquete, entonces el directorio del módulo que
   invoca se usa como el directorio base para los nombres de archivos
   relativos al módulo. Es un error especificar *package* si
   *module_relative* es "False".

   El argumento opcional *globs* proporciona un diccionario a ser
   usado como los globales cuando se ejecuten los ejemplos. Se crea
   una nueva copia superficial de este diccionario para el doctest,
   por lo que sus ejemplos empiezan con una pizarra en blanco. Por
   defecto, o si es "None", se usa un nuevo diccionario vacío.

   El argumento opcional *extraglobs* proporciona un diccionario
   mezclado con los globales usados para ejecutar ejemplos. Funciona
   como "dict.update()": si *globs* y *extraglobs* tienen una clave en
   común, el valor asociado en *extraglobs* aparece en el diccionario
   combinado. Por defecto, o si es "None", no se usa ninguna variable
   global. Es una característica avanzada que permite la
   parametrización de doctests. Por ejemplo, un doctest puede ser
   escribo para una clase base, usando un nombre genérico para la
   clase, y luego reusado para probar cualquier número de clases
   heredadas al pasar un diccionario de *extraglobs* mapeando el
   nombre genérico a la clase heredada para ser probada.

   Optional argument *verbose* prints lots of stuff if true, and
   prints only failures if false; by default, or if "None", it's true
   if and only if "'-v'" is in "sys.argv".

   El argumento opcional *report* imprime un resumen al final cuando
   es verdadero; si no, no imprime nada al final. En modo verboso
   (*verbose*), el resumen es detallado; si no, el resumen es muy
   corto (de hecho, vacío si todos las pruebas pasan).

   Optional argument *optionflags* (default value "0") takes the
   bitwise OR of option flags. See section Banderas de Opción.

   El argumento opcional *raise_on_error* tiene como valor por defecto
   *false*. Si es *true*, se lanza una excepción sobre la primera
   falla o excepción no esperada en un ejemplo. Esto permite que los
   fallos sean depurados en un análisis a posteriori. El
   comportamiento por defecto es continuar corriendo los ejemplos.

   El argumento opcional *parser* especifica un "DocTestParser" (o
   subclase) que debe ser usado para extraer las pruebas de los
   archivos. Su valor por defecto es un analizador sintáctico normal
   (i.e., "DocTestParser()").

   El argumento opcional *encoding* especifica una codificación que
   debe ser usada para convertir el archivo a *unicode*.

doctest.testmod(m=None, name=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, exclude_empty=False)

   Todos los argumentos son opcionales, y todos excepto por *m* deben
   ser especificados en forma de palabras claves.

   Prueba los ejemplos en los docstring de las funciones y clases
   alcanzables desde el módulo *m* (o desde el módulo "__main__" si
   *m* no es proporcionado o es "None"), empezando con "m.__doc__".

   Also test examples reachable from dict "m.__test__", if it exists.
   "m.__test__" maps names (strings) to functions, classes and
   strings; function and class docstrings are searched for examples;
   strings are searched directly, as if they were docstrings.

   Sólo se buscan los docstrings anexados a los objetos pertenecientes
   al módulo *m*.

   Retorna "(failure_count, test_count)".

   El argumento opcional *name* proporciona el nombre del módulo; por
   defecto, o si es "None", se usa "m.__name__".

   Optional argument *exclude_empty* defaults to false.  If true,
   objects for which no doctests are found are excluded from
   consideration. The default is a backward compatibility hack, so
   that code still using "doctest.master.summarize" in conjunction
   with "testmod()" continues to get output for objects with no tests.
   The *exclude_empty* argument to the newer "DocTestFinder"
   constructor defaults to true.

   Los argumentos opcionales *extraglobs*, *verbose*, *report*,
   *optionflags*, *raise_on_error*, y *globs* son los mismos en cuanto
   a la función "testfile()" arriba, excepto que *globs* es por
   defecto "m.__dict__".

doctest.run_docstring_examples(f, globs, verbose=False, name='NoName', compileflags=None, optionflags=0)

   Prueba los ejemplos asociados con el objeto *f*; por ejemplo, *f*
   puede ser una cadena de caracteres, un módulo, una función, o un
   objeto clase.

   Una copia superficial del diccionario del argumento *globs* se usa
   para la ejecución del contexto.

   Se usa el argumento opcional *name* en mensajes de fallos, y por
   defecto es ""NoName"".

   Si el argumento opcional *verbose* es verdadero, la salida se
   genera incluso si no hay fallas. Por defecto, la salida se genera
   sólo en caso de la falla de un ejemplo.

   El argumento opcional *compileflags* proporciona el conjunto de
   banderas que se deben usar por el compilador de Python cuando se
   corran los ejemplos. Por defecto, o si es "None", las banderas se
   deducen correspondiendo al conjunto de características futuras
   encontradas en *globs*.

   El argumento opcional *optionflags* trabaja con respecto a la
   función "testfile()" de arriba.

## API de unittest

As your collection of doctest'ed modules grows, you'll want a way to
run all their doctests systematically.  "doctest" provides two
functions that can be used to create "unittest" test suites from
modules and text files containing doctests.  To integrate with
"unittest" test discovery, include a load_tests function in your test
module:

   import unittest
   import doctest
   import my_module_with_doctests

   def load_tests(loader, tests, ignore):
       tests.addTests(doctest.DocTestSuite(my_module_with_doctests))
       return tests

Hay dos funciones principales para crear instancias de
"unittest.TestSuite" desde los archivos de texto y módulos con
doctests:

doctest.DocFileSuite(*paths, module_relative=True, package=None, setUp=None, tearDown=None, globs=None, optionflags=0, parser=DocTestParser(), encoding=None)

   Convierte las pruebas de doctest de uno o más archivos de texto a
   una "unittest.TestSuite".

   The returned "unittest.TestSuite" is to be run by the unittest
   framework and runs the interactive examples in each file.  If an
   example in any file fails, then the synthesized unit test fails,
   and a "failureException" exception is raised showing the name of
   the file containing the test and a (sometimes approximate) line
   number.  If all the examples in a file are skipped, then the
   synthesized unit test is also marked as skipped.

   Pasa una o más rutas (como cadenas de caracteres) a archivos de
   texto para ser examinados.

   Se pueden proporcionar las opciones como argumentos por palabra
   clave:

   El argumento opcional *module_relative* especifica cómo los nombres
   de archivos en *paths* se deben interpretar:

   * Si *module_relative* is "True" (el  valor por defecto), entonces
     cada archivo de nombre en *paths* especifica una ruta relativa al
     módulo independiente del SO. Por defecto, esta ruta es relativa
     al directorio del módulo lo está invocando; pero si se especifica
     el argumento *package*, entonces es relativo a ese paquete. Para
     asegurar la independencia del SO, cada nombre de archivo debe
     usar caracteres "/" para separar los segmentos de rutas, y puede
     no ser una ruta absoluta (i.e., puede no empezar con "/").

   * Si *module_relative* es "False", entonces cada archivo de nombre
     en *paths* especifica una ruta especifica al SO. La ruta puede
     ser absoluta o relativa; las rutas relativas son resueltas con
     respecto a directorio de trabajo actual.

   El argumento opcional *package* es un paquete de Python o el nombre
   de un paquete de Python cuyo directorio debe ser usado como el
   directorio base para los nombres de archivos relativos al módulo en
   *paths*. Si no se especifica ningún paquete, entonces el directorio
   del módulo que lo está invocando se usa como el directorio base
   para los archivos de nombres relativos al módulo. Es un error
   especificar *package* si *module_relative* es "False".

   Optional argument *setUp* specifies a set-up function for the test
   suite. This is called before running the tests in each file.  The
   *setUp* function will be passed a "DocTest" object.  The *setUp*
   function can access the test globals as the "globs" attribute of
   the test passed.

   Optional argument *tearDown* specifies a tear-down function for the
   test suite.  This is called after running the tests in each file.
   The *tearDown* function will be passed a "DocTest" object.  The
   *tearDown* function can access the test globals as the "globs"
   attribute of the test passed.

   El argumento opcional *globs* es un diccionario que contiene las
   variables globales iniciales para las pruebas. Se crea una nueva
   copia de este diccionario para cada prueba. Por defecto, *globs* es
   un nuevo diccionario vacío.

   El argumento opcional *optionflags* especifica las opciones de
   doctest por defecto para las pruebas, creado al juntar lógicamente
   las opciones de bandera individuales. Véase la sección Banderas de
   Opción. Véase la función "set_unittest_reportflags()" abajo para
   una mejor manera de definir las opciones de informe.

   El argumento opcional *parser* especifica un "DocTestParser" (o
   subclase) que debe ser usado para extraer las pruebas de los
   archivos. Su valor por defecto es un analizador sintáctico normal
   (i.e., "DocTestParser()").

   El argumento opcional *encoding* especifica una codificación que
   debe ser usada para convertir el archivo a *unicode*.

   Se añade el global "__file__" a los globales proporcionados a los
   doctests cargados desde un archivo de texto usando
   "DocFileSuite()".

doctest.DocTestSuite(module=None, globs=None, extraglobs=None, test_finder=None, setUp=None, tearDown=None, optionflags=0, checker=None)

   Convierte las pruebas de doctest para un módulo a un
   "unittest.TestSuite".

   The returned "unittest.TestSuite" is to be run by the unittest
   framework and runs each doctest in the module. Each docstring is
   run as a separate unit test. If any of the doctests fail, then the
   synthesized unit test fails, and a
   "unittest.TestCase.failureException" exception is raised showing
   the name of the file containing the test and a (sometimes
   approximate) line number.  If all the examples in a docstring are
   skipped, then the

   El argumento opcional *module* proporciona el módulo a probar.
   Puede ser un objeto de módulo o un nombre (posiblemente punteado)
   de módulo. Si no se especifica, se usa el módulo que invoca esta
   función.

   Optional argument *globs* is a dictionary containing the initial
   global variables for the tests.  A new copy of this dictionary is
   created for each test.  By default, *globs* is the module's
   "__dict__".

   El argumento opcional *extraglobs* especifica un conjunto de
   variables globales adicionales que son mezcladas con *globs*. Por
   defecto, no se usa ningún global adicional.

   El argumento opcional *test_finder* es el objeto "DocTestFinder" (o
   un reemplazo directo) que se usa para extraer doctests desde el
   módulo.

   Optional arguments *setUp*, *tearDown*, and *optionflags* are the
   same as for function "DocFileSuite()" above, but they are called
   for each docstring.

   Esta función usa la misma técnica de búsqueda que "testmod()".

   Distinto en la versión 3.5: "DocTestSuite()" retorna un
   "unittest.TestSuite" vacío si *module* no contiene ningún docstring
   en vez de lanzar  un "ValueError".

Under the covers, "DocTestSuite()" creates a "unittest.TestSuite" out
of "doctest.DocTestCase" instances, and "DocTestCase" is a subclass of
"unittest.TestCase". "DocTestCase" isn't documented here (it's an
internal detail), but studying its code can answer questions about the
exact details of "unittest" integration.

Similarly, "DocFileSuite()" creates a "unittest.TestSuite" out of
"doctest.DocFileCase" instances, and "DocFileCase" is a subclass of
"DocTestCase".

So both ways of creating a "unittest.TestSuite" run instances of
"DocTestCase".  This is important for a subtle reason: when you run
"doctest" functions yourself, you can control the "doctest" options in
use directly, by passing option flags to "doctest" functions.
However, if you're writing a "unittest" framework, "unittest"
ultimately controls when and how tests get run.  The framework author
typically wants to control "doctest" reporting options (perhaps, e.g.,
specified by command line options), but there's no way to pass options
through "unittest" to "doctest" test runners.

For this reason, "doctest" also supports a notion of "doctest"
reporting flags specific to "unittest" support, via this function:

doctest.set_unittest_reportflags(flags)

   Set the "doctest" reporting flags to use.

   El argumento *flags* toma la combinación por el operador OR de las
   banderas de opciones. Véase la sección Banderas de Opción. Sólo se
   pueden usar las "banderas de informe".

   This is a module-global setting, and affects all future doctests
   run by module "unittest":  the "runTest()" method of "DocTestCase"
   looks at the option flags specified for the test case when the
   "DocTestCase" instance was constructed.  If no reporting flags were
   specified (which is the typical and expected case), "doctest"'s
   "unittest" reporting flags are bitwise ORed into the option flags,
   and the option flags so augmented are passed to the "DocTestRunner"
   instance created to run the doctest.  If any reporting flags were
   specified when the "DocTestCase" instance was constructed,
   "doctest"'s "unittest" reporting flags are ignored.

   La función retorna el valor de las banderas de informe de
   "unittest" en efecto antes de que la función fuera invocada.

## API avanzada

La API básica es un simple envoltorio que sirve para hacer los doctest
fáciles de usar. Es bastante flexible, y debe cumplir las necesidades
de la mayoría de los usuarios; si requieres un control más preciso en
las pruebas, o deseas extender las capacidades de doctest, entonces
debes usar la API avanzada.

La API avanzada gira en torno a dos clases contenedoras, que se usan
para guardar los ejemplos interactivos extraídos de los casos doctest:

* "Example": Un *statement* de Python, emparejado con su salida
  esperada.

* "DocTest": Una colección de clases "Example", típicamente extraídos
  de un sólo docstring o archivo de texto.

Se definen clases de procesamiento adicionales para encontrar,
analizar sintácticamente, y ejecutar, y comprobar ejemplos de doctest:

* "DocTestFinder": Encuentra todos los docstrings en un módulo dado, y
  usa un "DocTestParser" para crear un "DocTest" de cada docstring que
  contiene ejemplos interactivos.

* "DocTestParser": Crea un objeto "DocTest" de una cadena de
  caracteres (tal como un docstring de un objeto).

* "DocTestRunner": Ejecuta los ejemplos en un "DocTest", y usa un
  "OutputChecker" para verificar su salida.

* "OutputChecker": Compara la salida real de un ejemplo de doctest con
  la salida esperada, y decide si coinciden.

Las relaciones entre estas clases de procesamiento se resumen en el
siguiente diagrama:

                               list of:
   +------+                   +---------+
   |module| --DocTestFinder-> | DocTest | --DocTestRunner-> results
   +------+    |        ^     +---------+     |       ^    (printed)
               |        |     | Example |     |       |
               v        |     |   ...   |     v       |
              DocTestParser   | Example |   OutputChecker
                              +---------+

### Objetos DocTest

class doctest.DocTest(examples, globs, name, filename, lineno, docstring)

   Una colección de ejemplos de doctest que deben ejecutarse en un
   sólo nombre de espacios. Se usan los argumentos del constructor
   para inicializar los atributos de los mismos nombres.

   "DocTest" define los siguientes atributos. Son inicializados por el
   constructor, y no deben ser modificados directamente.

   examples

      Una lista de objetos "Example" codificando los ejemplos
      interactivos de Python individuales que esta prueba debe
      ejecutar.

   globs

      El nombre de espacios (alias *globals*) en que los ejemplos se
      deben ejecutar. Este es un diccionario que mapea nombres a
      valores. Cualquier cambio al nombre de espacios hecho por los
      ejemplos (tal como juntar nuevas variables) se reflejará en
      "globs" después de que se ejecute la prueba.

   name

      Un nombre de cadena de caracteres que identifica el "DocTest".
      Normalmente, este es el nombre del objeto o archivo del que se
      extrajo la prueba.

   filename

      The name of the file that this "DocTest" was extracted from; or
      "None" if the filename is unknown, or if the "DocTest" was not
      extracted from a file.

   lineno

      El número de línea dentro de "filename" donde este "DocTest"
      comienza, o "None" si el número de línea no está disponible.
      Este número de línea es comienza en 0 con respecto al comienzo
      del archivo.

   docstring

      La cadena de caracteres del que se extrajo la cadena, o "None"
      si la cadena no está disponible, o si la prueba no se extrajo de
      una cadena de caracteres.

### Objetos *Example*

class doctest.Example(source, want, exc_msg=None, lineno=0, indent=0, options=None)

   Un sólo ejemplo interactivo, que consta de una sentencia de Python
   y su salida esperada. Los argumentos del constructor se usan para
   inicializar los atributos del mismo nombre.

   La clase "Example" define los siguientes atributos. Son
   inicializados por el constructor, y no deben ser modificados
   directamente.

   source

      Una cadena de caracteres que contiene el código fuente del
      ejemplo. Este código fuente consiste de una sola sentencia
      Python, y siempre termina en una nueva línea; el constructor
      añade una nueva línea cuando sea necesario.

   want

      La salida esperada de ejecutar el código fuente del ejemplo (o
      desde la salida estándar, o un seguimiento en caso de una
      excepción). "wants" termina con una nueva línea a menos que no
      se espera ninguna salida, en cuyo caso es una cadena vacía. El
      constructor añade una nueva línea cuando sea necesario.

   exc_msg

      El mensaje de excepción que el ejemplo genera, si se espera que
      el ejemplo genere una excepción; o "None" si no se espera que
      genere una excepción. Se compara este mensaje de excepción con
      el valor de retorno de "traceback.format_exception_only()".
      "exc_msg" termina con una nueva línea a menos que sea "None".
      El constructor añade una nueva línea si se necesita.

   lineno

      El número de línea dentro de la cadena de caracteres que
      contiene este ejemplo donde el ejemplo comienza. Este número de
      línea comienza en 0 con respecto al comienzo de la cadena que lo
      contiene.

   indent

      La sangría del ejemplo en la cadena que lo contiene; i.e., el
      número de caracteres de espacio que preceden la primera entrada
      del ejemplo.

   options

      A dictionary mapping from option flags to "True" or "False",
      which is used to override default options for this example.  Any
      option flags not contained in this dictionary are left at their
      default value (as specified by the "DocTestRunner"'s
      optionflags). By default, no options are set.

### Objetos *DocTestFinder*

class doctest.DocTestFinder(verbose=False, parser=DocTestParser(), recurse=True, exclude_empty=True)

   Una clase de procesamiento que se usa para extraer los "DocTest"
   que son relevantes para un objeto dado, desde su docstring y los
   docstring de sus objetos contenidos. Se puede extraer los "DocTest"
   de los módulos, clases, funciones, métodos, métodos estáticos,
   métodos de clase, y propiedades.

   Se puede usar el argumento opcional *verbose* para mostrar los
   objetos buscados por *finder*. Su valor por defecto es "False"
   (ninguna salida).

   El argumento opcional *parser* especifica el objeto "DocTestParser"
   (o un reemplazo directo) que se usa para extraer doctests desde
   docstrings.

   Si el argumento opcional *recurse* es falso, entonces el método
   "DocTestFinder.find()" sólo examinará el objeto dado, y no
   cualquier objeto contenido.

   Si el argumento opcional *exclude_empty* es falso, entonces
   "DocTestFinder.find()" incluirá pruebas para objetos con docstrings
   vacíos.

   "DocTestFinder" define los siguientes métodos:

   find(obj[, name][, module][, globs][, extraglobs])

      Retorna una lista de los "Doctest" que se definen por el
      docstring de *obj*, o por cualquiera de los docstring de sus
      objetos contenidos.

      El argumento opcional *name* especifica el nombre del objeto;
      este nombre será usado para construir los nombres de los
      "DocTest" retornados. Si *name* no se especifica, entonces se
      usa "obj.__name__".

      El parámetro opcional *module* es el módulo que contiene el
      objeto dado. Si no se especifica el módulo o si es "None",
      entonces el buscador de pruebas tratará de determinar
      automáticamente el módulo correcto. Se usa el módulo del objeto:

      * Como un espacio de nombres por defecto, si no se especifica
        *globs*.

      * Para evitar que *DocTestFinder* extraiga DocTests desde
        objetos que se importan desde otros módulos. (Se ignoran
        objetos contenidos con módulos aparte de *module*.)

      * Para encontrar el nombre del archivo conteniendo el objeto.

      * Para ayudar a encontrar el número de línea del objeto dentro
        de su archivo.

      Si *module* es falso, no se hará ningún intento de encontrar el
      módulo. Es poco claro, de uso mayormente para probar doctest en
      si mismo: si *module* es "False", o es "None" pero no se puede
      encontrar automáticamente, entonces todos los objetos se
      consideran que pertenecen al módulo (inexistente), por lo que
      todos los objetos contenidos se buscarán (recursivamente) por
      doctests.

      The globals for each "DocTest" is formed by combining *globs*
      and *extraglobs* (bindings in *extraglobs* override bindings in
      *globs*).  A new shallow copy of the globals dictionary is
      created for each "DocTest". If *globs* is not specified, then it
      defaults to the module's "__dict__", if specified, or "{}"
      otherwise. If *extraglobs* is not specified, then it defaults to
      "{}".

### Objetos *DocTestParser*

class doctest.DocTestParser

   Un clase de procesamiento usada para extraer ejemplos interactivos
   de una cadena de caracteres, y usarlos para crear un objeto
   "DocTest".

   "DocTestParser" define los siguientes métodos:

   get_doctest(string, globs, name, filename, lineno)

      Extrae todos los ejemplos de *doctest* de una cadena dada, y los
      recolecta en un objeto "DocTest".

      *globs*, *name*, *filename*, and *lineno* are attributes for the
      new "DocTest" object.  See the documentation for "DocTest" for
      more information.

   get_examples(string, name='<string>')

      Extrae todos los ejemplos de la cadena de caracteres dada, y los
      retorna como una lista de objetos "Example". Los números de
      línea empiezan en 0. El argumento opcional *name* es una nombre
      identificando esta cadena, y sólo es usada para mensajes de
      errores.

   parse(string, name='<string>')

      Divide the given string into examples and intervening text, and
      return them as a list of alternating "Example"s and strings.
      Line numbers for the "Example"s are 0-based.  The optional
      argument *name* is a name identifying this string, and is only
      used for error messages.

### TestResults objects

class doctest.TestResults(failed, attempted)

   failed

      Number of failed tests.

   attempted

      Number of attempted tests.

   skipped

      Number of skipped tests.

      Added in version 3.13.

### Objetos *DocTestRunner*

class doctest.DocTestRunner(checker=None, verbose=None, optionflags=0)

   Una clase de procesamiento usada para ejecutar y verificar los
   ejemplos interactivos en un "DocTest".

   The comparison between expected outputs and actual outputs is done
   by an "OutputChecker".  This comparison may be customized with a
   number of option flags; see section Banderas de Opción for more
   information.  If the option flags are insufficient, then the
   comparison may also be customized by passing a subclass of
   "OutputChecker" to the constructor.

   The test runner's display output can be controlled in two ways.
   First, an output function can be passed to "run()"; this function
   will be called with strings that should be displayed.  It defaults
   to "sys.stdout.write".  If capturing the output is not sufficient,
   then the display output can be also customized by subclassing
   DocTestRunner, and overriding the methods "report_start()",
   "report_success()", "report_unexpected_exception()", and
   "report_failure()".

   El argumento por palabra clave opcional *checker* especifica el
   objeto "OutputChecker" (o un reemplazo directo) que se debe usar
   para comparar las salidas esperadas con las salidas reales de los
   ejemplos de doctest.

   El argumento por palabra clave opcional *verbose* controla la
   verbosidad de "DocTestRunner". Si *verbose* es "True", entonces la
   información de cada ejemplo se imprime , mientras se ejecuta. Si
   *verbose* es "False", entonces sólo las fallas se imprimen. Si
   *verbose* no se especifica, o es "None", entonces la salida verbosa
   se usa si y sólo se usa el modificador de la línea de comandos
   "-v".

   El argumento por palabra clave opcional *optionflags* se puede usar
   para controlar cómo el *test runner* compara la salida esperada con
   una salida real, y cómo muestra las fallas. Para más información,
   véase la sección Banderas de Opción.

   The test runner accumulates statistics. The aggregated number of
   attempted, failed and skipped examples is also available via the
   "tries", "failures" and "skips" attributes. The "run()" and
   "summarize()" methods return a "TestResults" instance.

   "DocTestRunner" defines the following methods:

   report_start(out, test, example)

      Notifica que el *test runner* está a punto de procesar el
      ejemplo dado. Este método es proporcionado para permitir que
      clases heredadas de "DocTestRunner" personalicen su salida; no
      debe ser invocado directamente.

      *example* is the example about to be processed.  *test* is the
      test containing *example*.  *out* is the output function that
      was passed to "DocTestRunner.run()".

   report_success(out, test, example, got)

      Notifica que el ejemplo dado se ejecutó correctamente. Este
      método es proporcionado para permitir que las clases heredadas
      de "DocTestRunner" personalicen su salida; no debe ser invocado
      directamente.

      *example* es el ejemplo a punto de ser procesado. *got* es la
      salida real del ejemplo. *test* es la prueba conteniendo
      *example*. *out* es la función de salida que se pasa a
      "DocTestRunner.run()".

   report_failure(out, test, example, got)

      Notifica que el ejemplo dado falló. Este método es proporcionado
      para permitir que clases heredadas de "DocTestRunner"
      personalicen su salida; no debe ser invocado directamente.

      *example* es el ejemplo a punto de ser procesado. *got* es la
      salida real del ejemplo. *test* es la prueba conteniendo
      *example*. *out* es la función de salida que se pasa a
      "DocTestRunner.run()".

   report_unexpected_exception(out, test, example, exc_info)

      Notifica que el ejemplo dado lanzó una excepción inesperada.
      Este método es proporcionado para permitir que las clases
      heredadas de "DocTestRunner" personalicen su salida; no debe ser
      invocado directamente.

      *example* es el ejemplo a punto de ser procesado, *exc_info* es
      una tupla que contiene información sobre la excepción inesperada
      (como se retorna por "sys.exc_info()"). *test* es la prueba
      conteniendo *example*. *out* es la función de salida que debe
      ser pasada a "DocTestRunner.run()".

   run(test, compileflags=None, out=None, clear_globs=True)

      Run the examples in *test* (a "DocTest" object), and display the
      results using the writer function *out*. Return a "TestResults"
      instance.

      Los ejemplo se ejecutan en el espacio de nombres "test.globs".
      Si *clear_globs* es verdadero (el valor por defecto), entonces
      este espacio de nombres será limpiado después de la prueba se
      ejecute, para ayudar con la colección de basura. Si quisieras
      examinar el espacio de nombres después de que la prueba se
      complete, entonces use *clear_globs=False*.

      *compileflags* da el conjunto de banderas que se deben usar por
      el compilador de Python cuando se ejecutan los ejemplos. Si no
      se especifica, entonces su valor por defecto será el conjunto de
      banderas de *future-import* que aplican a *globs*.

      The output of each example is checked using the
      "DocTestRunner"'s output checker, and the results are formatted
      by the "DocTestRunner.report_*()" methods.

   summarize(verbose=None)

      Print a summary of all the test cases that have been run by this
      DocTestRunner, and return a "TestResults" instance.

      El argumento opcional *verbose* controla qué tan detallado es el
      resumen. Si no se especifica la verbosidad, entonces se usa la
      verbosidad de "DocTestRunner".

   "DocTestParser" has the following attributes:

   tries

      Number of attempted examples.

   failures

      Number of failed examples.

   skips

      Number of skipped examples.

      Added in version 3.13.

### Objetos *OutputChecker*

class doctest.OutputChecker

   Una clase que se usa para verificar si la salida real de un ejemplo
   de doctest coincide con la salida esperada. "OutputChecker" define
   dos métodos: "check_output()", que compara un par de salidas dadas,
   y retorna "True" si coinciden; y "output_difference()", que retorna
   una cadena que describe las diferencias entre las dos salidas.

   "OutputChecker" define los siguientes métodos:

   check_output(want, got, optionflags)

      Retorna "True" si y sólo si la salida real de un ejemplo (*got*)
      coincide con la salida esperada (*want*). Siempre se considera
      que estas cadenas coinciden si son idénticas; pero dependiendo
      de qué banderas de opción el *test runner* esté usando, varias
      coincidencias inexactas son posibles. Véase la sección Banderas
      de Opción para más información sobre las banderas de opción.

   output_difference(example, got, optionflags)

      Retorna una cadena que describe las diferencias entre la salida
      esperada para un ejemplo dado (*example*) y la salida real
      (*got*). *optionflags* es el conjunto de banderas de opción
      usado para comparar *want* y *got*.

## Depuración

Doctest proporciona varios mecanismos para depurar los ejemplos de
doctest:

* Varias funciones convierten los doctest en programas de Python
  ejecutables, que pueden ser ejecutadas bajo el depurador de Python,
  "pdb".

* La clase "DebugRunner" es una subclase de "DocTestRunner" que lanza
  una excepción por el primer ejemplo fallido, conteniendo información
  sobre ese ejemplo. Esta información se puede usar para realizar
  depuración a posteriori en el ejemplo.

* Los casos de "unittest" generados por "DocTestSuite()" admiten el
  método "debug()" definido por "unittest.TestCase".

* Puedes añadir una llamada a "pdb.set_trace()" en un ejemplo de
  doctest, y bajarás al depurador de Python cuando esa línea sea
  ejecutada. Entonces puedes inspeccionar los valores de las
  variables, y demás. Por ejemplo, supongamos que "a.py" contiene sólo
  este docstring de módulo:

     """
     >>> def f(x):
     ...     g(x*2)
     >>> def g(x):
     ...     print(x+3)
     ...     import pdb; pdb.set_trace()
     >>> f(3)
     9
     """

  Entonces una sesión interactiva puede lucir como esta:

     >>> import a, doctest
     >>> doctest.testmod(a)
     --Return--
     > <doctest a[1]>(3)g()->None
     -> import pdb; pdb.set_trace()
     (Pdb) list
       1     def g(x):
       2         print(x+3)
       3  ->     import pdb; pdb.set_trace()
     [EOF]
     (Pdb) p x
     6
     (Pdb) step
     --Return--
     > <doctest a[0]>(2)f()->None
     -> g(x*2)
     (Pdb) list
       1     def f(x):
       2  ->     g(x*2)
     [EOF]
     (Pdb) p x
     3
     (Pdb) step
     --Return--
     > <doctest a[2]>(1)?()->None
     -> f(3)
     (Pdb) cont
     (0, 3)
     >>>

Funciones que convierten los doctest a código de Python, y
posiblemente ejecuten el código sintetizado debajo del depurador:

doctest.script_from_examples(s)

   Convierte texto con ejemplos a un script.

   El argumento *s* es una cadena que contiene los ejemplos de
   doctest. La cadena se convierte a un script de Python, donde los
   ejemplos de doctest en *s* se convierten en código regular, y todo
   lo demás se convierte en comentarios de Python. El script generado
   se retorna como una cadena, Por ejemplo,

      import doctest
      print(doctest.script_from_examples(r"""
          Set x and y to 1 and 2.
          >>> x, y = 1, 2

          Print their sum:
          >>> print(x+y)
          3
      """))

   muestra:

      # Set x and y to 1 and 2.
      x, y = 1, 2
      #
      # Print their sum:
      print(x+y)
      # Expected:
      ## 3

   Esta función se usa internamente por otras funciones (véase más
   abajo), pero también pueden ser útiles cuando quieres transformar
   una sesión de Python interactiva en un script de Python.

doctest.testsource(module, name)

   Convierte el doctest para un objeto en un script.

   Argument *module* is a module object, or dotted name of a module,
   containing the object whose doctests are of interest.  Argument
   *name* is the name (within the module) of the object with the
   doctests of interest.  The result is a string, containing the
   object's docstring converted to a Python script, as described for
   "script_from_examples()" above.  For example, if module "a.py"
   contains a top-level function "f()", then

      import a, doctest
      print(doctest.testsource(a, "a.f"))

   prints a script version of function "f()"'s docstring, with
   doctests converted to code, and the rest placed in comments.

doctest.debug(module, name, pm=False)

   Depura los doctest para un objeto.

   Los argumentos *module* y *name* son los mismos que para la función
   "testsource()" arriba. El script de Python sintetizado para el
   docstring del objeto nombrado es escrito en un archivo temporal, y
   entonces ese archivo es ejecutado bajo el control del depurador de
   PYthon, "pdb".

   Se usa una copia superficial de "module.__dict__" para el contexto
   de ejecución local y global.

   El argumento opcional *pm* controla si se usa la depuración post-
   mortem. Si *pm* tiene un valor verdadero, el archivo de script es
   ejecutado directamente, y el depurador está involucrado sólo si el
   script termina a través del lanzamiento de una excepción. Si lo
   hace, entonces la depuración post-mortem es invocada, a través de
   "pdb.post_mortem()", pasando el objeto de rastreo desde la
   excepción sin tratar. Si no se especifica *pm*, o si es falso, el
   script se ejecuta bajo el depurador desde el inicio, a través de
   una llamada de "exec()" apropiada a "pdb.run()".

doctest.debug_src(src, pm=False, globs=None)

   Depura los doctest en una cadena de caracteres.

   Es como la función function "debug()" arriba, excepto que una
   cadena de caracteres que contiene los ejemplos de doctest se
   especifica directamente, a través del argumento *src*.

   El argumento opcional *pm* tiene el mismo significado como en la
   función "debug()" arriba.

   El argumento opcional *globs* proporciona un diccionario a usar
   como contexto de ejecución local y global. Si no se especifica, o
   es "None", se usa un diccionario vacío. Si se especifica, se usa
   una copia superficial del diccionario.

La clase "DebugRunner", y las excepciones especiales que puede lanzar,
son de más interés a los autores de frameworks de pruebas, y sólo
serán descritos brevemente aquí. Véase el código fuente, y
especialmente el docstring de "DebugRunner" (¡que es un doctest!) para
más detalles:

class doctest.DebugRunner(checker=None, verbose=None, optionflags=0)

   Una subclase de "DocTestRunner" que lanza una excepción tan pronto
   como se encuentra una falla. Si ocurre una excepción inesperada, se
   lanza una excepción "UnexpectedException", conteniendo la prueba,
   el ejemplo, y la excepción original. Si la salida no coincide,
   entonces se lanza una excepción "DocTestFailure", conteniendo la
   prueba, el ejemplo, y la salida real.

   Para información sobre los parámetros de construcción y los
   métodos, véase la documentación para "DocTestRunner" en la sección
   API avanzada.

Hay dos excepciones que se pueden lanzar por instancias de
"DebugRunner":

exception doctest.DocTestFailure(test, example, got)

   Una excepción lanzada por "DocTestRunner" para señalar que la
   salida real del ejemplo de un doctest no coincidió con su salida
   esperada. Los argumentos del constructor se usan para inicializar
   los atributos del mismo nombre.

"DocTestFailure" define los siguientes atributos:

DocTestFailure.test

   El objeto "DocTest" que estaba siendo ejecutado cuando el ejemplo
   falló.

DocTestFailure.example

   El objeto "Example" que falló.

DocTestFailure.got

   La salida real del ejemplo.

exception doctest.UnexpectedException(test, example, exc_info)

   Una excepción lanzada por "DocTestRunner" para señalar que un
   ejemplo de doctest lanzó una excepción inesperada. Los argumentos
   del constructor se usan para inicializar los atributos del mismo
   nombre.

"UnexpectedException" define los siguientes atributos:

UnexpectedException.test

   El objeto "DocTest" que estaba siendo ejecutado cuando el ejemplo
   falló.

UnexpectedException.example

   El objeto "Example" que falló.

UnexpectedException.exc_info

   Una tupla que contiene información sobre la excepción inesperada,
   como es retornado por "sys.exc_info()".

## Plataforma improvisada

As mentioned in the introduction, "doctest" has grown to have three
primary uses:

1. Verificar los ejemplos en los docstring.

2. Pruebas de regresión.

3. Documentación ejecutable / pruebas literarias.

Estos usos tienen diferentes requerimientos, y es importante
distinguirlos. En particular, llenar tus docstring con casos de prueba
desconocidos conduce a mala documentación.

When writing a docstring, choose docstring examples with care. There's
an art to this that needs to be learned---it may not be natural at
first.  Examples should add genuine value to the documentation.  A
good example can often be worth many words. If done with care, the
examples will be invaluable for your users, and will pay back the time
it takes to collect them many times over as the years go by and things
change.  I'm still amazed at how often one of my "doctest" examples
stops working after a "harmless" change.

Doctest también es una excelente herramienta para pruebas de
regresión, especialmente si no escatimas en texto explicativo. Al
intercalar prosa y ejemplos, se hace mucho más fácil mantener el
seguimiento de lo que realmente se está probando, y por qué. Cuando
una prueba falla, buena prosa puede hacer mucho más fácil comprender
cuál es el problema, y cómo debe ser arreglado. Es verdad que puedes
escribir comentarios extensos en pruebas basadas en código, pero pocos
programadores lo hacen. Quizás es porque simplemente doctest hace
escribir pruebas mucho más fácil que escribir código, mientras que
escribir comentarios en código es mucho más difícil. Pienso que va más
allá de eso: la actitud natural cuando se escribe una prueba basada en
doctest es que quieres explicar los puntos finos de tu software, e
ilustrarlos con ejemplos. Esto naturalmente lleva a archivos de
pruebas que empiezan con las características más simples, y
lógicamente progresan a complicaciones y casos extremos. Una narrativa
coherente es el resultado, en vez de una colección de funciones
aisladas que pruebas trozos aislados de funcionalidad aparentemente al
azar. Es una actitud diferente, y produce resultados diferentes,
difuminando la distinción entre probar y explicar.

Pruebas de regresión se limitan mejor a objetos o archivos dedicados.
Hay varias opciones para organizar pruebas:

* Escribe archivos de texto que contienen los casos de prueba como
  ejemplos interactivos, y prueba los archivos usando "testfile()" o
  "DocFileSuite()". Esto es lo recomendado, aunque es más fácil
  hacerlo para nuevos proyectos, diseñados desde el comienzo para usar
  doctest.

* Define funciones nombradas "_regrtest_topic" que consisten en
  docstrings únicas, que contienen casos de prueba por los tópicos
  nombrados. Estas funciones se pueden incluir en el mismo archivo que
  el módulo, o separadas en un archivo de prueba separado.

* Define a "__test__" dictionary mapping from regression test topics
  to docstrings containing test cases.

Cuando has puesto tus pruebas en un módulo, el módulo puede ser el
mismo *test runner*. Cuando una prueba falla, puedes hacer que tu
*test runner* vuelva a ejecutar sólo los doctest fallidos mientras que
tu depuras el problema. Aquí hay un ejemplo mínimo de tal *test
runner*:

   if __name__ == '__main__':
       import doctest
       flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST
       if len(sys.argv) > 1:
           name = sys.argv[1]
           if name in globals():
               obj = globals()[name]
           else:
               obj = __test__[name]
           doctest.run_docstring_examples(obj, globals(), name=name,
                                          optionflags=flags)
       else:
           fail, total = doctest.testmod(optionflags=flags)
           print(f"{fail} failures out of {total} tests")

-[ Notas al pie de página ]-

[1] No se admiten los ejemplos que contienen una salida esperada y una
    excepción. Intentar adivinar dónde una termina y la otra empieza
    es muy propenso a errores, y da lugar a una prueba confusa.
