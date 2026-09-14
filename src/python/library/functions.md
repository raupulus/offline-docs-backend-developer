---
title: Funciones incorporadas
source_url: https://docs.python.org/es/3
source_path: library/functions.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2690
---

# Funciones incorporadas

El intérprete de Python tiene una serie de funciones y tipos incluidos
en él que están siempre disponibles.  Están listados aquí en orden
alfabético.

+---------------------------+-------------------------+-------------------------+---------------------------+
| Funciones incorporadas                                                                                    |
|===========================|=========================|=========================|===========================|
| **A** "abs()" "aiter()"   | **E** "enumerate()"     | **L** "len()" "list()"  | **R** "range()" "repr()"  |
| "all()" "anext()" "any()" | "eval()" "exec()"       | "locals()"  **M**       | "reversed()" "round()"    |
| "ascii()"  **B** "bin()"  | **F** "filter()"        | "map()" "max()"         | **S** "set()" "setattr()" |
| "bool()" "breakpoint()"   | "float()" "format()"    | "memoryview()" "min()"  | "slice()" "sorted()"      |
| "bytearray()" "bytes()"   | "frozenset()"  **G**    | **N** "next()"  **O**   | "staticmethod()" "str()"  |
| **C** "callable()"        | "getattr()" "globals()" | "object()" "oct()"      | "sum()" "super()"  **T**  |
| "chr()" "classmethod()"   | **H** "hasattr()"       | "open()" "ord()"  **P** | "tuple()" "type()"  **V** |
| "compile()" "complex()"   | "hash()" "help()"       | "pow()" "print()"       | "vars()"  **Z** "zip()"   |
| **D** "delattr()"         | "hex()"  **I** "id()"   | "property()"            | **_** "__import__()"      |
| "dict()" "dir()"          | "input()" "int()"       |                         |                           |
| "divmod()"                | "isinstance()"          |                         |                           |
## |                           | "issubclass()" "iter()" |                         |                           |

abs(number, /)

   Return the absolute value of a number.  The argument may be an
   integer, a floating-point number, or an object implementing
   "__abs__()". If the argument is a complex number, its magnitude is
   returned.

aiter(async_iterable, /)

   Retorna un *asynchronous iterator* para un *asynchronous iterable*.
   Equivalente a llamar "x.__aiter__()".

   Nota: A diferencia de "iter()", "aiter()" no tiene una variante con
   2 argumentos.

   Added in version 3.10.

all(iterable, /)

   Retorna  "True"  si todos los elementos del *iterable* son
   verdaderos (o si el iterable está vacío). Equivalente a:

      def all(iterable):
          for element in iterable:
              if not element:
                  return False
          return True

awaitable anext(async_iterator, /)
awaitable anext(async_iterator, default, /)

   Cuando está esperado, retorna el siguiente elemento del
   *asynchronous iterator* otorgado, o *default* (por defecto) si se
   da y el iterador está agotado.

   Esta es la variante asincrónica del "next()" incorporado, y se
   comporta de manera similar.

   Esto llama al método "__anext__()" de *async_iterator*, retornando
   un *awaitable*. A la espera de esto se retorna el siguiente valor
   del iterador. Si se otorga *default* (por defecto), se retorna si
   el iterador está agotado, de lo contrario se lanza
   "StopAsyncIteration".

   Added in version 3.10.

any(iterable, /)

   Retorna  "True" si un elemento cualquiera del *iterable* es
   verdadero. Si el iterable está vacío, retorna "False". Equivalente
   a:

      def any(iterable):
          for element in iterable:
              if element:
                  return True
          return False

ascii(object, /)

   Como "repr()", retorna una cadena que contiene una representación
   imprimible de un objeto, pero que escapa los caracteres no ASCII
   que "repr()" retorna usando "\x", "\u" or "\U". Esto genera una
   cadena similar a la retornada por "repr()" en Python 2.

bin(integer, /)

   Convert an integer number to a binary string prefixed with "0b".
   The result is a valid Python expression. If *integer* is not a
   Python "int" object, it has to define an "__index__()" method that
   returns an integer. Some examples:

   >>> bin(3)
   '0b11'
   >>> bin(-10)
   '-0b1010'

   Según se desee o no el prefijo "0b", se puede usar uno u otro de
   las siguientes maneras.

   >>> format(14, '#b'), format(14, 'b')
   ('0b1110', '1110')
   >>> f'{14:#b}', f'{14:b}'
   ('0b1110', '1110')

   See also "enum.bin()" to represent negative values as twos-
   complement.

   Véase también "format()" para más información.

class bool(object=False, /)

   Return a Boolean value, i.e. one of "True" or "False".  The
   argument is converted using the standard truth testing procedure.
   If the argument is false or omitted, this returns "False";
   otherwise, it returns "True".  The "bool" class is a subclass of
   "int" (see Tipos numéricos --- int, float, complex). It cannot be
   subclassed further.  Its only instances are "False" and "True" (see
   Tipo Booleano --- bool).

   Distinto en la versión 3.7: The parameter is now positional-only.

breakpoint(*args, **kws)

   This function drops you into the debugger at the call site.
   Specifically, it calls "sys.breakpointhook()", passing "args" and
   "kws" straight through.  By default, "sys.breakpointhook()" calls
   "pdb.set_trace()" expecting no arguments.  In this case, it is
   purely a convenience function so you don't have to explicitly
   import "pdb" or type as much code to enter the debugger.  However,
   "sys.breakpointhook()" can be set to some other function and
   "breakpoint()" will automatically call that, allowing you to drop
   into the debugger of choice. If "sys.breakpointhook()" is not
   accessible, this function will raise "RuntimeError".

   Por defecto, el comportamiento de "breakpoint()" se puede cambiar
   con la variable de entorno "PYTHONBREAKPOINT". Véase
   "sys.breakpointhook()" para obtener detalles de uso.

   Tenga en cuenta que esto no está garantizado si se ha reemplazado
   "sys.breakpointhook()".

   Lanza un evento de auditoría "builtins.breakpoint" con
   "breakpointhook" como argumento.

   Added in version 3.7.

