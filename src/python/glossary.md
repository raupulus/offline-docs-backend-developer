---
title: Glosario
source_url: https://docs.python.org/es/3
source_path: glossary.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
order: 1130
---

# Glosario

">>>"
   The default Python prompt of the *interactive* shell.  Often seen
   for code examples which can be executed interactively in the
   interpreter.

"..."
   Puede referirse a:

   * The default Python prompt of the *interactive* shell when
     entering the code for an indented code block, when within a pair
     of matching left and right delimiters (parentheses, square
     brackets, curly braces or triple quotes), or after specifying a
     decorator.

   * The three dots form of the Ellipsis object.

clase base abstracta
   Las clases base abstractas (ABC, por sus siglas en inglés *Abstract
   Base Class*) complementan al *duck-typing* brindando un forma de
   definir interfaces con técnicas como "hasattr()" que serían
   confusas o sutilmente erróneas (por ejemplo con magic methods). Las
   ABC introduce subclases virtuales, las cuales son clases que no
   heredan desde una clase pero aún así son reconocidas por
   "isinstance()" y "issubclass()"; vea la documentación del módulo
   "abc". Python viene con muchas ABC incorporadas para las
   estructuras de datos( en el módulo "collections.abc"), números (en
   el módulo "numbers" ) , flujos de datos (en el módulo "io" ) ,
   buscadores y cargadores de importaciones (en el módulo
   "importlib.abc" ) . Puede crear sus propios ABCs con el módulo
   "abc".

annotate function
   A callable that can be called to retrieve the *annotations* of an
   object. Annotate functions are usually *functions*, automatically
   generated as the "__annotate__" attribute of functions, classes,
   and modules. Annotate functions are a subset of *evaluate
   functions*.

anotación
   Una etiqueta asociada a una variable, atributo de clase, parámetro
   de función o valor de retorno, usado por convención como un *type
   hint*.

   Annotations of local variables cannot be accessed at runtime, but
   annotations of global variables, class attributes, and functions
   can be retrieved by calling "annotationlib.get_annotations()" on
   modules, classes, and functions, respectively.

   See *variable annotation*, *function annotation*, **PEP 484**,
   **PEP 526**, and **PEP 649**, which describe this functionality.
   Also see Prácticas recomendadas para las anotaciones for best
   practices on working with annotations.

argumento
   Un valor pasado a una *function* (o *method*) cuando se llama a la
   función. Hay dos clases de argumentos:

   * *argumento nombrado*: es un argumento precedido por un
     identificador (por ejemplo, "nombre=") en una llamada a una
     función o pasado como valor en un diccionario precedido por "**".
     Por ejemplo "3" y "5" son argumentos nombrados en las llamadas a
     "complex()":

        complex(real=3, imag=5)
        complex(**{'real': 3, 'imag': 5})

   * *argumento posicional* son aquellos que no son nombrados. Los
     argumentos posicionales deben aparecer al principio de una lista
     de argumentos o ser pasados como elementos de un *iterable*
     precedido por "*". Por ejemplo, "3" y "5" son argumentos
     posicionales en las siguientes llamadas:

        complex(3, 5)
        complex(*(3, 5))

   Los argumentos son asignados a las variables locales en el cuerpo
   de la función. Vea en la sección Invocaciones las reglas que rigen
   estas asignaciones. Sintácticamente, cualquier expresión puede ser
   usada para representar un argumento; el valor evaluado es asignado
   a la variable local.

   Vea también el *parameter* en el glosario, la pregunta frecuente la
   diferencia entre argumentos y parámetros, y **PEP 362**.

administrador asincrónico de contexto
   Un objeto que controla el entorno visible en un sentencia "async
   with" al definir los métodos "__aenter__()" y "__aexit__()".
   Introducido por **PEP 492**.

generador asincrónico
   Informally used to mean either an *asynchronous generator function*
   or an *asynchronous generator iterator*, depending on context.  The
   formal terms *asynchronous generator function* and *asynchronous
   generator iterator* are uncommon in practice; "asynchronous
   generator" alone is almost always sufficient.

asynchronous generator function
   A function which returns an *asynchronous generator iterator*. It
   looks like a coroutine function defined with "async def" except
   that it contains "yield" expressions for producing a series of
   values usable in an "async for" loop.  See **PEP 525**.

   Una función generadora asincrónica puede contener expresiones
   "await" así como sentencias "async for", y "async with".

iterador generador asincrónico
   An object created by an *asynchronous generator function*.

   Este es un *asynchronous iterator* el cual cuando es llamado usa el
   método "__anext__()" retornando un objeto a la espera (*awaitable*)
   el cual ejecutará el cuerpo de la función generadora asincrónica
   hasta la siguiente expresión "yield".

   Each "yield" temporarily suspends processing, remembering the
   execution state (including local variables and pending try-
   statements).  When the *asynchronous generator iterator*
   effectively resumes with another awaitable returned by
   "__anext__()", it picks up where it left off.  See **PEP 492** and
   **PEP 525**.

iterable asincrónico
   Un objeto, que puede ser usado en una sentencia "async for". Debe
   retornar un *asynchronous iterator* de su método "__aiter__()".
   Introducido por **PEP 492**.

iterador asincrónico
   Un objeto que implementa los métodos "__aiter__()" y "__anext__()".
   "__anext__()" debe retornar un objeto *awaitable*. "async for"
   resuelve los esperables retornados por un método de iterador
   asincrónico "__anext__()" hasta que lanza una excepción
   "StopAsyncIteration". Introducido por **PEP 492**.

atomic operation
   An operation that appears to execute as a single, indivisible step:
   no other thread can observe it half-done, and its effects become
   visible all at once.  Python does not guarantee that high-level
   statements are atomic (for example, "x += 1" performs multiple
   bytecode operations and is not atomic).  Atomicity is only
   guaranteed where explicitly documented.  See also *race condition*
   and *data race*.

attached thread state
   A *thread state* that is active for the current OS thread.

   When a *thread state* is attached, the OS thread has access to the
   full Python C API and can safely invoke the bytecode interpreter.

   Unless a function explicitly notes otherwise, attempting to call
   the C API without an attached thread state will result in a fatal
   error or undefined behavior.  A thread state can be attached and
   detached explicitly by the user through the C API, or implicitly by
   the runtime, including during blocking C calls and by the bytecode
   interpreter in between calls.

   On most builds of Python, having an attached thread state implies
   that the caller holds the *GIL* for the current interpreter, so
   only one OS thread can have an attached thread state at a given
   moment. In *free-threaded builds* of Python, threads can
   concurrently hold an attached thread state, allowing for true
   parallelism of the bytecode interpreter.

atributo
   Un valor asociado a un objeto al que se suele hacer referencia por
   su nombre utilizando expresiones punteadas. Por ejemplo, si un
   objeto *o* tiene un atributo *a* se referenciaría como *o.a*.

   Es posible dar a un objeto un atributo cuyo nombre no sea un
   identificador definido por Names (identifiers and keywords), por
   ejemplo usando "setattr()", si el objeto lo permite. Dicho atributo
   no será accesible utilizando una expresión con puntos, y en su
   lugar deberá ser recuperado con "getattr()".

a la espera
   Un objeto que puede utilizarse en una expresión "await".  Puede ser
   una *corutina* o un objeto con un método "__await__()". Véase
   también **PEP 492**.

BDFL
   Sigla de *Benevolent Dictator For Life*, benevolente dictador
   vitalicio, es decir Guido van Rossum, el creador de Python.

archivo binario
   A *file object* able to read and write *bytes-like objects*.
   Examples of binary files are files opened in binary mode ("'rb'",
   "'wb'" or "'rb+'"), "sys.stdin.buffer", "sys.stdout.buffer", and
   instances of "io.BytesIO" and "gzip.GzipFile".

   Vea también *text file* para un objeto archivo capaz de leer y
   escribir objetos "str".

referencia prestada
   En la API C de Python, una referencia prestada es una referencia a
   un objeto, donde el código usando el objeto no posee la referencia.
   Se convierte en un puntero colgante si se destruye el objeto. Por
   ejemplo, una recolección de basura puede eliminar el último *strong
   reference* del objeto y así destruirlo.

   Se recomienda llamar a "Py_INCREF()" en la *referencia prestada*
   para convertirla en una *referencia fuerte* in situ, excepto cuando
   el objeto no se puede destruir antes del último uso de la
   referencia prestada. La función "Py_NewRef()" se puede utilizar
   para crear una nueva *referencia fuerte*.

