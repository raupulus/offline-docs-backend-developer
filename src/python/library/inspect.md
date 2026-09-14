---
title: '"inspect" --- Inspect live objects'
source_url: https://docs.python.org/es/3
source_path: library/inspect.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3000
---

# "inspect" --- Inspect live objects

**Código fuente:** Lib/inspect.py

======================================================================

The "inspect" module provides several useful functions to help get
information about live objects such as modules, classes, methods,
functions, tracebacks, frame objects, and code objects.  For example,
it can help you examine the contents of a class, retrieve the source
code of a method, extract and format the argument list for a function,
or get all the information you need to display a detailed traceback.

Hay cuatro tipos principales de servicios que ofrece este módulo:
comprobación de tipos, obtención del código fuente, inspección de
clases y funciones, y examinar la pila del intérprete.

## Tipos y miembros

The "getmembers()" function retrieves the members of an object such as
a class or module. The functions whose names begin with "is" are
mainly provided as convenient choices for the second argument to
"getmembers()". They also help you determine when you can expect to
find the following special attributes (see Import-related attributes
on module objects for module attributes):

+-------------------+---------------------+-----------------------------+
| Tipo              | Atributo            | Descripción                 |
|===================|=====================|=============================|
| clase             | __doc__             | cadena de caracteres de     |
## |                   |                     | documentación               |

|                   | __name__            | nombre con el que se        |
## |                   |                     | definió esta clase          |

## |                   | __qualname__        | nombre calificado           |

|                   | __module__          | nombre del módulo en el que |
## |                   |                     | se definió esta clase       |

|                   | __type_params__     | A tuple containing the type |
|                   |                     | parameters of a generic     |
## |                   |                     | class                       |

| método            | __doc__             | cadena de caracteres de     |
## |                   |                     | documentación               |

|                   | __name__            | nombre con el que se        |
## |                   |                     | definió este método         |

## |                   | __qualname__        | nombre calificado           |

|                   | __func__            | objeto función que contiene |
|                   |                     | la implementación del       |
## |                   |                     | método                      |

|                   | __self__            | instancia a la que este     |
|                   |                     | método está ligado, o       |
## |                   |                     | "None"                      |

|                   | __module__          | nombre del módulo en el     |
|                   |                     | cual este método fue        |
## |                   |                     | definido                    |

| función           | __doc__             | cadena de caracteres de     |
## |                   |                     | documentación               |

|                   | __name__            | nombre con el que se        |
## |                   |                     | definió esta función        |

## |                   | __qualname__        | nombre calificado           |

|                   | __code__            | objeto de código que        |
|                   |                     | contiene la función         |
## |                   |                     | compilada *bytecode*        |

|                   | __defaults__        | tupla de cualquier valor    |
|                   |                     | por defecto para los        |
|                   |                     | parámetros de posición o de |
## |                   |                     | palabras clave              |

|                   | __kwdefaults__      | mapeo de cualquier valor    |
|                   |                     | predeterminado para         |
|                   |                     | parámetros de sólo palabras |
## |                   |                     | clave                       |

|                   | __globals__         | namespace global en el que  |
## |                   |                     | se definió esta función     |

## |                   | __builtins__        | Espacio de nombres builtins |

|                   | __annotations__     | mapeo de los nombres de     |
|                   |                     | parámetros a las            |
|                   |                     | anotaciones; la tecla       |
|                   |                     | ""return"" está reservada   |
|                   |                     | para las anotaciones de     |
## |                   |                     | retorno.                    |

|                   | __type_params__     | A tuple containing the type |
|                   |                     | parameters of a generic     |
## |                   |                     | function                    |

|                   | __module__          | nombre del módulo en el     |
|                   |                     | cual esta función fue       |
## |                   |                     | definida                    |

| traceback         | tb_frame            | enmarcar el objeto a este   |
## |                   |                     | nivel                       |

|                   | tb_lasti            | índice del último intento   |
|                   |                     | de instrucción en código de |
## |                   |                     | bytes                       |

|                   | tb_lineno           | número de línea actual en   |
## |                   |                     | el código fuente de Python  |