class bytearray(source=b'')
class bytearray(source, encoding, errors='strict')

   Retorna un nuevo array de bytes. La clase  "bytearray" es una
   secuencia mutable de enteros en el rango 0 <= x < 256. Tiene la
   mayoría de los métodos comunes en las secuencias mutables,
   descritos en Tipos de secuencia mutables, así como la mayoría de
   los métodos que la clase "bytes" tiene, véase Operaciones de bytes
   y bytearray.

   El parámetro opcional *source* puede ser empleado para inicializar
   el vector (*array*) de varias maneras distintas:

   * Si es una *string*, debes proporcionar también el parámetro
     *encoding* (y opcionalmente, *errors*; entonces "bytearray()"
     convierte la cadena a bytes empleando "str.encode()".

   * Si es un *integer*, el array tendrá ese tamaño y será
     inicializado con bytes nulos.

   * Si es un objeto conforme a interfaz de búfer, se utilizará un
     búfer de solo lectura del objeto para inicializar el arreglo de
     bytes.

   * Si es un *iterable*, debe ser un iterable de enteros en el rango
     "0 <= x < 256", que son usados como los contenidos iniciales del
     array.

   Sin argumento, se crea un array de tamaño 0.

   Ver también: Tipos de secuencias binarias --- bytes, bytearray y
   memoryview y Objetos de tipo Bytearray.

class bytes(source=b'')
class bytes(source, encoding, errors='strict')

   Retorna un nuevo objeto "bytes", que es una secuencia inmutable de
   enteros en el rango "0 <= x < 256". "bytes" es una versión
   inmutable de "bytearray" -- tiene los mismos métodos no mutables y
   el mismo comportamiento en términos de indexación y segmentación.

   En consecuencia, los argumentos del constructor son interpretados
   como los de "bytearray()".

   Los objetos de bytes también pueden ser creados con literales, ver
   Literales de cadenas y bytes.

   Ver también Tipos de secuencias binarias --- bytes, bytearray y
   memoryview, Objetos de tipo Bytes, y Operaciones de bytes y
   bytearray.

callable(object, /)

   Return "True" if the *object* argument appears callable, "False" if
   not.  If this returns "True", it is still possible that a call
   fails, but if it is "False", calling *object* will never succeed.
   Note that classes are callable (calling a class returns a new
   instance); instances are callable if their class has a "__call__()"
   method.

   Added in version 3.2: Está función fue eliminada en Python 3.0 pero
   traída de vuelta en Python 3.2.

chr(codepoint, /)

   Return the string representing a character with the specified
   Unicode code point. For example, "chr(97)" returns the string
   "'a'", while "chr(8364)" returns the string "'€'". This is the
   inverse of "ord()".

   The valid range for the argument is from 0 through 1,114,111
   (0x10FFFF in base 16).  "ValueError" will be raised if it is
   outside that range.

@classmethod

   Transforma un método en un método de clase.

   Un método de clase recibe la clase como primer argumento implícito,
   de la misma forma que un método de instancia recibe la instancia.
   Para declarar un método de clase, emplea la siguiente expresión:

      class C:
          @classmethod
          def f(cls, arg1, arg2): ...

   La forma "@classmethod" es una función *decorator* — ver
   Definiciones de funciones para más detalles.

   Un método de clase puede ser llamado en la clase (como "C.f()") o
   en la instancia (como "C().f()"). La instancia es ignorada salvo
   por su clase. Si un método de clase es llamado desde una clase
   derivada, entonces el objeto de la clase derivada se pasa como
   primer argumento implícito.

   Los métodos de clase son diferentes a los métodos estáticos de C++
   o Java. Si los desea, consulte "staticmethod()" en esta sección.
   Para obtener más información sobre los métodos de clase, consulte
   Jerarquía de tipos estándar.

   Distinto en la versión 3.9: Los métodos de clase ahora pueden
   envolver otros *descriptores* como "property()".

   Distinto en la versión 3.10: Class methods now inherit the method
   attributes ("__module__", "__name__", "__qualname__", "__doc__" and
   "__annotations__") and have a new "__wrapped__" attribute.

   Deprecated since version 3.11, removed in version 3.13: Los métodos
   de clase ya no pueden envolver otros *descriptores* como
   "property()".

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

   Compila el *source* en código o en un objeto AST (*Abstract Syntax
   Tree*, árbol de sintaxis abstracta). Los objetos código pueden ser
   ejecutados por las funciones "exec()" or "eval()". *source* puede
   ser una cadena normal, una cadena de bytes o un objeto AST. Para
   más información sobre cómo trabajar con objetos AST, revisa la
   documentación del módulo "ast".

   El argumento *filename* debería dar el fichero desde el que el
   código fue leído; pasará un valor reconocible en caso este no fuera
   leído de un fichero  ("’<string>’" es usado comúnmente para esto).

   El argumento *mode* especifica que tipo de código debe ser
   compilado; puede ser  "’exec’" si *source* consiste en una
   secuencia de declaraciones, "’eval’" si consiste de una expresión
   sencilla, o "’single’" si consiste en una declaración única
   interactiva (en este último caso, las declaraciones de expresiones
   que evalúen a algo distinto de "None" serán impresas).

   Los argumentos opcionales *flags* y *dont_inherit* controlan qué
   opciones del compilador deben activarse y cuáles características
   futuras deben permitirse. Si ninguno está presente (o ambos son
   cero), el código se compila con los mismos flags que afectan al
   código que llama "compile()". Si se proporciona el argumento
   *flags* y *dont_inherit* no es (o es cero), las opciones del
   compilador y las declaraciones futuras especificadas por el
   argumento *flags* se utilizan además de las que se utilizarían de
   todos modos. Si *dont_inherit* es un número entero distinto de
   cero, entonces el argumento *flags* lo es: los indicadores
   (características futuras y opciones del compilador) en el código
   circundante se ignoran.

   Las opciones del compilador y las declaraciones futuras se
   especifican mediante bits que pueden combinarse mediante OR bit a
   bit para especificar varias opciones. El campo de bits requerido
   para especificar una característica futura dada se puede encontrar
   como el atributo "compiler_flag" en la instancia "_Feature" en el
   módulo "__future__". Las flags del compilador se pueden encontrar
   en el módulo "ast", con el prefijo "PyCF_".

   El argumento *optimize* especifica el nivel de optimización del
   compilador; el valor por defecto de "-1" selecciona el nivel de
   optimización del intérprete de la misma forma que las opciones
   "-O". Los niveles explícitos son "0" (sin optimización; "__debug__"
   es true), "1" (se eliminan los asserts, "__debug__" es false) or
   "2" (las *docstrings* también son eliminadas).

   This function raises "SyntaxError" or "ValueError" if the compiled
   source is invalid.

   Si quieres transformar código Python a su representación AST,
   revisa "ast.parse()".

   Lanza un evento de auditoría "compile" con argumentos "source" y
   "filename". Este evento también puede ser lanzado por la
   compilación implícita.

   Nota:

     Cuando se compile una cadena multilínea de código en los modos
     "’single’" o "’eval’", la entrada debe terminar con un carácter
     de nueva línea como mínimo. Esto facilita la detección de
     declaraciones completas e incompletas en el módulo "code".

   Advertencia:

     Con una cadena lo suficientemente larga o compleja, al compilar a
     un objeto AST es posible que el intérprete de Python pare
     inesperadamente debido a las limitaciones de la profundidad de la
     pila en el compilador del AST de Python.

   Distinto en la versión 3.2: Permite el uso de caracteres de nueva
   línea de Windows y Mac. También, la entrada en el modo "’exec’" ya
   no tiene que terminar necesariamente en una nueva línea. Se añade
   el parámetro *optimize*.

   Distinto en la versión 3.5: Anteriormente, un "TypeError" era
   lanzado cuando se encontraban bytes nulos en *source*.

   Added in version 3.8: "ast.PyCF_ALLOW_TOP_LEVEL_AWAIT"  puede ahora
   ser pasado en *flags* para permitir el soporte de "await", "async
   for", y "async with" en niveles superiores.

class complex(number=0, /)
class complex(string, /)
class complex(real=0, imag=0)

   Convert a single string or number to a complex number, or create a
   complex number from real and imaginary parts.

   Examples:

      >>> complex('+1.23')
      (1.23+0j)
      >>> complex('-4.5j')
      -4.5j
      >>> complex('-1.23+4.5j')
      (-1.23+4.5j)
      >>> complex('\t( -1.23+4.5J )\n')
      (-1.23+4.5j)
      >>> complex('-Infinity+NaNj')
      (-inf+nanj)
      >>> complex(1.23)
      (1.23+0j)
      >>> complex(imag=-4.5)
      -4.5j
      >>> complex(-1.23, 4.5)
      (-1.23+4.5j)

   If the argument is a string, it must contain either a real part (in
   the same format as for "float()") or an imaginary part (in the same
   format but with a "'j'" or "'J'" suffix), or both real and
   imaginary parts (the sign of the imaginary part is mandatory in
   this case). The string can optionally be surrounded by whitespaces
   and the round parentheses "'('" and "')'", which are ignored. The
   string must not contain whitespace between "'+'", "'-'", the "'j'"
   or "'J'" suffix, and the decimal number. For example,
   "complex('1+2j')" is fine, but "complex('1 + 2j')" raises
   "ValueError". More precisely, the input must conform to the
   "complexvalue" production rule in the following grammar, after
   parentheses and leading and trailing whitespace characters are
   removed:

      complexvalue: floatvalue |
                    floatvalue ("j" | "J") |
                    floatvalue sign absfloatvalue ("j" | "J")

   If the argument is a number, the constructor serves as a numeric
   conversion like "int" and "float". For a general Python object "x",
   "complex(x)" delegates to "x.__complex__()". If "__complex__()" is
   not defined then it falls back to "__float__()". If "__float__()"
   is not defined then it falls back to "__index__()".

   If two arguments are provided or keyword arguments are used, each
   argument may be any numeric type (including complex). If both
   arguments are real numbers, return a complex number with the real
   component *real* and the imaginary component *imag*. If both
   arguments are complex numbers, return a complex number with the
   real component "real.real-imag.imag" and the imaginary component
   "real.imag+imag.real". If one of arguments is a real number, only
   its real component is used in the above expressions.

   See also "complex.from_number()" which only accepts a single
   numeric argument.

   If all arguments are omitted, returns "0j".

   El tipo complejo está descrito en Tipos numéricos --- int, float,
   complex.

   Distinto en la versión 3.6: Agrupar dígitos con guiones bajos como
   en los literales de código está permitido.

   Distinto en la versión 3.8: Recurre a "__index__()" si
   "__complex__()" y "__float__()" no están definidos.

   Obsoleto desde la versión 3.14: Passing a complex number as the
   *real* or *imag* argument is now deprecated; it should only be
   passed as a single positional argument.

delattr(object, name, /)

   Esta función es relativa a "setattr()". Los argumentos son un
   objeto y una cadena. La cadena debe ser el mismo nombre que alguno
   de los atributos del objeto. La función elimina el atributo
   nombrado, si es que el objeto lo permite. Por ejemplo "delattr(x,
   ‘foobar’)" es equivalente a "del x.foobar". *name* necesita no ser
   un identificador Python (ver "setattr()").

class dict(**kwargs)
class dict(mapping, /, **kwargs)
class dict(iterable, /, **kwargs)

   Create a new dictionary.  The "dict" object is the dictionary
   class. See also Tipos mapa --- dict for documentation about this
   class.

   Para otros contenedores véase las clases incorporadas (*built-in*)
   "list", "set", y "tuple", así como el módulo "collections".

dir()
dir(object, /)

   Sin argumentos, retorna la lista de nombres en el ámbito local. Con
   un argumento, intenta retornar una lista de atributos válidos para
   ese objeto.

   If the object has a method named "__dir__()", this method will be
   called and must return the list of attributes. This allows objects
   that implement a custom "__getattr__()" or "__getattribute__()"
   function to customize the way "dir()" reports their attributes.

   If the object does not provide "__dir__()", the function tries its
   best to gather information from the object's "__dict__" attribute,
   if defined, and from its type object.  The resulting list is not
   necessarily complete and may be inaccurate when the object has a
   custom "__getattr__()".

   El mecanismo por defecto de "dir()"  se comporta de forma distinta
   con diferentes tipos de objeto, ya que intenta producir la
   información más relevante en vez de la más completa:

   * Si el objeto es un módulo, la lista contiene los nombres de los
     atributos del módulo.

   * Si el objeto es un tipo o una clase, la lista contiene los
     nombres de sus atributos, y recursivamente la de los atributos de
     sus clases base.

   * En cualquier otro caso, la lista contiene los nombres de los
     atributos del objeto, los nombres de los atributos de su clase, y
     recursivamente los atributos de sus clases base.

   La lista resultante está ordenada alfabéticamente. Por ejemplo:

   >>> import struct
   >>> dir()   # show the names in the module namespace
   ['__builtins__', '__name__', 'struct']
   >>> dir(struct)   # show the names in the struct module
   ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
    '__initializing__', '__loader__', '__name__', '__package__',
    '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
    'unpack', 'unpack_from']
   >>> class Shape:
   ...     def __dir__(self):
   ...         return ['area', 'perimeter', 'location']
   ...
   >>> s = Shape()
   >>> dir(s)
   ['area', 'location', 'perimeter']

   Nota:

     Ya que "dir()"  se ofrece como una herramienta para uso en una
     terminal de forma interactiva, intenta ofrecer un grupo
     interesante de nombres más que un uno rigurosamente definido, y
     su comportamiento detallado puede cambiar entre versiones. Por
     ejemplo, los atributos de metaclase no están en la lista
     resultante cuando el argumento es una clase.

divmod(a, b, /)

   Take two (non-complex) numbers as arguments and return a pair of
   numbers consisting of their quotient and remainder when using
   integer division.  With mixed operand types, the rules for binary
   arithmetic operators apply.  For integers, the result is the same
   as "(a // b, a % b)". For floating-point numbers the result is "(q,
   a % b)", where *q* is usually "math.floor(a / b)" but may be 1 less
   than that.  In any case "q * b + a % b" is very close to *a*, if "a
   % b" is non-zero it has the same sign as *b*, and "0 <= abs(a % b)
   < abs(b)".