objetos tipo binarios
   Un objeto que soporta Protocolo búfer  y puede exportar un búfer
   C-*contiguous*. Esto incluye todas los objetos "bytes",
   "bytearray", y "array.array", así como muchos objetos comunes
   "memoryview". Los objetos tipo binarios pueden ser usados para
   varias operaciones que usan datos binarios; éstas incluyen
   compresión, salvar a archivos binarios, y enviarlos a través de un
   socket.

   Algunas operaciones necesitan que los datos binarios sean mutables.
   La documentación frecuentemente se refiere a éstos como "objetos
   tipo binario de lectura y escritura". Ejemplos de objetos de búfer
   mutables incluyen a "bytearray" y "memoryview" de la "bytearray".
   Otras operaciones que requieren datos binarios almacenados en
   objetos inmutables ("objetos tipo binario de sólo lectura");
   ejemplos de éstos incluyen "bytes" y "memoryview" del objeto
   "bytes".

bytecode
   El código fuente Python es compilado en *bytecode*, la
   representación interna de un programa python en el intérprete
   CPython. El *bytecode* también es guardado en caché en los archivos
   *.pyc* de tal forma que ejecutar el mismo archivo es más fácil la
   segunda vez (la recompilación desde el código fuente a *bytecode*
   puede ser evitada). Este "lenguaje intermedio" deberá corren en una
   *virtual machine* que ejecute el código de máquina correspondiente
   a cada *bytecode*. Note que los *bytecodes* no tienen como
   requisito trabajar en las diversas máquina virtuales de Python, ni
   de ser estable entre versiones Python.

   Una lista de las instrucciones en *bytecode* está disponible en la
   documentación de el módulo dis.

callable
   Un callable es un objeto que puede ser llamado, posiblemente con un
   conjunto de argumentos (véase *argument*), con la siguiente
   sintaxis:

      callable(argument1, argument2, argumentN)

   Una *function*, y por extensión un *method*, es un callable. Una
   instancia de una clase que implementa el método "__call__()"
   también es un callable.

retrollamada
   Una función de subrutina que se pasa como un argumento para
   ejecutarse en algún momento en el futuro.

clase
   Una plantilla para crear objetos definidos por el usuario. Las
   definiciones de clase normalmente contienen definiciones de métodos
   que operan una instancia de la clase.

variable de clase
   Una variable definida en una clase y prevista para ser modificada
   sólo a nivel de clase (es decir, no en una instancia de la clase).

closure variable
   A *free variable* referenced from a *nested scope* that is defined
   in an outer scope rather than being resolved at runtime from the
   globals or builtin namespaces. May be explicitly defined with the
   "nonlocal" keyword to allow write access, or implicitly defined if
   the variable is only being read.

   For example, in the "inner" function in the following code, both
   "x" and "print" are *free variables*, but only "x" is a *closure
   variable*:

      def outer():
          x = 0
          def inner():
              nonlocal x
              x += 1
              print(x)
          return inner

   Due to the "codeobject.co_freevars" attribute (which, despite its
   name, only includes the names of closure variables rather than
   listing all referenced free variables), the more general *free
   variable* term is sometimes used even when the intended meaning is
   to refer specifically to closure variables.

número complejo
   Una extensión del sistema familiar de número reales en el cual los
   números son expresados como la suma de una parte real y una parte
   imaginaria.  Los números imaginarios son múltiplos de la unidad
   imaginaria (la raíz cuadrada de "-1"), usualmente escrita como "i"
   en matemáticas o "j" en ingeniería.  Python tiene soporte
   incorporado para números complejos, los cuales son escritos con la
   notación mencionada al final.; la parte imaginaria es escrita con
   un sufijo "j", por ejemplo, "3+1j".  Para tener acceso a los
   equivalentes complejos del módulo "math" module, use "cmath".  El
   uso de números complejos es matemática bastante avanzada.  Si no le
   parecen necesarios, puede ignorarlos sin inconvenientes.

concurrency
   The ability of a computer program to perform multiple tasks at the
   same time.  Python provides libraries for writing programs that
   make use of different forms of concurrency.  "asyncio" is a library
   for dealing with asynchronous tasks and coroutines.  "threading"
   provides access to operating system threads and "multiprocessing"
   to operating system processes. Multi-core processors can execute
   threads and processes on different CPU cores at the same time (see
   *parallelism*).

concurrent modification
   When multiple threads modify shared data at the same time.
   Concurrent modification without proper synchronization can cause
   *race conditions*, and might also trigger a *data race*, data
   corruption, or both.

context
   This term has different meanings depending on where and how it is
   used. Some common meanings:

   * The temporary state or environment established by a *context
     manager* via a "with" statement.

   * The collection of key­value bindings associated with a particular
     "contextvars.Context" object and accessed via "ContextVar"
     objects.  Also see *context variable*.

   * A "contextvars.Context" object.  Also see *current context*.

context management protocol
   The "__enter__()" and "__exit__()" methods called by the "with"
   statement.  See **PEP 343**.

administrador de contextos
   An object which implements the *context management protocol* and
   controls the environment seen in a "with" statement.  See **PEP
   343**.

variable de contexto
   A variable whose value depends on which context is the *current
   context*.  Values are accessed via "contextvars.ContextVar"
   objects.  Context variables are primarily used to isolate state
   between concurrent asynchronous tasks.

contiguo
   Un búfer es considerado contiguo con precisión si es *C-contiguo* o
   *Fortran contiguo*. Los búferes cero dimensionales con C y Fortran
   contiguos. En los arreglos unidimensionales, los ítems deben ser
   dispuestos en memoria uno siguiente al otro, ordenados por índices
   que comienzan en cero. En arreglos unidimensionales C-contiguos, el
   último índice varía más velozmente en el orden de las direcciones
   de memoria. Sin embargo, en arreglos Fortran contiguos, el primer
   índice vería más rápidamente.

corrutina
   Las corrutinas son una forma más generalizadas de las subrutinas. A
   las subrutinas se ingresa por un punto y se sale por otro punto.
   Las corrutinas pueden se iniciadas, finalizadas y reanudadas en
   muchos puntos diferentes. Pueden ser implementadas con la sentencia
   "async def". Vea además **PEP 492**.

función corrutina
   Un función que retorna un objeto  *coroutine* . Una función
   corrutina puede ser definida con la sentencia "async def", y puede
   contener las palabras claves "await", "async for", y "async with".
   Las mismas son introducidas en **PEP 492**.

CPython
   La implementación canónica del lenguaje de programación Python,
   como se distribuye en python.org. El término "CPython" es usado
   cuando es necesario distinguir esta implementación de otras como
   *Jython* o *IronPython*.

current context
   The *context* ("contextvars.Context" object) that is currently used
   by "ContextVar" objects to access (get or set) the values of
   *context variables*.  Each thread has its own current context.
   Frameworks for executing asynchronous tasks (see "asyncio")
   associate each task with a context which becomes the current
   context whenever the task starts or resumes execution.

cyclic isolate
   A subgroup of one or more objects that reference each other in a
   reference cycle, but are not referenced by objects outside the
   group.  The goal of the *cyclic garbage collector* is to identify
   these groups and break the reference cycles so that the memory can
   be reclaimed.

data race
   A situation where multiple threads access the same memory location
   concurrently, at least one of the accesses is a write, and the
   threads do not use any synchronization to control their access.
   Data races lead to *non-deterministic* behavior and can cause data
   corruption. Proper use of *locks* and other *synchronization
   primitives* prevents data races.  Note that data races can only
   happen in native code, but that *native code* might be exposed in a
   Python API.  See also *race condition* and *thread-safe*.

deadlock
   A situation in which two or more tasks (threads, processes, or
   coroutines) wait indefinitely for each other to release resources
   or complete actions, preventing any from making progress.  For
   example, if thread A holds lock 1 and waits for lock 2, while
   thread B holds lock 2 and waits for lock 1, both threads will wait
   indefinitely.  In Python this often arises from acquiring multiple
   locks in conflicting orders or from circular join/await
   dependencies.  Deadlocks can be avoided by always acquiring
   multiple *locks* in a consistent order.  See also *lock* and
   *reentrant*.

decorador
   A function returning another function, usually applied as a
   function transformation using the "@wrapper" syntax.  Common
   examples for decorators are "@classmethod" and "@staticmethod".

   La sintaxis del decorador es meramente azúcar sintáctico, las
   definiciones de las siguientes dos funciones son semánticamente
   equivalentes:

      def f(arg):
          ...
      f = staticmethod(f)

      @staticmethod
      def f(arg):
          ...

   El mismo concepto existe para clases, pero son menos usadas. Vea la
   documentación de function definitions y class definitions para
   mayor detalle sobre decoradores.

