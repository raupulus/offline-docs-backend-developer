---
title: Introducción
source_url: https://docs.python.org/es/3
source_path: c-api/intro.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 390
---

# Introducción

La interfaz del programador de aplicaciones (API) con Python brinda a
los programadores de C y C++ acceso al intérprete de Python en una
variedad de niveles. La API es igualmente utilizable desde C++, pero
por brevedad generalmente se conoce como la API Python/C. Hay dos
razones fundamentalmente diferentes para usar la API Python/C. La
primera razón es escribir *módulos de extensión* para propósitos
específicos; Estos son módulos C que extienden el intérprete de
Python. Este es probablemente el uso más común. La segunda razón es
usar Python como componente en una aplicación más grande; Esta técnica
se conoce generalmente como integración (*embedding*) Python en una
aplicación.

Escribir un módulo de extensión es un proceso relativamente bien
entendido, donde un enfoque de "libro de cocina" (*cookbook*) funciona
bien. Hay varias herramientas que automatizan el proceso hasta cierto
punto. Si bien las personas han integrado Python en otras aplicaciones
desde su existencia temprana, el proceso de integrar Python es menos
sencillo que escribir una extensión.

Muchas funciones API son útiles independientemente de si está
integrando o extendiendo Python; Además, la mayoría de las
aplicaciones que integran Python también necesitarán proporcionar una
extensión personalizada, por lo que probablemente sea una buena idea
familiarizarse con la escritura de una extensión antes de intentar
integrar Python en una aplicación real.

## Language version compatibility

Python's C API is compatible with C11 and C++11 versions of C and C++.

This is a lower limit: the C API does not require features from later
C/C++ versions. You do *not* need to enable your compiler's "c11
mode".

## Estándares de codificación

Si está escribiendo código C para su inclusión en CPython, **debe**
seguir las pautas y estándares definidos en **PEP 7**. Estas pautas se
aplican independientemente de la versión de Python a la que esté
contribuyendo. Seguir estas convenciones no es necesario para sus
propios módulos de extensión de terceros, a menos que eventualmente
espere contribuir con ellos a Python.

## Archivos de cabecera (*Include*)

Todas las definiciones de función, tipo y macro necesarias para usar
la API Python/C se incluyen en su código mediante la siguiente línea:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

Esto implica la inclusión de los siguientes archivos de encabezado
estándar: "<stdio.h>", "<string.h>", "<errno.h>", "<limits.h>",
"<assert.h>" y "<stdlib.h>" (si está disponible).

Nota:

  Dado que Python puede definir algunas definiciones de preprocesador
  que afectan los encabezados estándar en algunos sistemas, *debe*
  incluir "Python.h" antes de incluir encabezados estándar.Se
  recomienda definir siempre "PY_SSIZE_T_CLEAN" antes de incluir
  "Python.h". Consulte Analizando argumentos y construyendo valores
  para obtener una descripción de este macro.

Todos los nombres visibles del usuario definidos por "Python.h"
(excepto los definidos por los encabezados estándar incluidos) tienen
uno de los prefijos "Py" o "_Py". Los nombres que comienzan con "_Py"
son para uso interno de la implementación de Python y no deben ser
utilizados por escritores de extensiones. Los nombres de miembros de
estructura no tienen un prefijo reservado.

Nota:

  El código de usuario nunca debe definir nombres que comiencen con
  "Py" o "_Py". Esto confunde al lector y pone en peligro la
  portabilidad del código de usuario para futuras versiones de Python,
  que pueden definir nombres adicionales que comienzan con uno de
  estos prefijos.

The header files are typically installed with Python.  On Unix, these
are located in the directories "*prefix*/include/pythonversion/" and
"*exec_prefix*/include/pythonversion/", where "prefix" and
"exec_prefix" are defined by the corresponding parameters to Python's
**configure** script and *version* is "'%d.%d' %
sys.version_info[:2]".  On Windows, the headers are installed in
"*prefix*/include", where "prefix" is the installation directory
specified to the installer.

To include the headers, place both directories (if different) on your
compiler's search path for includes.  Do *not* place the parent
directories on the search path and then use "#include
<pythonX.Y/Python.h>"; this will break on multi-platform builds since
the platform independent headers under "prefix" include the platform
specific headers from "exec_prefix".

Los usuarios de C++ deben tener en cuenta que aunque la API se define
completamente usando C, los archivos de encabezado declaran
correctamente que los puntos de entrada son "extern "C"". Como
resultado, no es necesario hacer nada especial para usar la API desde
C++.

## Macros útiles

Several useful macros are defined in the Python header files.  Many
are defined closer to where they are useful (for example,
"Py_RETURN_NONE", "PyMODINIT_FUNC"). Others of a more general utility
are defined here.  This is not necessarily a complete listing.

Py_CAN_START_THREADS

   If this macro is defined, then the current system is able to start
   threads.

   Currently, all systems supported by CPython (per **PEP 11**), with
   the exception of some WebAssembly platforms, support starting
   threads.

   Added in version 3.13.