enumerate(iterable, start=0)

   Retorna un objeto enumerador. *iterable* tiene que ser una
   secuencia, un *iterator*, o algún otro objeto que soporte la
   iteración. El método "__next__()" del iterador retornado por la
   función "enumerate()" retorna una tupla que contiene un contador
   (desde *start*, cuyo valor por defecto es 0) y los valores
   obtenidos al iterar sobre *iterable*.

   >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
   >>> list(enumerate(seasons))
   [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
   >>> list(enumerate(seasons, start=1))
   [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

   Equivalente a:

      def enumerate(iterable, start=0):
          n = start
          for elem in iterable:
              yield n, elem
              n += 1

eval(source, /, globals=None, locals=None)

   Parámetros:
      * **source** ("str" | code object) -- A Python expression.

      * **globals** ("dict" | "None") -- The global namespace
        (default: "None").

      * **locals** (*mapping* | "None") -- The local namespace
        (default: "None").

   Devuelve:
      The result of the evaluated expression.

   Raises:
      Syntax errors are reported as exceptions.

   Advertencia:

     This function executes arbitrary code. Calling it with untrusted
     user-supplied input will lead to security vulnerabilities.

   The *source* argument is parsed and evaluated as a Python
   expression (technically speaking, an expression list) using the
   *globals* and *locals* mappings as global and local namespace. If
   the *globals* dictionary is present and does not contain a value
   for the key "__builtins__", a reference to the dictionary of the
   built-in module "builtins" is inserted under that key before
   *source* is parsed. Overriding "__builtins__" can be used to
   restrict or change the available names, but this is **not** a
   security mechanism: the executed code can still access all
   builtins. If the *locals* mapping is omitted it defaults to the
   *globals* dictionary.  If both mappings are omitted, the source is
   executed with the *globals* and *locals* in the environment where
   "eval()" is called.  Note, *eval()* will only have access to the
   *nested scopes* (non-locals) in the enclosing environment if they
   are already referenced in the scope that is calling "eval()" (e.g.
   via a "nonlocal" statement).

   Example:

   >>> x = 1
   >>> eval('x+1')
   2

   >>> eval("1, 2")
   (1, 2)

   Esta función también puede ser utilizada para ejecutar objetos de
   código arbitrario (como los que crea la función "compile()"). En
   este caso, se pasa un objeto de código en vez de una cadena de
   caracteres. Si el objeto de código ha sido compilado usando
   "'exec'" como el argumento *mode*, el valor que retornará
   "eval()"será "None".

   Consejos: la ejecución dinámica de declaraciones está soportada por
   la función "exec()". Las funciones "globals()" y "locals()"
   retornan los diccionarios global y local en ese momento,
   respectivamente, lo cual puede ser útil para su uso en "eval()" o
   "exec()".

   Si la fuente dada es una cadena de caracteres, se eliminan los
   espacios y tabulaciones principales y finales.

   See "ast.literal_eval()" for a function to evaluate strings with
   expressions containing only literals.

   Lanza un evento de auditoría "exec" con el objeto código como el
   argumento. También podrían ser lanzados eventos de compilación de
   código.

   Distinto en la versión 3.13: The *globals* and *locals* arguments
   can now be passed as keywords.

   Distinto en la versión 3.13: The semantics of the default *locals*
   namespace have been adjusted as described for the "locals()"
   builtin.

exec(source, /, globals=None, locals=None, *, closure=None)

   Advertencia:

     This function executes arbitrary code. Calling it with untrusted
     user-supplied input will lead to security vulnerabilities.

   This function supports dynamic execution of Python code. *source*
   must be either a string or a code object.  If it is a string, the
   string is parsed as a suite of Python statements which is then
   executed (unless a syntax error occurs). [1] If it is a code
   object, it is simply executed.  In all cases, the code that's
   executed is expected to be valid as file input (see the section
   Entrada de archivo in the Reference Manual). Be aware that the
   "nonlocal", "yield",  and "return" statements may not be used
   outside of function definitions even within the context of code
   passed to the "exec()" function. The return value is "None".

   In all cases, if the optional parts are omitted, the code is
   executed in the current scope.  If only *globals* is provided, it
   must be a dictionary (and not a subclass of dictionary), which will
   be used for both the global and the local variables.  If *globals*
   and *locals* are given, they are used for the global and local
   variables, respectively.  If provided, *locals* can be any mapping
   object.  Remember that at the module level, globals and locals are
   the same dictionary.

   Nota:

     When "exec" gets two separate objects as *globals* and *locals*,
     the code will be executed as if it were embedded in a class
     definition. This means functions and classes defined in the
     executed code will not be able to access variables assigned at
     the top level (as the "top level" variables are treated as class
     variables in a class definition).

   If the *globals* dictionary does not contain a value for the key
   "__builtins__", a reference to the dictionary of the built-in
   module "builtins" is inserted under that key. Overriding
   "__builtins__" can be used to restrict or change the available
   names, but this is **not** a security mechanism: the executed code
   can still access all builtins.

   The *closure* argument specifies a closure--a tuple of cellvars.
   It's only valid when the *object* is a code object containing *free
   (closure) variables*. The length of the tuple must exactly match
   the length of the code object's "co_freevars" attribute.

   Lanza un evento de auditoría "exec" con el objeto código como el
   argumento. También podrían ser lanzados eventos de compilación de
   código.

   Nota:

     The built-in functions "globals()" and "locals()" return the
     current global and local namespace, respectively, which may be
     useful to pass around for use as the second and third argument to
     "exec()".

   Nota:

     The default *locals* act as described for function "locals()"
     below. Pass an explicit *locals* dictionary if you need to see
     effects of the code on *locals* after function "exec()" returns.

   Distinto en la versión 3.11: Añadido el parámetro *closure*.

   Distinto en la versión 3.13: The *globals* and *locals* arguments
   can now be passed as keywords.

   Distinto en la versión 3.13: The semantics of the default *locals*
   namespace have been adjusted as described for the "locals()"
   builtin.

filter(function, iterable, /)

   Construye un iterador a partir de aquellos elementos de *iterable*
   para los cuales *function* retorna true. *iterable* puede ser una
   secuencia, un contenedor que soporta iteración, o un iterador. Si
   *function* es "None", se asume la función identidad, es decir,
   todos los elementos de *iterable* que son false son eliminados.

   Ten en cuenta que "filter(function, iterable)" es equivalente a la
   expresión de un generador "(item for item in iterable if
   function(item))" si *function* no es "None" y a "(item for item in
   iterable if item)" si *function* es "None".

   Ver "itertools.filterfalse()" para la función complementaria que
   retorna los elementos de *iterable* para los cuales *function*
   retorna false.

class float(number=0.0, /)
class float(string, /)

   Return a floating-point number constructed from a number or a
   string.

   Examples:

      >>> float('+1.23')
      1.23
      >>> float('   -12345\n')
      -12345.0
      >>> float('1e-003')
      0.001
      >>> float('+1E6')
      1000000.0
      >>> float('-Infinity')
      -inf

   If the argument is a string, it should contain a decimal number,
   optionally preceded by a sign, and optionally embedded in
   whitespace.  The optional sign may be "'+'" or "'-'"; a "'+'" sign
   has no effect on the value produced.  The argument may also be a
   string representing a NaN (not-a-number), or positive or negative
   infinity. More precisely, the input must conform to the
   "floatvalue" production rule in the following grammar, after
   leading and trailing whitespace characters are removed:

      sign:          "+" | "-"
      infinity:      "Infinity" | "inf"
      nan:           "nan"
      digit:         <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
      digitpart:     digit (["_"] digit)*
      number:        [digitpart] "." digitpart | digitpart ["."]
      exponent:      ("e" | "E") [sign] digitpart
      floatnumber:   number [exponent]
      absfloatvalue: floatnumber | infinity | nan
      floatvalue:    [sign] absfloatvalue

   Case is not significant, so, for example, "inf", "Inf", "INFINITY",
   and "iNfINity" are all acceptable spellings for positive infinity.

   Otherwise, if the argument is an integer or a floating-point
   number, a floating-point number with the same value (within
   Python's floating-point precision) is returned.  If the argument is
   outside the range of a Python float, an "OverflowError" will be
   raised.

   Para el objeto general de Python "x", "float(x)" delega a
   "x.__float__()". Si "__float__()" no está definido entonces recurre
   a "__index__()".

   See also "float.from_number()" which only accepts a numeric
   argument.

   Si no se le da un argumento, retorna "0.0".

   El tipo float está descrito en Tipos numéricos --- int, float,
   complex.

   Distinto en la versión 3.6: Agrupar dígitos con guiones bajos como
   en los literales de código está permitido.

   Distinto en la versión 3.7: The parameter is now positional-only.

   Distinto en la versión 3.8: Recurre a "__index__()" si
   "__float__()" no está definido.

format(value, format_spec='', /)

   Convierte *value* a su representación "con formato", de forma
   controlada por *format_spec*. La interpretación de *format_spec*
   dependerá del tipo del argumento *value*. Sin embargo, hay una
   sintaxis estándar de formato que emplean la mayoría de los tipos
   incorporados: Format specification mini-language.

   El *format_spec* por defecto es una cadena vacía que normalmente
   produce el mismo efecto que llamar a "str(value)".

   A call to "format(value, format_spec)" is translated to
   "type(value).__format__(value, format_spec)" which bypasses the
   instance dictionary when searching for the value's "__format__()"
   method. A "TypeError" exception is raised if the method search
   reaches "object" and the *format_spec* is non-empty, or if either
   the *format_spec* or the return value are not strings.

   Distinto en la versión 3.4: "object().__format__(format_spec)"
   lanza "TypeError" si *format_spec* no es una cadena vacía.

class frozenset(iterable=(), /)

   Return a new "frozenset" object, optionally with elements taken
   from *iterable*.  "frozenset" is a built-in class.  See also
   Conjuntos --- set, frozenset for documentation about this class.

   Para otro tipo de contenedores, ver las clases built-in  "set",
   "list", "tuple", y "dict", así como el módulo "collections".

getattr(object, name, /)
getattr(object, name, default, /)

   Retorna el valor del atributo nombrado de *object*. *name* debe ser
   una cadena. Si la cadena es el nombre de uno de los atributos del
   objeto, el resultado es el valor de ese atributo. Por ejemplo,
   "getattr(x, ‘foobar’)" es equivalente a "x.foobar". Si el atributo
   nombrado no existe, se retorna *default* si ha sido proporcionado
   como argumento, y sino se lanza una excepción "AttributeError".
   *name* no necesita ser un identificador de Python (ver
   "setattr()").

   Nota:

     Dado que private name mangling ocurre en el momento de la
     compilación, uno debe enredar manualmente el nombre de un
     atributo privado (atributos con dos guiones bajos principales)
     para recuperarlo con "getattr()".

globals()

   Retorna un diccionario que implementa el espacio de nombres del
   módulo actual. Para el código dentro de las funciones, esto se
   establece cuando se define la función y permanece igual
   independientemente de dónde se llame a la función.

hasattr(object, name, /)

   Los argumentos son un objeto y una cadena. El resultado es "True"
   si la cadena es el nombre de uno de los atributos del objeto, y
   "False" en caso contrario. (Está implementado mediante una llamada
   a "getattr(object, name)" que comprueba si se lanza una excepción
   "AttributeError"  o no).

hash(object, /)

   Retorna el valor hash del objeto (si tiene uno). Los valores hash
   son enteros. Se usan para comparar de forma rápida claves de
   diccionarios durante las operaciones de búsqueda. Valores numéricos
   que son iguales tienen el mismo valor hash (incluso si son de tipos
   diferentes, como es el caso para 1 y 1.0).

   Nota:

     For objects with custom "__hash__()" methods, note that "hash()"
     truncates the return value based on the bit width of the host
     machine.

help()
help(request)

   Invoca el sistema de ayuda integrado (built-in). (Esta función está
   indicada para su uso interactivo). Si no se le da argumento, el
   sistema interactivo de ayuda se inicia en la consola del
   intérprete. Si el argumento es una cadena, entonces es buscada como
   nombre de un módulo, función, clase, método, palabra clave o tema
   de documentación, y una página de ayuda es impresa en la consola.
   Si el argumento es cualquier otro tipo de objeto, una página de
   ayuda sobre el objeto es generada.

   Ten en cuenta que si aparece una barra(/) en la lista de parámetros
   de una función al invocar "help()", significa que los parámetros
   anteriores a la barra son solo posicionales. Para más información,
   puedes ver the FAQ entry on positional-only parameters.

   Esta función se añade al espacio de nombres built-in a través del
   módulo "site".

   Distinto en la versión 3.4: Cambios a los módulos "pydoc" y
   "inspect" implican que las signaturas reportadas para objetos
   invocables son más completas y consistentes.

hex(integer, /)

   Convert an integer number to a lowercase hexadecimal string
   prefixed with "0x". If *integer* is not a Python "int" object, it
   has to define an "__index__()" method that returns an integer. Some
   examples:

   >>> hex(255)
   '0xff'
   >>> hex(-42)
   '-0x2a'

   Si quieres convertir un número entero a una cadena hexadecimal de
   mayúsculas o minúsculas con prefijo o sin el, puedes usar
   cualquiera de las siguientes formas:

   >>> '%#x' % 255, '%x' % 255, '%X' % 255
   ('0xff', 'ff', 'FF')
   >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
   ('0xff', 'ff', 'FF')
   >>> f'{255:#x}', f'{255:x}', f'{255:X}'
   ('0xff', 'ff', 'FF')

   Véase también "format()" para más información.

   Ver también "int()" para convertir una cadena hexadecimal a un
   entero usando una base de 16.

   Nota:

     Para obtener una cadena hexadecimal que represente un punto
     flotante, utiliza el método "float.hex()".

id(object, /)

   Retorna la "identidad" de un objeto. Esto es un entero que está
   garantizado que es único y constante para este objeto durante toda
   su existencia. Dos objetos con existencias en el tiempo que no
   coincidan pueden tener el mismo valor de "id()".

   Esta es la dirección del objeto en memoria.

   Lanza un evento de auditoría "builtins.id" con el argumento "id".

input()
input(prompt, /)

   Si el argumento *prompt* está presente, se escribe a la salida
   estándar sin una nueva línea a continuación. La función lee
   entonces una línea de la entrada, la convierte en una cadena
   (eliminando la nueva línea), y retorna eso. Cuando se lee EOF, se
   lanza una excepción "EOFError". Ejemplo:

      >>> s = input('--> ')
      --> Monty Python's Flying Circus
      >>> s
      "Monty Python's Flying Circus"

   Si el módulo "readline" estaba cargado, entonces "input()" lo usará
   para proporcionar características más elaboradas de edición de
   líneas e historiales.

   Lanza un evento de auditoría "builtins.input" con el argumento
   "prompt" antes de leer entrada

   Lanza un evento de auditoría "builtins.input/result" con el
   resultado justo después de haber leído con éxito la entrada.

class int(number=0, /)
class int(string, /, base=10)

   Return an integer object constructed from a number or a string, or
   return "0" if no arguments are given.

   Examples:

      >>> int(123.45)
      123
      >>> int('123')
      123
      >>> int('   -12_345\n')
      -12345
      >>> int('FACE', 16)
      64206
      >>> int('0xface', 0)
      64206
      >>> int('01110011', base=2)
      115

   If the argument defines "__int__()", "int(x)" returns
   "x.__int__()".  If the argument defines "__index__()", it returns
   "x.__index__()". For floating-point numbers, this truncates towards
   zero.

   If the argument is not a number or if *base* is given, then it must
   be a string, "bytes", or "bytearray" instance representing an
   integer in radix *base*.  Optionally, the string can be preceded by
   "+" or "-" (with no space in between), have leading zeros, be
   surrounded by whitespace, and have single underscores interspersed
   between digits.

   Una cadena de enteros de base n contiene dígitos, cada uno de los
   cuales representa un valor de 0 a n-1. Los valores 0--9 se pueden
   representar por cualquier dígito decimal Unicode. Los valores 10--
   35 se pueden representar de "a" a "z" (o de "A" a "Z"). La *base*
   predeterminada es 10. Las bases permitidas son 0 y 2--36. Las
   cadenas de caracteres de base 2, 8 y 16 pueden tener opcionalmente
   el prefijo "0b"/"0B", "0o"/"0O" o "0x"/"0X", como ocurre con los
   literales enteros en el código. Para base 0, la cadena de
   caracteres se interpreta de manera similar a un literal entero en
   el código, en el que la base de verdad es 2, 8, 10 o 16 según lo
   determine el prefijo. La base 0 tampoco permite los ceros a la
   izquierda: "int('010', 0)" no es legal, mientras que "int('010')" e
   "int('010', 8)" sí lo son.

   El tipo entero se describe en Tipos numéricos --- int, float,
   complex.

   Distinto en la versión 3.4: Si *base* no es una instancia de "int"
   y el objeto *base* tiene un método "base.__index__", ese método es
   llamado para obtener un entero para esa base. En versiones
   anteriores se empleaba "base.__int__" en vez de "base.__index__".

   Distinto en la versión 3.6: Agrupar dígitos con guiones bajos como
   en los literales de código está permitido.

   Distinto en la versión 3.7: The first parameter is now positional-
   only.

   Distinto en la versión 3.8: Recurre a "__index__()" si no está
   definido "__int__()".

   Distinto en la versión 3.11: "int" string inputs and string
   representations can be limited to help avoid denial of service
   attacks. A "ValueError" is raised when the limit is exceeded while
   converting a string to an "int" or when converting an "int" into a
   string would exceed the limit. See the integer string conversion
   length limitation documentation.

   Distinto en la versión 3.14: "int()" no longer delegates to the
   "__trunc__()" method.

isinstance(object, classinfo, /)

   Retorna "True" si el argumento *object* es una instancia del
   argumento *classinfo*, o de una subclase (directa, indirecta o
   *virtual*) del mismo. Si *object* no es un objeto del tipo
   indicado, esta función siempre retorna "False".  Si *classinfo* es
   una tupla de objetos de tipo (o recursivamente, otras tuplas lo
   son) o Tipo de conversión de múltiples tipos , retorna "True" si
   *object* es una instancia de alguno de los tipos. Si *classinfo* no
   es un tipo, una tupla de tipos, o una tupla de tuplas de tipos, una
   excepción "TypeError" es lanzada. Es posible que "TypeError" no se
   genere para un tipo no válido si una verificación anterior tiene
   éxito.

   Distinto en la versión 3.10: *classinfo* puede ser una Tipo de
   conversión.

issubclass(class, classinfo, /)

   Retorna "True" si *class* es una subclase (directa, indirecta o
   *virtual*) de *classinfo*.  Una clase es considerada una subclase
   de sí misma.  *classinfo* puede ser una tupla de objetos de clase o
   una Tipo de conversión, en cuyo caso retorna "True" si *class* es
   una subclase de cualquier entrada en *classinfo*. En cualquier otro
   caso, se lanzará una excepción "TypeError".

   Distinto en la versión 3.10: *classinfo* puede ser una Tipo de
   conversión.

iter(iterable, /)
iter(callable, sentinel, /)

   Return an *iterator* object.  The first argument is interpreted
   very differently depending on the presence of the second argument.
   Without a second argument, the single argument must be a collection
   object which supports the *iterable* protocol (the "__iter__()"
   method), or it must support the sequence protocol (the
   "__getitem__()" method with integer arguments starting at "0").  If
   it does not support either of those protocols, "TypeError" is
   raised. If the second argument, *sentinel*, is given, then the
   first argument must be a callable object.  The iterator created in
   this case will call *callable* with no arguments for each call to
   its "__next__()" method; if the value returned is equal to
   *sentinel*, "StopIteration" will be raised, otherwise the value
   will be returned.

   Ver también Tipos de iteradores.

   Una aplicación muy útil de la segunda forma de "iter()" es la
   construcción de un lector de bloques. Por ejemplo, leer bloques de
   ancho fijo de una base de datos binaria hasta que el fin del
   fichero sea alcanzado:

      from functools import partial
      with open('mydata.db', 'rb') as f:
          for block in iter(partial(f.read, 64), b''):
              process_block(block)

len(object, /)

   Retorna el tamaño (el número de elementos) de un objeto. El
   argumento puede ser una secuencia (como una cadena, un objeto byte,
   una tupla, lista o rango) o una colección (como un diccionario, un
   set o un *frozen set*).

   "len" aumenta "OverflowError" en longitudes mayores que
   "sys.maxsize", como "range(2 ** 100)".

class list(iterable=(), /)

   Más que una función, "list" es realmente un tipo de secuencia
   mutable, como está documentado en Listas y Tipos secuencia ---
   list, tuple, range.

locals()

   Return a mapping object representing the current local symbol
   table, with variable names as the keys, and their currently bound
   references as the values.

   At module scope, as well as when using "exec()" or "eval()" with a
   single namespace, this function returns the same namespace as
   "globals()".

   At class scope, it returns the namespace that will be passed to the
   metaclass constructor.

   When using "exec()" or "eval()" with separate local and global
   arguments, it returns the local namespace passed in to the function
   call.

   In all of the above cases, each call to "locals()" in a given frame
   of execution will return the *same* mapping object. Changes made
   through the mapping object returned from "locals()" will be visible
   as assigned, reassigned, or deleted local variables, and assigning,
   reassigning, or deleting local variables will immediately affect
   the contents of the returned mapping object.

   In an *optimized scope* (including functions, generators, and
   coroutines), each call to "locals()" instead returns a fresh
   dictionary containing the current bindings of the function's local
   variables and any nonlocal cell references. In this case, name
   binding changes made via the returned dict are *not* written back
   to the corresponding local variables or nonlocal cell references,
   and assigning, reassigning, or deleting local variables and
   nonlocal cell references does *not* affect the contents of
   previously returned dictionaries.

   Calling "locals()" as part of a comprehension in a function,
   generator, or coroutine is equivalent to calling it in the
   containing scope, except that the comprehension's initialised
   iteration variables will be included. In other scopes, it behaves
   as if the comprehension were running as a nested function.

   Calling "locals()" as part of a generator expression is equivalent
   to calling it in a nested generator function.

   Distinto en la versión 3.12: The behaviour of "locals()" in a
   comprehension has been updated as described in **PEP 709**.

   Distinto en la versión 3.13: As part of **PEP 667**, the semantics
   of mutating the mapping objects returned from this function are now
   defined. The behavior in *optimized scopes* is now as described
   above. Aside from being defined, the behaviour in other scopes
   remains unchanged from previous versions.

map(function, iterable, /, *iterables, strict=False)

   Return an iterator that applies *function* to every item of
   *iterable*, yielding the results.  If additional *iterables*
   arguments are passed, *function* must take that many arguments and
   is applied to the items from all iterables in parallel.  With
   multiple iterables, the iterator stops when the shortest iterable
   is exhausted.  If *strict* is "True" and one of the iterables is
   exhausted before the others, a "ValueError" is raised. For cases
   where the function inputs are already arranged into argument
   tuples, see "itertools.starmap()".

   Distinto en la versión 3.14: Added the *strict* parameter.

max(iterable, /, *, key=None)
max(iterable, /, *, default, key=None)
max(arg1, arg2, /, *args, key=None)

   Retorna el elemento mayor en un iterable o el mayor de dos o más
   argumentos.

   Si un argumento posicional es dado, debe ser un *iterable*.  El
   elemento mayor en el iterable es retornado. Si dos o más argumentos
   posicionales son indicados, el mayor de los argumentos posicionales
   será retornado.

   Hay dos argumentos de solo palabra clave que son opcionales. El
   argumento *key* especifica una función de ordenación de un sólo
   argumento, como la usada para "list.sort()". El argumento *default*
   especifica un objeto a retornar si el iterable proporcionado está
   vacío. Si el iterable está vacío y *default* no ha sido indicado,
   se lanza un "ValueError".

   Si hay múltiples elementos con el valor máximo, la función retorna
   el primero que ha encontrado.  Esto es consistente con otras
   herramientas para preservar la estabilidad de la ordenación como
   "sorted(iterable, key=keyfunc, reverse=True)[0]" y
   "heapq.nlargest(1, iterable, key=keyfunc)".

   Distinto en la versión 3.4: Added the *default* keyword-only
   parameter.

   Distinto en la versión 3.8: *key* puede ser "None".

class memoryview(object)

   Retorna un objeto *"memory view"* creado a partir del argumento
   indicado. Para más información ver Vistas de memoria.

min(iterable, /, *, key=None)
min(iterable, /, *, default, key=None)
min(arg1, arg2, /, *args, key=None)

   Retorna el menor elemento en un iterable o el menor de dos o más
   argumentos.

   Si se le indica un argumento posicional, debe ser un *iterable*.
   El menor elemento del iterable es retornado. Si dos o más
   argumentos posicionales son indicados, el menor de los argumentos
   posicionales es retornado.

   Hay dos argumentos de solo palabra clave que son opcionales. El
   argumento *key* especifica una función de ordenación de un sólo
   argumento, como la usada para "list.sort()". El argumento *default*
   especifica un objeto a retornar si el iterable proporcionado está
   vacío. Si el iterable está vacío y *default* no ha sido indicado,
   se lanza un "ValueError".

   Si hay múltiples elementos con el valor mínimo, la función retorna
   el primero que encuentra. Esto es consistente con otras
   herramientas que preservan la estabilidad de la ordenación como
   "sorted(iterable, key=keyfunc)[0]" y "heapq.nsmallest(1, iterable,
   key=keyfunc)".

   Distinto en la versión 3.4: Added the *default* keyword-only
   parameter.

   Distinto en la versión 3.8: *key* puede ser "None".

next(iterator, /)
next(iterator, default, /)

   Extrae el siguiente elemento de *iterator* llamando a su método
   "__next__()". Si se le indica *default*, éste será retornado si se
   agota el iterador, de lo contrario, se lanza un  "StopIteration".

class object

   This is the ultimate base class of all other classes. It has
   methods that are common to all instances of Python classes. When
   the constructor is called, it returns a new featureless object. The
   constructor does not accept any arguments.

   Nota:

     "object" instances do *not* have "__dict__" attributes, so you
     can't assign arbitrary attributes to an instance of "object".

oct(integer, /)

   Convert an integer number to an octal string prefixed with "0o".
   The result is a valid Python expression. If *integer* is not a
   Python "int" object, it has to define an "__index__()" method that
   returns an integer. For example:

   >>> oct(8)
   '0o10'
   >>> oct(-56)
   '-0o70'

   Si quieres convertir un número entero a una cadena octal, tanto con
   prefijo "0o" como sin el, puedes usar cualquiera de las siguientes
   formas.

   >>> '%#o' % 10, '%o' % 10
   ('0o12', '12')
   >>> format(10, '#o'), format(10, 'o')
   ('0o12', '12')
   >>> f'{10:#o}', f'{10:o}'
   ('0o12', '12')

   Véase también "format()" para más información.

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

   Abre *file* y retorna un *file object* correspondiente. Si el
   archivo no se puede abrir, se lanza un "OSError". Consulte Leyendo
   y escribiendo archivos para obtener más ejemplos de cómo utilizar
   esta función.

   *file* es un *path-like object* que da la ruta (absoluta o relativa
   al directorio de trabajo actual) del fichero a ser abierto o un
   descriptor de fichero entero del fichero a ser envuelto. (Si un
   descriptor de fichero es dado, será cerrado cuando el objeto de
   entrada-salida sea cerrado, a menos que *closefd* esté puesto a
   "False".)

   *mode* is an optional string that specifies the mode in which the
   file is opened.  It defaults to "'r'" which means open for reading
   in text mode. Other common values are "'w'" for writing (truncating
   the file if it already exists), "'x'" for exclusive creation, and
   "'a'" for appending (which on *some* Unix systems, means that *all*
   writes append to the end of the file regardless of the current seek
   position).  In text mode, if *encoding* is not specified the
   encoding used is platform-dependent: "locale.getencoding()" is
   called to get the current locale encoding. (For reading and writing
   raw bytes use binary mode and leave *encoding* unspecified.)  The
   available modes are:

   +-----------+-----------------------------------------------------------------+
   | Carácter  | Significado                                                     |
   |===========|=================================================================|
   | "’r’"     | abierto para lectura (por defecto)                              |
   +-----------+-----------------------------------------------------------------+
   | "'w'"     | abierto para escritura, truncando primero el fichero            |
   +-----------+-----------------------------------------------------------------+
   | "'x'"     | abierto para creación en exclusiva, falla si el fichero ya      |
   |           | existe                                                          |
   +-----------+-----------------------------------------------------------------+
   | "’a’"     | abierto para escritura, añadiendo al final del fichero si este  |
   |           | existe                                                          |
   +-----------+-----------------------------------------------------------------+
   | "'b'"     | modo binario                                                    |
   +-----------+-----------------------------------------------------------------+
   | "’t’"     | modo texto (por defecto)                                        |
   +-----------+-----------------------------------------------------------------+
   | "’+’"     | abierto para actualizar (lectura y escritura)                   |
   +-----------+-----------------------------------------------------------------+

   El modo por defecto es  "’r’"  (abierto para lectura de texto,
   sinónimo de  "’rt’". Los modos "’w+’" y "’w+b’" abren y truncan el
   fichero.  Los modos "’r+’" y "’r+b’" abren el fichero sin
   truncarlo.

   Como se menciona en Resumen, Python distingue entre I/O binario y
   de texto. Los ficheros abiertos en modo binario (incluyendo "’b’"
   en el argumento *mode*) retornan su contenido como objetos de
   "bytes"  sin ninguna descodificación. En modo de texto (por
   defecto, o cuando se incluye  "’t’" en el argumento *mode*), los
   contenidos del fichero se retornan como "str", tras descodificar
   los *bytes* usando una codificación dependiente de plataforma o
   usando el *encoding* especificado como argumento.

   Nota:

     Python no depende de la noción de ficheros de texto del sistema
     operativo subyacente; todo el procesado lo hace Python, y es por
     tanto independiente de plataforma.

   *buffering* is an optional integer used to set the buffering
   policy.  Pass 0 to switch buffering off (only allowed in binary
   mode), 1 to select line buffering (only usable when writing in text
   mode), and an integer > 1 to indicate the size in bytes of a fixed-
   size chunk buffer. Note that specifying a buffer size this way
   applies for binary buffered I/O, but "TextIOWrapper" (i.e., files
   opened with "mode='r+'") would have another buffering. To disable
   buffering in "TextIOWrapper", consider using the "write_through"
   flag for "io.TextIOWrapper.reconfigure()". When no *buffering*
   argument is given, the default buffering policy works as follows:

   * Binary files are buffered in fixed-size chunks; the size of the
     buffer is "max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)" when
     the device block size is available. On most systems, the buffer
     will typically be 128 kilobytes long.

   * Los ficheros de texto "interactivos" (ficheros para los cuales
     "isatty()" retorna "True") usan buffering por líneas.  Otros
     ficheros de texto emplean la norma descrita anteriormente para
     ficheros binarios.

   *encoding* es el nombre de la codificación empleada con el fichero.
   Esto solo debe ser usado en el modo texto.  La codificación por
   defecto es dependiente de plataforma (aquello que retorna
   "locale.getencoding()"), pero puede emplearse cualquier  *text
   encoding*  soportado por Python.  Ver el módulo "codecs"  para la
   lista de codificaciones soportadas.

   *errors* es una cadena opcional que especifica como deben manejarse
   los errores de codificación y descodificación -- esto no puede ser
   usado en modo binario. Están disponibles varios gestores de error
   (listados en Manejadores de errores), pero también es válido
   cualquier nombre de gestión de error registrado con
   "codecs.register_error()". Los nombres estándar incluyen:

   * "'strict'" para lanzar una excepción "ValueError" si hay un error
     de codificación.  El valor por defecto, "None", produce el mismo
     efecto.

   * "'ignore'" ignora los errores.  Nótese que ignorar errores de
     codificación puede conllevar la pérdida de datos.

   * "'replace'"  provoca que se inserte un marcador de reemplazo
     (como  "'?'")  en aquellos sitios donde hay datos malformados.

   * "'surrogateescape'" representará cualquier bytes incorrectos como
     unidades de código sustituto bajo que van desde U+DC80 a U+DCFF.
     Estas unidades de código sustituto volverán a convertirse en los
     mismos bytes cuando el gestor de errores "surrogateescape" sea
     usado al escribir datos.  Esto es útil para el procesado de
     ficheros con una codificación desconocida.

   * "'xmlcharrefreplace'" está soportado solamente cuando se escribe
     a un fichero. Los caracteres que no estén soportados por la
     codificación son reemplazados por la referencia al carácter XML
     apropiado "&#*nnn*;".

   * "'backslashreplace'" reemplaza datos malformados con las
     secuencias de escapes de barra invertida de Python.

   * "'namereplace'" reemplaza caracteres no soportados con secuencias
     de escape  "\N{...}" (y también está sólo soportado en
     escritura).

   *newline* determina cómo analizar los caracteres de nueva línea de
   la secuencia.  Puede ser  "None", "''", "'\n'", "'\r'", y "'\r\n'".
   Funciona de la siguiente manera:

   * Cuando se está leyendo entrada desde el flujo, si *newline* es
     "None", el modo *universal newlines* es activado.  Las líneas en
     la entrada pueden terminar en  "'\n'", "'\r'", o "'\r\n'", y
     serán traducidas a  "'\n'"  antes de ser retornadas a la entidad
     que llama. Si es "''", el modo *universal newlines* estará
     activado pero los finales de línea se retornan sin traducir a la
     entidad que llama. Si tiene cualquiera de los otros valoras
     válidos, las líneas de entrada estarán terminadas sólo por la
     cadena dada, y los finales de línea serán retornados sin traducir
     a la entidad que llama.

   * Cuando se escribe salida al flujo, si *newline* es  "None",
     cualquier carácter "'\n'" escrito es traducido al separador de
     línea por defecto en el sistema, "os.linesep". Si *newline* es
     "''" o "'\n'", entonces no se produce ninguna traducción.  Si
     *newline* toma cualquiera de los otros valores válidos, entonces
     cualquier carácter "'\n'"  escrito es traducido a la cadena
     indicada.

   Si *closefd* es "False"  y se indica un descriptor de fichero en
   vez de un nombre de fichero, el descriptor del fichero se mantendrá
   abierto cuando se cierre el fichero. Si se indica un nombre de
   fichero, *closefd*  debe ser "True" (lo es por defecto), ya que de
   otra forma se lanzará un error.

   Un abridor personalizado puede emplearse pasando un invocable como
   *opener*. El descriptor de fichero del objeto se obtiene llamando a
   *opener* con (*file*, *flags*). *opener* debe retornar un
   descriptor de fichero abierto (pasando "os.open" como *opener*
   resulta en una funcionalidad similar a "None").

   El nuevo fichero creado es no-heredable.

   El siguiente ejemplo emplea el parámetro dir_fd  de la función
   "os.open()"  para abrir un fichero relativo a un directorio dado:

      >>> import os
      >>> dir_fd = os.open('somedir', os.O_RDONLY)
      >>> def opener(path, flags):
      ...     return os.open(path, flags, dir_fd=dir_fd)
      ...
      >>> with open('spamspam.txt', 'w', opener=opener) as f:
      ...     print('This will be written to somedir/spamspam.txt', file=f)
      ...
      >>> os.close(dir_fd)  # don't leak a file descriptor

   El tipo de *file object* retornado por la función "open()"  depende
   del modo. Cuando se emplea  "open()" para abrir un fichero en modo
   texto ("'w'", "'r'", "'wt'", "'rt'", etc.), retorna una subclase de
   "io.TextIOBase" (específicamente "io.TextIOWrapper").  Cuando se
   emplea para abrir un fichero en modo binario con buffering, la
   clase retornada es una subclase de "io.BufferedIOBase".  La clase
   exacta varía: en modo binario de lectura, retorna
   "io.BufferedReader"; en modo de escritura y adición en binario,
   retorna "io.BufferedWriter", y en modo de escritura/lectura,
   retorna "io.BufferedRandom".  Si el buffering está desactivado, el
   flujo en crudo, una subclase de "io.RawIOBase", "io.FileIO", es
   retornada.

   Véase también los módulos para manejo de ficheros, como
   "fileinput", "io" (donde es declarada "open()"), "os", "os.path",
   "tempfile", y "shutil".

   Raises an auditing event "open" with arguments "path", "mode",
   "flags".

   Los argumentos "mode" y "flags" pueden haber sido modificados o
   inferidos de la llamada original.

   Distinto en la versión 3.3:

   * El parámetro *opener* fue añadido.

   * El modo  "'x'" fue añadido.

   * "IOError"  era la excepción lanzada anteriormente, ahora es un
     alias de "OSError".

   * Se lanza "FileExistsError"  si ya existe el fichero abierto en
     modo de creación exclusiva  ("'x'").

   Distinto en la versión 3.4:

   * El fichero ahora es no-heredable.

   Distinto en la versión 3.5:

   * Si la llamada al sistema es interrumpida y el gestor de señales
     no lanza una excepción, ahora la función reintenta la llamada de
     sistema en vez de lanzar una excepción "InterruptedError" (véase
     **PEP 475** para la justificación).

   * El gestor de errores  "'namereplace'" fue añadido.

   Distinto en la versión 3.6:

   * Añadido el soporte para aceptar objetos que implementan
     "os.PathLike".

   * En Windows, abrir un búfer en la consola puede retornar una
     subclase de "io.RawIOBase"  en vez de "io.FileIO".

   Distinto en la versión 3.11: El modo  "'X'" has ido eliminado.

ord(character, /)

   Return the ordinal value of a character.

   If the argument is a one-character string, return the Unicode code
   point of that character.  For example, "ord('a')" returns the
   integer "97" and "ord('€')" (Euro sign) returns "8364".  This is
   the inverse of "chr()".

   If the argument is a "bytes" or "bytearray" object of length 1,
   return its single byte value. For example, "ord(b'a')" returns the
   integer "97".

pow(base, exp, mod=None)

   Retorna *base* elevado a *exp*; si *mod* está presente, retorna
   *base* elevado a *exp*, módulo *mod* (calculado de manera más
   eficiente que "pow(base, exp) % mod").  La forma con dos argumentos
   "pow(base, exp)" es equivalente a usar el operador potencia:
   "base**exp".

   When arguments are builtin numeric types with mixed operand types,
   the coercion rules for binary arithmetic operators apply.  For
   "int" operands, the result has the same type as the operands (after
   coercion) unless the second argument is negative; in that case, all
   arguments are converted to float and a float result is delivered.
   For example, "pow(10, 2)" returns "100", but "pow(10, -2)" returns
   "0.01".  For a negative base of type "int" or "float" and a non-
   integral exponent, a complex result is delivered.  For example,
   "pow(-9, 0.5)" returns a value close to "3j". Whereas, for a
   negative base of type "int" or "float" with an integral exponent, a
   float result is delivered. For example, "pow(-9, 2.0)" returns
   "81.0".

   Para operandos "int" como *base* y *exp*, si *mod* está presente,
   *mod* debe ser también de tipo entero y distinto de cero. Si *mod*
   está presente y *exp* es negativo, *base* debe ser un número primo
   relativo a *mod*.  En ese caso, se retorna  "pow(inv_base, -exp,
   mod)", dónde *inv_base* es la inversa al módulo *mod* de *base*.

   Aquí tienes un ejemplo de cómo calcular la inversa de "38" módulo
   "97":

      >>> pow(38, -1, mod=97)
      23
      >>> 23 * 38 % 97 == 1
      True

   Distinto en la versión 3.8: Para operandos "int", la forma de "pow"
   con tres argumentos acepta ahora que el segundo argumento sea
   negativo, lo que permite el cálculo de inversos modulares.

   Distinto en la versión 3.8: Permite argumentos de palabra clave.
   Anteriormente, solo se soportaba el uso de argumentos posicionales.

print(*objects, sep=' ', end='\n', file=None, flush=False)

   Imprime *objects* al flujo de texto *file*, separándolos por *sep*
   y seguidos por *end*.  *sep*, *end*, *file* y *flush*, si están
   presentes, deben ser dados como argumentos por palabra clave.

   Todos los argumentos que no son por palabra clave se convierten a
   cadenas tal y como "str()" hace y se escriben al flujo, separados
   por *sep* y seguidos por *end*.  Tanto *sep* como *end* deben ser
   cadenas; también pueden ser "None", lo cual significa que se
   empleen los valores por defecto. Si no se indica *objects*,
   "print()" escribirá *end*.

   El argumento *file* debe ser un objeto que implemente un método
   "write(string)"; si éste no está presente o es "None", se usará
   "sys.stdout".  Dado que los argumentos mostrados son convertidos a
   cadenas de texto, "print()" no puede ser utilizada con objetos
   fichero en modo binario.  Para esos, utiliza en cambio
   "file.write(…)".

   El almacenamiento en búfer de salida generalmente está determinado
   por *file*. Sin embargo, si *flush* es verdadero, el flujo se vacía
   forzosamente.

   Distinto en la versión 3.3: Añadido el argumento por palabra clave
   *flush*.

class property(fget=None, fset=None, fdel=None, doc=None)

   Retorna un atributo propiedad.

   *fget* es una función para obtener el valor de un atributo. *fset*
   es una función para asignar el valor de un atributo. *fdel* es una
   función para eliminar el valor de un atributo. Y *doc* crea un
   *docstring* para el atributo.

   Un caso de uso típico es la definición de un atributo gestionado
   "x":

      class C:
          def __init__(self):
              self._x = None

          def getx(self):
              return self._x

          def setx(self, value):
              self._x = value

          def delx(self):
              del self._x

          x = property(getx, setx, delx, "I'm the 'x' property.")

   Si *c* es una instancia de *C*, "c.x" invocará el obtenedor
   (*getter*), "c.x = value" invocará el asignador (*setter*) y "del
   c.x" el suprimidor (*deleter*).

   If given, *doc* will be the docstring of the property attribute.
   Otherwise, the property will copy *fget*'s docstring (if it
   exists).  This makes it possible to create read-only properties
   easily using "@property" as a *decorator*:

      class Parrot:
          def __init__(self):
              self._voltage = 100000

          @property
          def voltage(self):
              """Get the current voltage."""
              return self._voltage

   The "@property" decorator turns the "voltage()" method into a
   "getter" for a read-only attribute with the same name, and it sets
   the docstring for *voltage* to "Get the current voltage."

   @getter

   @setter

   @deleter

      A property object has "getter", "setter", and "deleter" methods
      usable as decorators that create a copy of the property with the
      corresponding accessor function set to the decorated function.
      This is best explained with an example:

         class C:
             def __init__(self):
                 self._x = None

             @property
             def x(self):
                 """I'm the 'x' property."""
                 return self._x

             @x.setter
             def x(self, value):
                 self._x = value

             @x.deleter
             def x(self):
                 del self._x

      Este código equivale exactamente al primer ejemplo.  Asegúrese
      de otorgarle a las funciones adicionales el mismo nombre que la
      propiedad original ("x" en este caso.)

      El objeto propiedad retornado tiene también los atributos
      "fget", "fset", y "fdel" correspondientes a los argumentos del
      constructor.

   Distinto en la versión 3.5: Las *docstrings* de los objetos
   propiedad son escribibles.

   __name__

      Attribute holding the name of the property. The name of the
      property can be changed at runtime.

      Added in version 3.13.

