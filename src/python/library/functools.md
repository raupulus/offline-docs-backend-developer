---
title: '"functools" --- Higher-order functions and operations on callable objects'
source_url: https://docs.python.org/es/3
source_path: library/functools.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2700
---

# "functools" --- Higher-order functions and operations on callable objects

**Código fuente:** Lib/functools.py

======================================================================

The "functools" module is for higher-order functions: functions that
act on or return other functions. In general, any callable object can
be treated as a function for the purposes of this module.

The "functools" module defines the following functions:

@functools.cache(user_function)

   Caché de funciones ilimitado, ligero y simple. Aveces llamado
   "memoización".

   Returns the same as "lru_cache(maxsize=None)", creating a thin
   wrapper around a dictionary lookup for the function arguments.
   Because it never needs to evict old values, this is smaller and
   faster than "@lru_cache" with a size limit.

   Por ejemplo:

      @cache
      def factorial(n):
          return n * factorial(n-1) if n else 1

      >>> factorial(10)   # no previously cached result, makes 11 recursive calls
      3628800
      >>> factorial(5)    # no new calls, just returns the cached result
      120
      >>> factorial(12)   # two new recursive calls, factorial(10) is cached
      479001600

   The cache is threadsafe so that the wrapped function can be used in
   multiple threads.  This means that the underlying data structure
   will remain coherent during concurrent updates.

   It is possible for the wrapped function to be called more than once
   if another thread makes an additional call before the initial call
   has been completed and cached.

   Added in version 3.9.

@functools.cached_property(func)

   Transform a method of a class into a property whose value is
   computed once and then cached as a normal attribute for the life of
   the instance. Similar to "@property", with the addition of caching.
   Useful for expensive computed properties of instances that are
   otherwise effectively immutable.

   Ejemplo:

      class DataSet:

          def __init__(self, sequence_of_numbers):
              self._data = tuple(sequence_of_numbers)

          @cached_property
          def stdev(self):
              return statistics.stdev(self._data)

   The mechanics of "@cached_property" are somewhat different from
   "@property".  A regular property blocks attribute writes unless a
   setter is defined. In contrast, a *cached_property* allows writes.

   El decorador *cached_property* solo se ejecuta en búsquedas y solo
   cuando no existe un atributo con el mismo nombre. Cuando se
   ejecuta, *cached_property* escribe en el atributo con el mismo
   nombre. Las lecturas y escrituras de atributos posteriores tienen
   prioridad sobre el método *cached_property* y funciona como un
   atributo normal.

   El valor en caché se puede borrar eliminando el atributo. Esto
   permite que el método *cached_property* se ejecute nuevamente.

   The *cached_property* does not prevent a possible race condition in
   multi-threaded usage. The getter function could run more than once
   on the same instance, with the latest run setting the cached value.
   If the cached property is idempotent or otherwise not harmful to
   run more than once on an instance, this is fine. If synchronization
   is needed, implement the necessary locking inside the decorated
   getter function or around the cached property access.

   Tenga en cuenta que este decorador interfiere con el funcionamiento
   de diccionarios de intercambio de claves **PEP 412**. Esto
   significa que los diccionarios de instancias pueden ocupar más
   espacio de lo habitual.

   Además, este decorador requiere que el atributo "__dict__" en cada
   instancia sea un mapeo mutable. Esto significa que no funcionará
   con algunos tipos, como las metaclases (ya que los atributos
   "__dict__" en las instancias de tipos son proxies de solo lectura
   para el espacio de nombres de la clase) y aquellos que especifican
   "__slots__" sin incluir "__dict__" como una de las ranuras
   definidas (ya que tales clases no proporcionan un atributo
   "__dict__" en absoluto).

   If a mutable mapping is not available or if space-efficient key
   sharing is desired, an effect similar to "@cached_property" can
   also be achieved by stacking "@property" on top of "@lru_cache".
   See ¿Cómo cacheo llamadas de método? for more details on how this
   differs from "@cached_property".

   Added in version 3.8.

   Distinto en la versión 3.12: Prior to Python 3.12,
   "@cached_property" included an undocumented lock to ensure that in
   multi-threaded usage the getter function was guaranteed to run only
   once per instance. However, the lock was per-property, not per-
   instance, which could result in unacceptably high lock contention.
   In Python 3.12+ this locking is removed.