Py_GETENV(s)

   Like "getenv(*s*)", but returns "NULL" if "-E" was passed on the
   command line (see "PyConfig.use_environment").

### Docstring macros

PyDoc_STRVAR(name, str)

   Creates a variable with name *name* that can be used in docstrings.
   If Python is built without docstrings ("--without-doc-strings"),
   the value will be an empty string.

   Ejemplo:

      PyDoc_STRVAR(pop_doc, "Remove and return the rightmost element.");

      static PyMethodDef deque_methods[] = {
          // ...
          {"pop", (PyCFunction)deque_pop, METH_NOARGS, pop_doc},
          // ...
      }

   Expands to "PyDoc_VAR(*name*) = PyDoc_STR(*str*)".

PyDoc_STR(str)

   Expands to the given input string, or an empty string if docstrings
   are disabled ("--without-doc-strings").

   Ejemplo:

      static PyMethodDef pysqlite_row_methods[] = {
          {"keys", (PyCFunction)pysqlite_row_keys, METH_NOARGS,
              PyDoc_STR("Returns the keys of the row.")},
          {NULL, NULL}
      };

PyDoc_VAR(name)

   Declares a static character array variable with the given *name*.
   Expands to "static const char *name*[]"

   For example:

      PyDoc_VAR(python_doc) = PyDoc_STR(
         "A genus of constricting snakes in the Pythonidae family native "
         "to the tropics and subtropics of the Eastern Hemisphere.");

### General utility macros

The following macros are for common tasks not specific to Python.

Py_UNUSED(arg)

   Use esto para argumentos no utilizados en una definición de función
   para silenciar las advertencias del compilador. Ejemplo: "int
   func(int a, int Py_UNUSED(b)) {return a; }".

   Added in version 3.4.

Py_GCC_ATTRIBUTE(name)

   Use a GCC attribute *name*, hiding it from compilers that don't
   support GCC attributes (such as MSVC).

   This expands to "__attribute__((*name)*)" on a GCC compiler, and
   expands to nothing on compilers that don't support GCC attributes.

#### Numeric utilities

Py_ABS(x)

   Retorna el valor absoluto de "x".

   The argument may be evaluated more than once. Consequently, do not
   pass an expression with side-effects directly to this macro.

   If the result cannot be represented (for example, if "x" has
   "INT_MIN" value for int type), the behavior is undefined.

   Corresponds roughly to "((*x*) < 0 ? -(*x*) : (*x*))"

   Added in version 3.3.

Py_MAX(x, y)
Py_MIN(x, y)

   Return the larger or smaller of the arguments, respectively.

   Any arguments may be evaluated more than once. Consequently, do not
   pass an expression with side-effects directly to this macro.

   "Py_MAX" corresponds roughly to "(((*x*) > (*y*)) ? (*x*) :
   (*y*))".

   Added in version 3.3.

Py_ARITHMETIC_RIGHT_SHIFT(type, integer, positions)

   Similar to "*integer* >> *positions*", but forces sign extension,
   as the C standard does not define whether a right-shift of a signed
   integer will perform sign extension or a zero-fill.

   *integer* should be any signed integer type. *positions* is the
   number of positions to shift to the right.

   Both *integer* and *positions* can be evaluated more than once;
   consequently, avoid directly passing a function call or some other
   operation with side-effects to this macro. Instead, store the
   result as a variable and then pass it.

   *type* is unused and only kept for backwards compatibility.
   Historically, *type* was used to cast *integer*.

   Distinto en la versión 3.1: This macro is now valid for all signed
   integer types, not just those for which "unsigned type" is legal.
   As a result, *type* is no longer used.

Py_CHARMASK(c)

   El argumento debe ser un carácter o un número entero en el rango
   [-128, 127] o [0, 255]. Este macro retorna la conversión "c" a un
   "unsigned char".

#### Assertion utilities

Py_UNREACHABLE()

   Use esto cuando tenga una ruta de código a la que no se pueda
   acceder por diseño. Por ejemplo, en la cláusula "default:" en una
   declaración "switch" para la cual todos los valores posibles están
   cubiertos en declaraciones "case". Use esto en lugares donde podría
   tener la tentación de poner una llamada "assert(0)" o "abort()".

   En el modo de lanzamiento, la macro ayuda al compilador a optimizar
   el código y evita una advertencia sobre el código inalcanzable. Por
   ejemplo, la macro se implementa con "__builtin_unreachable()" en
   GCC en modo de lanzamiento.

   In debug mode, and on unsupported compilers, the macro expands to a
   call to "Py_FatalError()".

   A use for "Py_UNREACHABLE()" is following a call to a function that
   never returns but that is not declared "_Noreturn".

   Si una ruta de código es un código muy poco probable pero se puede
   acceder en casos excepcionales, esta macro no debe utilizarse. Por
   ejemplo, en condiciones de poca memoria o si una llamada al sistema
   retorna un valor fuera del rango esperado. En este caso, es mejor
   informar el error a la persona que llama. Si no se puede informar
   del error a la persona que llama, se puede utilizar
   "Py_FatalError()".

   Added in version 3.7.