class range(stop, /)
class range(start, stop, step=1, /)

   "range", más que una función, es en realidad un tipo de secuencia
   inmutable, tal y como está documentado en Rangos y Tipos secuencia
   --- list, tuple, range.

repr(object, /)

   Return a string containing a printable representation of an object.
   For many types, this function makes an attempt to return a string
   that would yield an object with the same value when passed to
   "eval()"; otherwise, the representation is a string enclosed in
   angle brackets that contains the name of the type of the object
   together with additional information often including the name and
   address of the object.  A class can control what this function
   returns for its instances by defining a "__repr__()" method. If
   "sys.displayhook()" is not accessible, this function will raise
   "RuntimeError".

   This class has a custom representation that can be evaluated:

      class Person:
         def __init__(self, name, age):
            self.name = name
            self.age = age

         def __repr__(self):
            return f"Person('{self.name}', {self.age})"

reversed(object, /)

   Return a reverse *iterator*.  The argument must be an object which
   has a "__reversed__()" method or supports the sequence protocol
   (the "__len__()" method and the "__getitem__()" method with integer
   arguments starting at "0").

round(number, ndigits=None)

   Retorna *number* redondeado a *ndigits* de precisión después del
   punto decimal. Si *ndigits* es omitido o es "None", retorna el
   entero más cercano a su entrada.

   Para los tipos integrados que admiten "round()", los valores se
   redondean al múltiplo más cercano de 10 a la potencia menos
   *ndigits*; si dos múltiplos están igualmente cerca, el redondeo se
   realiza hacia la opción par (así, por ejemplo, tanto "round(0.5)"
   como "round(-0.5)" son "0", y "round(1.5)" es "2").  Cualquier
   valor entero es válido para *ndigits* (positivo, cero o negativo).
   El valor retornado es un entero si se omite *ndigits* o "None". De
   lo contrario, el valor retornado tiene el mismo tipo que *number*.

   Para un objeto "number" general de Python,  "round" delega a
   "number.__round__".

   Nota:

     El comportamiento de "round()" para flotantes puede ser
     sorprendente: por ejemplo, "round(2.675, 2)" da "2.67" en vez de
     los "2.68" esperados. Esto no es un error: es el resultado del
     hecho de que la mayoría de fracciones decimales no se puede
     representar de forma exacta como flotantes. Véase Floating-Point
     Arithmetic:  Issues and Limitations para más información.