functools.cmp_to_key(func)

   Transformar una función de comparación de estilo antiguo en una
   *key function*.  Se utiliza con herramientas que aceptan funciones
   clave (como "sorted()", "min()", "max()", "heapq.nlargest()",
   "heapq.nsmallest()", "itertools.groupby()").  Esta función se
   utiliza principalmente como una herramienta de transición para los
   programas que se están convirtiendo a partir de Python 2, que
   soportaba el uso de funciones de comparación.

   Una función de comparación es cualquier invocable que acepta dos
   argumentos, los compara y devuelve un número negativo para menor
   que, cero para igualdad o un número positivo para mayor que. Una
   función clave es una función invocable que acepta un argumento y
   devuelve otro valor para usar como clave de ordenación.

   Ejemplo:

      sorted(iterable, key=cmp_to_key(locale.strcoll))  # locale-aware sort order

   Para ejemplos de clasificación y un breve tutorial de
   clasificación, ver Sorting Techniques.

   Added in version 3.2.

@functools.lru_cache(user_function)
@functools.lru_cache(maxsize=128, typed=False)

   Decorador para envolver una función con un memorizador invocable
   que guarda hasta el *maxsize* de las llamadas más recientes.  Puede
   salvar el tiempo cuando una función costosa o de E/S es llamada
   periódicamente con los mismos argumentos.

   The cache is threadsafe so that the wrapped function can be used in
   multiple threads.  This means that the underlying data structure
   will remain coherent during concurrent updates.

   It is possible for the wrapped function to be called more than once
   if another thread makes an additional call before the initial call
   has been completed and cached.

   Since a dictionary is used to cache results, the positional and
   keyword arguments to the function must be *hashable*.

   Los patrones de argumentos distintos pueden considerarse llamadas
   distintas con entradas de memoria caché separadas. Por ejemplo,
   "f(a=1, b=2)" y "f(b=2, a=1)" difieren en el orden de sus
   argumentos de palabras clave y pueden tener dos entradas de caché
   separadas.

   Si se especifica *user_function*, debe ser una llamada. Esto
   permite que el decorador *lru_cache* se aplique directamente a una
   función de usuario, dejando el *maxsize* en su valor por defecto de
   128:

      @lru_cache
      def count_vowels(sentence):
          return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

   Si *maxsize* está configurado como "None", la función LRU está
   desactivada y la caché puede crecer sin límites.

   Si *typed* se establece en verdadero, los argumentos de función de
   diferentes tipos se almacenarán en caché por separado. Si *typed*
   es falso, la implementación generalmente las considerará como
   llamadas equivalentes y solo almacenará en caché un único
   resultado. (Algunos tipos como *str* y *int* pueden almacenarse en
   caché por separado incluso cuando *typed* es falso).

   Note, type specificity applies only to the function's immediate
   arguments rather than their contents.  The scalar arguments,
   "Decimal(42)" and "Fraction(42)" are treated as distinct calls with
   distinct results. In contrast, the tuple arguments "('answer',
   Decimal(42))" and "('answer', Fraction(42))" are treated as
   equivalent.

   The wrapped function is instrumented with a "cache_parameters()"
   function that returns a new "dict" showing the values for *maxsize*
   and *typed*.  This is for information purposes only.  Mutating the
   values has no effect.

   To help measure the effectiveness of the cache and tune the
   *maxsize* parameter, the wrapped function is instrumented with a
   "cache_info()" function that returns a *named tuple* showing
   *hits*, *misses*, *maxsize* and *currsize*.

   The decorator also provides a "cache_clear()" function for clearing
   or invalidating the cache.

   La función subyacente original es accesible a través del atributo
   "__wrapped__".  Esto es útil para la introspección, para evitar el
   caché, o para volver a envolver la función con un caché diferente.

   La caché mantiene referencias de los argumentos y retorna los
   valores hasta que se caduquen de la caché o hasta que se borre la
   caché.

   Si un método se almacena en caché, el argumento de la instancia
   "self" se incluye en el caché. Ver ¿Cómo cacheo llamadas de método?

   An LRU (least recently used) cache works best when the most recent
   calls are the best predictors of upcoming calls (for example, the
   most popular articles on a news server tend to change each day).
   The cache's size limit assures that the cache does not grow without
   bound on long-running processes such as web servers.

   In general, the LRU cache should only be used when you want to
   reuse previously computed values.  Accordingly, it doesn't make
   sense to cache functions with side-effects, functions that need to
   create distinct mutable objects on each call (such as generators
   and async functions), or impure functions such as time() or
   random().

   Ejemplo de un caché de la LRU para contenido web estático:

      @lru_cache(maxsize=32)
      def get_pep(num):
          'Retrieve text of a Python Enhancement Proposal'
          resource = f'https://peps.python.org/pep-{num:04d}'
          try:
              with urllib.request.urlopen(resource) as s:
                  return s.read()
          except urllib.error.HTTPError:
              return 'Not Found'

      >>> for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
      ...     pep = get_pep(n)
      ...     print(n, len(pep))

      >>> get_pep.cache_info()
      CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)

   Ejemplo de computar eficientemente los números de Fibonacci usando
   una memoria caché para implementar una técnica de programación
   dinámica:

      @lru_cache(maxsize=None)
      def fib(n):
          if n < 2:
              return n
          return fib(n-1) + fib(n-2)

      >>> [fib(n) for n in range(16)]
      [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

      >>> fib.cache_info()
      CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

   Added in version 3.2.

   Distinto en la versión 3.3: Añadida la opción *typed* option.

   Distinto en la versión 3.8: Añadida la opción *user_function*.

   Distinto en la versión 3.9: Added the function "cache_parameters()"

@functools.total_ordering

   Dada una clase que define uno o más métodos de ordenamiento de
   comparación ricos, este decorador de clase suministra el resto.
   Esto simplifica el esfuerzo de especificar todas las posibles
   operaciones de comparación rica:

   The class must define one of "__lt__()", "__le__()", "__gt__()", or
   "__ge__()". In addition, the class should supply an "__eq__()"
   method.

   Por ejemplo:

      @total_ordering
      class Student:
          def _is_valid_operand(self, other):
              return (hasattr(other, "lastname") and
                      hasattr(other, "firstname"))
          def __eq__(self, other):
              if not self._is_valid_operand(other):
                  return NotImplemented
              return ((self.lastname.lower(), self.firstname.lower()) ==
                      (other.lastname.lower(), other.firstname.lower()))
          def __lt__(self, other):
              if not self._is_valid_operand(other):
                  return NotImplemented
              return ((self.lastname.lower(), self.firstname.lower()) <
                      (other.lastname.lower(), other.firstname.lower()))

   Nota:

     Mientras que este decorador facilita la creación de tipos bien
     comportados y totalmente ordenados, *does* a costa de una
     ejecución más lenta y de trazos de pila (*stack traces*) más
     complejos para los métodos de comparación derivados. Si la
     evaluación comparativa del rendimiento indica que se trata de un
     cuello de botella para una aplicación determinada, la aplicación
     de los seis métodos de comparación ricos en su lugar es probable
     que proporcione un fácil aumento de la velocidad.

   Nota:

     Este decorador no intenta anular métodos que han sido declarados
     en la clase *sus superclases*. Lo que significa que si una
     superclase define un operador de comparación, *total_ordering* no
     lo implementará de nuevo, incluso si el método original es
     abstracto.

   Added in version 3.2.

   Distinto en la versión 3.4: Returning "NotImplemented" from the
   underlying comparison function for unrecognised types is now
   supported.

functools.Placeholder

   A singleton object used as a sentinel to reserve a place for
   positional arguments when calling "partial()" and
   "partialmethod()".

   Added in version 3.14.

functools.partial(func, /, *args, **keywords)

   Retorna un nuevo partial object que cuando sea llamado se
   comportará como *func* llamado con los argumentos posicionales
   *args* y los argumentos de palabras clave *keywords*. Si se
   suministran más argumentos a la llamada, se añaden a *args*. Si se
   suministran más argumentos de palabras clave, se extienden y anulan
   las *keywords*. Aproximadamente equivalente a:

      def partial(func, /, *args, **keywords):
          def newfunc(*more_args, **more_keywords):
              return func(*args, *more_args, **(keywords | more_keywords))
          newfunc.func = func
          newfunc.args = args
          newfunc.keywords = keywords
          return newfunc

   The "partial()" function is used for partial function application
   which "freezes" some portion of a function's arguments and/or
   keywords resulting in a new object with a simplified signature.
   For example, "partial()" can be used to create a callable that
   behaves like the "int()" function where the *base* argument
   defaults to "2":

      >>> basetwo = partial(int, base=2)
      >>> basetwo.__doc__ = 'Convert base 2 string to an int.'
      >>> basetwo('10010')
      18

   If "Placeholder" sentinels are present in *args*, they will be
   filled first when "partial()" is called. This makes it possible to
   pre-fill any positional argument with a call to "partial()";
   without "Placeholder", only the chosen number of leading positional
   arguments can be pre-filled.

   If any "Placeholder" sentinels are present, all must be filled at
   call time:

      >>> say_to_world = partial(print, Placeholder, Placeholder, "world!")
      >>> say_to_world('Hello', 'dear')
      Hello dear world!

   Calling "say_to_world('Hello')" raises a "TypeError", because only
   one positional argument is provided, but there are two placeholders
   that must be filled in.

   If "partial()" is applied to an existing "partial()" object,
   "Placeholder" sentinels of the input object are filled in with new
   positional arguments. A placeholder can be retained by inserting a
   new "Placeholder" sentinel to the place held by a previous
   "Placeholder":

      >>> from functools import partial, Placeholder as _
      >>> remove = partial(str.replace, _, _, '')
      >>> message = 'Hello, dear dear world!'
      >>> remove(message, ' dear')
      'Hello, world!'
      >>> remove_dear = partial(remove, _, ' dear')
      >>> remove_dear(message)
      'Hello, world!'
      >>> remove_first_dear = partial(remove_dear, _, 1)
      >>> remove_first_dear(message)
      'Hello, dear world!'

   "Placeholder" cannot be passed to "partial()" as a keyword
   argument.

   Distinto en la versión 3.14: Added support for "Placeholder" in
   positional arguments.

class functools.partialmethod(func, /, *args, **keywords)

   Retorna un nuevo descriptor "partialmethod" que se comporta como
   "partial" excepto que está diseñado para ser usado como una
   definición de método en lugar de ser directamente invocable.

   *func* debe ser un *descriptor* o un invocable (los objetos que son
   ambos, como las funciones normales, se manejan como descriptores).

   When *func* is a descriptor (such as a normal Python function,
   "classmethod()", "staticmethod()", "abstractmethod()" or another
   instance of "partialmethod"), calls to "__get__" are delegated to
   the underlying descriptor, and an appropriate partial object
   returned as the result.

   Cuando *func* es una llamada no descriptiva, se crea dinámicamente
   un método de unión apropiado. Esto se comporta como una función
   Python normal cuando se usa como método: el argumento *self* se
   insertará como el primer argumento posicional, incluso antes de las
   *args* y *keywords* suministradas al constructor "partialmethod".

   Ejemplo:

      >>> class Cell:
      ...     def __init__(self):
      ...         self._alive = False
      ...     @property
      ...     def alive(self):
      ...         return self._alive
      ...     def set_state(self, state):
      ...         self._alive = bool(state)
      ...     set_alive = partialmethod(set_state, True)
      ...     set_dead = partialmethod(set_state, False)
      ...
      >>> c = Cell()
      >>> c.alive
      False
      >>> c.set_alive()
      >>> c.alive
      True

   Added in version 3.4.

functools.reduce(function, iterable, /[, initial])

   Apply *function* of two arguments cumulatively to the items of
   *iterable*, from left to right, so as to reduce the iterable to a
   single value.  For example, "reduce(lambda x, y: x+y, [1, 2, 3, 4,
   5])" calculates "((((1+2)+3)+4)+5)". The left argument, *x*, is the
   accumulated value and the right argument, *y*, is the update value
   from the *iterable*.  If the optional *initial* is present, it is
   placed before the items of the iterable in the calculation, and
   serves as a default when the iterable is empty.  If *initial* is
   not given and *iterable* contains only one item, the first item is
   returned.

   Aproximadamente equivalente a:

      initial_missing = object()

      def reduce(function, iterable, /, initial=initial_missing):
          it = iter(iterable)
          if initial is initial_missing:
              value = next(it)
          else:
              value = initial
          for element in it:
              value = function(value, element)
          return value

   Ver "itertools.accumulate()" para un iterador que produce todos los
   valores intermedios.

   Distinto en la versión 3.14: *initial* is now supported as a
   keyword argument.