|                   | tb_next             | el siguiente objeto de      |
|                   |                     | traceback interno (llamado  |
## |                   |                     | por este nivel)             |

| marco             | f_back              | el siguiente objeto         |
|                   |                     | exterior del marco (el que  |
## |                   |                     | llama a este marco)         |

|                   | f_builtins          | construye el namespace      |
## |                   |                     | visto por este marco        |

|                   | f_code              | objeto de código que se     |
## |                   |                     | ejecuta en este marco       |

|                   | f_globals           | el namespace global visto   |
## |                   |                     | por este marco              |

|                   | f_lasti             | índice del último intento   |
|                   |                     | de instrucción en código de |
## |                   |                     | bytes                       |

|                   | f_lineno            | número de línea actual en   |
## |                   |                     | el código fuente de Python  |

|                   | f_locals            | el namespace local visto    |
## |                   |                     | por este marco              |

|                   | f_generator         | returns the generator or    |
|                   |                     | coroutine object that owns  |
|                   |                     | this frame, or "None" if    |
|                   |                     | the frame is of a regular   |
## |                   |                     | function                    |

|                   | f_trace             | función de rastreo para     |
## |                   |                     | este marco, o "None"        |

|                   | f_trace_lines       | indicate whether a tracing  |
|                   |                     | event is triggered for each |
## |                   |                     | source source line          |

|                   | f_trace_opcodes     | indicate whether per-opcode |
## |                   |                     | events are requested        |

|                   | clear()             | used to clear all           |
|                   |                     | references to local         |
## |                   |                     | variables                   |

| code              | co_argcount         | número de argumentos (sin   |
|                   |                     | incluir los argumentos de   |
|                   |                     | palabras clave, * o **      |
## |                   |                     | args)                       |

|                   | co_code             | cadena de bytecode          |
## |                   |                     | compilados en bruto         |

|                   | co_cellvars         | tupla de nombres de         |
|                   |                     | variables de celda          |
|                   |                     | (referenciados por contener |
## |                   |                     | alcances)                   |

|                   | co_consts           | tupla de constantes         |
## |                   |                     | utilizadas en el bytecode   |

|                   | co_filename         | nombre del archivo en el    |
|                   |                     | que este objeto código fue  |
## |                   |                     | creado                      |

|                   | co_firstlineno      | número de la primera línea  |
## |                   |                     | del código fuente de Python |

|                   | co_flags            | mapa de bits de los flags   |
## |                   |                     | "CO_*", leer más aquí       |

|                   | co_lnotab           | mapeo codificado de los     |
|                   |                     | números de línea a los      |
## |                   |                     | índices de bytecode         |

|                   | co_freevars         | tupla de nombres de         |
|                   |                     | variables libres            |
|                   |                     | (referenciados a través del |
## |                   |                     | cierre de una función)      |

|                   | co_posonlyargcount  | número de argumentos solo   |
## |                   |                     | posicionales                |

|                   | co_kwonlyargcount   | número de argumentos de     |
|                   |                     | sólo palabras clave (sin    |
## |                   |                     | incluir el ** arg)          |

|                   | co_name             | nombre con el que se        |
|                   |                     | definió este objeto de      |
## |                   |                     | código                      |

|                   | co_qualname         | nombre completo con el que  |
|                   |                     | se definió este objeto de   |
## |                   |                     | código                      |

|                   | co_names            | tupla de nombres que no     |
|                   |                     | sean argumentos y funciones |
## |                   |                     | locales                     |

## |                   | co_nlocals          | número de variables locales |

|                   | co_stacksize        | se requiere espacio en la   |
## |                   |                     | pila de máquina virtual     |

|                   | co_varnames         | tupla de nombres de         |
|                   |                     | argumentos y variables      |
## |                   |                     | locales                     |

|                   | co_lines()          | returns an iterator that    |
|                   |                     | yields successive bytecode  |
## |                   |                     | ranges                      |

|                   | co_positions()      | returns an iterator of      |
|                   |                     | source code positions for   |
## |                   |                     | each bytecode instruction   |

|                   | replace()           | returns a copy of the code  |
## |                   |                     | object with new values      |

## | generador         | __name__            | nombre                      |

## |                   | __qualname__        | nombre calificado           |

## |                   | gi_frame            | marco                       |

|                   | gi_running          | ¿Está el generador en       |
## |                   |                     | ejecución?                  |

## |                   | gi_suspended        | is the generator suspended? |

## |                   | gi_code             | code                        |

|                   | gi_yieldfrom        | el objeto siendo iterado    |
## |                   |                     | por "yield from", o "None"  |

## | async generator   | __name__            | nombre                      |

## |                   | __qualname__        | nombre calificado           |

|                   | ag_await            | objeto al que se espera, o  |
## |                   |                     | "None"                      |

## |                   | ag_frame            | marco                       |

|                   | ag_running          | ¿Está el generador en       |
## |                   |                     | ejecución?                  |

## |                   | ag_suspended        | is the generator suspended? |

## |                   | ag_code             | code                        |

## | corutina          | __name__            | nombre                      |

## |                   | __qualname__        | nombre calificado           |

|                   | cr_await            | objeto al que se espera, o  |
## |                   |                     | "None"                      |

## |                   | cr_frame            | marco                       |

|                   | cr_running          | ¿Está la corutina en        |
## |                   |                     | ejecución?                  |

## |                   | cr_suspended        | is the coroutine suspended? |

## |                   | cr_code             | code                        |

|                   | cr_origin           | donde se creó la corutina,  |
|                   |                     | o "None". Ver "sys.set_cor  |
|                   |                     | outine_origin_tracking_dep  |
## |                   |                     | th()"                       |

| incorporado       | __doc__             | cadena de caracteres de     |
## |                   |                     | documentación               |

|                   | __name__            | nombre original de esta     |
## |                   |                     | función o método            |

## |                   | __qualname__        | nombre calificado           |

|                   | __self__            | instancia a la que está     |
## |                   |                     | ligada un método, o "None"  |

Distinto en la versión 3.5: Agrega atributos "__qualname__" y
"gi_yieldfrom" a los generadores.El atributo "__name__" de los
generadores se establece ahora a partir del nombre de la función, en
lugar del nombre del código, y ahora puede ser modificado.

Distinto en la versión 3.7: Agrega el atributo "cr_origin" a las
corutinas.

Distinto en la versión 3.10: Agrega el atributo "__builtins__" a
funciones.

Distinto en la versión 3.11: Add "gi_suspended" attribute to
generators.

Distinto en la versión 3.11: Add "cr_suspended" attribute to
coroutines.

Distinto en la versión 3.12: Add "ag_suspended" attribute to async
generators.

Distinto en la versión 3.14: Add "f_generator" attribute to frames.

inspect.getmembers(object[, predicate])

   Retorna todos los miembros de un objeto en una lista de pares
   "(name, value)" ordenados por nombre. Si se proporciona el
   argumento *predicate* opcional, que se llamará con el objeto
   "value" de cada miembro, solo se incluyen los miembros para los que
   el predicado retorna un valor verdadero.

   Nota:

     "getmembers()" will only return class attributes defined in the
     metaclass when the argument is a class and those attributes have
     been listed in the metaclass' custom "__dir__()".

inspect.getmembers_static(object[, predicate])

   Retorna todos los miembros de un objeto en una lista de pares
   "(name, value)" ordenados por nombre sin activar la búsqueda
   dinámica a través del protocolo descriptor, __getattr__ o
   __getattribute__. Opcionalmente, solo retorna miembros que
   satisfagan un predicado determinado.

   Nota:

     Es posible que "getmembers_static()" no pueda recuperar todos los
     miembros que getmembers puede obtener (como atributos creados
     dinámicamente) y puede encontrar miembros que getmembers no puede
     (como descriptores que generan AttributeError). También puede
     retornar objetos descriptores en lugar de miembros de instancia
     en algunos casos.

   Added in version 3.11.

inspect.getmodulename(path)

   Retorna el nombre del módulo nombrado por el *ruta* de archivo, sin
   incluir los nombres de los paquetes adjuntos. La extensión del
   archivo se comprueba con todas las entradas en
   "importlib.machinery.all_suffixes()". Si coincide, el componente
   final de la ruta se retorna con la extensión eliminada. En caso
   contrario, se retorna "None".

   Ten en cuenta que esta función *sólo* retorna un nombre
   significativo para los módulos reales de Python - las rutas que
   potencialmente se refieren a los paquetes de Python seguirán
   retornando "None".

   Distinto en la versión 3.3: La función se basa directamente en
   "importlib".

inspect.ismodule(object)

   Retorna "True" si el objeto es un módulo.

inspect.isclass(object)

   Retorna "True" si el objeto es una clase, ya sea incorporada o
   creada en código Python.

   This function returns "False" for generic aliases of classes, such
   as "list[int]".

inspect.ismethod(object)

   Retorna "True" si el objeto es un método ligado escrito en Python.

   Nota:

     For example, given this class:

        >>> class Greeter:
        ...     def say_hello(self):
        ...         print('hello!')

     A bound method (also known as an *instance method*) is created
     when accessing "say_hello" (a *function* defined in the "Greeter"
     namespace) through an instance of the "Greeter" class:

        >>> instance = Greeter()

        >>> instance.say_hello
        <bound method Greeter.say_hello of <__main__.Greeter object ...>>
        >>> ismethod(instance.say_hello)
        True
        >>> isfunction(instance.say_hello)
        False

     Accessing "say_hello" through the "Greeter" class will return the
     function itself. For this function, "ismethod()" will return
     "False", but "isfunction()" will return "True":

        >>> Greeter.say_hello
        <function Greeter.say_hello at 0x7f7503854a90>
        >>> ismethod(Greeter.say_hello)
        False
        >>> isfunction(Greeter.say_hello)
        True

     See Métodos for details.

inspect.isfunction(object)

   Retorna "True" si el objeto es una función de Python, que incluye
   funciones creadas por una expresión *lambda*.

   See the note for "ismethod()" for an example.

inspect.ispackage(object)

   Return "True" if the object is a *package*.

   Added in version 3.14.

inspect.isgeneratorfunction(object)

   Retorna "True" si el objeto es una función generadora de Python.

   It also returns "True" for bound methods created from Python
   generator functions (see Métodos for more information).

   Distinto en la versión 3.8: Funciones envueltas en
   "functools.partial()" ahora retornan "True" si la función envuelta
   es una función Python generadora.

   Distinto en la versión 3.13: Functions wrapped in
   "functools.partialmethod()" now return "True" if the wrapped
   function is a Python generator function.

inspect.isgenerator(object)

   Retorna "True" si el objeto es un generador.

inspect.iscoroutinefunction(object)

   Return "True" if the object is a *coroutine function* (a function
   defined with an "async def" syntax), a "functools.partial()"
   wrapping a *coroutine function*, or a sync function marked with
   "markcoroutinefunction()".

   Added in version 3.5.

   Distinto en la versión 3.8: Funciones envueltas en
   "functools.partial()" ahora retornan "True" si la función envuelta
   es un *coroutine function*.

   Distinto en la versión 3.12: Sync functions marked with
   "markcoroutinefunction()" now return "True".

   Distinto en la versión 3.13: Functions wrapped in
   "functools.partialmethod()" now return "True" if the wrapped
   function is a *coroutine function*.

inspect.markcoroutinefunction(func)

   Decorator to mark a callable as a *coroutine function* if it would
   not otherwise be detected by "iscoroutinefunction()".

   This may be of use for sync functions that return a *coroutine*, if
   the function is passed to an API that requires
   "iscoroutinefunction()".

   When possible, using an "async def" function is preferred. Also
   acceptable is calling the function and testing the return with
   "iscoroutine()".

   Added in version 3.12.

inspect.iscoroutine(object)

   Retorna verdadero si el objeto es un *coroutine* creado por una
   función "async def".

   Added in version 3.5.

inspect.isawaitable(object)

   Retorna "True" si el objeto puede ser usado en la expresión
   "await".

   Can also be used to distinguish generator-based coroutines from
   regular generators:

      import types

      def gen():
          yield
      @types.coroutine
      def gen_coro():
          yield

      assert not isawaitable(gen())
      assert isawaitable(gen_coro())

   Added in version 3.5.

inspect.isasyncgenfunction(object)

   Return "True" if the object is an *asynchronous generator*
   function, for example:

      >>> async def agen():
      ...     yield 1
      ...
      >>> inspect.isasyncgenfunction(agen)
      True

   Added in version 3.6.

   Distinto en la versión 3.8: Functions wrapped in
   "functools.partial()" now return "True" if the wrapped function is
   an *asynchronous generator* function.

   Distinto en la versión 3.13: Functions wrapped in
   "functools.partialmethod()" now return "True" if the wrapped
   function is a *asynchronous generator* function.

inspect.isasyncgen(object)

   Retorna verdadero si el objeto es un *asynchronous generator
   iterator* creado por una función *asynchronous generator*.

   Added in version 3.6.

inspect.istraceback(object)

   Retorna "True" si el objeto es un traceback.

inspect.isframe(object)

   Retorna "True" si el objeto es un marco.

inspect.iscode(object)

   Retorna "True" si el objeto es un código.

inspect.isbuiltin(object)

   Retorna "True" si el objeto es una función incorporada o un método
   ligado incorporado.

inspect.ismethodwrapper(object)

   Retorna "True" si el tipo de objeto es "MethodWrapperType".

   Estas son instancias de "MethodWrapperType", como "__str__()",
   "__eq__()" y "__repr__()".

   Added in version 3.11.

inspect.isroutine(object)

   Retorna "True" si el objeto es una función o método definido por el
   usuario o incorporado.

inspect.isabstract(object)

   Retorna "True" si el objeto es una clase base abstracta.

inspect.ismethoddescriptor(object)

   Return "True" if the object is a method descriptor, but not if
   "isclass()", "ismethod()" or "isfunction()" is true.

   This, for example, is true of "int.__add__".  An object passing
   this test has a "__get__()" method, but not a "__set__()" method or
   a "__delete__()" method.  Beyond that, the set of attributes
   varies.  A "__name__" attribute is usually sensible, and "__doc__"
   often is.

   Method descriptors that also pass any of the other tests
   ("isclass()", "ismethod()" or "isfunction()") make this function
   return "False", simply because those other tests promise more --
   you can, for example, count on having the "__func__" attribute when
   an object passes "ismethod()".

   Distinto en la versión 3.13: This function no longer incorrectly
   reports objects with "__get__()" and "__delete__()", but not
   "__set__()", as being method descriptors (such objects are data
   descriptors, not method descriptors).

inspect.isdatadescriptor(object)

   Return "True" if the object is a data descriptor, but not if
   "isclass()", "ismethod()" or "isfunction()" is true.

   Data descriptors always have a "__set__()" method and/or a
   "__delete__()" method.  Optionally, they may also have a
   "__get__()" method.

   Examples of data descriptors are "properties", getsets and member
   descriptors.  Note that for the latter two (defined only in C
   extension modules), more specific tests are available:
   "isgetsetdescriptor()" and "ismemberdescriptor()", respectively.

   While data descriptors may also have "__name__" and "__doc__"
   attributes (as properties, getsets and member descriptors do), this
   is not necessarily the case in general.

   Distinto en la versión 3.8: This function now reports objects with
   only a "__set__()" method as being data descriptors (the presence
   of "__get__()" is no longer required for that).  Moreover, objects
   with "__delete__()", but not "__set__()", are now properly
   recognized as data descriptors as well, which was not the case
   previously.

inspect.isgetsetdescriptor(object)

   Retorna "True" si el objeto es un descriptor de conjunto.

   conjuntos son atributos definidos en módulos de extensión a través
   de estructuras "PyGetSetDef".  Para implementaciones de Python sin
   tales tipos, este método siempre retornará "False".

inspect.ismemberdescriptor(object)

   Retorna "True" si el objeto es un descriptor de miembro.

   Los descriptores de miembros son atributos definidos en los módulos
   de extensión a través de las estructuras "PyMemberDef".  Para
   implementaciones de Python sin tales tipos, este método siempre
   retornará "False".

## Recuperar el código fuente

inspect.getdoc(object)

   Obtiene la cadena de documentación de un objeto, limpiada con
   "cleandoc()". Si no se proporciona la cadena de documentación para
   un objeto y el objeto es una clase, un método, una propiedad o un
   descriptor, recupera la cadena de documentación de la jerarquía de
   herencia. Retorna "None" si la cadena de documentación no es válida
   o falta.

   Distinto en la versión 3.5: Las cadenas de documentación son ahora
   heredadas, si no anuladas.

inspect.getcomments(object)

   Retorna en una sola cadena las líneas de comentarios que preceden
   inmediatamente al código fuente del objeto (para una clase, función
   o método), o en la parte superior del archivo fuente de Python (si
   el objeto es un módulo).  Si el código fuente del objeto no está
   disponible, retorna "None".  Esto podría suceder si el objeto ha
   sido definido en C o en el shell interactivo.

inspect.getfile(object)

   Retorna el nombre del archivo (de texto o binario) en el que se
   definió un objeto. Esto fallará con un "TypeError" si el objeto es
   un módulo, clase o función incorporada.

inspect.getmodule(object)

   Intenta adivinar en qué módulo se definió un objeto. Retorna "None"
   si no se puede determinar el módulo.

inspect.getsourcefile(object)

   Retorna el nombre del archivo fuente de Python en el que se definió
   un objeto o "None" si no se puede identificar ninguna forma de
   obtener la fuente. Esto fallará con un "TypeError" si el objeto es
   un módulo, una clase o una función incorporados.

inspect.getsourcelines(object)

   Return a list of source lines and starting line number for an
   object. The argument may be a module, class, method, function,
   traceback, frame, or code object.  The source code is returned as a
   list of the lines corresponding to the object and the line number
   indicates where in the original source file the first line of code
   was found.  An "OSError" is raised if the source code cannot be
   retrieved. A "TypeError" is raised if the object is a built-in
   module, class, or function.

   Distinto en la versión 3.3: "OSError" se lanza en lugar de
   "IOError", ahora un alias del primero.

inspect.getsource(object)

   Return the text of the source code for an object. The argument may
   be a module, class, method, function, traceback, frame, or code
   object.  The source code is returned as a single string.  An
   "OSError" is raised if the source code cannot be retrieved. A
   "TypeError" is raised if the object is a built-in module, class, or
   function.

   Distinto en la versión 3.3: "OSError" se lanza en lugar de
   "IOError", ahora un alias del primero.

inspect.cleandoc(doc)

   Limpiar la indentación de los docstrings que están indentados para
   alinearse con los bloques de código.

   Todos los espacios blancos principales se eliminan de la primera
   línea.  Cualquier espacio blanco principal que pueda ser
   uniformemente removido de la segunda línea en adelante es removido.
   Las líneas vacías al principio y al final se eliminan
   posteriormente.  Además, todas las pestañas se expanden a los
   espacios.

## Introspección de los invocables con el objeto Signature

Added in version 3.3.

The "Signature" object represents the call signature of a callable
object and its return annotation. To retrieve a "Signature" object,
use the "signature()" function.

inspect.signature(callable, *, follow_wrapped=True, globals=None, locals=None, eval_str=False, annotation_format=Format.VALUE)

   Return a "Signature" object for the given *callable*:

      >>> from inspect import signature
      >>> def foo(a, *, b:int, **kwargs):
      ...     pass

      >>> sig = signature(foo)

      >>> str(sig)
      '(a, *, b: int, **kwargs)'

      >>> str(sig.parameters['b'])
      'b: int'

      >>> sig.parameters['b'].annotation
      <class 'int'>

   Acepta un amplio rango de invocables de Python, desde funciones y
   clases simples hasta objetos "functools.partial()".

   If some of the annotations are strings (e.g., because "from
   __future__ import annotations" was used), "signature()" will
   attempt to automatically un-stringize the annotations using
   "annotationlib.get_annotations()".  The *globals*, *locals*, and
   *eval_str* parameters are passed into
   "annotationlib.get_annotations()" when resolving the annotations;
   see the documentation for "annotationlib.get_annotations()" for
   instructions on how to use these parameters. A member of the
   "annotationlib.Format" enum can be passed to the
   *annotation_format* parameter to control the format of the returned
   annotations. For example, use
   "annotation_format=annotationlib.Format.STRING" to return
   annotations in string format.

   Raises "ValueError" if no signature can be provided, and
   "TypeError" if that type of object is not supported.  Also, if the
   annotations are stringized, and *eval_str* is not false, the
   "eval()" call(s) to un-stringize the annotations in
   "annotationlib.get_annotations()" could potentially raise any kind
   of exception.

   A slash (/) in the signature of a function denotes that the
   parameters prior to it are positional-only. For more info, see the
   FAQ entry on positional-only parameters.

   Distinto en la versión 3.5: The *follow_wrapped* parameter was
   added. Pass "False" to get a signature of *callable* specifically
   ("callable.__wrapped__" will not be used to unwrap decorated
   callables.)

   Distinto en la versión 3.10: The *globals*, *locals*, and
   *eval_str* parameters were added.

   Distinto en la versión 3.14: The *annotation_format* parameter was
   added.

   Nota:

     Algunos invocables pueden no ser introspeccionables en ciertas
     implementaciones de Python.  Por ejemplo, en CPython, algunas
     funciones incorporadas definidas en C no proporcionan metadatos
     sobre sus argumentos.

   **Detalles de implementación de CPython:** If the passed object has
   a "__signature__" attribute, we may use it to create the signature.
   The exact semantics are an implementation detail and are subject to
   unannounced changes. Consult the source code for current semantics.

class inspect.Signature(parameters=None, *, return_annotation=Signature.empty)

   A "Signature" object represents the call signature of a function
   and its return annotation.  For each parameter accepted by the
   function it stores a "Parameter" object in its "parameters"
   collection.

   El argumento opcional *parámetros* es una secuencia de objetos
   "Parameter", que se valida para comprobar que no hay parámetros con
   nombres duplicados, y que los parámetros están en el orden
   correcto, es decir, primero sólo de posición, luego de posición o
   palabra clave, y que los parámetros con valores por defecto siguen
   a los parámetros sin valores por defecto.

   The optional *return_annotation* argument can be an arbitrary
   Python object. It represents the "return" annotation of the
   callable.

   "Signature" objects are *immutable*.  Use "Signature.replace()" or
   "copy.replace()" to make a modified copy.

   Distinto en la versión 3.5: "Signature" objects are now picklable
   and *hashable*.

   empty

      Un marcador especial de clase para especificar la ausencia de
      una anotación de retorno.

   parameters

      Un mapeo ordenado de los nombres de los parámetros a los
      correspondientes objetos "Parameter".  Los parámetros aparecen
      en estricto orden de definición, incluyendo parámetros de sólo
      palabras clave.

      Distinto en la versión 3.7: Python sólo garantizó explícitamente
      que conservaba el orden de declaración de los parámetros de sólo
      palabras clave a partir de la versión 3.7, aunque en la práctica
      este orden siempre se había conservado en Python 3.

   return_annotation

      La anotación de "retorno" para el invocable.  Si el invocable no
      tiene ninguna anotación de "return", este atributo se establece
      en "Signature.empty".

   bind(*args, **kwargs)

      Crear un mapeo de argumentos posicionales y de palabras clave a
      los parámetros. Retorna "BoundArguments" si "*args" y "**kwargs"
      coinciden con el signature, o lanza un "TypeError".

   bind_partial(*args, **kwargs)

      Funciona de la misma manera que "Signature.bind()", pero permite
      la omisión de algunos argumentos requeridos (imita el
      comportamiento de "functools.partial()".) Retorna
      "BoundArguments", o lanza un "TypeError" si los argumentos
      pasados no coinciden con la firma.

   replace(*[, parameters][, return_annotation])

      Create a new "Signature" instance based on the instance
      "replace()" was invoked on. It is possible to pass different
      *parameters* and/or *return_annotation* to override the
      corresponding properties of the base signature.  To remove
      "return_annotation" from the copied "Signature", pass in
      "Signature.empty".

         >>> def test(a, b):
         ...     pass
         ...
         >>> sig = signature(test)
         >>> new_sig = sig.replace(return_annotation="new return anno")
         >>> str(new_sig)
         "(a, b) -> 'new return anno'"

      "Signature" objects are also supported by the generic function
      "copy.replace()".

   format(*, max_width=None, quote_annotation_strings=True)

      Create a string representation of the "Signature" object.

      If *max_width* is passed, the method will attempt to fit the
      signature into lines of at most *max_width* characters. If the
      signature is longer than *max_width*, all parameters will be on
      separate lines.

      If *quote_annotation_strings* is False, *annotations* in the
      signature are displayed without opening and closing quotation
      marks if they are strings. This is useful if the signature was
      created with the "STRING" format or if "from __future__ import
      annotations" was used.

      Added in version 3.13.

      Distinto en la versión 3.14: The *unquote_annotations* parameter
      was added.

   classmethod from_callable(obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)

      Return a "Signature" (or its subclass) object for a given
      callable *obj*.

      This method simplifies subclassing of "Signature":

         class MySignature(Signature):
             pass
         sig = MySignature.from_callable(sum)
         assert isinstance(sig, MySignature)

      Its behavior is otherwise identical to that of "signature()".

      Added in version 3.5.

      Distinto en la versión 3.10: The *globals*, *locals*, and
      *eval_str* parameters were added.

class inspect.Parameter(name, kind, *, default=Parameter.empty, annotation=Parameter.empty)

   "Parameter" objects are *immutable*. Instead of modifying a
   "Parameter" object, you can use "Parameter.replace()" or
   "copy.replace()" to create a modified copy.

   Distinto en la versión 3.5: Parameter objects are now picklable and
   *hashable*.

   empty

      Un marcador especial de clase para especificar la ausencia de
      valores predeterminados y anotaciones.

   name

      El nombre del parámetro como una cadena.  El nombre debe ser un
      identificador Python válido.

      CPython genera nombres de parámetros implícitos de la forma ".0"
      en los objetos de código utilizados para implementar expresiones
      de comprensiones y generadores.

      Distinto en la versión 3.6: These parameter names are now
      exposed by this module as names like "implicit0".

   default

      El valor por defecto del parámetro.  Si el parámetro no tiene un
      valor por defecto, este atributo se establece en
      "Parameter.empty".

   annotation

      La anotación para el parámetro.  Si el parámetro no tiene
      ninguna anotación, este atributo se establece como
      "Parameter.empty".

   kind

      Describes how argument values are bound to the parameter.  The
      possible values are accessible via "Parameter" (like
      "Parameter.KEYWORD_ONLY"), and support comparison and ordering,
      in the following order:

      +--------------------------+------------------------------------------------+
      | Nombre                   | Significado                                    |
      |==========================|================================================|
      | *POSITIONAL_ONLY*        | El valor debe proporcionarse como un argumento |
      |                          | posicional. Los parámetros solo posicionales   |
      |                          | son aquellos que aparecen antes de una entrada |
      |                          | "/" (si está presente) en una definición de    |
      |                          | función de Python. aceptan sólo uno o dos      |
      |                          | parámetros) los aceptan.                       |
      +--------------------------+------------------------------------------------+
      | *POSITIONAL_OR_KEYWORD*  | El valor puede ser suministrado como una       |
      |                          | palabra clave o como un argumento posicional   |
      |                          | (este es el comportamiento estándar de unión   |
      |                          | para las funciones implementadas en Python)    |
      +--------------------------+------------------------------------------------+
      | *VAR_POSITIONAL*         | Una tupla de argumentos posicionales que no    |
      |                          | están ligados a ningún otro parámetro. Esto    |
      |                          | corresponde a un parámetro "*args" en una      |
      |                          | definición de función Python.                  |
      +--------------------------+------------------------------------------------+
      | *KEYWORD_ONLY*           | El valor debe ser suministrado como argumento  |
      |                          | de la palabra clave. Los parámetros de sólo    |
      |                          | palabras clave son los que aparecen después de |
      |                          | una entrada "*" o "*args" en una definición de |
      |                          | función Python.                                |
      +--------------------------+------------------------------------------------+
      | *VAR_KEYWORD*            | Un dictado de argumentos de palabras clave que |
      |                          | no están ligadas a ningún otro parámetro. Esto |
      |                          | corresponde a un parámetro "**kwargs" en una   |
      |                          | definición de función Python.                  |
      +--------------------------+------------------------------------------------+

      Example: print all keyword-only arguments without default
      values:

         >>> def foo(a, b, *, c, d=10):
         ...     pass

         >>> sig = signature(foo)
         >>> for param in sig.parameters.values():
         ...     if (param.kind == param.KEYWORD_ONLY and
         ...                        param.default is param.empty):
         ...         print('Parameter:', param)
         Parameter: c

   kind.description

      Describes an enum value of "Parameter.kind".

      Added in version 3.8.

      Example: print all descriptions of arguments:

         >>> def foo(a, b, *, c, d=10):
         ...     pass

         >>> sig = signature(foo)
         >>> for param in sig.parameters.values():
         ...     print(param.kind.description)
         positional or keyword
         positional or keyword
         keyword-only
         keyword-only

   replace(*[, name][, kind][, default][, annotation])

      Create a new "Parameter" instance based on the instance replaced
      was invoked on.  To override a "Parameter" attribute, pass the
      corresponding argument.  To remove a default value or/and an
      annotation from a "Parameter", pass "Parameter.empty".

         >>> from inspect import Parameter
         >>> param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)
         >>> str(param)
         'foo=42'

         >>> str(param.replace()) # Will create a shallow copy of 'param'
         'foo=42'

         >>> str(param.replace(default=Parameter.empty, annotation='spam'))
         "foo: 'spam'"

      "Parameter" objects are also supported by the generic function
      "copy.replace()".

   Distinto en la versión 3.4: In Python 3.3 "Parameter" objects were
   allowed to have "name" set to "None" if their "kind" was set to
   "POSITIONAL_ONLY". This is no longer permitted.

class inspect.BoundArguments

   Resultado de una llamada "Signature.bind()" o
   "Signature.bind_partial()". Mantiene el mapeo de los argumentos a
   los parámetros de la función.

   arguments

      Un mapeo mutable de los nombres de los parámetros a los valores
      de los argumentos. Contiene solo argumentos vinculados
      explícitamente. Los cambios en "arguments" se reflejarán en
      "args" y "kwargs".

      Debe ser usado en conjunto con "Signature.parameters" para
      cualquier propósito de procesamiento de argumentos.

      Nota:

        Los argumentos para los cuales "Signature.bind()" o
        "Signature.bind_partial()" se basaban en un valor por defecto
        se saltan. Sin embargo, si es necesario, use
        "BoundArguments.apply_defaults()" para añadirlos.

      Distinto en la versión 3.9: "arguments" ahora es de tipo "dict".
      Anteriormente, era de tipo "collections.OrderedDict".

   args

      Una tupla de valores de argumentos posicionales.  Calculados
      dinámicamente a partir del atributo "arguments".

   kwargs

      A dict of keyword arguments values.  Dynamically computed from
      the "arguments" attribute.  Arguments that can be passed
      positionally are included in "args" instead.

   signature

      Una referencia al objeto padre "Signature".

   apply_defaults()

      Establece valores por defecto para los argumentos que faltan.

      Para los argumentos de posición variable ("*args") el valor por
      defecto es una tupla vacía.

      Para los argumentos de palabras clave variables ("**kwargs") el
      valor por defecto es un diccionario vacío.

         >>> def foo(a, b='ham', *args): pass
         >>> ba = inspect.signature(foo).bind('spam')
         >>> ba.apply_defaults()
         >>> ba.arguments
         {'a': 'spam', 'b': 'ham', 'args': ()}

      Added in version 3.5.

   The "args" and "kwargs" properties can be used to invoke functions:

      def test(a, *, b):
          ...

      sig = signature(test)
      ba = sig.bind(10, b=20)
      test(*ba.args, **ba.kwargs)

Ver también:

  **PEP 362** - Función Objeto Signature.
     La especificación detallada, los detalles de implementación y los
     ejemplos.

## Clases y funciones

inspect.getclasstree(classes, unique=False)

   Organizar la lista de clases dada en una jerarquía de listas
   anidadas. Cuando aparece una lista anidada, contiene clases
   derivadas de la clase cuya entrada precede inmediatamente a la
   lista.  Cada entrada es una tupla de 2 valores que contienen una
   clase y una tupla de sus clases base.  Si el argumento *unique* es
   cierto, aparece exactamente una entrada en la estructura retornada
   para cada clase de la lista dada.  De lo contrario, las clases que
   utilizan la herencia múltiple y sus descendientes aparecerán varias
   veces.

inspect.getfullargspec(func)

   Obtener los nombres y valores por defecto de los parámetros de una
   función de Python.  Se retorna un *named tuple*:

   "FullArgSpec(args, varargs, varkw, defaults, kwonlyargs,
   kwonlydefaults, annotations)"

   *args* es una lista de los nombres de los parámetros posicionales.
   *varargs* es el nombre del parámetro "*" o "None" si no se aceptan
   argumentos posicionales arbitrarios. *varkw* es el nombre del
   parámetro "**" o "None" si no se aceptan argumentos de palabras
   clave arbitrarias. *defaults* es una *n*-tupla de valores de
   argumentos por defecto que corresponden a los últimos parámetros de
   posición *n*, o "None" si no hay tales valores por defecto
   definidos. *kwonlyargs* es una lista de nombres de parámetros de
   sólo palabras clave en orden de declaración. *kwonlydefaults* es un
   diccionario que asigna los nombres de los parámetros de
   *kwonlyargs* a los valores por defecto utilizados si no se
   suministra ningún argumento. *annotations* es un diccionario que
   asigna los nombres de los parámetros a las anotaciones. La tecla
   especial ""return"" se utiliza para informar de la anotación del
   valor de retorno de la función (si existe).

   Observe que "signature()" y Objeto Signature proporcionan la API
   recomendada para la introspección invocable, y soportan
   comportamientos adicionales (como los argumentos de sólo posición)
   que a veces se encuentran en las API de los módulos de extensión.
   Esta función se conserva principalmente para su uso en el código
   que necesita mantener la compatibilidad con la API de módulos de
   "inspect" de Python 2.

   Distinto en la versión 3.4: Esta función se basa ahora en
   "signature()", pero sigue ignorando los atributos "__wrapped__" e
   incluye el primer parámetro ya ligado en la salida del signature
   para los métodos ligados.

   Distinto en la versión 3.6: This method was previously documented
   as deprecated in favour of "signature()" in Python 3.5, but that
   decision has been reversed in order to restore a clearly supported
   standard interface for single-source Python 2/3 code migrating away
   from the legacy "getargspec()" API.

   Distinto en la versión 3.7: Python sólo garantizó explícitamente
   que conservaba el orden de declaración de los parámetros de sólo
   palabras clave a partir de la versión 3.7, aunque en la práctica
   este orden siempre se había conservado en Python 3.

inspect.getargvalues(frame)

   Obtener información sobre los argumentos pasados en un marco
   particular.  Un *named tuple* "ArgInfo(args, varargs, keywords,
   locals)" es retornado. *args* es una lista de los nombres de los
   argumentos.  *varargs* y *keywords* son los nombres de los
   argumentos "*" y "**" o "None".  *locals* es el diccionario local
   del marco dado.

   Nota:

     Esta función fue inadvertidamente marcada como obsoleta en Python
     3.5.

inspect.formatargvalues(args[, varargs, varkw, locals, formatarg, formatvarargs, formatvarkw, formatvalue])

   Formatea una bonita especificación de argumentos de los cuatro
   valores retornados por "getargvalues()".  Los argumentos de
   formato* son las correspondientes funciones de formato opcionales
   que se llaman para convertir nombres y valores en cadenas.

   Nota:

     Esta función fue inadvertidamente marcada como obsoleta en Python
     3.5.

inspect.getmro(cls)

   Retorna una tupla de clases base de cls, incluyendo cls, en orden
   de resolución de métodos.  Ninguna clase aparece más de una vez en
   esta tupla. Obsérvese que el orden de resolución de los métodos
   depende del tipo de cls.  A menos que se utilice un meta tipo muy
   peculiar definido por el usuario, cls será el primer elemento de la
   tupla.

inspect.getcallargs(func, /, *args, **kwds)

   Bind the *args* and *kwds* to the argument names of the Python
   function or method *func*, as if it was called with them. For bound
   methods, bind also the first argument (typically named "self") to
   the associated instance. A dict is returned, mapping the argument
   names (including the names of the "*" and "**" arguments, if any)
   to their values from *args* and *kwds*. In case of invoking *func*
   incorrectly, i.e. whenever "func(*args, **kwds)" would raise an
   exception because of incompatible signature, an exception of the
   same type and the same or similar message is raised. For example:

      >>> from inspect import getcallargs
      >>> def f(a, b=1, *pos, **named):
      ...     pass
      ...
      >>> getcallargs(f, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
      True
      >>> getcallargs(f, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
      True
      >>> getcallargs(f)
      Traceback (most recent call last):
      ...
      TypeError: f() missing 1 required positional argument: 'a'

   Added in version 3.2.

   Obsoleto desde la versión 3.5: Usa "Signature.bind()" y
   "Signature.bind_partial()" en su lugar.

inspect.getclosurevars(func)

   Obtener el mapeo de referencias de nombres externos en una función
   o método *func* de Python a sus valores actuales. Un *named tuple*
   "ClosureVars(nonlocals, globals, builtins, unbound)" es retornado.
   *nonlocals* asigna los nombres referidos a las variables de cierre
   léxicas, *globals* a los globals de los módulos de la función y
   *builtins* a los builtins visibles desde el cuerpo de la función.
   *unbound* es el conjunto de nombres referenciados en la función que
   no pudieron ser resueltos en absoluto dados los actuales globals y
   builtins del módulo.

   "TypeError" es lanzado si *func* no es una función o método de
   Python.

   Added in version 3.3.

inspect.unwrap(func, *, stop=None)

   Obtiene el objeto envuelto por *func*. Sigue la cadena de atributos
   "__wrapped__" retornando el último objeto de la cadena.

   *stop* es una retrollamada opcional que acepta un objeto de la
   cadena envuelta como único argumento que permite terminar el
   desenvolvimiento antes de tiempo si la retrollamada retorna un
   valor real. Si la retrollamada nunca retorna un valor verdadero, el
   último objeto de la cadena se retorna como de costumbre. Por
   ejemplo, "signature()" utiliza esto para detener el
   desenvolvimiento si algún objeto de la cadena tiene definido el
   atributo "__signature__".

   "ValueError" es lanzado si se encuentra un ciclo.

   Added in version 3.4.

inspect.get_annotations(obj, *, globals=None, locals=None, eval_str=False, format=annotationlib.Format.VALUE)

   Calcular el diccionario de anotaciones de un objeto.

   This is an alias for "annotationlib.get_annotations()"; see the
   documentation of that function for more information.

   Prudencia:

     This function may execute arbitrary code contained in
     annotations. See Security implications of introspecting
     annotations for more information.

   Added in version 3.10.

   Distinto en la versión 3.14: This function is now an alias for
   "annotationlib.get_annotations()". Calling it as
   "inspect.get_annotations" will continue to work.

## La pila del interprete

Algunas de las siguientes funciones retornan objetos "FrameInfo". Por
compatibilidad con versiones anteriores, estos objetos permiten
operaciones similares a tuplas en todos los atributos excepto
"positions". Este comportamiento se considera obsoleto y puede
eliminarse en el futuro.

class inspect.FrameInfo

   frame

      El frame object al que corresponde el registro.

   filename

      El nombre del archivo asociado con el código que está ejecutando
      el marco al que corresponde este registro.

   lineno

      El número de línea de la línea actual asociada con el código que
      está ejecutando el marco al que corresponde este registro.

   function

      El nombre de la función que está ejecutando el marco al que
      corresponde este registro.

   code_context

      Una lista de líneas de contexto del código fuente que ejecuta el
      marco al que corresponde este registro.

   index

      El índice de la línea actual que se está ejecutando en la lista
      "code_context".

   positions

      Un objeto "dis.Positions" que contiene el número de línea
      inicial, el número de línea final, el desplazamiento de columna
      inicial y el desplazamiento de columna final asociado con la
      instrucción que ejecuta el marco al que corresponde este
      registro.

   Distinto en la versión 3.5: Retorna un *named tuple* en lugar de un
   "tuple".

   Distinto en la versión 3.11: "FrameInfo" ahora es una instancia de
   clase (que es retrocompatible con el anterior *named tuple*).

class inspect.Traceback

   filename

      El nombre de archivo asociado con el código que ejecuta el marco
      al que corresponde este rastreo.

   lineno

      El número de línea de la línea actual asociada con el código que
      está ejecutando el marco al que corresponde este rastreo.

   function

      El nombre de la función que está ejecutando el marco al que
      corresponde este rastreo.

   code_context

      Una lista de líneas de contexto del código fuente que ejecuta el
      marco al que corresponde este rastreo.

   index

      El índice de la línea actual que se está ejecutando en la lista
      "code_context".

   positions

      Un objeto "dis.Positions" que contiene el número de línea
      inicial, el número de línea final, el desplazamiento de columna
      inicial y el desplazamiento de columna final asociado con la
      instrucción que ejecuta el marco al que corresponde este
      rastreo.

   Distinto en la versión 3.11: "Traceback" ahora es una instancia de
   clase (que es retrocompatible con el anterior *named tuple*).

Nota:

  Mantener referencias a los objetos marco, como se encuentra en el
  primer elemento de los registros marco que estas funciones retornan,
  puede hacer que su programa cree ciclos de referencia.  Una vez
  creado un ciclo de referencia, la vida útil de todos los objetos a
  los que se puede acceder desde los objetos que forman el ciclo puede
  ser mucho mayor, incluso si el detector de ciclos opcional de Python
  está activado.  Si es necesario crear tales ciclos, es importante
  asegurarse de que se rompen explícitamente para evitar la
  destrucción retardada de los objetos y el aumento del consumo de
  memoria que se produce.Aunque el detector de ciclos los captará, la
  destrucción de los marcos (y las variables locales) puede hacerse
  determinísticamente eliminando el ciclo en una cláusula de
  "finally".  Esto también es importante si el detector de ciclos fue
  desactivado cuando se compiló Python o usando "gc.disable()".  Por
  ejemplo:

     def handle_stackframe_without_leak():
         frame = inspect.currentframe()
         try:
             # do something with the frame
         finally:
             del frame

  Si quieres mantener el marco alrededor (por ejemplo para imprimir
  una traceback más tarde), también puedes romper los ciclos de
  referencia utilizando el método "frame.clear()".

El argumento opcional de *context*, apoyado por la mayoría de estas
funciones, especifica el número de líneas de contexto a retornar, que
se centran en la línea actual.

inspect.getframeinfo(frame, context=1)

   Obtiene información sobre un marco o un objeto de rastreo. Se
   retorna un objeto "Traceback".

   Distinto en la versión 3.11: Se retorna un objeto "Traceback" en
   lugar de una tupla con nombre.

inspect.getouterframes(frame, context=1)

   Obtiene una lista de objetos "FrameInfo" para un marco y todos los
   marcos externos. Estos marcos representan las llamadas que conducen
   a la creación de *frame*. La primera entrada en la lista retornada
   representa *frame*; la última entrada representa la llamada más
   externa en la pila de *frame*.

   Distinto en la versión 3.5: Una lista de *named tuples*
   "FrameInfo(frame, filename, lineno, function, code_context, index)"
   es retornada.

   Distinto en la versión 3.11: Se retorna una lista de objetos
   "FrameInfo".

inspect.getinnerframes(traceback, context=1)

   Obtiene una lista de objetos "FrameInfo" para el marco de un
   rastreo y todos los marcos internos. Estos marcos representan
   llamadas realizadas como consecuencia de *frame*. La primera
   entrada de la lista representa *traceback*; la última entrada
   representa dónde se generó la excepción.

   Distinto en la versión 3.5: Una lista de *named tuples*
   "FrameInfo(frame, filename, lineno, function, code_context, index)"
   es retornada.

   Distinto en la versión 3.11: Se retorna una lista de objetos
   "FrameInfo".

inspect.currentframe()

   Retorna el objeto marco para el marco de la pila del que llama.

   Esta función se basa en el soporte del marco de la pila de Python
   en el intérprete, que no está garantizado que exista en todas las
   implementaciones de Python.  Si se ejecuta en una implementación
   sin soporte de marcos de pila de Python, esta función retorna
   "None".

inspect.stack(context=1)

   Retorna una lista de objetos "FrameInfo" para la pila del que
   llama. La primera entrada en la lista retornada representa al que
   llama; la última entrada representa la llamada más externa de la
   pila.

   Distinto en la versión 3.5: Una lista de *named tuples*
   "FrameInfo(frame, filename, lineno, function, code_context, index)"
   es retornada.

   Distinto en la versión 3.11: Se retorna una lista de objetos
   "FrameInfo".

inspect.trace(context=1)

   Retorna una lista de objetos "FrameInfo" para la pila entre el
   marco actual y el marco en el que se generó una excepción que se
   está manejando actualmente. La primera entrada en la lista
   representa al que llama; la última entrada representa dónde se
   generó la excepción.

   Distinto en la versión 3.5: Una lista de *named tuples*
   "FrameInfo(frame, filename, lineno, function, code_context, index)"
   es retornada.

   Distinto en la versión 3.11: Se retorna una lista de objetos
   "FrameInfo".

## Obteniendo atributos estáticamente

Both "getattr()" and "hasattr()" can trigger code execution when
fetching or checking for the existence of attributes. Descriptors,
like properties, will be invoked and "__getattr__()" and
"__getattribute__()" may be called.

For cases where you want passive introspection, like documentation
tools, this can be inconvenient. "getattr_static()" has a similar
signature as "getattr()" but avoids executing code when it fetches
attributes.

inspect.getattr_static(obj, attr)
inspect.getattr_static(obj, attr, default)

   Retrieve attributes without triggering dynamic lookup via the
   descriptor protocol, "__getattr__()" or "__getattribute__()".

   Nota: es posible que esta función no pueda recuperar todos los
   atributos que getattr puede recuperar (como los atributos creados
   dinámicamente) y puede encontrar atributos que getattr no puede
   (como los descriptores que lanzan AttributeError). También puede
   retornar objetos descriptores en lugar de miembros de la instancia.

   Si la instancia "__dict__" es ensombrecida por otro miembro (por
   ejemplo una propiedad) entonces esta función no podrá encontrar
   miembros de la instancia.

   Added in version 3.2.

"getattr_static()" no resuelve los descriptores, por ejemplo los
descriptores de ranura o los descriptores de getset en los objetos
implementados en C. El objeto descriptor se retorna en lugar del
atributo subyacente.

Puedes manejar esto con un código como el siguiente. Tenga en cuenta
que la invocación de los descriptores de getset arbitrarios pueden
desencadenar la ejecución del código:

   # example code for resolving the builtin descriptor types
   class _foo:
       __slots__ = ['foo']

   slot_descriptor = type(_foo.foo)
   getset_descriptor = type(type(open(__file__)).name)
   wrapper_descriptor = type(str.__dict__['__add__'])
   descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)

   result = getattr_static(some_object, 'foo')
   if type(result) in descriptor_types:
       try:
           result = result.__get__()
       except AttributeError:
           # descriptors can raise AttributeError to
           # indicate there is no underlying value
           # in which case the descriptor itself will
           # have to do
           pass

## Current State of Generators, Coroutines, and Asynchronous Generators

Al implementar los programadores de corutinas y para otros usos
avanzados de los generadores, es útil determinar si un generador se
está ejecutando actualmente, si está esperando para iniciarse o
reanudarse o si ya ha terminado. "getgeneratorstate()" permite
determinar fácilmente el estado actual de un generador.

inspect.getgeneratorstate(generator)

   Obtener el estado actual de un generador-iterador.

   Los posibles estados son:

   * GEN_CREATED: Esperando para iniciar la ejecución.

   * GEN_RUNNING: Actualmente está siendo ejecutado por el intérprete.

   * GEN_SUSPENDED: Actualmente suspendido en una expresión yield.

   * GEN_CLOSED: La ejecución se ha completado.

   Added in version 3.2.

inspect.getcoroutinestate(coroutine)

   Obtener el estado actual de un objeto de corutina.  La función está
   pensada para ser usada con objetos de corutina creados por las
   funciones "async def", pero aceptará cualquier objeto de corutina
   que tenga los atributos "cr_running" y "cr_frame".

   Los posibles estados son:

   * CORO_CREATED: Esperando para iniciar la ejecución.

   * CORO_RUNNING: Actualmente está siendo ejecutado por el
     intérprete.

   * CORO_SUSPENDED: Actualmente suspendido en una expresión de
     espera.

   * CORO_CLOSED: La ejecución se ha completado.

   Added in version 3.5.

inspect.getasyncgenstate(agen)

   Get current state of an asynchronous generator object.  The
   function is intended to be used with asynchronous iterator objects
   created by "async def" functions which use the "yield" statement,
   but will accept any asynchronous generator-like object that has
   "ag_running" and "ag_frame" attributes.

   Los posibles estados son:

   * AGEN_CREATED: Waiting to start execution.

   * AGEN_RUNNING: Currently being executed by the interpreter.

   * AGEN_SUSPENDED: Currently suspended at a yield expression.

   * AGEN_CLOSED: Execution has completed.

   Added in version 3.12.

También se puede consultar el estado interno actual del generador.
Esto es mayormente útil para fines de prueba, para asegurar que el
estado interno se actualiza como se espera:

inspect.getgeneratorlocals(generator)

   Consigue el mapeo de las variables vivas locales en *generator* a
   sus valores actuales.  Se retorna un diccionario que mapea de los
   nombres de las variables a los valores. Esto es el equivalente a
   llamar "locals()" en el cuerpo del generador, y se aplican todas
   las mismas advertencias.

   Si *generator* es un *generator* sin marco asociado actualmente,
   entonces se retorna un diccionario vacío. "TypeError" es lanzado si
   *generator* no es un objeto generador de Python.

   Esta función se basa en que el generador exponga un marco de pila
   de Python para la introspección, lo cual no está garantizado en
   todas las implementaciones de Python. En tales casos, esta función
   siempre retornará un diccionario vacío.

   Added in version 3.3.

inspect.getcoroutinelocals(coroutine)

   Esta función es análoga a "getgeneratorlocals()", pero funciona
   para los objetos de corutina creados por funciones "async def".

   Added in version 3.5.

inspect.getasyncgenlocals(agen)

   This function is analogous to "getgeneratorlocals()", but works for
   asynchronous generator objects created by "async def" functions
   which use the "yield" statement.

   Added in version 3.12.

## Objetos de código Bit Flags

Python code objects have a "co_flags" attribute, which is a bitmap of
the following flags:

inspect.CO_OPTIMIZED

   El objeto del código está optimizado, usando locales rápidas (*fast
   locals*).

inspect.CO_NEWLOCALS

   If set, a new dict will be created for the frame's "f_locals" when
   the code object is executed.

inspect.CO_VARARGS

   El objeto del código tiene un parámetro posicional variable
   (similar a "*args").

inspect.CO_VARKEYWORDS

   El objeto del código tiene un parámetro de palabra clave variable
   (similar a "**kwargs").

inspect.CO_NESTED

   El flag se fija cuando el objeto del código es una función anidada.

inspect.CO_GENERATOR

   El flag se fija cuando el objeto del código es una función
   generadora, es decir, un objeto generador es retornado cuando el
   objeto del código se ejecuta.

inspect.CO_COROUTINE

   El flag se configura cuando el objeto del código es una función de
   corutina. Cuando el objeto código se ejecuta, retorna un objeto de
   corutina. Ver **PEP 492** para más detalles.

   Added in version 3.5.

inspect.CO_ITERABLE_COROUTINE

   El flag se utiliza para transformar generadores en corutinas
   basadas en generadores.  Los objetos generadores con este flag
   pueden ser usados en la expresión "await", y objetos de corutina
   "yield from". Ver **PEP 492** para más detalles.

   Added in version 3.5.

inspect.CO_ASYNC_GENERATOR

   El flag se configura cuando el objeto del código es una función
   generadora asíncrona.  Cuando el objeto código se ejecuta, retorna
   un objeto generador asíncrono.  Ver **PEP 525** para más detalles.

   Added in version 3.6.

inspect.CO_HAS_DOCSTRING

   The flag is set when there is a docstring for the code object in
   the source code. If set, it will be the first item in "co_consts".

   Added in version 3.14.

inspect.CO_METHOD

   The flag is set when the code object is a function defined in class
   scope.

   Added in version 3.14.

Nota:

  The flags are specific to CPython, and may not be defined in other
  Python implementations.  Furthermore, the flags are an
  implementation detail, and can be removed or deprecated in future
  Python releases. It's recommended to use public APIs from the
  "inspect" module for any introspection needs.

## Buffer flags

class inspect.BufferFlags

   This is an "enum.IntFlag" that represents the flags that can be
   passed to the "__buffer__()" method of objects implementing the
   buffer protocol.

   The meaning of the flags is explained at Tipos de solicitud búfer.

   SIMPLE

   WRITABLE

   FORMAT

   ND

   STRIDES

   C_CONTIGUOUS

   F_CONTIGUOUS

   ANY_CONTIGUOUS

   INDIRECT

   CONTIG

   CONTIG_RO

   STRIDED

   STRIDED_RO

   RECORDS

   RECORDS_RO

   FULL

   FULL_RO

   READ

   WRITE

   Added in version 3.12.

## Command-line interface

The "inspect" module also provides a basic introspection capability
from the command line.

Por defecto, acepta el nombre de un módulo e imprime la fuente de ese
módulo. Una clase o función dentro del módulo puede imprimirse en su
lugar añadiendo dos puntos y el nombre calificado del objeto objetivo.

--details

   Imprimir información sobre el objeto especificado en lugar del
   código fuente