Py_SAFE_DOWNCAST(value, larger, smaller)

   Cast *value* to type *smaller* from type *larger*, validating that
   no information was lost.

   On release builds of Python, this is roughly equivalent to
   "((*smaller*) *value*)" (in C++, "static_cast<*smaller*>(*value*)"
   will be used instead).

   On debug builds (implying that "Py_DEBUG" is defined), this asserts
   that no information was lost with the cast from *larger* to
   *smaller*.

   *value*, *larger*, and *smaller* may all be evaluated more than
   once in the expression; consequently, do not pass an expression
   with side-effects directly to this macro.

Py_BUILD_ASSERT(cond)

   Asserts a compile-time condition *cond*, as a statement. The build
   will fail if the condition is false or cannot be evaluated at
   compile time.

   Corresponds roughly to "static_assert(*cond*)" on C23 and above.

   For example:

      Py_BUILD_ASSERT(sizeof(PyTime_t) == sizeof(int64_t));

   Added in version 3.3.

Py_BUILD_ASSERT_EXPR(cond)

   Asserts a compile-time condition *cond*, as an expression that
   evaluates to "0". The build will fail if the condition is false or
   cannot be evaluated at compile time.

   For example:

      #define foo_to_char(foo) \
          ((char *)(foo) + Py_BUILD_ASSERT_EXPR(offsetof(struct foo, string) == 0))

   Added in version 3.3.

#### Type size utilities

Py_ARRAY_LENGTH(array)

   Compute the length of a statically allocated C array at compile
   time.

   The *array* argument must be a C array with a size known at compile
   time. Passing an array with an unknown size, such as a heap-
   allocated array, will result in a compilation error on some
   compilers, or otherwise produce incorrect results.

   This is roughly equivalent to:

      sizeof(array) / sizeof((array)[0])

Py_MEMBER_SIZE(type, member)

   Return the size of a structure (*type*) *member* in bytes.

   Corresponds roughly to "sizeof(((*type* *)NULL)->*member*)".

   Added in version 3.6.

#### Macro definition utilities

Py_FORCE_EXPANSION(X)

   This is equivalent to "*X*", which is useful for token-pasting in
   macros, as macro expansions in *X* are forcefully evaluated by the
   preprocessor.

Py_STRINGIFY(x)

   Convert "x" to a C string.  For example, "Py_STRINGIFY(123)"
   returns ""123"".

   Added in version 3.4.

### Declaration utilities

The following macros can be used in declarations. They are most useful
for defining the C API itself, and have limited use for extension
authors. Most of them expand to compiler-specific spellings of common
extensions to the C language.

Py_ALWAYS_INLINE

   Ask the compiler to always inline a static inline function. The
   compiler can ignore it and decide to not inline the function.

   Corresponds to "always_inline" attribute in GCC and "__forceinline"
   in MSVC.

   Puede ser usado para usar inline en funciones estáticas inline de
   rendimiento crítico cuando se corre Python en modo de depuración
   con inline de funciones deshabilitado. Por ejemplo, MSC deshabilita
   el inline de funciones cuando se configura en modo de depuración.

   Marcar ciegamente una función estática inline con Py_ALWAYS_INLINE
   puede resultar en peor rendimientos (debido a un aumento del tamaño
   del código, por ejemplo). El compilador es generalmente más
   inteligente que el desarrollador para el análisis costo/beneficio.

   If Python is built in debug mode (if the "Py_DEBUG" macro is
   defined), the "Py_ALWAYS_INLINE" macro does nothing.

   Debe ser especificado antes del tipo de retorno de la función. Uso:

      static inline Py_ALWAYS_INLINE int random(void) { return 4; }

   Added in version 3.11.

Py_NO_INLINE

   Deshabilita el uso de inline en una función. Por ejemplo, reduce el
   consumo de la pila C: útil en compilaciones LTO+PGO que usan mucho
   inline (ver bpo-33720).

   Corresponds to the "noinline" attribute/specification on GCC and
   MSVC.

   Uso:

      Py_NO_INLINE static int random(void) { return 4; }

   Added in version 3.11.

Py_DEPRECATED(version)

   Use this to declare APIs that were deprecated in a specific CPython
   version. The macro must be placed before the symbol name.

   Ejemplo:

      Py_DEPRECATED(3.8) PyAPI_FUNC(int) Py_OldFunction(void);

   Distinto en la versión 3.8: Soporte para MSVC fue agregado.

Py_LOCAL(type)

   Declare a function returning the specified *type* using a fast-
   calling qualifier for functions that are local to the current file.
   Semantically, this is equivalent to "static *type*".

Py_LOCAL_INLINE(type)

   Equivalent to "Py_LOCAL" but additionally requests the function be
   inlined.

Py_LOCAL_SYMBOL

   Macro used to declare a symbol as local to the shared library
   (hidden). On supported platforms, it ensures the symbol is not
   exported.

   On compatible versions of GCC/Clang, it expands to
   "__attribute__((visibility("hidden")))".