descriptor
   Any object which defines the methods "__get__()", "__set__()", or
   "__delete__()". When a class attribute is a descriptor, its special
   binding behavior is triggered upon attribute lookup.  Normally,
   using *a.b* to get, set or delete an attribute looks up the object
   named *b* in the class dictionary for *a*, but if *b* is a
   descriptor, the respective descriptor method gets called.
   Understanding descriptors is a key to a deep understanding of
   Python because they are the basis for many features including
   functions, methods, properties, class methods, static methods, and
   reference to super classes.

   Para obtener más información sobre los métodos de los descriptores,
   consulte Implementando descriptores o Guía práctica de uso de los
   descriptores.

diccionario
   An associative array, where arbitrary keys are mapped to values.
   The keys can be any object with "__hash__()" and "__eq__()"
   methods. Called a hash in Perl.

comprensión de diccionarios
   Una forma compacta de procesar todos o parte de los elementos en un
   iterable y retornar un diccionario con los resultados. "results =
   {n: n ** 2 for n in range(10)}" genera un diccionario que contiene
   la clave "n" asignada al valor "n ** 2". Ver Despliegues para
   listas, conjuntos y diccionarios.

vista de diccionario
   Los objetos retornados por los métodos  "dict.keys()",
   "dict.values()", y "dict.items()" son llamados vistas de
   diccionarios. Proveen una vista dinámica de las entradas de un
   diccionario, lo que significa que cuando el diccionario cambia, la
   vista refleja éstos cambios. Para forzar a la vista de diccionario
   a convertirse en una lista completa, use "list(dictview)".  Vea
   Objetos tipos vista de diccionario.

docstring
   A string literal which appears as the first expression in a class,
   function or module.  While ignored when the suite is executed, it
   is recognized by the compiler and put into the "__doc__" attribute
   of the enclosing class, function or module.  Since it is available
   via introspection, it is the canonical place for documentation of
   the object.