@functools.singledispatch

   Transformar una función en una *single-dispatch* *generic
   function*.

   Para definir una función genérica, decórala con el decorador
   "@singledispatch". Al definir una función usando "@singledispatch",
   tenga en cuenta que el envío ocurre en el tipo del primer
   argumento:

      >>> from functools import singledispatch
      >>> @singledispatch
      ... def fun(arg, verbose=False):
      ...     if verbose:
      ...         print("Let me just say,", end=" ")
      ...     print(arg)

   To add overloaded implementations to the function, use the
   "register()" attribute of the generic function, which can be used
   as a decorator.  For functions annotated with types, the decorator
   will infer the type of the first argument automatically:

      >>> @fun.register
      ... def _(arg: int, verbose=False):
      ...     if verbose:
      ...         print("Strength in numbers, eh?", end=" ")
      ...     print(arg)
      ...
      >>> @fun.register
      ... def _(arg: list, verbose=False):
      ...     if verbose:
      ...         print("Enumerate this:")
      ...     for i, elem in enumerate(arg):
      ...         print(i, elem)

   "typing.Union" can also be used:

      >>> @fun.register
      ... def _(arg: int | float, verbose=False):
      ...     if verbose:
      ...         print("Strength in numbers, eh?", end=" ")
      ...     print(arg)
      ...
      >>> from typing import Union
      >>> @fun.register
      ... def _(arg: Union[list, set], verbose=False):
      ...     if verbose:
      ...         print("Enumerate this:")
      ...     for i, elem in enumerate(arg):
      ...         print(i, elem)
      ...

   Para el código que no utiliza anotaciones de tipo, el argumento de
   tipo apropiado puede ser pasado explícitamente al propio decorador:

      >>> @fun.register(complex)
      ... def _(arg, verbose=False):
      ...     if verbose:
      ...         print("Better than complicated.", end=" ")
      ...     print(arg.real, arg.imag)
      ...

   For code that dispatches on a collections type (e.g., "list"), but
   wants to typehint the items of the collection (e.g., "list[int]"),
   the dispatch type should be passed explicitly to the decorator
   itself with the typehint going into the function definition:

      >>> @fun.register(list)
      ... def _(arg: list[int], verbose=False):
      ...     if verbose:
      ...         print("Enumerate this:")
      ...     for i, elem in enumerate(arg):
      ...         print(i, elem)

   Nota:

     At runtime the function will dispatch on an instance of a list
     regardless of the type contained within the list i.e. "[1,2,3]"
     will be dispatched the same as "["foo", "bar", "baz"]". The
     annotation provided in this example is for static type checkers
     only and has no runtime impact.

   To enable registering *lambdas* and pre-existing functions, the
   "register()" attribute can also be used in a functional form:

      >>> def nothing(arg, verbose=False):
      ...     print("Nothing.")
      ...
      >>> fun.register(type(None), nothing)

   The "register()" attribute returns the undecorated function. This
   enables decorator stacking, "pickling", and the creation of unit
   tests for each variant independently:

      >>> @fun.register(float)
      ... @fun.register(Decimal)
      ... def fun_num(arg, verbose=False):
      ...     if verbose:
      ...         print("Half of your number:", end=" ")
      ...     print(arg / 2)
      ...
      >>> fun_num is fun
      False

   Cuando se llama, la función genérica despacha sobre el tipo del
   primer argumento:

      >>> fun("Hello, world.")
      Hello, world.
      >>> fun("test.", verbose=True)
      Let me just say, test.
      >>> fun(42, verbose=True)
      Strength in numbers, eh? 42
      >>> fun(['spam', 'spam', 'eggs', 'spam'], verbose=True)
      Enumerate this:
      0 spam
      1 spam
      2 eggs
      3 spam
      >>> fun(None)
      Nothing.
      >>> fun(1.23)
      0.615

   Cuando no hay una implementación registrada para un tipo
   específico, se usa su orden de resolución de métodos para encontrar
   una implementación más genérica. La función original decorada con
   "@singledispatch" está registrada para el tipo base "object", lo
   que significa que se usa si no se encuentra una implementación
   mejor.

   Si una implementación está registrada en un *abstract base class*,
   las subclases virtuales de la clase base se enviarán a esa
   implementación:

      >>> from collections.abc import Mapping
      >>> @fun.register
      ... def _(arg: Mapping, verbose=False):
      ...     if verbose:
      ...         print("Keys & Values")
      ...     for key, value in arg.items():
      ...         print(key, "=>", value)
      ...
      >>> fun({"a": "b"})
      a => b

   Para verificar qué implementación elegirá la función genérica para
   un tipo dado, use el atributo "dispatch()":

      >>> fun.dispatch(float)
      <function fun_num at 0x1035a2840>
      >>> fun.dispatch(dict)    # note: default implementation
      <function fun at 0x103fe0000>

   Para acceder a todas las implementaciones registradas, utilice el
   atributo "registry" de sólo lectura:

      >>> fun.registry.keys()
      dict_keys([<class 'NoneType'>, <class 'int'>, <class 'object'>,
                <class 'decimal.Decimal'>, <class 'list'>,
                <class 'float'>])
      >>> fun.registry[float]
      <function fun_num at 0x1035a2840>
      >>> fun.registry[object]
      <function fun at 0x103fe0000>

   Added in version 3.4.

   Distinto en la versión 3.7: The "register()" attribute now supports
   using type annotations.

   Distinto en la versión 3.11: The "register()" attribute now
   supports "typing.Union" as a type annotation.