Py_EXPORTED_SYMBOL

   Macro used to declare a symbol (function or data) as exported. On
   Windows, this expands to "__declspec(dllexport)". On compatible
   versions of GCC/Clang, it expands to
   "__attribute__((visibility("default")))". This macro is for
   defining the C API itself; extension modules should not use it.

Py_IMPORTED_SYMBOL

   Macro used to declare a symbol as imported. On Windows, this
   expands to "__declspec(dllimport)". This macro is for defining the
   C API itself; extension modules should not use it.

PyAPI_FUNC(type)

   Macro used by CPython to declare a function as part of the C API.
   Its expansion depends on the platform and build configuration. This
   macro is intended for defining CPython's C API itself; extension
   modules should not use it for their own symbols.

PyAPI_DATA(type)

   Macro used by CPython to declare a public global variable as part
   of the C API. Its expansion depends on the platform and build
   configuration. This macro is intended for defining CPython's C API
   itself; extension modules should not use it for their own symbols.

### Outdated macros

The following macros have been used to features that have been
standardized in C11.

Py_ALIGNED(num)

   Specify alignment to *num* bytes on compilers that support it.

   Consider using the C11 standard "_Alignas" specifier over this
   macro.

Py_LL(number)
Py_ULL(number)

   Use *number* as a "long long" or "unsigned long long" integer
   literal, respectively.

   Expands to *number* followed by "LL" or "LLU", respectively, but
   will expand to some compiler-specific suffixes on some older
   compilers.

   Consider using the C99 standard suffixes "LL" and "LLU" directly.

Py_MEMCPY(dest, src, n)

   This is an alias to "memcpy()".

   Soft deprecated since version 3.14: Use "memcpy()" directly
   instead.

Py_VA_COPY

   This is an alias to the C99-standard "va_copy" function.

   Historically, this would use a compiler-specific method to copy a
   "va_list".

   Distinto en la versión 3.6: This is now an alias to "va_copy".

   Soft deprecated since version 3.14.

## Objetos, tipos y conteos de referencias

Most Python/C API functions have one or more arguments as well as a
return value of type PyObject*.  This type is a pointer to an opaque
data type representing an arbitrary Python object.  Since all Python
object types are treated the same way by the Python language in most
situations (e.g., assignments, scope rules, and argument passing), it
is only fitting that they should be represented by a single C type.
Almost all Python objects live on the heap: you never declare an
automatic or static variable of type "PyObject", only pointer
variables of type PyObject* can  be declared.  The sole exception are
the type objects; since these must never be deallocated, they are
typically static "PyTypeObject" objects.

Todos los objetos de Python (incluso los enteros de Python) tienen un
tipo (*type*) y un conteo de referencia (*reference count*). El tipo
de un objeto determina qué tipo de objeto es (por ejemplo, un número
entero, una lista o una función definida por el usuario; hay muchos
más como se explica en Jerarquía de tipos estándar). Para cada uno de
los tipos conocidos hay un macro para verificar si un objeto es de ese
tipo; por ejemplo, "PyList_Check(a)" es verdadero si (y solo si) el
objeto al que apunta *a* es una lista de Python.

### Conteo de Referencias

The reference count is important because today's computers have a
finite (and often severely limited) memory size; it counts how many
different places there are that have a *strong reference* to an
object. Such a place could be another object, or a global (or static)
C variable, or a local variable in some C function. When the last
*strong reference* to an object is released (i.e. its reference count
becomes zero), the object is deallocated. If it contains references to
other objects, those references are released. Those other objects may
be deallocated in turn, if there are no more references to them, and
so on.  (There's an obvious problem  with objects that reference each
other here; for now, the solution is "don't do that.")

Reference counts are always manipulated explicitly.  The normal way is
to use the macro "Py_INCREF()" to take a new reference to an object
(i.e. increment its reference count by one), and "Py_DECREF()" to
release that reference (i.e. decrement the reference count by one).
The "Py_DECREF()" macro is considerably more complex than the incref
one, since it must check whether the reference count becomes zero and
then cause the object's deallocator to be called.  The deallocator is
a function pointer contained in the object's type structure.  The
type-specific deallocator takes care of releasing references for other
objects contained in the object if this is a compound object type,
such as a list, as well as performing any additional finalization
that's needed.  There's no chance that the reference count can
overflow; at least as many bits are used to hold the reference count
as there are distinct memory locations in virtual memory (assuming
"sizeof(Py_ssize_t) >= sizeof(void*)"). Thus, the reference count
increment is a simple operation.

It is not necessary to hold a *strong reference* (i.e. increment the
reference count) for every local variable that contains a pointer to
an object.  In theory, the  object's reference count goes up by one
when the variable is made to  point to it and it goes down by one when
the variable goes out of  scope.  However, these two cancel each other
out, so at the end the  reference count hasn't changed.  The only real
reason to use the  reference count is to prevent the object from being
deallocated as  long as our variable is pointing to it.  If we know
that there is at  least one other reference to the object that lives
at least as long as our variable, there is no need to take a new
*strong reference* (i.e. increment the reference count) temporarily.
An important situation where this arises is in objects  that are
passed as arguments to C functions in an extension module  that are
called from Python; the call mechanism guarantees to hold a  reference
to every argument for the duration of the call.