tipado de pato
   Un estilo de programación que no revisa el tipo del objeto para
   determinar si tiene la interfaz correcta; en vez de ello, el método
   o atributo es simplemente llamado o usado ("Si se ve como un pato y
   grazna como un pato, debe ser un pato").  Enfatizando las
   interfaces en vez de hacerlo con los tipos específicos, un código
   bien diseñado pues tener mayor flexibilidad permitiendo la
   sustitución polimórfica.  El tipado de pato *duck-typing* evita
   usar pruebas llamando a "type()" o "isinstance()".  (Nota: si
   embargo, el tipado de pato puede ser complementado con *abstract
   base classes*. En su lugar, generalmente pregunta con "hasattr()" o
   *EAFP*.

dunder
   An informal short-hand for "double underscore", used when talking
   about a *special method*. For example, "__init__" is often
   pronounced "dunder init".

EAFP
   Del inglés *Easier to ask for forgiveness than permission*, es más
   fácil pedir perdón que pedir permiso.  Este estilo de codificación
   común en Python asume la existencia de claves o atributos válidos y
   atrapa las excepciones si esta suposición resulta falsa.  Este
   estilo rápido y limpio está caracterizado por muchas sentencias
   "try" y "except".  Esta técnica contrasta con estilo *LBYL* usual
   en otros lenguajes como C.

evaluate function
   A function that can be called to evaluate a lazily evaluated
   attribute of an object, such as the value of type aliases created
   with the "type" statement.

expresión
   Una construcción sintáctica que puede ser evaluada, hasta dar un
   valor.  En otras palabras, una expresión es una acumulación de
   elementos de expresión tales como literales, nombres, accesos a
   atributos, operadores o llamadas a funciones, todos ellos
   retornando valor.  A diferencia de otros lenguajes, no toda la
   sintaxis del lenguaje son expresiones. También hay *statement*s que
   no pueden ser usadas como expresiones, como la "while".  Las
   asignaciones también son sentencias, no expresiones.

módulo de extensión
   Un módulo escrito en C o C++, usando la API para C de Python para
   interactuar con el núcleo y el código del usuario.

f-string
f-strings
   String literals prefixed with "f" or "F" are commonly called
   "f-strings" which is short for formatted string literals.  See also
   **PEP 498**.

objeto archivo
   An object exposing a file-oriented API (with methods such as
   "read()" or "write()") to an underlying resource.  Depending on the
   way it was created, a file object can mediate access to a real on-
   disk file or to another type of storage or communication device
   (for example standard input/output, in-memory buffers, sockets,
   pipes, etc.).  File objects are also called *file-like objects* or
   *streams*.

   Existen tres categorías de objetos archivo: crudos *raw* *archivos
   binarios*, con búfer *archivos binarios* y *archivos de texto*.
   Sus interfaces son definidas en el módulo "io".  La forma canónica
   de crear objetos archivo es usando la función "open()".

objetos tipo archivo
   Un sinónimo de *file object*.

codificación del sistema de archivos y manejador de errores
   Controlador de errores y codificación utilizado por Python para
   decodificar bytes del sistema operativo y codificar Unicode en el
   sistema operativo.

   La codificación del sistema de archivos debe garantizar la
   decodificación exitosa de todos los bytes por debajo de 128. Si la
   codificación del sistema de archivos no proporciona esta garantía,
   las funciones de API pueden lanzar "UnicodeError".

   Las funciones "sys.getfilesystemencoding()" y
   "sys.getfilesystemencodeerrors()" se pueden utilizar para obtener
   la codificación del sistema de archivos y el controlador de
   errores.

   La *codificación del sistema de archivos y el manejador de errores*
   se configuran al inicio de Python mediante la función
   "PyConfig_Read()": consulte los miembros "filesystem_encoding" y
   "filesystem_errors" de "PyConfig".

   Vea también *locale encoding*.

buscador
   Un objeto que trata de encontrar el *loader* para el módulo que
   está siendo importado.

   There are two types of finder: *meta path finders* for use with
   "sys.meta_path", and *path entry finders* for use with
   "sys.path_hooks".

   See Buscadores y cargadores and "importlib" for much more detail.

división entera a la baja
   Una división matemática que se redondea hacia el entero menor más
   cercano.  El operador de la división entera a la baja es "//".  Por
   ejemplo, la expresión "11 // 4" evalúa "2" a diferencia del "2.75"
   retornado por la verdadera división de números flotantes.  Note que
   "(-11) // 4" es "-3" porque es "-2.75" redondeado *para abajo*. Ver
   **PEP 238**.

free threading
   A threading model where multiple threads can run Python bytecode
   simultaneously within the same interpreter.  This is in contrast to
   the *global interpreter lock* which allows only one thread to
   execute Python bytecode at a time.  See **PEP 703**.

free-threaded build
   A build of *CPython* that supports *free threading*, configured
   using the "--disable-gil" option before compilation.

   See Python support for free threading.

free variable
   Formally, as defined in the language execution model, a free
   variable is any variable used in a namespace which is not a local
   variable in that namespace. See *closure variable* for an example.
   Pragmatically, due to the name of the "codeobject.co_freevars"
   attribute, the term is also sometimes used as a synonym for
   *closure variable*.

función
   Una serie de sentencias que retornan un valor al que las llama.
   También se le puede pasar cero o más *argumentos* los cuales pueden
   ser usados en la ejecución de la misma. Vea también *parameter*,
   *method*, y la sección Definiciones de funciones.

anotación de función
   Una *annotation* del parámetro de una función o un valor de
   retorno.

   Las anotaciones de funciones son usadas frecuentemente para
   *indicadores de tipo*, por ejemplo, se espera que una función tome
   dos argumentos de clase "int"  y también se espera que retorne dos
   valores "int":

      def sum_two_numbers(a: int, b: int) -> int:
         return a + b

   La sintaxis de las anotaciones de funciones son explicadas en la
   sección Definiciones de funciones.

   Consulte *variable annotation* y **PEP 484**, que describen esta
   funcionalidad. Consulte también Prácticas recomendadas para las
   anotaciones para conocer las mejores prácticas sobre cómo trabajar
   con anotaciones.

__future__
   Un future statement, "from __future__ import <feature>", indica al
   compilador que compile el módulo actual utilizando una sintaxis o
   semántica que se convertirá en estándar en una versión futura de
   Python. El módulo "__future__" documenta los posibles valores de
   *feature*. Al importar este módulo y evaluar sus variables, puede
   ver cuándo se agregó por primera vez una nueva característica al
   lenguaje y cuándo se convertirá (o se convirtió) en la
   predeterminada:

      >>> import __future__
      >>> __future__.division
      _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

recolección de basura
   El proceso de liberar la memoria de lo que ya no está en uso.
   Python realiza recolección de basura (*garbage collection*)
   llevando la cuenta de las referencias, y el recogedor de basura
   cíclico es capaz de detectar y romper las referencias cíclicas.  El
   recogedor de basura puede ser controlado mediante el módulo "gc" .

generador
   Informally used to mean either a *generator function* or a
   *generator iterator*, depending on context.  The formal terms
   *generator function* and *generator iterator* are uncommon in
   practice; "generator" alone is almost always sufficient.

generator function
   A function which returns a *generator* object.  It looks like a
   normal function except that it contains "yield" expressions for
   producing a series of values usable in a "for"-loop or that can be
   retrieved one at a time with the "next()" function. See Expresiones
   yield.

iterador generador
   An object created by a *generator function* or a *generator
   expression*.

   Each "yield" temporarily suspends processing, remembering the
   execution state (including local variables and pending try-
   statements). When the *generator iterator* resumes, it picks up
   where it left off (in contrast to functions which start fresh on
   every invocation).

   Generator iterators also implement the "send()" method to send a
   value into the suspended generator, and the "throw()" method to
   raise an exception at the point where the generator was paused.
   See Métodos generador-iterador.

expresión generadora
   An *expression* that returns an *iterator*.  It looks like a normal
   expression followed by a "for" clause defining a loop variable,
   range, and an optional "if" clause.  The combined expression
   generates values for an enclosing function:

      >>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
      285

función genérica
   Una función compuesta de muchas funciones que implementan la misma
   operación para diferentes tipos. Qué implementación deberá ser
   usada durante la llamada a la misma es determinado por el algoritmo
   de despacho.

   See also the *single dispatch* glossary entry, the
   "@functools.singledispatch" decorator, and **PEP 443**.

tipos genéricos
   Un *type* que se puede parametrizar; normalmente un container class
   como "list" o "dict". Usado para *type hints* y *annotations*.

   Para más detalles, véase generic alias types, **PEP 483**, **PEP
   484**, **PEP 585**, y el módulo "typing".

GIL
   Vea *global interpreter lock*.

bloqueo global del intérprete
   Mecanismo empleado por el intérprete *CPython* para asegurar que
   sólo un hilo ejecute el  *bytecode* Python por vez. Esto simplifica
   la implementación de CPython haciendo que el modelo de objetos
   (incluyendo algunos críticos como "dict") están implícitamente a
   salvo de acceso concurrente.  Bloqueando el intérprete completo se
   simplifica hacerlo multi-hilos, a costa de mucho del paralelismo
   ofrecido por las máquinas con múltiples procesadores.

   Sin embargo, algunos módulos de extensión, tanto estándar como de
   terceros, están diseñados para liberar el GIL cuando se realizan
   tareas computacionalmente intensivas como la compresión o el
   *hashing*.  Además, el GIL siempre es liberado cuando se hace
   entrada/salida.

   As of Python 3.13, the GIL can be disabled using the "--disable-
   gil" build configuration. After building Python with this option,
   code must be run with "-X gil=0" or after setting the
   "PYTHON_GIL=0" environment variable. This feature enables improved
   performance for multi-threaded applications and makes it easier to
   use multi-core CPUs efficiently. For more details, see **PEP 703**.

   In prior versions of Python's C API, a function might declare that
   it requires the GIL to be held in order to use it. This refers to
   having an *attached thread state*.

global state
   Data that is accessible throughout a program, such as module-level
   variables, class variables, or C static variables in *extension
   modules*.  In multi-threaded programs, global state shared between
   threads typically requires synchronization to avoid *race
   conditions* and *data races*.

hash-based pyc
   Un archivo cache de *bytecode* que usa el *hash* en vez de usar el
   tiempo de la última modificación del archivo fuente correspondiente
   para determinar su validez. Vea Invalidación del código de bytes en
   caché.

hashable
   An object is *hashable* if it has a hash value which never changes
   during its lifetime (it needs a "__hash__()" method), and can be
   compared to other objects (it needs an "__eq__()" method). Hashable
   objects which compare equal must have the same hash value.

   Ser *hashable* hace a un objeto utilizable como clave de un
   diccionario y miembro de un set, porque éstas estructuras de datos
   usan los valores de hash internamente.

   La mayoría de los objetos inmutables incorporados en Python son
   *hashables*; los contenedores mutables (como las listas o los
   diccionarios) no lo son; los contenedores inmutables (como tuplas y
   conjuntos *frozensets*) son *hashables* si sus elementos son
   *hashables* .  Los objetos que son instancias de clases definidas
   por el usuario son *hashables* por defecto.  Todos se comparan como
   desiguales (excepto consigo mismos), y su valor de hash está
   derivado de su función "id()".

IDLE
   Un Entorno Integrado de Desarrollo y Aprendizaje para Python. IDLE
   --- Python editor and shell es un editor básico y un entorno de
   intérprete que se incluye con la distribución estándar de Python.

immortal
   *Immortal objects* are a CPython implementation detail introduced
   in **PEP 683**.

   If an object is immortal, its *reference count* is never modified,
   and therefore it is never deallocated while the interpreter is
   running. For example, "True" and "None" are immortal in CPython.

   Immortal objects can be identified via "sys._is_immortal()", or via
   "PyUnstable_IsImmortal()" in the C API.

inmutable
   An object with a fixed value.  Immutable objects include numbers,
   strings and tuples.  Such an object cannot be altered.  A new
   object has to be created if a different value has to be stored.
   They play an important role in places where a constant hash value
   is needed, for example as a key in a dictionary.  Immutable objects
   are inherently *thread-safe* because their state cannot be modified
   after creation, eliminating concerns about improperly synchronized
   *concurrent modification*.

ruta de importación
   Una lista de las ubicaciones (o *entradas de ruta*) que son
   revisadas por *path based finder* al importar módulos. Durante la
   importación, ésta lista de localizaciones usualmente viene de
   "sys.path", pero para los subpaquetes también puede incluir al
   atributo "__path__" del paquete padre.

importar
   El proceso mediante el cual el código Python dentro de un módulo se
   hace alcanzable desde otro código Python en otro módulo.

importador
   Un objeto que buscan y lee un módulo; un objeto que es tanto
   *finder* como *loader*.

index
   A numeric value that represents the position of an element in a
   *sequence*.

   In Python, indexing starts at zero. For example, "things[0]" names
   the *first* element of "things"; "things[1]" names the second one.

   In some contexts, Python allows negative indexes for counting from
   the end of a sequence, and indexing using *slices*.

   See also *subscript*.

interactivo
   Python has an interactive interpreter which means you can enter
   statements and expressions at the interpreter prompt, immediately
   execute them and see their results.  Just launch "python" with no
   arguments (possibly by selecting it from your computer's main
   menu). It is a very powerful way to test out new ideas or inspect
   modules and packages (remember "help(x)"). For more on interactive
   mode, see Modo interactivo.

interpretado
   Python es un lenguaje interpretado, a diferencia de uno compilado,
   a pesar de que la distinción puede ser difusa debido al compilador
   a *bytecode*.  Esto significa que los archivos fuente pueden ser
   corridos directamente, sin crear explícitamente un ejecutable que
   es corrido luego. Los lenguajes interpretados típicamente tienen
   ciclos de desarrollo y depuración más cortos que los compilados,
   sin embargo sus programas suelen correr más lentamente.  Vea
   también  *interactive*.

apagado del intérprete
   Cuando se le solicita apagarse, el intérprete Python ingresa a un
   fase especial en la cual gradualmente libera todos los recursos
   reservados, como módulos y varias estructuras internas críticas.
   También hace varias llamadas al *recolector de basura*.  Esto puede
   disparar la ejecución de código de destructores definidos por el
   usuario o *weakref callbacks*. El código ejecutado durante la fase
   de apagado puede encontrar varias excepciones debido a que los
   recursos que necesita pueden no funcionar más (ejemplos comunes son
   los módulos de bibliotecas o los artefactos de advertencias
   *warnings machinery*)

   La principal razón para el apagado del intérpreter es que el módulo
   "__main__" o el script que estaba corriendo termine su ejecución.

iterable
   An object capable of returning its members one at a time. Examples
   of iterables include all sequence types (such as "list", "str", and
   "tuple") and some non-sequence types like "dict", *file objects*,
   and objects of any classes you define with an "__iter__()" method
   or with a "__getitem__()" method that implements *sequence*
   semantics.

   Iterables can be used in a "for" loop and in many other places
   where a sequence is needed ("zip()", "map()", ...).  When an
   iterable object is passed as an argument to the built-in function
   "iter()", it returns an iterator for the object.  This iterator is
   good for one pass over the set of values.  When using iterables, it
   is usually not necessary to call "iter()" or deal with iterator
   objects yourself.  The "for" statement does that automatically for
   you, creating a temporary unnamed variable to hold the iterator for
   the duration of the loop.  See also *iterator*, *sequence*, and
   *generator*.

iterador
   An object representing a stream of data.  Repeated calls to the
   iterator's "__next__()" method (or passing it to the built-in
   function "next()") return successive items in the stream.  When no
   more data are available a "StopIteration" exception is raised
   instead.  At this point, the iterator object is exhausted and any
   further calls to its "__next__()" method just raise "StopIteration"
   again.  Iterators are required to have an "__iter__()" method that
   returns the iterator object itself so every iterator is also
   iterable and may be used in most places where other iterables are
   accepted.  One notable exception is code which attempts multiple
   iteration passes.  A container object (such as a "list") produces a
   fresh new iterator each time you pass it to the "iter()" function
   or use it in a "for" loop.  Attempting this with an iterator will
   just return the same exhausted iterator object used in the previous
   iteration pass, making it appear like an empty container.

   Puede encontrar más información en Tipos de iteradores.

   **Detalles de implementación de CPython:** CPython does not
   consistently apply the requirement that an iterator define
   "__iter__()". And also please note that *free-threaded* CPython
   does not guarantee *thread-safe* behavior of iterator operations.

key
   A value that identifies an entry in a *mapping*. See also
   *subscript*.

función clave
   Una función clave o una función de colación es un invocable que
   retorna un valor usado para el ordenamiento o clasificación.  Por
   ejemplo, "locale.strxfrm()" es usada para producir claves de
   ordenamiento que se adaptan a las convenciones específicas de
   ordenamiento de un *locale*.

   Cierta cantidad de herramientas de Python aceptan funciones clave
   para controlar como los elementos son ordenados o agrupados.
   Incluyendo a  "min()", "max()", "sorted()", "list.sort()",
   "heapq.merge()", "heapq.nsmallest()", "heapq.nlargest()", y
   "itertools.groupby()".

   There are several ways to create a key function.  For example. the
   "str.casefold()" method can serve as a key function for case
   insensitive sorts.  Alternatively, a key function can be built from
   a "lambda" expression such as "lambda r: (r[0], r[2])".  Also,
   "operator.attrgetter()", "operator.itemgetter()", and
   "operator.methodcaller()" are three key function constructors.  See
   the Sorting HOW TO for examples of how to create and use key
   functions.

argumento nombrado
   Vea *argument*.

lambda
   Una función anónima de una línea consistente en un sola
   *expression* que es evaluada cuando la función es llamada.  La
   sintaxis para crear una función lambda es "lambda [parameters]:
   expression"

LBYL
   Del inglés *Look before you leap*, "mira antes de saltar".  Es un
   estilo de codificación que prueba explícitamente las condiciones
   previas antes de hacer llamadas o búsquedas.  Este estilo contrasta
   con la manera *EAFP* y está caracterizado por la presencia de
   muchas sentencias "if".

   In a multi-threaded environment, the LBYL approach can risk
   introducing a *race condition* between "the looking" and "the
   leaping".  For example, the code, "if key in mapping: return
   mapping[key]" can fail if another thread removes *key* from
   *mapping* after the test, but before the lookup. This issue can be
   solved with *locks* or by using the *EAFP* approach.  See also
   *thread-safe*.

lexical analyzer
   Formal name for the *tokenizer*; see *token*.

lista
   A built-in Python *sequence*.  Despite its name it is more akin to
   an array in other languages than to a linked list since access to
   elements is *O*(1).

comprensión de listas
   Una forma compacta de procesar todos o parte de los elementos en
   una secuencia y retornar una lista como resultado.  "result =
   ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]" genera una
   lista de cadenas conteniendo números hexadecimales (0x..) entre 0 y
   255. La cláusula "if" es opcional.  Si es omitida, todos los
   elementos en "range(256)" son procesados.