class set(iterable=(), /)

   Return a new "set" object, optionally with elements taken from
   *iterable*.  "set" is a built-in class.  See also Conjuntos ---
   set, frozenset for documentation about this class.

   Para otros contenedores ver las clases integradas (*built-in*)
   "frozenset", "list", "tuple", y "dict", así como el módulo
   "collections".

setattr(object, name, value, /)

   Es la función complementaria a "getattr()".  Los argumentos son un
   objeto, una cadena de caracteres, y un valor arbitrario. La cadena
   de caracteres puede nombrar un atributo existente o uno nuevo. La
   función asigna el valor al atributo si el objeto lo permite. Por
   ejemplo, "setattr(x, 'foobar', 123)" es equivalente a "x.foobar =
   123".

   *name* no necesita ser un identificador de Python como se define en
   Names (identifiers and keywords) a menos que el objeto decida
   imponerlo, por ejemplo, en un  "__getattribute__()" personalizado o
   a través de "__slots__". Un atributo cuyo nombre no es un
   identificador no será accesible usando la notación de puntos, pero
   sí a través de "getattr()" etc..

   Nota:

     Dado que private name mangling ocurre en el momento de la
     compilación, uno debe enredar manualmente el nombre de un
     atributo privado (atributos con dos guiones bajos principales)
     para recuperarlo con "getattr()".