However, a common pitfall is to extract an object from a list and hold
on to it for a while without taking a new reference.  Some other
operation might conceivably remove the object from the list, releasing
that reference, and possibly deallocating it. The real danger is that
innocent-looking operations may invoke arbitrary Python code which
could do this; there is a code path which allows control to flow back
to the user from a "Py_DECREF()", so almost any operation is
potentially dangerous.

A safe approach is to always use the generic operations (functions
whose name begins with "PyObject_", "PyNumber_", "PySequence_" or
"PyMapping_"). These operations always create a new *strong reference*
(i.e. increment the reference count) of the object they return. This
leaves the caller with the responsibility to call "Py_DECREF()" when
they are done with the result; this soon becomes second nature.

#### Detalles del conteo de referencia

The reference count behavior of functions in the Python/C API is best
explained in terms of *ownership of references*.  Ownership pertains
to references, never to objects (objects are not owned: they are
always shared).  "Owning a reference" means being responsible for
calling Py_DECREF on it when the reference is no longer needed.
Ownership can also be transferred, meaning that the code that receives
ownership of the reference then becomes responsible for eventually
releasing it by calling "Py_DECREF()" or "Py_XDECREF()" when it's no
longer needed---or passing on this responsibility (usually to its
caller). When a function passes ownership of a reference on to its
caller, the caller is said to receive a *new* reference.  When no
ownership is transferred, the caller is said to *borrow* the
reference. Nothing needs to be done for a *borrowed reference*.

Conversely, when a calling function passes in a reference to an
object, there are two possibilities: the function *steals* a
reference to the object, or it does not.

*Stealing a reference* means that when you pass a reference to a
function, that function assumes that it now owns that reference. Since
the new owner can use "Py_DECREF()" at its discretion, you (the
caller) must not use that reference after the call.

Pocas funciones roban referencias; las dos excepciones notables son
"PyList_SetItem()" y "PyTuple_SetItem()", que roban una referencia al
elemento (¡pero no a la tupla o lista en la que se coloca el
elemento!). Estas funciones fueron diseñadas para robar una referencia
debido a un idioma común para poblar una tupla o lista con objetos
recién creados; por ejemplo, el código para crear la tupla "(1, 2,
"tres")" podría verse así (olvidando el manejo de errores por el
momento; una mejor manera de codificar esto se muestra a
continuación):

   PyObject *t;

   t = PyTuple_New(3);
   PyTuple_SetItem(t, 0, PyLong_FromLong(1L));
   PyTuple_SetItem(t, 1, PyLong_FromLong(2L));
   PyTuple_SetItem(t, 2, PyUnicode_FromString("three"));

Aquí "PyLong_FromLong()" retorna una nueva referencia que es
inmediatamente robada por "PyTuple_SetItem()". Cuando quiera seguir
usando un objeto aunque se le robe la referencia, use "Py_INCREF()"
para tomar otra referencia antes de llamar a la función de robo de
referencias.

Por cierto, "PyTuple_SetItem()" es la *única* forma de establecer
elementos de tupla; "PySequence_SetItem()" y "PyObject_SetItem()" se
niegan a hacer esto ya que las tuplas son un tipo de datos inmutable.
Solo debe usar "PyTuple_SetItem()" para las tuplas que está creando
usted mismo.

El código equivalente para llenar una lista se puede escribir usando
"PyList_New()" y "PyList_SetItem()".

Sin embargo, en la práctica, rara vez utilizará estas formas de crear
y completar una tupla o lista. Hay una función genérica,
"Py_BuildValue()", que puede crear los objetos más comunes a partir de
valores C, dirigidos por un una cadena de caracteres de formato
(*format string*). Por ejemplo, los dos bloques de código anteriores
podrían reemplazarse por lo siguiente (que también se ocupa de la
comprobación de errores):

   PyObject *tuple, *list;

   tuple = Py_BuildValue("(iis)", 1, 2, "three");
   list = Py_BuildValue("[iis]", 1, 2, "three");