lock
   A *synchronization primitive* that allows only one thread at a time
   to access a shared resource.  A thread must acquire a lock before
   accessing the protected resource and release it afterward.  If a
   thread attempts to acquire a lock that is already held by another
   thread, it will block until the lock becomes available.  Python's
   "threading" module provides "Lock" (a basic lock) and "RLock" (a
   *reentrant* lock).  Locks are used to prevent *race conditions* and
   ensure *thread-safe* access to shared data.  Alternative design
   patterns to locks exist such as queues, producer/consumer patterns,
   and thread-local state. See also *deadlock*, and *reentrant*.

lock-free
   An operation that does not acquire any *lock* and uses atomic CPU
   instructions to ensure correctness. Lock-free operations can
   execute concurrently without blocking each other and cannot be
   blocked by operations that hold locks. In *free-threaded* Python,
   built-in types like "dict" and "list" provide lock-free read
   operations, which means other threads may observe intermediate
   states during multi-step modifications even when those
   modifications hold the *per-object lock*.

cargador
   An object that loads a module. It must define the "exec_module()"
   and "create_module()" methods to implement the "Loader" interface.
   A loader is typically returned by a *finder*. See also:

   * Buscadores y cargadores

   * "importlib.abc.Loader"

   * **PEP 302**

codificación de la configuración regional
   En Unix, es la codificación de la configuración regional LC_CTYPE.
   Se puede configurar con "locale.setlocale(locale.LC_CTYPE,
   new_locale)".

   En Windows, es la página de códigos ANSI (por ejemplo, ""cp1252"").

   En Android y VxWorks, Python utiliza ""utf-8"" como codificación
   regional.

   "locale.getencoding()" can be used to get the locale encoding.

   Vea también *filesystem encoding and error handler*.

método mágico
   Una manera informal de llamar a un *special method*.

mapeado
   Un objeto contenedor que permite recupero de claves arbitrarias y
   que implementa los métodos especificados en la
   "collections.abc.Mapping" o "collections.abc.MutableMapping"
   abstract base classes.  Por ejemplo, "dict",
   "collections.defaultdict", "collections.OrderedDict" y
   "collections.Counter".

meta buscadores de ruta
   Un *finder* retornado por una búsqueda de "sys.meta_path".  Los
   meta buscadores de ruta están relacionados a *buscadores de
   entradas de rutas*, pero son algo diferente.

   Vea en "importlib.abc.MetaPathFinder" los métodos que los meta
   buscadores de ruta implementan.

metaclase
   La clase de una clase.  Las definiciones de clases crean nombres de
   clase, un diccionario de clase, y una lista de clases base.  Las
   metaclases son responsables de tomar estos tres argumentos y crear
   la clase.  La mayoría de los objetos de un lenguaje de programación
   orientado a objetos provienen de una implementación por defecto.
   Lo que hace a Python especial que es posible crear metaclases a
   medida.  La mayoría de los usuario nunca necesitarán esta
   herramienta, pero cuando la necesidad surge, las metaclases pueden
   brindar soluciones poderosas y elegantes.  Han sido usadas para
   *loggear* acceso de atributos, agregar seguridad a hilos, rastrear
   la creación de objetos, implementar *singletons*, y muchas otras
   tareas.

   Más información hallará en Metaclases.

método
   Una función que es definida dentro del cuerpo de una clase.  Si es
   llamada como un atributo de una instancia de otra clase, el método
   tomará el objeto instanciado como su primer *argument* (el cual es
   usualmente denominado *self*). Vea *function* y *nested scope*.

orden de resolución de métodos
   Method Resolution Order is the order in which base classes are
   searched for a member during lookup. See The Python 2.3 Method
   Resolution Order for details of the algorithm used by the Python
   interpreter since the 2.3 release.

módulo
   Un objeto que sirve como unidad de organización del código Python.
   Los módulos tienen espacios de nombres conteniendo objetos Python
   arbitrarios.  Los módulos son cargados en Python por el proceso de
   *importing*.

   Vea también *package*.

especificador de módulo
   Un espacio de nombres que contiene la información relacionada a la
   importación usada al leer un módulo.  Una instancia de
   "importlib.machinery.ModuleSpec".

   See also Module specs.

MRO
   Vea *method resolution order*.