class slice(stop, /)
class slice(start, stop, step=None, /)

   Return a *slice* object representing the set of indices specified
   by "range(start, stop, step)".  The *start* and *step* arguments
   default to "None".

   Slice objects are also generated when slicing syntax is used.  For
   example: "a[start:stop:step]" or "a[start:stop, i]".

   See "itertools.islice()" for an alternate version that returns an
   *iterator*.

   start
   stop
   step

      These read-only attributes are set to the argument values (or
      their default).  They have no other explicit functionality;
      however, they are used by NumPy and other third-party packages.

   Distinto en la versión 3.12: Ahora los objetos slice son *hashable*
   (siempre que "start", "stop" y "step" sean *hashable*).

sorted(iterable, /, *, key=None, reverse=False)

   Retorna una nueva lista ordenada a partir de los elementos en
   *iterable*.

   Tiene dos argumentos opcionales que deben ser especificados como
   argumentos de palabra clave.

   *key* especifica una función de un argumento que es empleada para
   extraer una clave de comparación de cada elemento en *iterable*
   (por ejemplo, "key=str.lower"). El valor por defecto es "None"
   (compara los elementos directamente).

   *reverse* es un valor boleado. Si está puesto a "True", entonces la
   lista de elementos se ordena como si cada comparación fuera
   reversa.

   Puedes usar "functools.cmp_to_key()" para convertir las funciones
   *cmp* a la antigua usanza en funciones *key*.

   La función built-in "sorted()" está garantizada en cuanto a su
   estabilidad. Un ordenamiento es estable si garantiza que no cambia
   el orden relativo de elementos que resultan igual en la comparación
   — esto es de gran ayuda para ordenar en múltiples pases (por
   ejemplo, ordenar por departamento, después por el escalafón de
   salario).

   The sort algorithm uses only "<" comparisons between items.  While
   defining an "__lt__()" method will suffice for sorting, **PEP 8**
   recommends that all six rich comparisons be implemented.  This will
   help avoid bugs when using the same data with other ordering tools
   such as "max()" that rely on a different underlying method.
   Implementing all six comparisons also helps avoid confusion for
   mixed type comparisons which can call the reflected "__gt__()"
   method.

   Para ejemplos de ordenamiento y para un breve tutorial sobre ello,
   ver Sorting Techniques.