It is much more common to use "PyObject_SetItem()" and friends with
items whose references you are only borrowing, like arguments that
were passed in to the function you are writing.  In that case, their
behaviour regarding references is much saner, since you don't have to
take a new reference just so you can give that reference away ("have
it be stolen").  For example, this function sets all items of a list
(actually, any mutable sequence) to a given item:

   int
   set_all(PyObject *target, PyObject *item)
   {
       Py_ssize_t i, n;

       n = PyObject_Length(target);
       if (n < 0)
           return -1;
       for (i = 0; i < n; i++) {
           PyObject *index = PyLong_FromSsize_t(i);
           if (!index)
               return -1;
           if (PyObject_SetItem(target, index, item) < 0) {
               Py_DECREF(index);
               return -1;
           }
           Py_DECREF(index);
       }
       return 0;
   }

La situación es ligeramente diferente para los valores de retorno de
la función. Si bien pasar una referencia a la mayoría de las funciones
no cambia sus responsabilidades de propiedad para esa referencia,
muchas funciones que retornan una referencia a un objeto le otorgan la
propiedad de la referencia. La razón es simple: en muchos casos, el
objeto retornado se crea sobre la marcha, y la referencia que obtiene
es la única referencia al objeto. Por lo tanto, las funciones
genéricas que retornan referencias de objeto, como
"PyObject_GetItem()" y "PySequence_GetItem()", siempre retornan una
nueva referencia (la entidad que llama se convierte en el propietario
de la referencia).

Es importante darse cuenta de que si posee una referencia retornada
por una función depende de a qué función llame únicamente --- *el
plumaje* (el tipo del objeto pasado como argumento a la función) *no
entra en él!* Por lo tanto, si extrae un elemento de una lista usando
"PyList_GetItem()", no posee la referencia --- pero si obtiene el
mismo elemento de la misma lista usando "PySequence_GetItem()" (que
toma exactamente los mismos argumentos), usted posee una referencia al
objeto retornado.

Aquí hay un ejemplo de cómo podría escribir una función que calcule la
suma de los elementos en una lista de enteros; una vez usando
"PyList_GetItem()", y una vez usando "PySequence_GetItem()".

   long
   sum_list(PyObject *list)
   {
       Py_ssize_t i, n;
       long total = 0, value;
       PyObject *item;

       n = PyList_Size(list);
       if (n < 0)
           return -1; /* Not a list */
       for (i = 0; i < n; i++) {
           item = PyList_GetItem(list, i); /* Can't fail */
           if (!PyLong_Check(item)) continue; /* Skip non-integers */
           value = PyLong_AsLong(item);
           if (value == -1 && PyErr_Occurred())
               /* Integer too big to fit in a C long, bail out */
               return -1;
           total += value;
       }
       return total;
   }

   long
   sum_sequence(PyObject *sequence)
   {
       Py_ssize_t i, n;
       long total = 0, value;
       PyObject *item;
       n = PySequence_Length(sequence);
       if (n < 0)
           return -1; /* Has no length */
       for (i = 0; i < n; i++) {
           item = PySequence_GetItem(sequence, i);
           if (item == NULL)
               return -1; /* Not a sequence, or other failure */
           if (PyLong_Check(item)) {
               value = PyLong_AsLong(item);
               Py_DECREF(item);
               if (value == -1 && PyErr_Occurred())
                   /* Integer too big to fit in a C long, bail out */
                   return -1;
               total += value;
           }
           else {
               Py_DECREF(item); /* Discard reference ownership */
           }
       }
       return total;
   }

### Tipos

There are few other data types that play a significant role in  the
Python/C API; most are simple C types such as int,  long, double and
char*.  A few structure types  are used to describe static tables used
to list the functions exported  by a module or the data attributes of
a new object type, and another is used to describe the value of a
complex number.  These will  be discussed together with the functions
that use them.

type Py_ssize_t
    * Part of the Stable ABI.*

   Un tipo integral con signo tal que "sizeof(Py_ssize_t) ==
   sizeof(size_t)". C99 no define directamente tal cosa (size_t es un
   tipo integral sin signo). Vea **PEP 353** para más detalles.
   "PY_SSIZE_T_MAX" es el valor positivo más grande del tipo
   "Py_ssize_t".

## Excepciones

El programador de Python solo necesita lidiar con excepciones si se
requiere un manejo específico de errores; las excepciones no manejadas
se propagan automáticamente a la persona que llama, luego a la persona
que llama, y así sucesivamente, hasta que llegan al intérprete de
nivel superior, donde se informan al usuario acompañado de un
seguimiento de pila (*stack traceback*).

Para los programadores de C, sin embargo, la comprobación de errores
siempre tiene que ser explícita. Todas las funciones en la API
Python/C pueden generar excepciones, a menos que se señale
explícitamente en la documentación de una función. En general, cuando
una función encuentra un error, establece una excepción, descarta
cualquier referencia de objeto que posea y retorna un indicador de
error. Si no se documenta lo contrario, este indicador es "NULL" o
"-1", dependiendo del tipo de retorno de la función. Algunas funciones
retornan un resultado booleano verdadero/falso, con falso que indica
un error. Muy pocas funciones no retornan ningún indicador de error
explícito o tienen un valor de retorno ambiguo, y requieren pruebas
explícitas de errores con "PyErr_Occurred()". Estas excepciones
siempre se documentan explícitamente.

El estado de excepción se mantiene en el almacenamiento por subproceso
(esto es equivalente a usar el almacenamiento global en una aplicación
sin subprocesos). Un subproceso puede estar en uno de dos estados: se
ha producido una excepción o no. La función "PyErr_Occurred()" puede
usarse para verificar esto: retorna una referencia prestada al objeto
de tipo de excepción cuando se produce una excepción, y "NULL" de lo
contrario. Hay una serie de funciones para establecer el estado de
excepción: "PyErr_SetString()" es la función más común (aunque no la
más general) para establecer el estado de excepción, y "PyErr_Clear()"
borra la excepción estado.