mutable
   An *object* with state that is allowed to change during the course
   of the program.  In multi-threaded programs, mutable objects that
   are shared between threads require careful synchronization to avoid
   *race conditions*.  See also *immutable*, *thread-safe*, and
   *concurrent modification*.

tupla nombrada
   La denominación "tupla nombrada" se aplica a cualquier tipo o clase
   que hereda de una tupla y cuyos elementos indexables son también
   accesibles usando atributos nombrados. Este tipo o clase puede
   tener además otras capacidades.

   Varios tipos incorporados son tuplas nombradas, incluyendo los
   valores retornados por "time.localtime()" y "os.stat()".  Otro
   ejemplo es "sys.float_info":

      >>> sys.float_info[1]                   # indexed access
      1024
      >>> sys.float_info.max_exp              # named field access
      1024
      >>> isinstance(sys.float_info, tuple)   # kind of tuple
      True

   Some named tuples are built-in types (such as the above examples).
   Alternatively, a named tuple can be created from a regular class
   definition that inherits from "tuple" and that defines named
   fields.  Such a class can be written by hand, or it can be created
   by inheriting "typing.NamedTuple", or with the factory function
   "collections.namedtuple()".  The latter techniques also add some
   extra methods that may not be found in hand-written or built-in
   named tuples.

espacio de nombres
   El lugar donde la variable es almacenada.  Los espacios de nombres
   son implementados como diccionarios.  Hay espacio de nombre local,
   global, e incorporado así como espacios de nombres anidados en
   objetos (en métodos).  Los espacios de nombres soportan modularidad
   previniendo conflictos de nombramiento.  Por ejemplo, las funciones
   "builtins.open" y "os.open()" se distinguen por su espacio de
   nombres.  Los espacios de nombres también ayuda a la legibilidad y
   mantenibilidad dejando claro qué módulo implementa una función.
   Por ejemplo, escribiendo "random.seed()" o "itertools.islice()"
   queda claro que éstas funciones están implementadas en los módulos
   "random" y "itertools", respectivamente.

paquete de espacios de nombres
   A *package* which serves only as a container for subpackages.
   Namespace packages may have no physical representation, and
   specifically are not like a *regular package* because they have no
   "__init__.py" file.

   Namespace packages allow several individually installable packages
   to have a common parent package. Otherwise, it is recommended to
   use a *regular package*.

   For more information, see **PEP 420** and Paquetes de espacio de
   nombres.

   Vea también *module*.

native code
   Code that is compiled to machine instructions and runs directly on
   the processor, as opposed to code that is interpreted or runs in a
   virtual machine.  In the context of Python, native code typically
   refers to C, C++, Rust or Fortran code in *extension modules* that
   can be called from Python.  See also *extension module*.

alcances anidados
   La habilidad de referirse a una variable dentro de una definición
   encerrada.  Por ejemplo, una función definida dentro de otra
   función puede referir a variables en la función externa.  Note que
   los alcances anidados por defecto sólo funcionan para referencia y
   no para asignación.  Las variables locales leen y escriben sólo en
   el alcance más interno.  De manera semejante, las variables
   globales pueden leer y escribir en el espacio de nombres global.
   Con "nonlocal" se puede escribir en alcances exteriores.

clase de nuevo estilo
   Old name for the flavor of classes now used for all class objects.
   In earlier Python versions, only new-style classes could use
   Python's newer, versatile features like "__slots__", descriptors,
   properties, "__getattribute__()", class methods, and static
   methods.

non-deterministic
   Behavior where the outcome of a program can vary between executions
   with the same inputs.  In multi-threaded programs, non-
   deterministic behavior often results from *race conditions* where
   the relative timing or interleaving of threads affects the result.
   Proper synchronization using *locks* and other *synchronization
   primitives* helps ensure deterministic behavior.

objeto
   Cualquier dato con estado (atributo o valor) y comportamiento
   definido (métodos).  También es la más básica clase base para
   cualquier *new-style class*.

optimized scope
   A scope where target local variable names are reliably known to the
   compiler when the code is compiled, allowing optimization of read
   and write access to these names. The local namespaces for
   functions, generators, coroutines, comprehensions, and generator
   expressions are optimized in this fashion. Note: most interpreter
   optimizations are applied to all scopes, only those relying on a
   known set of local and nonlocal variable names are restricted to
   optimized scopes.

optional module
   An *extension module* that is part of the *standard library*, but
   may be absent in some builds of *CPython*, usually due to missing
   third-party libraries or because the module is not available for a
   given platform.

   See Requirements for optional modules for a list of optional
   modules that require third-party libraries.

paquete
   Un *module* Python que puede contener submódulos o recursivamente,
   subpaquetes.  Técnicamente, un paquete es un módulo Python con un
   atributo "__path__".

   Vea también *regular package* y *namespace package*.

parallelism
   Executing multiple operations at the same time (e.g. on multiple
   CPU cores).  In Python builds with the *global interpreter lock
   (GIL)*, only one thread runs Python bytecode at a time, so taking
   advantage of multiple CPU cores typically involves multiple
   processes (e.g. "multiprocessing") or native extensions that
   release the GIL. In *free-threaded* Python, multiple Python threads
   can run Python code simultaneously on different cores.

parámetro
   Una entidad nombrada en una definición de una *function* (o método)
   que especifica un *argument* (o en algunos casos, varios
   argumentos) que la función puede aceptar.  Existen cinco tipos de
   argumentos:

   * *posicional o nombrado*: especifica un argumento que puede ser
     pasado tanto como *posicional* o como *nombrado*.  Este es el
     tipo por defecto de parámetro, como *foo* y *bar* en el siguiente
     ejemplo:

        def func(foo, bar=None): ...

   * *sólo posicional*: especifica un argumento que puede ser pasado
     sólo por posición.  Los parámetros sólo posicionales pueden ser
     definidos incluyendo un carácter "/" en la lista de parámetros de
     la función después de ellos, como *posonly1* y *posonly2* en el
     ejemplo que sigue:

        def func(posonly1, posonly2, /, positional_or_keyword): ...

   * *sólo nombrado*: especifica un argumento que sólo puede ser
     pasado por nombre.  Los parámetros sólo por nombre pueden ser
     definidos incluyendo un parámetro posicional de una sola variable
     o un simple "*`" antes de ellos en la lista de parámetros en la
     definición de la función, como *kw_only1* y *kw_only2* en el
     ejemplo siguiente:

        def func(arg, *, kw_only1, kw_only2): ...

   * *variable posicional*: especifica una secuencia arbitraria de
     argumentos posicionales que pueden ser brindados (además de
     cualquier argumento posicional aceptado por otros parámetros).
     Este parámetro puede ser definido anteponiendo al nombre del
     parámetro "*", como a *args* en el siguiente ejemplo:

        def func(*args, **kwargs): ...

   * *variable nombrado*: especifica que arbitrariamente muchos
     argumentos nombrados pueden ser brindados (además de cualquier
     argumento nombrado ya aceptado por cualquier otro parámetro).
     Este parámetro puede ser definido anteponiendo al nombre del
     parámetro con "**", como *kwargs* en el ejemplo precedente.

   Los parámetros puede especificar tanto argumentos opcionales como
   requeridos, así como valores por defecto para algunos argumentos
   opcionales.

   Vea también el glosario de *argument*, la pregunta respondida en la
   diferencia entre argumentos y parámetros, la clase
   "inspect.Parameter", la sección Definiciones de funciones , y **PEP
   362**.

per-object lock
   A *lock* associated with an individual object instance rather than
   a global lock shared across all objects. In *free-threaded* Python,
   built-in types like "dict" and "list" use per-object locks to allow
   concurrent operations on different objects while serializing
   operations on the same object. Operations that hold the per-object
   lock prevent other locking operations on the same object from
   proceeding, but do not block *lock-free* operations.

entrada de ruta
   Una ubicación única en el *import path* que el *path based finder*
   consulta para encontrar los módulos a importar.

buscador de entradas de ruta
   Un *finder* retornado por un invocable en "sys.path_hooks" (esto
   es, un *path entry hook*) que sabe cómo localizar módulos dada una
   *path entry*.

   Vea en "importlib.abc.PathEntryFinder" los métodos que los
   buscadores de entradas de ruta implementan.

gancho a entrada de ruta
   A callable on the "sys.path_hooks" list which returns a *path entry
   finder* if it knows how to find modules on a specific *path entry*.

buscador basado en ruta
   Uno de los *meta buscadores de ruta* por defecto que busca un
   *import path* para los módulos.