@staticmethod

   Transforma un método en un método estático.

   Un método estático no recibe un primer argumento implícito. Para
   declarar un método estático, utiliza esta expresión:

      class C:
          @staticmethod
          def f(arg1, arg2, argN): ...

   La forma "@staticmethod" es una función *decorator* — ver
   Definiciones de funciones  para más detalles.

   A static method can be called either on the class (such as "C.f()")
   or on an instance (such as "C().f()"). Moreover, the static method
   *descriptor* is also callable, so it can be used in the class
   definition (such as "f()").

   Static methods in Python are similar to those found in Java or C++.
   Also, see "@classmethod" for a variant that is useful for creating
   alternate class constructors.

   Como todos los decoradores, es también posible llamar a
   "staticmethod" como una función normal y hacer algo con su
   resultado. Esto es necesario a veces cuando necesitas una
   referencia a una función desde el cuerpo de una clase y quieres
   evitar la transformación automática a un método de la instancia.
   Para dichos casos, emplea esta expresión:

      def regular_function():
          ...

      class C:
          method = staticmethod(regular_function)

   Para más información sobre métodos estáticos, ver Jerarquía de
   tipos estándar.

   Distinto en la versión 3.10: Static methods now inherit the method
   attributes ("__module__", "__name__", "__qualname__", "__doc__" and
   "__annotations__"), have a new "__wrapped__" attribute, and are now
   callable as regular functions.

class str(*, encoding='utf-8', errors='strict')
class str(object)
class str(object, encoding, errors='strict')
class str(object, *, errors)

   Retorna una versión "str" del *object*. Ver "str()" para más
   detalles.

   "str" es la *class* cadena built-in . Para información general
   sobre strings, ver Cadenas de caracteres --- str.

sum(iterable, /, start=0)

   Suma *start* y los elementos de un *iterable* de izquierda a
   derecha y Retorna el total. Los elementos del *iterable* son
   normalmente números, y el valor *start* no puede ser una cadena.

   For some use cases, there are good alternatives to "sum()". The
   preferred, fast way to concatenate a sequence of strings is by
   calling "''.join(sequence)".  To add floating-point values with
   extended precision, see "math.fsum()".  To concatenate a series of
   iterables, consider using "itertools.chain()".

   Distinto en la versión 3.8: El parámetro *start* puede ser
   especificado como un argumento de palabra clave.

   Distinto en la versión 3.12: Summation of floats switched to an
   algorithm that gives higher accuracy and better commutativity on
   most builds.

   Distinto en la versión 3.14: Added specialization for summation of
   complexes, using same algorithm as for summation of floats.

class super
class super(type, object_or_type=None, /)

   Retorna un objeto proxy que delega las llamadas de métodos a clases
   padre o hermanas de *type*. Esto es útil para acceder métodos
   heredados que han sido invalidados en una clase.

   *object-or-type* determina el *method resolution order* a ser
   buscado. La búsqueda empieza desde la clase justo después de
   *type*.

   For example, if "__mro__" of *object_or_type* is "D -> B -> C -> A
   -> object" and the value of *type* is "B", then "super()" searches
   "C -> A -> object".

   The "__mro__" attribute of the class corresponding to
   *object_or_type* lists the method resolution search order used by
   both "getattr()" and "super()".  The attribute is dynamic and can
   change whenever the inheritance hierarchy is updated.

   Si se omite el segundo argumento, el objeto super retornado no está
   vinculado.  Si el segundo argumento es un objeto, "isinstance(obj,
   type)" debe ser verdadero.  Si el segundo argumento es un tipo,
   "issubclass(type2, type)" debe ser verdadero (esto es útil para
   classmethods).

   When called directly within an ordinary method of a class, both
   arguments may be omitted ("zero-argument "super()""). In this case,
   *type* will be the enclosing class, and *obj* will be the first
   argument of the immediately enclosing function (typically "self").
   (This means that zero-argument "super()" will not work as expected
   within nested functions, including generator expressions, which
   implicitly create nested functions.)

   Hay dos casos de uso típicos para *super*.  En una jerarquía de
   clases con herencia única, *super* puede ser utilizado para
   referirse a las clases padre sin llamarlas explícitamente, haciendo
   el código más sencillo de mantener. Este uso es muy similar al de
   *super* en otros lenguajes de programación.

   El segundo caso de uso es el soporte de herencia múltiple
   cooperativa en un entorno de ejecución dinámica.  Este caso de uso
   es único en Python y no se encuentra en lenguajes estáticos
   compilados o que solo soportan herencia única.  Esto hace posible
   implementar los "diagramas de diamantes", donde múltiples clases
   base implementan el mismo método. Las buenas prácticas de diseño
   dictan que estas implementaciones tengan la misma signatura de
   llamada en cada caso (porque el orden de llamadas se determina en
   tiempo de ejecución, porque ese orden se adapta a los cambios en la
   jerarquía de clase y porque ese orden puede incluir clases hermanas
   que son desconocidas antes de la ejecución).

   Para ambos casos, la llamada típica de una superclase se parece a:

      class C(B):
          def method(self, arg):
              super().method(arg)    # This does the same thing as:
                                     # super(C, self).method(arg)

   Además de para los métodos de búsqueda, "super()"  también funciona
   para búsquedas de atributos.  Un caso de uso posible para esto es
   llamar a  *descriptores*  en una clase padre o hermana.

   Note that "super()" is implemented as part of the binding process
   for explicit dotted attribute lookups such as
   "super().__getitem__(name)". It does so by implementing its own
   "__getattribute__()" method for searching classes in a predictable
   order that supports cooperative multiple inheritance. Accordingly,
   "super()" is undefined for implicit lookups using statements or
   operators such as "super()[name]".

   Nótese también, que aparte de en su forma sin argumentos,
   "super()"  no está limitada a su uso dentro de métodos.  La forma
   con dos argumentos especifica de forma exacta los argumentos y hace
   las referencias apropiadas.  La forma sin argumentos solo funciona
   dentro de una definición de clase, ya que el compilador completa
   los detalles necesarios para obtener correctamente la clase que
   está siendo definida, así como accediendo a la instancia actual
   para métodos ordinarios.

   Para sugerencias prácticas sobre como diseñas clases cooperativas
   usando  "super()", véase guía de uso de super().

   Distinto en la versión 3.14: "super" objects are now "pickleable"
   and  "copyable".