El estado de excepción completo consta de tres objetos (todos los
cuales pueden ser "NULL"): el tipo de excepción, el valor de excepción
correspondiente y el rastreo. Estos tienen los mismos significados que
el resultado de Python de "sys.exc_info()"; sin embargo, no son lo
mismo: los objetos Python representan la última excepción manejada por
una declaración de Python "try" ... "except", mientras que el estado
de excepción de nivel C solo existe mientras se está pasando una
excepción entre las funciones de C hasta que llega al bucle principal
del intérprete de código de bytes (*bytecode*) de Python, que se
encarga de transferirlo a "sys.exc_info()" y amigos.

Tenga en cuenta que a partir de Python 1.5, la forma preferida y
segura de subprocesos para acceder al estado de excepción desde el
código de Python es llamar a la función "sys.exc_info()", que retorna
el estado de excepción por subproceso para el código de Python.
Además, la semántica de ambas formas de acceder al estado de excepción
ha cambiado de modo que una función que detecta una excepción guardará
y restaurará el estado de excepción de su hilo para preservar el
estado de excepción de su llamador. Esto evita errores comunes en el
código de manejo de excepciones causado por una función de aspecto
inocente que sobrescribe la excepción que se maneja; También reduce la
extensión de vida útil a menudo no deseada para los objetos a los que
hacen referencia los marcos de pila en el rastreo.

Como principio general, una función que llama a otra función para
realizar alguna tarea debe verificar si la función llamada generó una
excepción y, de ser así, pasar el estado de excepción a quien la llama
(*caller*). Debe descartar cualquier referencia de objeto que posea y
retornar un indicador de error, pero *no* debe establecer otra
excepción --- que sobrescribirá la excepción que se acaba de generar y
perderá información importante sobre la causa exacta del error.

A simple example of detecting exceptions and passing them on is shown
in the "sum_sequence()" example above.  It so happens that this
example doesn't need to clean up any owned references when it detects
an error.  The following example function shows some error cleanup.
First, to remind you why you like Python, we show the equivalent
Python code:

   def incr_item(dict, key):
       try:
           item = dict[key]
       except KeyError:
           item = 0
       dict[key] = item + 1

Aquí está el código C correspondiente, en todo su esplendor:

   int
   incr_item(PyObject *dict, PyObject *key)
   {
       /* Objects all initialized to NULL for Py_XDECREF */
       PyObject *item = NULL, *const_one = NULL, *incremented_item = NULL;
       int rv = -1; /* Return value initialized to -1 (failure) */

       item = PyObject_GetItem(dict, key);
       if (item == NULL) {
           /* Handle KeyError only: */
           if (!PyErr_ExceptionMatches(PyExc_KeyError))
               goto error;

           /* Clear the error and use zero: */
           PyErr_Clear();
           item = PyLong_FromLong(0L);
           if (item == NULL)
               goto error;
       }
       const_one = PyLong_FromLong(1L);
       if (const_one == NULL)
           goto error;

       incremented_item = PyNumber_Add(item, const_one);
       if (incremented_item == NULL)
           goto error;

       if (PyObject_SetItem(dict, key, incremented_item) < 0)
           goto error;
       rv = 0; /* Success */
       /* Continue with cleanup code */

    error:
       /* Cleanup code, shared by success and failure path */

       /* Use Py_XDECREF() to ignore NULL references */
       Py_XDECREF(item);
       Py_XDECREF(const_one);
       Py_XDECREF(incremented_item);

       return rv; /* -1 for error, 0 for success */
   }

Este ejemplo representa un uso aprobado de la declaración "goto" en C!
Ilustra el uso de "PyErr_ExceptionMatches()" y "PyErr_Clear()" para
manejar excepciones específicas, y el uso de "Py_XDECREF()" para
eliminar referencias propias que pueden ser "NULL" (tenga en cuenta la
"'X'"' en el nombre; "Py_DECREF()" se bloqueará cuando se enfrente con
una referencia "NULL"). Es importante que las variables utilizadas
para contener referencias propias se inicialicen en "NULL" para que
esto funcione; Del mismo modo, el valor de retorno propuesto se
inicializa a "-1" (falla) y solo se establece en éxito después de que
la última llamada realizada sea exitosa.

## Integración de Python

La única tarea importante de la que solo tienen que preocuparse los
integradores (a diferencia de los escritores de extensión) del
intérprete de Python es la inicialización, y posiblemente la
finalización, del intérprete de Python. La mayor parte de la
funcionalidad del intérprete solo se puede usar después de que el
intérprete se haya inicializado.

La función básica de inicialización es "Py_Initialize()". Esto
inicializa la tabla de módulos cargados y crea los módulos
fundamentales "builtins", "__main__", y "sys". También inicializa la
ruta de búsqueda del módulo ("sys.path").