objeto tipo ruta
   Un objeto que representa una ruta del sistema de archivos. Un
   objeto tipo ruta puede ser tanto una "str" como un "bytes"
   representando una ruta, o un objeto que implementa el protocolo
   "os.PathLike". Un objeto que soporta el protocolo  "os.PathLike"
   puede ser convertido a ruta del sistema de archivo de clase "str" o
   "bytes" usando la función "os.fspath()"; "os.fsdecode()"
   "os.fsencode()" pueden emplearse para garantizar que retorne
   respectivamente "str" o "bytes". Introducido por **PEP 519**.

PEP
   Propuesta de mejora de Python, del inglés *Python Enhancement
   Proposal*. Un PEP es un documento de diseño que brinda información
   a la comunidad Python, o describe una nueva capacidad para Python,
   sus procesos o entorno. Los PEPs deberían dar una especificación
   técnica concisa y una fundamentación para las capacidades
   propuestas.

   Los PEPs tienen como propósito ser los mecanismos primarios para
   proponer nuevas y mayores capacidad, para recoger la opinión de la
   comunidad sobre un tema, y para documentar las decisiones de diseño
   que se han hecho en Python. El autor del PEP es el responsable de
   lograr consenso con la comunidad y documentar las opiniones
   disidentes.

   Vea **PEP 1**.

porción
   Un conjunto de archivos en un único directorio (posiblemente guardo
   en un archivo comprimido *zip*) que contribuye a un espacio de
   nombres de paquete, como está definido en **PEP 420**.

argumento posicional
   Vea *argument*.

API provisional
   Una API provisoria es aquella que deliberadamente fue excluida de
   las garantías de compatibilidad hacia atrás de la biblioteca
   estándar.  Aunque no se esperan cambios fundamentales en dichas
   interfaces, como están marcadas como provisionales, los cambios
   incompatibles hacia atrás (incluso remover la misma interfaz)
   podrían ocurrir si los desarrolladores principales lo estiman.
   Estos cambios no se hacen gratuitamente -- solo ocurrirán si fallas
   fundamentales y serias son descubiertas que no fueron vistas antes
   de la inclusión de la API.

   Incluso para APIs provisorias, los cambios incompatibles hacia
   atrás son vistos como una "solución de último recurso" - se
   intentará todo para encontrar una solución compatible hacia atrás
   para los problemas identificados.

   Este proceso permite que la biblioteca estándar continúe
   evolucionando con el tiempo, sin bloquearse por errores de diseño
   problemáticos por períodos extensos de tiempo. Vea **PEP 411** para
   más detalles.

paquete provisorio
   Vea *provisional API*.

Python 3000
   Apodo para la fecha de lanzamiento de Python 3.x (acuñada en un
   tiempo cuando llegar a la versión 3 era algo distante en el
   futuro.)  También se lo abrevió como *Py3k*.

Pythónico
   Una idea o pieza de código que sigue ajustadamente la convenciones
   idiomáticas comunes del lenguaje Python, en vez de implementar
   código usando conceptos comunes a otros lenguajes.  Por ejemplo,
   una convención común en Python es hacer bucles sobre todos los
   elementos de un iterable con la sentencia "for".  Muchos otros
   lenguajes no tienen este tipo de construcción, así que los que no
   están familiarizados con Python podrían usar contadores numéricos:

      for i in range(len(food)):
          print(food[i])

   En contraste, un método Pythónico más limpio:

      for piece in food:
          print(piece)

nombre calificado
   Un nombre con puntos mostrando la ruta desde el alcance global del
   módulo a la clase, función o método definido en dicho módulo, como
   se define en **PEP 3155**.  Para las funciones o clases de más alto
   nivel, el nombre calificado es el igual al nombre del objeto:

      >>> class C:
      ...     class D:
      ...         def meth(self):
      ...             pass
      ...
      >>> C.__qualname__
      'C'
      >>> C.D.__qualname__
      'C.D'
      >>> C.D.meth.__qualname__
      'C.D.meth'

   Cuando es usado para referirse a los módulos, *nombre completamente
   calificado* significa la ruta con puntos completo al módulo,
   incluyendo cualquier paquete padre, por ejemplo, "email.mime.text":

      >>> import email.mime.text
      >>> email.mime.text.__name__
      'email.mime.text'

race condition
   A condition of a program where the behavior depends on the relative
   timing or ordering of events, particularly in multi-threaded
   programs.  Race conditions can lead to *non-deterministic* behavior
   and bugs that are difficult to reproduce.  A *data race* is a
   specific type of race condition involving unsynchronized access to
   shared memory.  The *LBYL* coding style is particularly susceptible
   to race conditions in multi-threaded code.  Using *locks* and other
   *synchronization primitives* helps prevent race conditions.

contador de referencias
   The number of references to an object.  When the reference count of
   an object drops to zero, it is deallocated.  Some objects are
   *immortal* and have reference counts that are never modified, and
   therefore the objects are never deallocated.  Reference counting is
   generally not visible to Python code, but it is a key element of
   the *CPython* implementation.  Programmers can call the
   "sys.getrefcount()" function to return the reference count for a
   particular object.

   In *CPython*, reference counts are not considered to be stable or
   well-defined values; the number of references to an object, and how
   that number is affected by Python code, may be different between
   versions.

paquete regular
   Un  *package* tradicional, como aquellos con un directorio
   conteniendo el archivo "__init__.py".

   Vea también *namespace package*.

reentrant
   A property of a function or *lock* that allows it to be called or
   acquired multiple times by the same thread without causing errors
   or a *deadlock*.

   For functions, reentrancy means the function can be safely called
   again before a previous invocation has completed, which is
   important when functions may be called recursively or from signal
   handlers. Thread-unsafe functions may be *non-deterministic* if
   they're called reentrantly in a multithreaded program.

   For locks, Python's "threading.RLock" (reentrant lock) is
   reentrant, meaning a thread that already holds the lock can acquire
   it again without blocking.  In contrast, "threading.Lock" is not
   reentrant - attempting to acquire it twice from the same thread
   will cause a deadlock.

   See also *lock* and *deadlock*.

REPL
   An acronym for the "read–eval–print loop", another name for the
   *interactive* interpreter shell.

__slots__
   Es una declaración dentro de una clase que ahorra memoria
   predeclarando espacio para las atributos de la instancia y
   eliminando diccionarios de la instancia.  Aunque es popular, esta
   técnica es algo dificultosa de lograr correctamente y es mejor
   reservarla para los casos raros en los que existen grandes
   cantidades de instancias en aplicaciones con uso crítico de
   memoria.

secuencia
   An *iterable* which supports efficient element access using integer
   indices via the "__getitem__()" special method and defines a
   "__len__()" method that returns the length of the sequence. Some
   built-in sequence types are "list", "str", "tuple", and "bytes".
   Note that "dict" also supports "__getitem__()" and "__len__()", but
   is considered a mapping rather than a sequence because the lookups
   use arbitrary *hashable* keys rather than integers.

   The "collections.abc.Sequence" abstract base class defines a much
   richer interface that goes beyond just "__getitem__()" and
   "__len__()", adding "count()", "index()", "__contains__()", and
   "__reversed__()". Types that implement this expanded interface can
   be registered explicitly using "register()". For more documentation
   on sequence methods generally, see Common Sequence Operations.

comprensión de conjuntos
   Una forma compacta de procesar todos o parte de los elementos en un
   iterable y retornar un conjunto con los resultados. "results = {c
   for c in 'abracadabra' if c not in 'abc'}" genera el conjunto de
   cadenas "{'r', 'd'}". Ver Despliegues para listas, conjuntos y
   diccionarios.

despacho único
   Una forma de despacho de una *generic function* donde la
   implementación es elegida a partir del tipo de un sólo argumento.

rebanada
   An object of type "slice", used to describe a portion of a
   *sequence*. A slice object is created when using the slicing form
   of subscript notation, with colons inside square brackets, such as
   in "variable_name[1:3:5]".

soft deprecated
   A soft deprecated API should not be used in new code, but it is
   safe for already existing code to use it. The API remains
   documented and tested, but will not be enhanced further.

   Soft deprecation, unlike normal deprecation, does not plan on
   removing the API and will not emit warnings.

   See PEP 387: Soft Deprecation.

método especial
   Un método que es llamado implícitamente por Python cuando ejecuta
   ciertas operaciones en un tipo, como la adición.  Estos métodos
   tienen nombres que comienzan y terminan con doble barra baja.  Los
   métodos especiales están documentados en Nombres especiales de
   método.