class functools.singledispatchmethod(func)

   Transformar un método en un  *single-dispatch* *generic function*.

   To define a generic method, decorate it with the
   "@singledispatchmethod" decorator. When defining a method using
   "@singledispatchmethod", note that the dispatch happens on the type
   of the first non-*self* or non-*cls* argument:

      class Negator:
          @singledispatchmethod
          def neg(self, arg):
              raise NotImplementedError("Cannot negate a")

          @neg.register
          def _(self, arg: int):
              return -arg

          @neg.register
          def _(self, arg: bool):
              return not arg

   "@singledispatchmethod" supports nesting with other decorators such
   as "@classmethod". Note that to allow for "dispatcher.register",
   "singledispatchmethod" must be the *outer most* decorator. Here is
   the "Negator" class with the "neg" methods bound to the class,
   rather than an instance of the class:

      class Negator:
          @singledispatchmethod
          @classmethod
          def neg(cls, arg):
              raise NotImplementedError("Cannot negate a")

          @neg.register
          @classmethod
          def _(cls, arg: int):
              return -arg

          @neg.register
          @classmethod
          def _(cls, arg: bool):
              return not arg

   The same pattern can be used for other similar decorators:
   "@staticmethod", "@~abc.abstractmethod", and others.

   Added in version 3.8.

functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)

   Update a *wrapper* function to look like the *wrapped* function.
   The optional arguments are tuples to specify which attributes of
   the original function are assigned directly to the matching
   attributes on the wrapper function and which attributes of the
   wrapper function are updated with the corresponding attributes from
   the original function. The default values for these arguments are
   the module level constants "WRAPPER_ASSIGNMENTS" (which assigns to
   the wrapper function's "__module__", "__name__", "__qualname__",
   "__annotations__", "__type_params__", and "__doc__", the
   documentation string) and "WRAPPER_UPDATES" (which updates the
   wrapper function's "__dict__", i.e. the instance dictionary).

   To allow access to the original function for introspection and
   other purposes (e.g. bypassing a caching decorator such as
   "@lru_cache"), this function automatically adds a "__wrapped__"
   attribute to the wrapper that refers to the function being wrapped.

   El principal uso previsto para esta función es en *decorator*
   functions que envuelven la función decorada y retornan el
   envoltorio. Si la función de envoltura no se actualiza, los
   metadatos de la función retornada reflejarán la definición de la
   envoltura en lugar de la definición de la función original, lo que
   normalmente no es de gran ayuda.

   "update_wrapper()" puede ser usado con otros invocables que no sean
   funciones. Cualquier atributo nombrado en *assigned* o *updated*
   que falte en el objeto que se está invoca se ignora (es decir, esta
   función no intentará establecerlos en la función de envoltura
   (*wrapper*)). "AttributeError" sigue apareciendo si la propia
   función de envoltura no tiene ningún atributo nombrado en
   *updated*.

   Distinto en la versión 3.2: The "__wrapped__" attribute is now
   automatically added. The "__annotations__" attribute is now copied
   by default. Missing attributes no longer trigger an
   "AttributeError".

   Distinto en la versión 3.4: El atributo "__wrapped__" ahora siempre
   se refiere a la función envuelta, incluso si esa función definió un
   atributo "__wrapped__". (see bpo-17482)

   Distinto en la versión 3.12: The "__type_params__" attribute is now
   copied by default.

@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)

   Esta es una función conveniente para invocar "update_wrapper()"
   como decorador de la función cuando se define una función de
   envoltura (*wrapper*).  Es equivalente a "partial(update_wrapper,
   wrapped=wrapped, assigned=assigned, updated=updated)". Por ejemplo:

      >>> from functools import wraps
      >>> def my_decorator(f):
      ...     @wraps(f)
      ...     def wrapper(*args, **kwds):
      ...         print('Calling decorated function')
      ...         return f(*args, **kwds)
      ...     return wrapper
      ...
      >>> @my_decorator
      ... def example():
      ...     """Docstring"""
      ...     print('Called example function')
      ...
      >>> example()
      Calling decorated function
      Called example function
      >>> example.__name__
      'example'
      >>> example.__doc__
      'Docstring'

   Without the use of this decorator factory, the name of the example
   function would have been "'wrapper'", and the docstring of the
   original "example()" would have been lost.

## "partial" Objetos

Los objetos "partial" son objetos invocables creados por "partial()".
Tienen tres atributos de sólo lectura:

partial.func

   Un objeto o función invocable.  Las llamadas al objeto "partial"
   serán reenviadas a "func" con nuevos argumentos y palabras clave.

partial.args

   Los argumentos posicionales de la izquierda que se prepararán para
   los argumentos posicionales proporcionados un llamado al objeto
   "partial".

partial.keywords

   Los argumentos de la palabra clave que se suministrarán cuando se
   llame al objeto "partial".

"partial" objects are like function objects in that they are callable,
weak referenceable, and can have attributes.  There are some important
differences.  For instance, the "__name__" and "__doc__" attributes
are not created automatically.