"Py_Initialize()" no establece la "lista de argumentos de script"
("sys.argv"). Si esta variable es necesaria por el código Python que
se ejecutará más tarde, debe establecerse "PyConfig.argv" y
"PyConfig.parse_argv": consulte Python Initialization Configuration.

En la mayoría de los sistemas (en particular, en Unix y Windows,
aunque los detalles son ligeramente diferentes), "Py_Initialize()"
calcula la ruta de búsqueda del módulo basándose en su mejor
estimación de la ubicación del ejecutable del intérprete de Python
estándar, suponiendo que la biblioteca de Python se encuentra en una
ubicación fija en relación con el ejecutable del intérprete de Python.
En particular, busca un directorio llamado "lib/python*X.Y*" relativo
al directorio padre donde se encuentra el ejecutable llamado "python"
en la ruta de búsqueda del comando *shell* (la variable de entorno
"PATH").

Por ejemplo, si el ejecutable de Python se encuentra en
"/usr/local/bin/python", se supondrá que las bibliotecas están en
"/usr/local/lib/python*X.Y*". (De hecho, esta ruta particular también
es la ubicación "alternativa", utilizada cuando no se encuentra un
archivo ejecutable llamado "python" junto con "PATH".) El usuario
puede anular este comportamiento configurando la variable de entorno
"PYTHONHOME", o inserte directorios adicionales delante de la ruta
estándar estableciendo "PYTHONPATH".

The embedding application can steer the search by setting
"PyConfig.program_name" *before* calling "Py_InitializeFromConfig()".
Note that "PYTHONHOME" still overrides this and "PYTHONPATH" is still
inserted in front of the standard path.  An application that requires
total control has to provide its own implementation of "Py_GetPath()",
"Py_GetPrefix()", "Py_GetExecPrefix()", and "Py_GetProgramFullPath()"
(all defined in "Modules/getpath.c").

A veces, es deseable "no inicializar" Python. Por ejemplo, la
aplicación puede querer comenzar de nuevo (hacer otra llamada a
"Py_Initialize()") o la aplicación simplemente se hace con el uso de
Python y quiere liberar memoria asignada por Python. Esto se puede
lograr llamando a "Py_FinalizeEx()". La función "Py_IsInitialized()"
retorna verdadero si Python se encuentra actualmente en el estado
inicializado. Se proporciona más información sobre estas funciones en
un capítulo posterior. Tenga en cuenta que "Py_FinalizeEx()" *no*
libera toda la memoria asignada por el intérprete de Python, por
ejemplo, la memoria asignada por los módulos de extensión actualmente
no se puede liberar.

## Depuración de compilaciones

Python se puede construir con varios macros para permitir
verificaciones adicionales del intérprete y los módulos de extensión.
Estas comprobaciones tienden a agregar una gran cantidad de sobrecarga
al tiempo de ejecución, por lo que no están habilitadas de forma
predeterminada.

A full list of the various types of debugging builds is in the file
"Misc/SpecialBuilds.txt" in the Python source distribution. Builds are
available that support tracing of reference counts, debugging the
memory allocator, or low-level profiling of the main interpreter loop.
Only the most frequently used builds will be described in the
remainder of this section.

Py_DEBUG

Compiling the interpreter with the "Py_DEBUG" macro defined produces
what is generally meant by a debug build of Python. "Py_DEBUG" is
enabled in the Unix build by adding "--with-pydebug" to the
"./configure" command. It is also implied by the presence of the not-
Python-specific "_DEBUG" macro.  When "Py_DEBUG" is enabled in the
Unix build, compiler optimization is disabled.

Además de la depuración del recuento de referencia que se describe a
continuación, se realizan verificaciones adicionales, véase
compilaciones de depuración.

Defining "Py_TRACE_REFS" enables reference tracing (see the "configure
--with-trace-refs option"). When defined, a circular doubly linked
list of active objects is maintained by adding two extra fields to
every "PyObject".  Total allocations are tracked as well.  Upon exit,
all existing references are printed.  (In interactive mode this
happens after every statement run by the interpreter.)

Consulte "Misc/SpecialBuilds.txt" en la distribución fuente de Python
para obtener información más detallada.

## Recommended third party tools

The following third party tools offer both simpler and more
sophisticated approaches to creating C, C++ and Rust extensions for
Python:

* Cython

* cffi

* HPy

* nanobind (C++)

* Numba

* pybind11 (C++)

* PyO3 (Rust)

* SWIG

Using tools such as these can help avoid writing code that is tightly
bound to a particular version of CPython, avoid reference counting
errors, and focus more on your own code than on using the CPython API.
In general, new versions of Python can be supported by updating the
tool, and your code will often use newer and more efficient APIs
automatically. Some tools also support compiling for other
implementations of Python from a single set of sources.

These projects are not supported by the same people who maintain
Python, and issues need to be raised with the projects directly.
Remember to check that the project is still maintained and supported,
as the list above may become outdated.

Ver también:

  Python Packaging User Guide: Binary Extensions
     The Python Packaging User Guide not only covers several available
     tools that simplify the creation of binary extensions, but also
     discusses the various reasons why creating an extension module
     may be desirable in the first place.