standard library
   The collection of *packages*, *modules* and *extension modules*
   distributed as a part of the official Python interpreter package.
   The exact membership of the collection may vary based on platform,
   available system libraries, or other criteria.  Documentation can
   be found at La biblioteca estándar de Python.

   See also "sys.stdlib_module_names" for a list of all possible
   standard library module names.

sentencia
   Una sentencia es parte de un conjunto (un "bloque" de código).  Una
   sentencia tanto es una *expression*  como alguna de las varias
   sintaxis usando una palabra clave, como "if", "while" o "for".

static type checker
   An external tool that reads Python code and analyzes it, looking
   for issues such as incorrect types. See also *type hints* and the
   "typing" module.

stdlib
   An abbreviation of *standard library*.

steal
   In Python's C API, "*stealing*" an argument means that ownership of
   the argument is transferred to the called function. The caller must
   not use that reference after the call. Generally, functions that
   "steal" an argument do so even if they fail.

   See Detalles del conteo de referencia for a full explanation.

referencia fuerte
   En la API de C de Python, una referencia fuerte es una referencia a
   un objeto que es propiedad del código que mantiene la referencia.
   La referencia fuerte se toma llamando a "Py_INCREF()" cuando se
   crea la referencia y se libera con "Py_DECREF()" cuando se elimina
   la referencia.

   La función "Py_NewRef()" se puede utilizar para crear una
   referencia fuerte a un objeto. Por lo general, se debe llamar a la
   función "Py_DECREF()" en la referencia fuerte antes de salir del
   alcance de la referencia fuerte, para evitar filtrar una
   referencia.

   Consulte también *borrowed reference*.

subscript
   The expression in square brackets of a subscription expression, for
   example, the "3" in "items[3]". Usually used to select an element
   of a container. Also called a *key* when subscripting a *mapping*,
   or an *index* when subscripting a *sequence*.

synchronization primitive
   A basic building block for coordinating (synchronizing) the
   execution of multiple threads to ensure *thread-safe* access to
   shared resources. Python's "threading" module provides several
   synchronization primitives including "Lock", "RLock", "Semaphore",
   "Condition", "Event", and "Barrier".  Additionally, the "queue"
   module provides multi-producer, multi-consumer queues that are
   especially useful in multithreaded programs. These primitives help
   prevent *race conditions* and coordinate thread execution.  See
   also *lock*.

t-string
t-strings
   String literals prefixed with "t" or "T" are commonly called
   "t-strings" which is short for template string literals.

codificación de texto
   Una cadena de caracteres en Python es una secuencia de puntos de
   código Unicode (en el rango "U+0000"--"U+10FFFF"). Para almacenar o
   transferir una cadena de caracteres, es necesario serializarla como
   una secuencia de bytes.

   La serialización de una cadena de caracteres en una secuencia de
   bytes se conoce como "codificación", y la recreación de la cadena
   de caracteres a partir de la secuencia de bytes se conoce como
   "decodificación".

   Existe una gran variedad de serializaciones de texto codecs, que se
   denominan colectivamente "codificaciones de texto".

archivo de texto
   Un *file object* capaz de leer y escribir objetos "str".
   Frecuentemente, un archivo de texto también accede a un flujo de
   datos binario y maneja automáticamente el *text encoding*. Ejemplos
   de archivos de texto que son abiertos en modo texto ("'r'" o
   "'w'"), "sys.stdin", "sys.stdout", y las instancias de
   "io.StringIO".

   Vea también *binary file* por objeto de archivos capaces de leer y
   escribir *objeto tipo binario*.

thread state
   The information used by the *CPython* runtime to run in an OS
   thread. For example, this includes the current exception, if any,
   and the state of the bytecode interpreter.

   Each thread state is bound to a single OS thread, but threads may
   have many thread states available.  At most, one of them may be
   *attached* at once.

   An *attached thread state* is required to call most of Python's C
   API, unless a function explicitly documents otherwise. The bytecode
   interpreter only runs under an attached thread state.

   Each thread state belongs to a single interpreter, but each
   interpreter may have many thread states, including multiple for the
   same OS thread. Thread states from multiple interpreters may be
   bound to the same thread, but only one can be *attached* in that
   thread at any given moment.

   See Thread State and the Global Interpreter Lock for more
   information.

thread-safe
   A module, function, or class that behaves correctly when used by
   multiple threads concurrently.  Thread-safe code uses appropriate
   *synchronization primitives* like *locks* to protect shared mutable
   state, or is designed to avoid shared mutable state entirely.  In
   the *free-threaded* build, built-in types like "dict", "list", and
   "set" use internal locking to make many operations thread-safe,
   although thread safety is not necessarily guaranteed.  Code that is
   not thread-safe may experience *race conditions* and *data races*
   when used in multi-threaded programs.

token
   A small unit of source code, generated by the lexical analyzer
   (also called the *tokenizer*). Names, numbers, strings, operators,
   newlines and similar are represented by tokens.

   The "tokenize" module exposes Python's lexical analyzer. The
   "token" module contains information on the various types of tokens.

cadena con triple comilla
   Una cadena que está enmarcada por tres instancias de comillas (") o
   apostrofes (').  Aunque no brindan ninguna funcionalidad que no
   está disponible usando cadenas con comillas simple, son útiles por
   varias razones.  Permiten incluir comillas simples o dobles sin
   escapar dentro de las cadenas y pueden abarcar múltiples líneas sin
   el uso de caracteres de continuación, haciéndolas particularmente
   útiles para escribir docstrings.

tipo
   The type of a Python object determines what kind of object it is;
   every object has a type.  An object's type is accessible as its
   "__class__" attribute or can be retrieved with "type(obj)".

alias de tipos
   Un sinónimo para un tipo, creado al asignar un tipo a un
   identificador.

   Los alias de tipos son útiles para simplificar los *indicadores de
   tipo*. Por ejemplo:

      def remove_gray_shades(
              colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
          pass

   podría ser más legible así:

      Color = tuple[int, int, int]

      def remove_gray_shades(colors: list[Color]) -> list[Color]:
          pass

   Vea "typing" y **PEP 484**, que describen esta funcionalidad.

indicador de tipo
   Una  *annotation* que especifica el tipo esperado para una
   variable, un atributo de clase, un parámetro para una función o un
   valor de retorno.

   Type hints are optional and are not enforced by Python but they are
   useful to *static type checkers*. They can also aid IDEs with code
   completion and refactoring.

   Los indicadores de tipo de las variables globales, atributos de
   clase, y funciones, no de variables locales, pueden ser accedidos
   usando "typing.get_type_hints()".

   Vea "typing" y **PEP 484**, que describen esta funcionalidad.

saltos de líneas universales
   Una manera de interpretar flujos de texto en la cual son
   reconocidos como finales de línea todas siguientes formas: la
   convención de Unix para fin de línea "'\n'", la convención de
   Windows "'\r\n'", y la vieja convención de Macintosh "'\r'".  Vea
   **PEP 278** y **PEP 3116**, además de "bytes.splitlines()" para
   usos adicionales.

anotación de variable
   Una *annotation* de una variable o un atributo de clase.

   Cuando se anota una variable o un atributo de clase, la asignación
   es opcional:

      class C:
          field: 'annotation'

   Las anotaciones de variables son frecuentemente usadas para *type
   hints*: por ejemplo, se espera que esta variable tenga valores de
   clase "int":

      count: int = 0

   La sintaxis de la anotación de variables está explicada en la
   sección Declaraciones de asignación anotadas.

   Consulte *function annotation*, **PEP 484** y **PEP 526**, que
   describen esta funcionalidad. Consulte también Prácticas
   recomendadas para las anotaciones para conocer las mejores
   prácticas sobre cómo trabajar con anotaciones.

entorno virtual
   Un entorno cooperativamente aislado de ejecución que permite a los
   usuarios de Python y a las aplicaciones instalar y actualizar
   paquetes de distribución de Python sin interferir con el
   comportamiento de otras aplicaciones de Python en el mismo sistema.

   Vea también "venv".

máquina virtual
   Una computadora definida enteramente por software.  La máquina
   virtual de Python ejecuta el *bytecode* generado por el compilador
   de *bytecode*.

walrus operator
   A light-hearted way to refer to the assignment expression operator
   ":=" because it looks a bit like a walrus if you turn your head.

Zen de Python
   Un listado de los principios de diseño y la filosofía de Python que
   son útiles para entender y usar el lenguaje.  El listado puede
   encontrarse ingresando  ""import this"" en la consola interactiva.