class tuple(iterable=(), /)

   Más que una función, "tuple"  es en realidad un tipo de secuencia
   inmutable, tal y como está documentado en Tuplas y  Tipos secuencia
   --- list, tuple, range.

class type(object, /)
class type(name, bases, dict, /, **kwargs)

   With one argument, return the type of an *object*.  The return
   value is a type object and generally the same object as returned by
   "object.__class__".

   La función integrada  "isinstance()" es la recomendada para testear
   el tipo de un objeto, ya que tiene en cuenta las subclases.

   With three arguments, return a new type object.  This is
   essentially a dynamic form of the "class" statement. The *name*
   string is the class name and becomes the "__name__" attribute. The
   *bases* tuple contains the base classes and becomes the "__bases__"
   attribute; if empty, "object", the ultimate base of all classes, is
   added.  The *dict* dictionary contains attribute and method
   definitions for the class body; it may be copied or wrapped before
   becoming the "__dict__" attribute. The following two statements
   create identical "type" objects:

   >>> class X:
   ...     a = 1
   ...
   >>> X = type('X', (), dict(a=1))

   See also:

   * Documentation on attributes and methods on classes.

   * Objetos Tipo

   Los argumentos de palabras clave proporcionados al formulario de
   tres argumentos se pasan a la maquinaria de metaclase apropiada
   (generalmente "__init_subclass__()") de la misma manera que lo
   harían las palabras clave en una definición de clase (además de
   *metaclase*).

   Unlike a "class" statement, the three argument form does not call
   the metaclass "__prepare__" method (see Preparando el espacio de
   nombres de la clase).  Use "types.new_class()" to dynamically
   create a class using the appropriate metaclass.

   Ver también  Personalización de creación de clases.

   Distinto en la versión 3.6: Subclasses of "type" which don't
   override "type.__new__" may no longer use the one-argument form to
   get the type of an object.

vars()
vars(object, /)

   Return the "__dict__" attribute for a module, class, instance, or
   any other object with a "__dict__" attribute.

   Objects such as modules and instances have an updateable "__dict__"
   attribute; however, other objects may have write restrictions on
   their "__dict__" attributes (for example, classes use a
   "types.MappingProxyType" to prevent direct dictionary updates).

   Without an argument, "vars()" acts like "locals()".

   Una excepción "TypeError" se genera si se especifica un objeto pero
   no tiene un atributo "__dict__" (por ejemplo, si su clase define el
   atributo "__slots__").

   Distinto en la versión 3.13: The result of calling this function
   without an argument has been updated as described for the
   "locals()" builtin.

zip(*iterables, strict=False)

   Iterar sobre varios iterables en paralelo, generando tuplas con un
   item para cada una.

   Ejemplo:

      >>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
      ...     print(item)
      ...
      (1, 'sugar')
      (2, 'spice')
      (3, 'everything nice')

   Más formalmente: "zip()" retorna un iterador de tuplas, donde la
   tupla *i*-ésima contiene el elemento *i*-ésimo de cada uno de los
   argumentos iterables.

   Otra forma de pensar en "zip()" es que convierte las filas en
   columnas y las columnas en filas.  Esto es similar a transponer una
   matriz.

   "zip()" es perezoso: los elementos no se procesarán hasta que el
   iterable sea iterado, por ejemplo, mediante un bucle "for" o
   envolviendo en un "list".

   Una cosa a considerar es que los iterables pasados a "zip()"
   podrían tener diferentes longitudes; a veces por diseño, y a veces
   por un error en el código que preparó estos iterables. Python
   ofrece tres enfoques diferentes para tratar este problema:

   * De forma predeterminada, "zip()" se detiene cuando se agota el
     iterable más corto. Ignorará los elementos restantes en las
     iteraciones más largas, cortando el resultado a la longitud del
     iterable más corto:

        >>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
        [(0, 'fee'), (1, 'fi'), (2, 'fo')]

   * "zip()" se usa a menudo en los casos en que se supone que los
     iterables son de igual longitud. En tales casos, se recomienda
     usar la opción "strict=True". Su salida es la misma que la normal
     "zip()":

        >>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
        [('a', 1), ('b', 2), ('c', 3)]

     A diferencia del comportamiento predeterminado, lanza una
     excepción "ValueError" si un iterable se agota antes que los
     demás:

     >>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):
     ...     print(item)
     ...
     (0, 'fee')
     (1, 'fi')
     (2, 'fo')
     Traceback (most recent call last):
       ...
     ValueError: zip() argument 2 is longer than argument 1

     Sin el argumento "strict=True", cualquier error que resulte en
     iterables de diferentes longitudes será silenciado, posiblemente
     manifestándose como un error difícil de encontrar en otra parte
     del programa.

   * Las iteraciones más cortas se pueden acolchar con un valor
     constante para que todas las iteraciones tengan la misma
     longitud.  Esto lo hace "itertools.zip_longest()".

   Casos extremos: con un único argumento iterable, "zip()" retorna un
   iterador de 1-tuplas. Sin argumentos, retorna un iterador vacío.

   Consejos y trucos:

   * La evaluación de izquierda a derecha de los iterables está
     garantizada. Esto permite emplear una expresión idiomática para
     agregar una serie de datos en grupos de tamaño *n* usando
     "zip(*[iter(s)]*n, strict=True)". Esto repite el *mismo* iterador
     "n" veces de forma que cada tupla de salida tiene el resultado de
     "n" llamadas al iterador. Esto tiene el efecto de dividir la
     entrada en trozos de longitud *n*.

   * "zip()"  en conjunción con el operador  "*"  puede usar para
     descomprimir (*unzip*) una lista:

        >>> x = [1, 2, 3]
        >>> y = [4, 5, 6]
        >>> list(zip(x, y))
        [(1, 4), (2, 5), (3, 6)]
        >>> x2, y2 = zip(*zip(x, y))
        >>> x == list(x2) and y == list(y2)
        True

   Distinto en la versión 3.10: Añadido el argumento "strict".

__import__(name, globals=None, locals=None, fromlist=(), level=0)

   Nota:

     Ésta es una función avanzada que no se necesita en el uso
     cotidiano de programación en Python, a diferencia de
     "importlib.import_module()".

   Esta función es invocada por la declaración "import". Puede ser
   reemplazada para cambiar la semántica de la declaración "import"
   (mediante la importación del módulo "builtins" y su asignación a
   "builtins.__import__"), pero esto está **fuertemente** no
   recomendado ya que es normalmente mucho más simple usar ganchos
   (*hooks*) de importación (ver **PEP 302**) para obtener los mismos
   objetivos y sin causar problemas en código que asume que la
   implementación por defecto de importaciones está siendo utilizada.
   El uso directo de  "__import__()" tampoco está recomendado y se
   prefiere  "importlib.import_module()".

   La función importa el módulo *name*, usando potencialmente las
   *globals* y *locals* indicadas para determinar como interpretar el
   nombre en el contexto de un paquete. *fromlist* indica los nombres
   de objetos o submódulos que deberían ser importados del módulo
   indicado por *name*.  La implementación estándar no utiliza su
   argumento *locals* para nada, y usa *globals* solo para determinar
   el contexto en un paquete de la declaración "import".

   *level* especifica si usar importaciones absolutas o relativas. "0"
   (por defecto) significa sólo realizar importaciones absolutas.
   Valores positivos de  *level* indican el número de directorios
   progenitores relativos al del módulo para buscar llamando a
   "__import__()" (ver **PEP 328** para los detalles).

   Cuando la variable *name* tiene la forma "package.module",
   normalmente el paquete del nivel más alto (el nombre hasta el
   primer punto) se retorna, *no* el modulo llamado por *name*.  Sin
   embargo, cuando un argumento *fromlist* no vacío es indicado, el
   módulo llamado por *name* es retornado.

   Por ejemplo, la declaración "import spam" resulta en un bytecode
   similar al siguiente código:

      spam = __import__('spam', globals(), locals(), [], 0)

   La declaración "import spam.ham"  resulta en esta llamada:

      spam = __import__('spam.ham', globals(), locals(), [], 0)

   Nótese cómo "__import__()" retorna el módulo del nivel superior en
   este caso porque este es el objeto que está enlazado a un nombre
   por la declaración "import".

   Por otra parte, la declaración  "from spam.ham import eggs, sausage
   as saus" resulta en

      _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
      eggs = _temp.eggs
      saus = _temp.sausage

   Aquí, el módulo "spam.ham" es retornado desde  "__import__()".
   Desde este objeto, los nombres a importar son obtenidos y asignados
   a sus nombres respectivos.

   Si simplemente quieres importar un módulo (potencialmente dentro de
   un paquete) por nombre, usa  "importlib.import_module()".

   Distinto en la versión 3.3: Valores negativos para *level* ya no
   están soportados (lo que también cambia el valor por defecto a 0).

   Distinto en la versión 3.9: Cuando se utilizan las opciones de
   línea de comando "-E" o "-I", la variable de entorno "PYTHONCASEOK"
   ahora se ignora.

-[ Notas al pie ]-

[1] Ten en cuenta que el *parser* sólo acepta la convención de final
    de línea de tipo Unix. Si estás leyendo el código de un fichero,
    asegúrate de usar la el modo de conversión de nueva línea para
    convertir las líneas de tipo Windows o Mac.
